import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="audit_db",
    user="postgres",
    password="pasword anda"
)

cursor = conn.cursor()