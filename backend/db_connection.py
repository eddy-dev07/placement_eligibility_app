import sqlite3

class DatabaseConnection:
    def __init__(self, db_name="placement_eligibility.db"):
        self.db_name = db_name
        self.conn = None
        self.cursor = None

    def connect(self):
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()
        print(" Connected to database")

    def disconnect(self):
        if self.conn:
            self.conn.close()
            print("🔌 Disconnected from database")

    def execute_query(self, query, params=None):
     if params:
        self.cursor.execute(query, params)
     else:
        self.cursor.execute(query)
     return self.cursor.fetchall()
