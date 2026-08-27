import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datetime import date

from database import (
    initialize_database,
    add_subject,
    get_subjects,
    delete_subject,
    add_topic,
    get_topics,
    update_topic_status,
    delete_topic,
    add_study_session,
    get_study_sessions
)


# -------------------------
# PAGE CONFIGURATION
# -------------------------

st.set_page_config(
    page_title="Student Study Planner",
    page_icon="📚",
    layout="wide"
)

initialize_database()


# -------------------------
# CUSTOM CSS
# -------------------------

st.markdown("""
<style>

.main-title {
    font-size: 40px;
    font-weight: bold;
}

.subtitle {
    font-size: 18px;
    color: #666;
}

.card {
    padding: 20px;
    border-radius: 10px;
    background-color: #f5f5f5;
    text-align: center;
}

</style>
""", unsafe_allow_html=True)


# -------------------------
# SIDEBAR
# -------------------------

st.sidebar.title("📚 Study Planner")

page = st.sidebar.radio(
    "Navigation",
    [
        "Dashboard",
        "Subjects",
        "Topics",
        "Study Sessions",
        "Progress"
    ]
)


# ==========================================================
# DASHBOARD
# ==========================================================

if page == "Dashboard":

    st.markdown(
        '<div class="main-title">📚 Student Study Planner</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">Plan your learning. Track your progress. Improve every day.</div>',
        unsafe_allow_html=True
    )

    st.divider()

    subjects = get_subjects()
    topics = get_topics()
    sessions = get_study_sessions()

    total_subjects = len(subjects)
    total_topics = len(topics)

    completed_topics = len([
        topic for topic in topics
        if topic[4] == "Completed"
    ])

    total_hours = sum(
        session[2]
        for session in sessions
    )

    progress = (
        completed_topics / total_topics * 100
        if total_topics > 0
        else 0
    )

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "📚 Subjects",
            total_subjects
        )

    with col2:
        st.metric(
            "📝 Topics",
            total_topics
        )

    with col3:
        st.metric(
            "✅ Completed",
            completed_topics
        )

    with col4:
        st.metric(
            "⏱️ Study Hours",
            round(total_hours, 2)
        )

    st.divider()

    st.subheader("Overall Progress")

    st.progress(
        int(progress)
    )

    st.write(
        f"**{progress:.1f}%** of your topics are completed."
    )

    st.divider()

    if topics:

        st.subheader("Recent Topics")

        topic_df = pd.DataFrame(
            topics,
            columns=[
                "ID",
                "Subject",
                "Topic",
                "Priority",
                "Status",
                "Created"
            ]
        )

        st.dataframe(
            topic_df[
                [
                    "Subject",
                    "Topic",
                    "Priority",
                    "Status"
                ]
            ].head(10),
            use_container_width=True,
            hide_index=True
        )

    else:

        st.info(
            "No topics yet. Go to the Topics section and add your first topic."
        )


# ==========================================================
# SUBJECTS
# ==========================================================

elif page == "Subjects":

    st.title("📚 Subjects")

    st.write(
        "Create and manage the subjects you are studying."
    )

    st.divider()

    with st.form("subject_form"):

        subject_name = st.text_input(
            "Subject Name",
            placeholder="Example: Python Programming"
        )

        submitted = st.form_submit_button(
            "➕ Add Subject"
        )

        if submitted:

            if subject_name.strip():

                add_subject(
                    subject_name.strip()
                )

                st.success(
                    f"Subject '{subject_name}' added!"
                )

                st.rerun()

            else:

                st.warning(
                    "Please enter a subject name."
                )

    st.divider()

    subjects = get_subjects()

    if subjects:

        for subject_id, subject_name in subjects:

            col1, col2 = st.columns(
                [5, 1]
            )

            with col1:

                st.write(
                    f"📖 **{subject_name}**"
                )

            with col2:

                if st.button(
                    "Delete",
                    key=f"delete_subject_{subject_id}"
                ):

                    delete_subject(
                        subject_id
                    )

                    st.rerun()

    else:

        st.info(
            "No subjects added yet."
        )


# ==========================================================
# TOPICS
# ==========================================================

elif page == "Topics":

    st.title("📝 Study Topics")

    subjects = get_subjects()

    if not subjects:

        st.warning(
            "Please add a subject first."
        )

    else:

        subject_dictionary = {
            name: subject_id
            for subject_id, name in subjects
        }

        with st.form("topic_form"):

            subject_name = st.selectbox(
                "Subject",
                list(subject_dictionary.keys())
            )

            topic_name = st.text_input(
                "Topic",
                placeholder="Example: Python Functions"
            )

            priority = st.selectbox(
                "Priority",
                [
                    "Low",
                    "Medium",
                    "High"
                ]
            )

            submitted = st.form_submit_button(
                "➕ Add Topic"
            )

            if submitted:

                if topic_name.strip():

                    add_topic(
                        subject_dictionary[subject_name],
                        topic_name.strip(),
                        priority
                    )

                    st.success(
                        "Topic added successfully!"
                    )

                    st.rerun()

                else:

                    st.warning(
                        "Please enter a topic."
                    )

        st.divider()

        topics = get_topics()

        if topics:

            st.subheader("Your Topics")

            for topic in topics:

                topic_id = topic[0]
                subject = topic[1]
                topic_name = topic[2]
                priority = topic[3]
                status = topic[4]

                col1, col2, col3, col4 = st.columns(
                    [3, 2, 1.5, 1]
                )

                with col1:

                    st.write(
                        f"**{topic_name}**"
                    )

                    st.caption(
                        subject
                    )

                with col2:

                    new_status = st.selectbox(
                        "Status",
                        [
                            "Not Started",
                            "In Progress",
                            "Completed"
                        ],
                        index=[
                            "Not Started",
                            "In Progress",
                            "Completed"
                        ].index(status),
                        key=f"status_{topic_id}"
                    )

                    if new_status != status:

                        update_topic_status(
                            topic_id,
                            new_status
                        )

                        st.rerun()

                with col3:

                    st.write(
                        f"Priority: **{priority}**"
                    )

                with col4:

                    if st.button(
                        "🗑️",
                        key=f"delete_topic_{topic_id}"
                    ):

                        delete_topic(
                            topic_id
                        )

                        st.rerun()

                st.divider()

        else:

            st.info(
                "No topics added yet."
            )


