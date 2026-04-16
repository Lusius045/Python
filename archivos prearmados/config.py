import mysql.connector

DB = {
    "host":"localhost",
    "user":"root",
    "password":"admin",
    "database":"instituto"
}

def get_conn():
    return mysql.connector.connect(**DB)