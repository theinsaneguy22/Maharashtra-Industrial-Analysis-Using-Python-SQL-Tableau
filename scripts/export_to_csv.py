import pandas as pd
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="maharashtra_industry"
)

query = "SELECT * FROM industries"

df = pd.read_sql(query, conn)

df.to_excel("data/exports/mysql_export.xlsx", index=False)

conn.close()

print("✅ MySQL data exported to Excel successfully!")