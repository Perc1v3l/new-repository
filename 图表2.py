import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


categories = [
    "Work Efficiency",
    "Emotional Health",
    "Creativity",
    "Team Belonging",
    "Work-Life Balance"
]


remote = [80, 55, 70, 40, 85]
hybrid = [75, 70, 75, 65, 80]
office = [70, 60, 68, 75, 65]

df = pd.DataFrame({
    "Category": categories,
    "Remote": remote,
    "Hybrid": hybrid,
    "Office": office
})


x = np.arange(len(categories))
width = 0.25  # 每个柱子的宽度

plt.figure(figsize=(12, 6))
plt.bar(x - width, df["Remote"], width, label="Remote")
plt.bar(x, df["Hybrid"], width, label="Hybrid")
plt.bar(x + width, df["Office"], width, label="Office")

plt.xlabel("Satisfaction Indicators")
plt.ylabel("Score (0–100)")
plt.title("Employee Satisfaction Comparison: Remote vs Hybrid vs Office")
plt.xticks(x, categories, rotation=20)
plt.legend()
plt.tight_layout()

plt.show()
