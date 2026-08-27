import sqlite3
from datetime import datetime

DB_NAME = "study_planner.db"


def get_connection():
    return sqlite3.connect(DB_NAME, check_same_thread=False)


def initialize_database():
    conn = get_connection()
    cursor = conn.cursor()

    # Subjects table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS subjects (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE
        )
    """)

    # Topics table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS topics (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            subject_id INTEGER NOT NULL,
            name TEXT NOT NULL,
            priority TEXT DEFAULT 'Medium',
            status TEXT DEFAULT 'Not Started',
            created_at TEXT,
            FOREIGN KEY (subject_id) REFERENCES subjects(id)
        )
    """)

    # Study sessions table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS study_sessions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            subject_id INTEGER NOT NULL,
            hours REAL NOT NULL,
            study_date TEXT NOT NULL,
            notes TEXT,
            FOREIGN KEY (subject_id) REFERENCES subjects(id)
        )
    """)

    conn.commit()
    conn.close()


# -------------------------
# SUBJECT FUNCTIONS
# -------------------------

def add_subject(name):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(
            "INSERT INTO subjects (name) VALUES (?)",
            (name,)
        )
        conn.commit()
    except sqlite3.IntegrityError:
        pass

    conn.close()


def get_subjects():
    conn = get_connection()

    data = conn.execute("""
        SELECT id, name
        FROM subjects
        ORDER BY name
    """).fetchall()

    conn.close()

    return data


def delete_subject(subject_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM topics WHERE subject_id = ?",
        (subject_id,)
    )

    cursor.execute(
        "DELETE FROM study_sessions WHERE subject_id = ?",
        (subject_id,)
    )

    cursor.execute(
        "DELETE FROM subjects WHERE id = ?",
        (subject_id,)
    )

    conn.commit()
    conn.close()


# -------------------------
# TOPIC FUNCTIONS
# -------------------------

def add_topic(subject_id, name, priority):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO topics
        (subject_id, name, priority, status, created_at)
        VALUES (?, ?, ?, ?, ?)
    """, (
        subject_id,
        name,
        priority,
        "Not Started",
        datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ))

    conn.commit()
    conn.close()


def get_topics():
    conn = get_connection()

    data = conn.execute("""
        SELECT
            topics.id,
            subjects.name,
            topics.name,
            topics.priority,
            topics.status,
            topics.created_at
        FROM topics
        JOIN subjects
        ON topics.subject_id = subjects.id
        ORDER BY topics.id DESC
    """).fetchall()

    conn.close()

    return data


def update_topic_status(topic_id, status):
    conn = get_connection()

    conn.execute("""
        UPDATE topics
        SET status = ?
        WHERE id = ?
    """, (status, topic_id))

    conn.commit()
    conn.close()


def delete_topic(topic_id):
    conn = get_connection()

    conn.execute(
        "DELETE FROM topics WHERE id = ?",
        (topic_id,)
    )

    conn.commit()
    conn.close()


# -------------------------
# STUDY SESSION FUNCTIONS
# -------------------------

def add_study_session(subject_id, hours, study_date, notes):
    conn = get_connection()

    conn.execute("""
        INSERT INTO study_sessions
        (subject_id, hours, study_date, notes)
        VALUES (?, ?, ?, ?)
    """, (
        subject_id,
        hours,
        study_date,
        notes
    ))

    conn.commit()
    conn.close()


def get_study_sessions():
    conn = get_connection()

    data = conn.execute("""
        SELECT
            study_sessions.id,
            subjects.name,
            study_sessions.hours,
            study_sessions.study_date,
            study_sessions.notes
        FROM study_sessions
        JOIN subjects
        ON study_sessions.subject_id = subjects.id
        ORDER BY study_sessions.study_date DESC
    """).fetchall()

    conn.close()

    return data