# ==========================================================
# STUDY SESSIONS
# ==========================================================

elif page == "Study Sessions":

    st.title("⏱️ Study Sessions")

    subjects = get_subjects()

    if not subjects:

        st.warning(
            "Please add a subject first."
        )

    else:

        subject_dictionary = {
            name: subject_id
            for subject_id, name in subjects
        }

        with st.form("session_form"):

            subject_name = st.selectbox(
                "Subject",
                list(subject_dictionary.keys())
            )

            hours = st.number_input(
                "Study Hours",
                min_value=0.1,
                max_value=24.0,
                value=1.0,
                step=0.5
            )

            study_date = st.date_input(
                "Study Date",
                value=date.today()
            )

            notes = st.text_area(
                "Notes",
                placeholder="What did you study?"
            )

            submitted = st.form_submit_button(
                "➕ Record Session"
            )

            if submitted:

                add_study_session(
                    subject_dictionary[subject_name],
                    hours,
                    study_date.isoformat(),
                    notes
                )

                st.success(
                    "Study session recorded!"
                )

                st.rerun()

        st.divider()

        sessions = get_study_sessions()

        if sessions:

            session_df = pd.DataFrame(
                sessions,
                columns=[
                    "ID",
                    "Subject",
                    "Hours",
                    "Date",
                    "Notes"
                ]
            )

            st.dataframe(
                session_df[
                    [
                        "Subject",
                        "Hours",
                        "Date",
                        "Notes"
                    ]
                ],
                use_container_width=True,
                hide_index=True
            )

        else:

            st.info(
                "No study sessions recorded yet."
            )


# ==========================================================
# PROGRESS
# ==========================================================

elif page == "Progress":

    st.title("📊 Progress Analytics")

    subjects = get_subjects()
    topics = get_topics()
    sessions = get_study_sessions()

    if not subjects:

        st.info(
            "Add subjects and topics to see your progress."
        )

    else:

        # -------------------------
        # SUBJECT PROGRESS
        # -------------------------

        progress_data = []

        for subject_id, subject_name in subjects:

            subject_topics = [
                topic for topic in topics
                if topic[1] == subject_name
            ]

            total = len(subject_topics)

            completed = len([
                topic for topic in subject_topics
                if topic[4] == "Completed"
            ])

            percentage = (
                completed / total * 100
                if total > 0
                else 0
            )

            progress_data.append({
                "Subject": subject_name,
                "Total Topics": total,
                "Completed": completed,
                "Progress": percentage
            })

        progress_df = pd.DataFrame(
            progress_data
        )

        st.subheader(
            "Subject Progress"
        )

        st.dataframe(
            progress_df,
            use_container_width=True,
            hide_index=True
        )

        # -------------------------
        # PROGRESS CHART
        # -------------------------

        if not progress_df.empty:

            st.subheader(
                "📈 Progress Chart"
            )

            fig, ax = plt.subplots()

            ax.bar(
                progress_df["Subject"],
                progress_df["Progress"]
            )

            ax.set_ylabel(
                "Progress (%)"
            )

            ax.set_xlabel(
                "Subjects"
            )

            ax.set_title(
                "Subject-wise Study Progress"
            )

            ax.set_ylim(
                0,
                100
            )

            plt.xticks(
                rotation=45,
                ha="right"
            )

            st.pyplot(
                fig
            )

        # -------------------------
        # STUDY HOURS
        # -------------------------

        if sessions:

            st.subheader(
                "⏱️ Study Hours by Subject"
            )

            session_df = pd.DataFrame(
                sessions,
                columns=[
                    "ID",
                    "Subject",
                    "Hours",
                    "Date",
                    "Notes"
                ]
            )

            hours_df = (
                session_df
                .groupby("Subject")["Hours"]
                .sum()
                .reset_index()
            )

            fig2, ax2 = plt.subplots()

            ax2.bar(
                hours_df["Subject"],
                hours_df["Hours"]
            )

            ax2.set_xlabel(
                "Subject"
            )

            ax2.set_ylabel(
                "Hours"
            )

            ax2.set_title(
                "Total Study Hours"
            )

            plt.xticks(
                rotation=45,
                ha="right"
            )

            st.pyplot(
                fig2
            )