import pandas as pd
import matplotlib.pyplot as plt

# Simulated data for hybrid work adoption rates (2020-2025)
years = [2020, 2021, 2022, 2023, 2024, 2025]
data = {
    "Year": years,
    "USA": [20, 55, 50, 60, 62, 63],
    "UK": [18, 50, 48, 58, 60, 61],
    "Japan": [5, 12, 15, 18, 20, 22],
    "China": [8, 15, 18, 22, 25, 30]
}

df = pd.DataFrame(data)

# Plot
plt.figure(figsize=(10, 6))
plt.plot(df["Year"], df["USA"], label="USA")
plt.plot(df["Year"], df["UK"], label="UK")
plt.plot(df["Year"], df["Japan"], label="Japan")
plt.plot(df["Year"], df["China"], label="China")

plt.xlabel("Year")
plt.ylabel("Hybrid Work Adoption (%)")
plt.title("Global Hybrid Work Adoption Rates (2020–2025)")
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()

