from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(
        host='localhost',
        user='user',
        password='pass',
        database='testdb'
    )

@app.route("/user", methods=["GET"])
def get_user():
    user_id = request.args.get("id")
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    
    # ❌ Consulta vulnerable a SQLi
    query = f"SELECT * FROM users WHERE id = {user_id};"
    cursor.execute(query)
    result = cursor.fetchall()

    cursor.close()
    conn.close()
    return jsonify(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
