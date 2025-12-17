import matplotlib.pyplot as plt
import numpy as np


years = np.array([2020, 2021, 2022, 2023, 2024, 2025])
policy_stage = np.array([0, 1, 1, 2, 3, 3])

labels = {
    0: "Emergency Remote",
    1: "Digital Fatigue / Soft Return",
    2: "3-Day Office Requirement",
    3: "Hybrid Institutionalized"
}


plt.figure(figsize=(12, 4))

plt.scatter(years, policy_stage, s=120)

plt.plot(years, policy_stage, linestyle="--")

plt.yticks([0, 1, 2, 3], [
    "Emergency Remote",
    "Digital Fatigue",
    "Return Required",
    "Hybrid Institutionalized"
])

plt.xlabel("Year")
plt.ylabel("Corporate Policy Stage")
plt.title("Corporate Policy Shift Timeline (2020–2025)")


for i, year in enumerate(years):
    plt.text(year, policy_stage[i] + 0.05, labels[policy_stage[i]], ha="center", fontsize=9)

plt.tight_layout()
plt.show()
