from flask import Flask, request
import sqlite3

#Connect flask to the database
def get_db_connection():
    conn = sqlite3.connect('tasks.db')
    conn.row_factory = sqlite3.Row
    return conn

app = Flask(__name__)

@app.route('/add', methods=['POST'])
def add_task():
    data = request.get_json()
    if 'title' not in data:
        return {"error": "Task title required"}, 400

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        'INSERT INTO tasks (Task_Name) VALUES (?)',
        (data['title'],)
    )
    conn.commit()
    task_id = cursor.lastrowid
    conn.close()

    return {"Task_Id": task_id, "Task_Name": data['title'], "done": False}, 201

