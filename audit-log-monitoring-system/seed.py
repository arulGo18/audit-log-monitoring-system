import requests

url = "http://127.0.0.1:8000/log"

data_list = [

    {"user_id": "andi", "action": "SELECT", "table_name": "users"},
    {"user_id": "budi", "action": "INSERT", "table_name": "orders"},
    {"user_id": "cahya", "action": "UPDATE", "table_name": "products"},
    {"user_id": "dimas", "action": "DELETE", "table_name": "payments"},
    {"user_id": "eko", "action": "SELECT", "table_name": "transactions"},
    {"user_id": "fajar", "action": "UPDATE", "table_name": "users"},
    {"user_id": "galih", "action": "INSERT", "table_name": "products"},
    {"user_id": "hanif", "action": "SELECT", "table_name": "orders"},
    {"user_id": "indra", "action": "DELETE", "table_name": "transactions"},
    {"user_id": "joko", "action": "SELECT", "table_name": "payments"},
    {"user_id": "kevin", "action": "UPDATE", "table_name": "orders"},
    {"user_id": "luthfi", "action": "INSERT", "table_name": "users"},
    {"user_id": "miko", "action": "SELECT", "table_name": "products"},
    {"user_id": "nanda", "action": "DELETE", "table_name": "orders"},
    {"user_id": "opri", "action": "SELECT", "table_name": "transactions"},
    {"user_id": "putra", "action": "UPDATE", "table_name": "payments"},
    {"user_id": "qori", "action": "INSERT", "table_name": "products"},
    {"user_id": "rizky", "action": "SELECT", "table_name": "users"},
    {"user_id": "surya", "action": "DELETE", "table_name": "transactions"},
    {"user_id": "tono", "action": "SELECT", "table_name": "orders"},
    {"user_id": "udin", "action": "UPDATE", "table_name": "products"},
    {"user_id": "vito", "action": "INSERT", "table_name": "payments"},
    {"user_id": "wahyu", "action": "SELECT", "table_name": "transactions"},
    {"user_id": "xavier", "action": "DELETE", "table_name": "users"},
    {"user_id": "yusuf", "action": "SELECT", "table_name": "orders"},
    {"user_id": "zaki", "action": "UPDATE", "table_name": "products"},
    {"user_id": "farhan", "action": "INSERT", "table_name": "transactions"},
    {"user_id": "aditya", "action": "SELECT", "table_name": "payments"},
    {"user_id": "bagas", "action": "DELETE", "table_name": "orders"},
    {"user_id": "candra", "action": "SELECT", "table_name": "users"},
]

for data in data_list:
    res = requests.post(url, json=data)
    print(res.json())