# analysis.py
# Healthcare Performance Analysis - Quarterly Patient Satisfaction
# Author: (prepared for) 22f2001398@ds.study.iitm.ac.in
# Purpose: load quarterly scores, compute average, produce trend chart vs benchmark

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Quarterly data (2024)
quarters = ["Q1", "Q2", "Q3", "Q4"]
scores = [-0.23, 6.26, 7.3, 5.11]

# Create DataFrame
df = pd.DataFrame({
    "quarter": quarters,
    "score": scores
})

# Compute average (should be 4.61)
avg = df["score"].mean()

print(f"Quarterly scores: {list(df['score'])}")
print(f"Computed average patient satisfaction score: {avg:.2f}")

# Benchmark / target
benchmark = 4.5

# Plot: trend with benchmark and average
plt.style.use("seaborn-whitegrid")
fig, ax = plt.subplots(figsize=(8, 5))

# Line + markers
ax.plot(df["quarter"], df["score"], marker="o", linewidth=2, label="Quarterly Score")
ax.axhline(benchmark, color="#d62728", linestyle="--", linewidth=1.5, label=f"Industry Target = {benchmark:.2f}")
ax.axhline(avg, color="#2ca02c", linestyle=":", linewidth=1.5, label=f"Average = {avg:.2f}")

# Annotate points
for q, s in zip(df["quarter"], df["score"]):
    ax.annotate(f"{s:.2f}", xy=(q, s), xytext=(0, 6), textcoords="offset points", ha="center", fontsize=10)

ax.set_title("Patient Satisfaction Score — 2024 Quarterly Trend", fontsize=14, weight="bold")
ax.set_xlabel("Quarter")
ax.set_ylabel("Satisfaction Score")
ax.set_ylim(min(scores) - 1, max(scores) + 2)
ax.legend(loc="upper left")
plt.tight_layout()

# Save figure
out_img = "trend.png"
plt.savefig(out_img, dpi=150)
plt.close()

# Also save the data as CSV for reproducibility (optional)
df.to_csv("quarterly_scores.csv", index=False)

print(f"Saved chart to {out_img} and data to quarterly_scores.csv")
