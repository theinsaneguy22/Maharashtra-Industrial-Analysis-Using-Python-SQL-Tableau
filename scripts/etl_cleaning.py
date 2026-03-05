import pandas as pd

# 1. EXTRACT DATA

file_path = "data/raw/Maharashtra_Industrial_Zones_Noisy.xlsx"
df = pd.read_excel(file_path)

print("Original Data Loaded")
print(df.head())


# 2. DATA CLEANING

# Remove duplicates
df = df.drop_duplicates()

# Strip column names
df.columns = df.columns.str.strip()

# Clean turnover column (remove commas, spaces, symbols)
df["Estimated_Annual_Turnover_INR"] = (
    df["Estimated_Annual_Turnover_INR"]
    .astype(str)
    .str.replace(",", "")
    .str.replace("₹", "")
    .str.strip()
)

# Convert to numeric
df["Estimated_Annual_Turnover_INR"] = pd.to_numeric(
    df["Estimated_Annual_Turnover_INR"],
    errors="coerce"
)

# Fill missing turnover with median
df["Estimated_Annual_Turnover_INR"].fillna(
    df["Estimated_Annual_Turnover_INR"].median(),
    inplace=True
)

# Standardize City/District names
df["City/District"] = df["City/District"].str.title().str.strip()


print("Data Cleaning Completed")


# 3. CONVERT TURNOVER INTO CRORES

df["Turnover_in_Crores"] = df["Estimated_Annual_Turnover_INR"] / 10000000

print("Turnover Converted to Crores")


# 4. Profit Estimation 

# Profit estimation (assume 18% margin)
df["Estimated_Profit_Cr"] = df["Turnover_in_Crores"] * 0.18

print("Profit Column Added")


# 5. ADD BUSINESS SIZE CATEGORY

df["Business_Size"] = pd.cut(
    df["Turnover_in_Crores"],
    bins=[0, 10000, 20000, 40000],
    labels=["Small", "Medium", "Large"]
)

print("Business Size Category Added")


# 6. RANK ZONES

df["Zone_Rank"] = df["Turnover_in_Crores"].rank(
    ascending=False
)

print("Ranking Completed")


# 7. CITY SUMMARY TABLE

city_summary = df.groupby("City/District").agg({
    "Turnover_in_Crores": "sum",
    "Number_of_Companies": "sum"
}).reset_index()

print("\nCity Summary")
print(city_summary)


# 8. INDUSTRY SUMMARY TABLE

industry_summary = df.groupby("Industry_Type")[
    "Turnover_in_Crores"
].sum().reset_index()

print("\nIndustry Summary")
print(industry_summary)


# 9. TOP 5 INDUSTRIAL ZONES

top_zones = df.sort_values(
    by="Turnover_in_Crores",
    ascending=False
).head(5)

print("\nTop 5 Industrial Zones")
print(top_zones)


# 10. EXPORT FILES

df.to_csv("data/processed/cleaned_full_data.csv", index=False)
city_summary.to_csv("data/processed/city_summary.csv", index=False)
industry_summary.to_csv("data/processed/industry_summary.csv", index=False)
top_zones.to_csv("data/processed/top_zones.csv", index=False)

print("\n✅ All Files Exported Successfully")



