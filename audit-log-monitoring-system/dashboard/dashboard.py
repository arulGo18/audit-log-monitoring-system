import streamlit as st
import requests
import pandas as pd

st.title("📊 Audit Log Dashboard")

API_URL = "http://127.0.0.1:8000"

#get data
logs_res = requests.get(f"{API_URL}/logs")
stats_res = requests.get(f"{API_URL}/logs/stats")

logs_data = logs_res.json()["logs"]
stats_data = stats_res.json()["stats"]

logs_df = pd.DataFrame(logs_data)
stats_df = pd.DataFrame(stats_data)

#metric
st.metric("Total Activity", len(logs_df))

#chart form data
st.subheader("User Activity")
st.bar_chart(stats_df.set_index("user_id"))

#filter
user_filter = st.selectbox("Filter User", ["All"] + list(logs_df["user_id"].unique()))

if user_filter != "All":
    logs_df = logs_df[logs_df["user_id"] == user_filter]

#table data from logs
st.subheader("Logs")
st.dataframe(logs_df)