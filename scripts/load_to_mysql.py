import numpy as np
import pandas as pd
import mysql.connector

df = pd.read_csv("data/processed/cleaned_full_data.csv")
df = df.replace({np.nan: None})

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="maharashtra_industry"
)

cursor = conn.cursor()

for _, row in df.iterrows():
    cursor.execute("""
        INSERT INTO industries
        (industrial_zone, city_district, industry_type,
         turnover_in_crores, estimated_profit_cr,
         business_size, zone_rank, number_of_companies)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
    """, (
        row["Industrial_Area"],
        row["City/District"],
        row["Industry_Type"],
        row["Turnover_in_Crores"],
        row["Estimated_Profit_Cr"],
        row["Business_Size"],
        row["Zone_Rank"],
        row["Number_of_Companies"]
    ))

conn.commit()
print("✅ Data Loaded into MySQL")