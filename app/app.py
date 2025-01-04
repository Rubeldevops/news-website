from flask import Flask, request, jsonify, render_template
import sqlite3

app = Flask(_name_)
DATABASE = "news.db"

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def home():
    return jsonify({"message": "Welcome to the News API!"})

@app.route('/news', methods=['GET'])
def get_news():
    conn = get_db_connection()
    news = conn.execute('SELECT * FROM news').fetchall()
    conn.close()
    return jsonify([dict(row) for row in news])

@app.route('/news', methods=['POST'])
def add_news():
    new_data = request.json
    title = new_data.get('title')
    content = new_data.get('content')
    name = new_data.get('name')  # New field for the author's name

    if not title or not content or not name:
        return jsonify({"error": "Title, content, and name are required"}), 400

    conn = get_db_connection()
    conn.execute('INSERT INTO news (title, content, name) VALUES (?, ?, ?)', (title, content, name))
    conn.commit()
    conn.close()
    return jsonify({"message": "News added successfully!"}), 201

# New route for welcome page
@app.route('/welcome')
def welcome_page():
    return 
render_template('welcome.html')  # Render an HTML page

if _name_ == '_main_':
    app.run(host='0.0.0.0', port=5000)
