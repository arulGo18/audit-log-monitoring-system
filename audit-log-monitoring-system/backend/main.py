from fastapi import FastAPI
from backend.db import conn, cursor
from pydantic import BaseModel
from datetime import datetime

app = FastAPI()


#model
class LogRequest(BaseModel):
    user_id: str
    action: str
    table_name: str

#root
@app.get("/")
def root():
    return {"message": "API running"}

#create log
@app.post("/log")
def create_log(log: LogRequest):
    query = """
        INSERT INTO audit_logs (user_id, action, table_name, timestamp, ip_address)
        VALUES (%s, %s, %s, %s, %s)
    """
    values = (
        log.user_id,
        log.action,
        log.table_name,
        datetime.now(),
        "127.0.0.1"
    )

    cursor.execute(query, values)
    conn.commit()

    return {"message": "Log berhasil disimpan"}

#get logs
@app.get("/logs")
def get_logs():
    cursor.execute("SELECT * FROM audit_logs")
    rows = cursor.fetchall()

    logs = []
    for row in rows:
        logs.append({
            "id": row[0],
            "user_id": row[1],
            "action": row[2],
            "table_name": row[3],
            "timestamp": str(row[4]),
            "ip_address": row[5]
        })

    return {"logs": logs}

#filter logs
@app.get("/logs/filter")
def filter_logs(user_id: str = None, action: str = None):
    query = "SELECT * FROM audit_logs WHERE 1=1"
    params = []

    if user_id:
        query += " AND user_id = %s"
        params.append(user_id)

    if action:
        query += " AND action = %s"
        params.append(action)

    cursor.execute(query, params)
    rows = cursor.fetchall()

    logs = []
    for row in rows:
        logs.append({
            "id": row[0],
            "user_id": row[1],
            "action": row[2],
            "table_name": row[3],
            "timestamp": str(row[4]),
            "ip_address": row[5]
        })

    return {"logs": logs}

#stats
@app.get("/logs/stats")
def get_stats():
    cursor.execute("""
        SELECT user_id, COUNT(*) as total
        FROM audit_logs
        GROUP BY user_id
        ORDER BY total DESC
    """)

    rows = cursor.fetchall()

    stats = []
    for row in rows:
        stats.append({
            "user_id": row[0],
            "total_activity": row[1]
        })

    return {"stats": stats}