import streamlit as st
from query_manager import QueryManager

st.set_page_config(page_title="Placement Eligibility App", layout="centered")

st.title("🎓 Placement Eligibility Dashboard")

qm = QueryManager()

# Sidebar filters
st.sidebar.header(" Filter Criteria")
min_problems = st.sidebar.slider("Min Problems Solved (Coding)", 0, 200, 50)
min_soft_skill = st.sidebar.slider("Min Avg Soft Skill Score", 0, 100, 75)

# Fetch and display eligible students
st.subheader(" Eligible Students")
eligible = qm.get_eligible_students(min_problems, min_soft_skill)

if eligible:
    st.write("Total Eligible:", len(eligible))
    st.dataframe(eligible)
else:
    st.warning("No students matched the criteria.")

qm.close()
