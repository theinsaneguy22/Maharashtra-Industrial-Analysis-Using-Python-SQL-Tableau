#Maharashtra-Industrial-Analysis-Using-Python-SQL-Tableau

A beginner-friendly data analytics project that analyzes industrial zones of Maharashtra using Python, Pandas, MySQL, and Tableau.
The project demonstrates how raw industrial business data can be cleaned, transformed, analyzed, and visualized to generate meaningful insights about industrial distribution, city-wise business growth, and revenue contribution across industrial zones.

This project focuses on industrial turnover analysis, business size classification, city-wise revenue contribution, and data-driven visualization dashboards using Tableau.

#Technologies Used
- Python
- Pandas
- NumPy
- Matplotlib
- MySQL
- Tableau
- Excel / CSV Dataset

#Flow of Project
Raw Industrial Excel Data

Data Cleaning & Preparation (Pandas) -> Feature Engineering -> Business Analytics & Aggregations -> Data Visualization (Matplotlib) -> Data Storage in MySQL -> Data Export from MySQL -> Tableau Dashboard Creation -> Industrial Business Insight Reporting

# Project Features
1. Data Extraction
- Imported industrial zone dataset from Excel file
- Dataset includes:
  - Industrial Area / MIDC Zones
  - City/District
  - Industry Type
  - Number of Companies
  - Estimated Annual Turnover

2. Data Cleaning & Preparation
- Removed duplicate records
- Cleaned currency formatting from turnover column
- Converted turnover values into numeric format


3. Feature Engineering
- Turnover Conversion
- Profit Estimation
- Business Size Classification
  - Industries were categorized into:
    - Small
    - Medium
    - Large
- Industrial Zone Ranking


4. Business Analytics
- City-wise Business Analysis
- Industry Type Analysis
- Top Industrial Zones
- Identified Top 5 industrial zones based on turnover.


5. Data Visualization (Matplotlib)
- Industrial Area Turnover Chart
- City-wise Business Distribution
- Business Size Distribution

6. MySQL Database Integration
- Cleaned dataset was loaded into a MySQL database.
- Created table:
  - industries
- This step demonstrates ETL pipeline integration with relational databases.

7. Data Export for Visualization Tools
- The MySQL dataset was exported to CSV format for use in Tableau dashboards.
- Exported dataset includes all engineered columns for advanced analysis.

8. Tableau Dashboard Integration
- The processed dataset was imported into Tableau to build interactive dashboards.
- Visualizations created include:
  - MIDC Industrial Distribution
  - City Revenue Share
  - Business Size Distribution
  - Industrial Performance Dashboard

9. Insight Generation

- The analysis provided insights such as:
  - Which cities dominate industrial business
  - Major industrial hubs in Maharashtra
  - Distribution of small vs large industries
  - Revenue contribution by industrial zones
  - Profit estimation across industrial clusters
- These insights help understand regional economic activity and industrial concentration.
