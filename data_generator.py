from faker import Faker
import sqlite3
import random

fake = Faker()

# Connect to SQLite DB
conn = sqlite3.connect("placement_eligibility.db")
cursor = conn.cursor()

# ---------- STUDENTS TABLE ----------
cursor.execute('''
CREATE TABLE IF NOT EXISTS students (
    student_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER,
    gender TEXT,
    email TEXT,
    phone TEXT,
    enrollment_year INTEGER,
    course_batch TEXT,
    city TEXT,
    graduation_year INTEGER
)
''')

# Insert students
student_ids = []
for _ in range(100):
    name = fake.name()
    age = random.randint(20, 25)
    gender = random.choice(['Male', 'Female', 'Other'])
    email = fake.email()
    phone = fake.phone_number()
    enrollment_year = random.randint(2019, 2023)
    course_batch = random.choice(['Batch A', 'Batch B', 'Batch C'])
    city = fake.city()
    graduation_year = enrollment_year + 3

    cursor.execute('''
    INSERT INTO students (name, age, gender, email, phone, enrollment_year, course_batch, city, graduation_year)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (name, age, gender, email, phone, enrollment_year, course_batch, city, graduation_year))

    student_ids.append(cursor.lastrowid)

# ---------- PROGRAMMING TABLE ----------
cursor.execute('''
CREATE TABLE IF NOT EXISTS programming (
    programming_id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER,
    language TEXT,
    problems_solved INTEGER,
    assessments_completed INTEGER,
    mini_projects INTEGER,
    certifications_earned INTEGER,
    latest_project_score INTEGER,
    FOREIGN KEY(student_id) REFERENCES students(student_id)
)
''')

for sid in student_ids:
    language = random.choice(['Python', 'Java', 'SQL'])
    problems_solved = random.randint(20, 200)
    assessments_completed = random.randint(1, 10)
    mini_projects = random.randint(0, 5)
    certifications_earned = random.randint(0, 3)
    latest_project_score = random.randint(50, 100)

    cursor.execute('''
    INSERT INTO programming (student_id, language, problems_solved, assessments_completed, mini_projects, certifications_earned, latest_project_score)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (sid, language, problems_solved, assessments_completed, mini_projects, certifications_earned, latest_project_score))

# ---------- SOFT SKILLS TABLE ----------
cursor.execute('''
CREATE TABLE IF NOT EXISTS soft_skills (
    soft_skill_id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER,
    communication INTEGER,
    teamwork INTEGER,
    presentation INTEGER,
    leadership INTEGER,
    critical_thinking INTEGER,
    interpersonal_skills INTEGER,
    FOREIGN KEY(student_id) REFERENCES students(student_id)
)
''')

for sid in student_ids:
    communication = random.randint(60, 100)
    teamwork = random.randint(60, 100)
    presentation = random.randint(60, 100)
    leadership = random.randint(60, 100)
    critical_thinking = random.randint(60, 100)
    interpersonal_skills = random.randint(60, 100)

    cursor.execute('''
    INSERT INTO soft_skills (student_id, communication, teamwork, presentation, leadership, critical_thinking, interpersonal_skills)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (sid, communication, teamwork, presentation, leadership, critical_thinking, interpersonal_skills))

# ---------- PLACEMENTS TABLE ----------
cursor.execute('''
CREATE TABLE IF NOT EXISTS placements (
    placement_id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER,
    mock_interview_score INTEGER,
    internships_completed INTEGER,
    placement_status TEXT,
    company_name TEXT,
    placement_package REAL,
    interview_rounds_cleared INTEGER,
    placement_date TEXT,
    FOREIGN KEY(student_id) REFERENCES students(student_id)
)
''')

for sid in student_ids:
    mock_score = random.randint(50, 100)
    internships = random.randint(0, 3)
    status = random.choice(['Placed', 'Ready', 'Not Ready'])
    company = fake.company() if status == 'Placed' else ''
    package = round(random.uniform(3.0, 12.0), 2) if status == 'Placed' else 0
    rounds = random.randint(1, 5) if status == 'Placed' else 0
    date = fake.date_this_year() if status == 'Placed' else ''

    cursor.execute('''
    INSERT INTO placements (student_id, mock_interview_score, internships_completed, placement_status,
    company_name, placement_package, interview_rounds_cleared, placement_date)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', (sid, mock_score, internships, status, company, package, rounds, date))

# Commit changes
conn.commit()
conn.close()

print(" All tables created and populated successfully.")
