import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="audit_db",
    user="postgres",
    password="P180304ilyas"  # pakai yang kamu tadi berhasil
)

cursor = conn.cursor()