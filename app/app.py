from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)
DATABASE = "/data/news.db"

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
    if not title or not content:
        return jsonify({"error": "Title and content are required"}), 400

    conn = get_db_connection()
    conn.execute('INSERT INTO news (title, content) VALUES (?, ?)', (title, content))
    conn.commit()
    conn.close()
    return jsonify({"message": "News added successfully!"}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
