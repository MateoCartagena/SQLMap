# app/app.py

from flask import Flask, request, jsonify
import mysql.connector
import time
import os # Importar el módulo 'os'

app = Flask(__name__)

def get_db_connection():
    # El host ahora es 'mysql', el nombre del servicio en docker-compose.yml
    # Las credenciales son las mismas que definiste en docker-compose.yml
    return mysql.connector.connect(
        host='mysql',
        user='user',
        password='pass',
        database='testdb'
    )

@app.route("/user", methods=["GET"])
def get_user():
    user_id = request.args.get("id")

    # Bucle de reintento para esperar a la base de datos
    conn = None
    for _ in range(10): # Intentar por 20 segundos
        try:
            conn = get_db_connection()
            break
        except mysql.connector.Error as err:
            print(f"Error conectando a la base de datos: {err}. Reintentando en 2 segundos...")
            time.sleep(2)
    
    if not conn:
        return jsonify({"error": "No se pudo conectar a la base de datos"}), 500

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