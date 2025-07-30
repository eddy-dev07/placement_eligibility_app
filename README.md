#  Placement Eligibility App

This is a Streamlit-based web application that checks the placement eligibility of students based on their programming scores, soft skills scores, and placement status. It is built using Python, SQLite, and Faker for realistic test data generation.

##  Features

- Generates fake student data using Faker
- Stores data in SQLite database
- Filters students by programming and soft skill score thresholds
- Displays eligible students using SQL joins
- Interactive frontend built with Streamlit

## Technologies Used

- Python
- Streamlit
- SQLite
- Faker (for fake data)

 ##  Project Structure

```
placement_eligibility_app/
├── backend/
│   └── db_connection.py       # Handles database connection
├── query_manager.py           # SQL queries for student data
├── streamlit_app.py           # Streamlit-based frontend
├── placement_eligibility.db   # SQLite database
└── test/ (optional)
    ├── test_connection.py
    └── test_query.py
```

##  How to Run

```bash
pip install streamlit
streamlit run streamlit_app.py
```

##  Requirements

```bash
pip install streamlit faker
```


##  Author

- Aaditya Bhardwaj

 This project is part of the GUVI AI/ML course submission.

