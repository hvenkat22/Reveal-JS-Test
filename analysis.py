# analysis.py
# Author: HARI VENKATARAMAN
# Email: 22f2001398@ds.study.iitm.ac.in

import marimo

__generated_with = "0.1.0"
app = marimo.App()


# Cell 1: Imports and dataset
# This cell loads the dataset and sets up initial variables.
@app.cell
def __():
    import numpy as np
    import pandas as pd
    np.random.seed(42)

    # Create a synthetic dataset
    df = pd.DataFrame({
        "x": np.linspace(0, 10, 100),
    })
    df["y"] = 2 * df["x"] + np.random.normal(0, 2, 100)
    df.head()
    return df, np, pd


# Cell 2: Interactive widget
# The slider controls the slope used in a fitted line.
@app.cell
def __(mo):
    slope = mo.ui.slider(start=0, stop=5, step=0.1, value=2, label="Slope")
    slope
    return slope,


# Cell 3: Visualization depending on widget
# The chart updates dynamically when the slope slider changes.
@app.cell
def __(df, slope, np):
    import matplotlib.pyplot as plt

    plt.scatter(df["x"], df["y"], label="Data")
    plt.plot(df["x"], slope.value * df["x"], color="red", label=f"Fit: y={slope.value}x")
    plt.legend()
    plt.show()
    return


# Cell 4: Dynamic markdown output
# This output reacts to the slider state.
@app.cell
def __(mo, slope):
    mo.md(f"""
    ### Model Fit
    The current slope is **{slope.value:.2f}**.  
    Adjust the slider to see how the fitted line changes dynamically.
    """)
    return


if __name__ == "__main__":
    app.run()
