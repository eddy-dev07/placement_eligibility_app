import streamlit as st
import pandas as pd
from query_manager import QueryManager

st.set_page_config(page_title="Placement Eligibility App", layout="wide")
st.title("🎓 Placement Eligibility Dashboard")

qm = QueryManager()

# Sidebar filters
st.sidebar.header(" Filter Criteria")
min_problems = st.sidebar.slider("Min Problems Solved (Coding)", 0, 200, 50)
min_soft_skill = st.sidebar.slider("Min Avg Soft Skill Score", 0, 100, 75)

# Section 1: Eligible Students
st.subheader(" Eligible Students")
eligible = qm.get_eligible_students(min_problems, min_soft_skill)
if eligible:
    df_eligible = pd.DataFrame(eligible, columns=[
        "Student ID", "Name", "Age", "Problems Solved", "Communication", "Teamwork", "Placement Status"
    ])
    st.success(f"Total Eligible: {len(df_eligible)}")
    st.dataframe(df_eligible)
else:
    st.warning("No students matched the criteria.")

# Section 2: Placement Distribution (Filtered)
with st.expander(" Placement Status Distribution (Filtered)"):
    placed_count = sum(1 for row in eligible if row[-1] == "Placed")
    not_placed_count = sum(1 for row in eligible if row[-1] != "Placed")
    st.write(f" Placed (Filtered): {placed_count} students")
    st.write(f" Not Placed (Filtered): {not_placed_count} students")

# Section 3: Top 5 Problem Solvers
with st.expander(" Top 5 Problem Solvers"):
    top_coders = qm.get_top_problem_solvers()
    st.table(pd.DataFrame(top_coders, columns=["Name", "Problems Solved"]))

# Section 4: Low Soft Skills
with st.expander(" Students with Soft Skills < 40"):
    low_soft = qm.get_students_with_low_soft_skills()
    st.table(pd.DataFrame(low_soft, columns=["Name", "Avg Soft Skills"]))

# Section 5: Average Scores
with st.expander(" Average Scores"):
    avg_prog = qm.get_avg_problem_score()
    avg_soft = qm.get_avg_soft_skills()
    st.write(f" Avg Programming Score: {avg_prog}")
    st.write(f" Avg Soft Skill Score: {avg_soft}")

# Section 6: Students Above Average Problem Solving
with st.expander(" Students Above Avg Coding Score"):
    above_avg = qm.get_students_above_avg_coding()
    st.table(pd.DataFrame(above_avg, columns=["Name", "Problems Solved"]))

# Section 7: Students with Excellent Skills
with st.expander(" Students with Coding > 150 and Soft Skills > 85"):
    excellent = qm.get_excellent_students()
    st.table(pd.DataFrame(excellent, columns=["Name", "Problems Solved", "Avg Soft Skills"]))

# Section 8: Students by Age (Grouped)
with st.expander(" Students Grouped by Age"):
    age_groups = qm.get_students_by_age()
    st.table(pd.DataFrame(age_groups, columns=["Age", "Count"]))

# Section 9: Count by Placement Status
with st.expander(" Count by Placement Status"):
    status_counts = qm.get_count_by_status()
    st.table(pd.DataFrame(status_counts, columns=["Placement Status", "Count"]))

# Section 10: Top 5 by Soft Skills
with st.expander(" Top 5 by Soft Skills Score"):
    top_soft = qm.get_top_soft_skills()
    st.table(pd.DataFrame(top_soft, columns=["Name", "Avg Soft Skills"]))
    
   


# Cleanup
qm.close()
