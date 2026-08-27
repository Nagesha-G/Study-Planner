# 📚 Student Study Planner

A simple and practical **Python-based study management web application** that helps students organize subjects, manage study topics, record study sessions, and track their learning progress.

## 🚀 Features

* 📚 Add and manage subjects
* 📝 Create and manage study topics
* 🎯 Set topic priorities
* ✅ Track topic status

  * Not Started
  * In Progress
  * Completed
* ⏱️ Record study sessions and study hours
* 📊 View overall learning progress
* 📈 View subject-wise progress
* 📉 Analyze total study hours
* 💾 Store data using SQLite
* 🖥️ Simple web interface using Streamlit

## 🛠️ Technologies Used

* **Python** — Application logic
* **Streamlit** — Web interface
* **SQLite** — Database
* **Pandas** — Data processing
* **Matplotlib** — Data visualization

## 📂 Project Structure

```text
student-study-planner/
│
├── app.py
├── database.py
├── requirements.txt
├── README.md
└── study_planner.db
```

### File Description

| File               | Purpose                                           |
| ------------------ | ------------------------------------------------- |
| `app.py`           | Main Streamlit application                        |
| `database.py`      | Database creation and database operations         |
| `requirements.txt` | Required Python packages                          |
| `README.md`        | Project documentation                             |
| `study_planner.db` | SQLite database created when the application runs |

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/student-study-planner.git
```

### 2. Open the project directory

```bash
cd student-study-planner
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

**Windows:**

```bash
venv\Scripts\activate
```

**Linux/macOS:**

```bash
source venv/bin/activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

## ▶️ Run the Application

Start the Streamlit application:

```bash
streamlit run app.py
```

The application will open in your web browser.

## 🧩 How It Works

The application follows a simple architecture:

```text
              Student
                 │
                 ↓
          Streamlit Interface
                 │
                 ↓
              app.py
                 │
                 ↓
           database.py
                 │
                 ↓
             SQLite
                 │
        ┌────────┼────────┐
        ↓        ↓        ↓
    Subjects   Topics   Sessions
```

### Subjects

Students can create subjects such as:

```text
Python
Mathematics
Networking
Database
Operating Systems
```

### Topics

Topics can be organized under each subject:

```text
Python
├── Variables
├── Functions
├── OOP
├── File Handling
└── APIs
```

Each topic can have a priority:

```text
Low
Medium
High
```

And a status:

```text
Not Started
In Progress
Completed
```

### Study Sessions

Students can record:

```text
Subject: Python
Hours: 2
Date: 2026-08-27
Notes: Practiced functions and classes
```

The application uses this information to calculate study statistics.

## 📊 Dashboard

The dashboard provides an overview of:

* Total subjects
* Total topics
* Completed topics
* Total study hours
* Overall completion percentage
* Recent topics

Example:

```text
Subjects       Topics       Completed       Study Hours
   5             25            12              32.5
```

## 📈 Progress Analytics

The application generates charts showing:

* Subject-wise completion percentage
* Total study hours by subject

This helps students identify which subjects need more attention.

## 🗄️ Database

The project uses SQLite with three main tables:

```text
subjects
   │
   ├── topics
   │
   └── study_sessions
```

### Subjects Table

Stores subject information.

### Topics Table

Stores:

* Topic name
* Subject
* Priority
* Completion status
* Creation date

### Study Sessions Table

Stores:

* Subject
* Study hours
* Study date
* Study notes

## 🎯 Project Objective

The objective of this project is to build a simple study management system while demonstrating practical skills in:

* Python programming
* Database management
* CRUD operations
* Data analysis
* Data visualization
* Web application development

## 🔮 Future Improvements

The project can be extended with:

* 🤖 AI-generated study plans
* 📅 Calendar-based scheduling
* 🔔 Study reminders
* 🔥 Study streak tracking
* 🧠 AI-generated quizzes
* 📖 Notes and learning resources
* 🎯 Exam preparation mode
* 📊 Advanced learning analytics
* 👤 User authentication
* ☁️ Cloud database
* 📱 Mobile-friendly interface

## 🤝 Contributing

Contributions are welcome.

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Commit your changes
5. Push the branch
6. Create a Pull Request

## 📄 License

This project is open-source and available for educational and personal use.

## 👨‍💻 Author

**Nagesha G**

Built with Python, Streamlit, SQLite, Pandas, and Matplotlib.

---

⭐ If you find this project useful, consider giving the repository a star!
