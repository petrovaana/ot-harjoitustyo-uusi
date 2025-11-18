from database_connection import get_database_connection
import os

#Asked AI to edit this file so that my database would finally work
#AI Generated code begins

def initialize_database():
    data_dir = os.path.join(os.path.dirname(__file__), "..", "data")
    os.makedirs(data_dir, exist_ok=True)

    connection = get_database_connection()
    cursor = connection.cursor()

    schema_path = os.path.join(
        os.path.dirname(__file__),
        "schema.sql"
    )

    with open(schema_path, "r", encoding="utf-8") as f:
        sql_script = f.read()
    
    cursor.executescript(sql_script)
    connection.commit()
    connection.close()

if __name__ == "__main__":
    initialize_database()

#AI Generated code ends. 