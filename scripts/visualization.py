import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/processed/cleaned_full_data.csv")


#Industrial Area
plt.figure()
plt.bar(df["Industrial_Area"], df["Turnover_in_Crores"])
plt.xticks(rotation=90)
plt.xlabel("Industrial Area")
plt.ylabel("Turnover (Crores)")
plt.title("Turnover by Industrial Area")

plt.tight_layout()
plt.savefig("visualization_outputs/industrial_area_turnover.png")
plt.close()


# City-wise turnover
city_data = df.groupby("City/District")["Turnover_in_Crores"].sum()

plt.figure()
city_data.plot(kind="bar")
plt.title("Total Business by City")
plt.xticks(rotation=45)
plt.ylabel("Turnover (Cr)")

plt.tight_layout()
plt.savefig("visualization_outputs/city_turnover.png")
plt.close()

# Business size distribution
size_data = df["Business_Size"].value_counts()

plt.figure()
size_data.plot(kind="pie", autopct="%1.1f%%")
plt.title("Business Size Distribution")
plt.ylabel("")

plt.tight_layout()
plt.savefig("visualization_outputs/business_size_distribution.png")
plt.close()


print("✅ All visualizations saved in 'visualization' folder")