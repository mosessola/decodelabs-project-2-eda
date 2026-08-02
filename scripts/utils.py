"""
utils.py
Shared helper functions used by every analysis script in this project.
Keeping data loading logic in one place ensures every script works from
the exact same cleaned dataset and column definitions.
"""

import os
import pandas as pd

# Path to the cleaned dataset (relative to the project root)
DATA_PATH = os.path.join(os.path.dirname(__file__), "..", "Dataset_for_Data_Analytics_CLEANED.xlsx")
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "outputs")

os.makedirs(OUTPUT_DIR, exist_ok=True)


def load_data():
    """Load the cleaned dataset and return a pandas DataFrame."""
    df = pd.read_excel(DATA_PATH)
    df["Date"] = pd.to_datetime(df["Date"])
    return df


def save_text_report(filename, content):
    """Save a plain-text summary of a script's findings to /outputs."""
    path = os.path.join(OUTPUT_DIR, filename)
    with open(path, "w") as f:
        f.write(content)
    print(f"\nSaved report -> {path}")


def money(x):
    """Format a number as currency for printing."""
    return f"${x:,.2f}"
