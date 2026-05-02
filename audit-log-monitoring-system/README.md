# Audit Log Monitoring System

## Overview
This project is a simple audit logging and monitoring system that tracks user activity, stores logs in a PostgreSQL database, and visualizes insights through a dashboard.

## Features
- Record user activity (audit trail)
- Store logs into PostgreSQL
- Retrieve and filter logs
- Generate user activity statistics
- Interactive dashboard visualization

## Tech Stack
- FastAPI (Backend API)
- PostgreSQL (Database)
- Streamlit (Dashboard)
- Python


## Architecture
User  - FastAPI  - PostgreSQL - Streamlit Dashboard

## To run
1. Install dependencies
2. Run backend
3. Run dashboard

4. Structure Database : 
CREATE TABLE audit_logs (
id SERIAL PRIMARY KEY,
user_id VARCHAR(50),
action VARCHAR(20),
table_name VARCHAR(50),
timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
ip_address VARCHAR(50)
);