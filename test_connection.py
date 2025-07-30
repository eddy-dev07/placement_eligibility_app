from backend.db_connection import DatabaseConnection

db = DatabaseConnection()
db.connect()

# Run a test query
result = db.execute_query("SELECT * FROM students LIMIT 5;")

# Print results
if result:
    for row in result:
        print(row)
else:
    print(" No data found.")

db.disconnect()
