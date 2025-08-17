# chart.py
# Customer Support Response Time Distribution
# Author: 22f2001398@ds.study.iitm.ac.in

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# -----------------------------
# 1. Generate synthetic dataset
# -----------------------------
np.random.seed(42)

channels = ["Email", "Chat", "Phone", "Social Media"]
data = []

# Generate realistic response times (minutes) by channel
for ch in channels:
    if ch == "Email":
        times = np.random.normal(loc=120, scale=30, size=200)  # slower
    elif ch == "Chat":
        times = np.random.normal(loc=10, scale=5, size=200)   # very fast
    elif ch == "Phone":
        times = np.random.normal(loc=30, scale=10, size=200)
    else:  # Social Media
        times = np.random.normal(loc=60, scale=20, size=200)
    
    df_temp = pd.DataFrame({
        "Channel": ch,
        "ResponseTime": times
    })
    data.append(df_temp)

df = pd.concat(data, ignore_index=True)

# Clip negative times
df["ResponseTime"] = df["ResponseTime"].clip(lower=1)

# -----------------------------
# 2. Seaborn violinplot
# -----------------------------
sns.set_style("whitegrid")
sns.set_context("talk")

plt.figure(figsize=(8, 8))  # ensures 512x512 when saved with dpi=64

ax = sns.violinplot(
    data=df,
    x="Channel",
    y="ResponseTime",
    palette="Set2",
    cut=0
)

# Titles and labels
ax.set_title("Customer Support Response Times by Channel", fontsize=16, weight="bold")
ax.set_xlabel("Support Channel", fontsize=14)
ax.set_ylabel("Response Time (minutes)", fontsize=14)

# -----------------------------
# 3. Export chart
# -----------------------------
plt.savefig("chart.png", dpi=64, bbox_inches="tight")  # 512x512 px
plt.close()
