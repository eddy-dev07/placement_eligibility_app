from backend.db_connection import DatabaseConnection

class QueryManager:
    def __init__(self):
        self.db = DatabaseConnection()
        self.db.connect()

    def get_eligible_students(self, min_problems=50, min_soft_skill=75):
        query = """
        SELECT s.student_id, s.name, s.age, p.problems_solved, 
               ss.communication, ss.teamwork, pl.placement_status
        FROM students s
        JOIN programming p ON s.student_id = p.student_id
        JOIN soft_skills ss ON s.student_id = ss.student_id
        JOIN placements pl ON s.student_id = pl.student_id
        WHERE p.problems_solved >= ?
          AND ((ss.communication + ss.teamwork + ss.presentation)/3) >= ?
          AND pl.placement_status != 'Not Ready'
        """
        return self.db.execute_query(query, (min_problems, min_soft_skill))

    def get_average_programming_by_batch(self):
        query = """
        SELECT s.course_batch, AVG(p.problems_solved) as avg_solved
        FROM students s
        JOIN programming p ON s.student_id = p.student_id
        GROUP BY s.course_batch
        """
        return self.db.execute_query(query)

    def get_top_5_placements(self):
        query = """
        SELECT s.name, pl.placement_package
        FROM students s
        JOIN placements pl ON s.student_id = pl.student_id
        WHERE pl.placement_status = 'Placed'
        ORDER BY pl.placement_package DESC
        LIMIT 5
        """
        return self.db.execute_query(query)

    def get_soft_skills_distribution(self):
        query = """
        SELECT 
            ROUND((communication + teamwork + presentation + leadership + critical_thinking + interpersonal_skills)/6.0) AS avg_score,
            COUNT(*) AS student_count
        FROM soft_skills
        GROUP BY avg_score
        ORDER BY avg_score DESC
        """
        return self.db.execute_query(query)

    def get_total_students_placed(self):
        query = """
        SELECT COUNT(*) 
        FROM placements
        WHERE placement_status = 'Placed'
        """
        return self.db.execute_query(query)

    def get_students_with_internships(self):
        query = """
        SELECT s.name, pl.internships_completed
        FROM students s
        JOIN placements pl ON s.student_id = pl.student_id
        WHERE pl.internships_completed >= 1
        """
        return self.db.execute_query(query)

    def get_avg_mock_scores_by_batch(self):
        query = """
        SELECT s.course_batch, AVG(pl.mock_interview_score)
        FROM students s
        JOIN placements pl ON s.student_id = pl.student_id
        GROUP BY s.course_batch
        """
        return self.db.execute_query(query)

    def get_students_not_ready(self):
        query = """
        SELECT s.name, pl.placement_status
        FROM students s
        JOIN placements pl ON s.student_id = pl.student_id
        WHERE pl.placement_status = 'Not Ready'
        """
        return self.db.execute_query(query)
    
    def get_students_by_age(self):
     query = """
     SELECT age, COUNT(*) as student_count
     FROM students
     GROUP BY age
     ORDER BY age
     """
     return self.db.execute_query(query)
 

    def get_certification_distribution(self):
        query = """
        SELECT certifications_earned, COUNT(*) as student_count
        FROM programming
        GROUP BY certifications_earned
        ORDER BY certifications_earned DESC
        """
        return self.db.execute_query(query)

    def get_avg_project_scores(self):
        query = """
        SELECT AVG(latest_project_score)
        FROM programming
        """
        return self.db.execute_query(query)

    def get_placed_students(self):
        query = """
        SELECT * FROM placements
        WHERE placement_status = 'Placed'
        """
        return self.db.execute_query(query)

    def get_not_placed_students(self):
        query = """
        SELECT * FROM placements
        WHERE placement_status = 'Ready'
        """
        return self.db.execute_query(query)

    def get_top_problem_solvers(self):
        query = """
        SELECT s.name, p.problems_solved
        FROM students s
        JOIN programming p ON s.student_id = p.student_id
        ORDER BY p.problems_solved DESC
        LIMIT 5
        """
        return self.db.execute_query(query)

    def get_students_with_low_soft_skills(self):
        query = """
        SELECT s.name, ((communication + teamwork + presentation)/3.0) as avg_soft
        FROM students s
        JOIN soft_skills ss ON s.student_id = ss.student_id
        WHERE ((communication + teamwork + presentation)/3.0) < 40
        """
        return self.db.execute_query(query)

    def get_avg_problem_score(self):
        query = """
        SELECT AVG(problems_solved) FROM programming
        """
        result = self.db.execute_query(query)
        return round(result[0][0], 2) if result else 0

    def get_avg_soft_skills(self):
        query = """
        SELECT AVG((communication + teamwork + presentation)/3.0)
        FROM soft_skills
        """
        result = self.db.execute_query(query)
        return round(result[0][0], 2) if result else 0

    def get_students_above_avg_coding(self):
        query = """
        SELECT s.name, p.problems_solved
        FROM students s
        JOIN programming p ON s.student_id = p.student_id
        WHERE p.problems_solved > (
            SELECT AVG(problems_solved) FROM programming
        )
        """
        return self.db.execute_query(query)
    
    def get_excellent_students(self):
     query = """
      SELECT s.name, p.problems_solved, 
           ((ss.communication + ss.teamwork + ss.presentation)/3.0) AS avg_soft_skill
     FROM students s
     JOIN programming p ON s.student_id = p.student_id
     JOIN soft_skills ss ON s.student_id = ss.student_id
      WHERE p.problems_solved > 150 
      AND ((ss.communication + ss.teamwork + ss.presentation)/3.0) > 85
     """
     return self.db.execute_query(query)


    def get_count_by_status(self):
      query = """
      SELECT placement_status, COUNT(*) as count
      FROM placements
      GROUP BY placement_status
      ORDER BY count DESC
      """
      return self.db.execute_query(query)

    def get_top_soft_skills(self):
        query = """
        SELECT s.name, 
               ROUND((ss.communication + ss.teamwork + ss.presentation + ss.leadership + ss.critical_thinking + ss.interpersonal_skills)/6.0, 2) AS avg_soft_skill
        FROM students s
        JOIN soft_skills ss ON s.student_id = ss.student_id
        ORDER BY avg_soft_skill DESC
        LIMIT 5
        """
        return self.db.execute_query(query)


    def close(self):
        self.db.disconnect()

