from flask import Flask, request, render_template
import psycopg2
from werkzeug.security import generate_password_hash

app = Flask(__name__)

# Opret forbindelse til PostgreSQL ved hjælp af psycopg2
def get_db_connection():
    conn = psycopg2.connect('postgresql://avnadmin:AVNS_GEfpyamT7kd4de4fIwU@pg-2f37e134-empire1266.f.aivencloud.com:19276/registering?sslmode=require')
    return conn

@app.route('/')
def index():
    return render_template('registration.html')

@app.route('/register', methods=['POST'])
def register():
    username = request.form.get('username')
    email = request.form.get('email')
    password = request.form.get('password')
    user_type = request.form.get('user_type')
    terms = request.form.get('terms')

    # Simpel validering
    if not all([username, email, password, user_type, terms]):
        return "Alle felter skal udfyldes og betingelserne accepteres.", 400

    # Hash adgangskoden
    hashed_password = generate_password_hash(password)

    # Forbind til databasen
    conn = get_db_connection()
    cur = conn.cursor()

    # Opret tabellen users, hvis den ikke findes (dette gør vi én gang)
    cur.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            username VARCHAR(80) NOT NULL,
            email VARCHAR(120) NOT NULL,
            password VARCHAR(255) NOT NULL,
            user_type VARCHAR(20) NOT NULL
        )
    ''')

    # Indsæt brugerens data i databasen
    cur.execute('INSERT INTO users (username, email, password, user_type) VALUES (%s, %s, %s, %s)',
                (username, email, hashed_password, user_type))

    conn.commit()

    # Luk forbindelsen
    cur.close()
    conn.close()

    return f"Tak for din registrering, {username}!"

if __name__ == '__main__':
    app.run(debug=True)
