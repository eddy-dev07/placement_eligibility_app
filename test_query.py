from query_manager import QueryManager

qm = QueryManager()

print(" Eligible Students:")
for row in qm.get_eligible_students():
    print(row)

print("\n Avg Programming by Batch:")
for row in qm.get_average_programming_by_batch():
    print(row)

print("\n Top 5 Placement Packages:")
for row in qm.get_top_5_placements():
    print(row)

#  New Queries (PDF-based Insights)
print("\n Soft Skills Distribution:")
for row in qm.get_soft_skills_distribution():
    print(row)

print("\n Average Mock Interview Score by Batch:")
for row in qm.get_avg_mock_scores_by_batch():
    print(row)

print("\n Students Not Ready for Placement:")
for row in qm.get_students_not_ready():
    print(row)

print("\n Students with Internships:")
for row in qm.get_students_with_internships():
    print(row)

print("\n Total Students Placed:")
for row in qm.get_total_students_placed():
    print(row)

print("\n Certification Distribution:")
for row in qm.get_certification_distribution():
    print(row)

print("\n Average Project Score:")
for row in qm.get_avg_project_scores():
    print(row)

qm.close()
