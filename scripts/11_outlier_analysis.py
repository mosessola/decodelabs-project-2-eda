"""
11_outlier_analysis.py

Phase 3 - Exploratory Data Analysis
Detects unusual/outlier values using the IQR (Interquartile Range) method:
    - Outliers in order value (TotalPrice)
    - Outliers in quantity ordered
"""

from utils import load_data, save_text_report, money


def iqr_bounds(series):
    q1 = series.quantile(0.25)
    q3 = series.quantile(0.75)
    iqr = q3 - q1
    lower = q1 - 1.5 * iqr
    upper = q3 + 1.5 * iqr
    return lower, upper


def run():
    df = load_data()

    # --- Order value outliers ---
    low_p, high_p = iqr_bounds(df["TotalPrice"])
    price_outliers = df[(df["TotalPrice"] < low_p) | (df["TotalPrice"] > high_p)]

    # --- Quantity outliers ---
    low_q, high_q = iqr_bounds(df["Quantity"])
    qty_outliers = df[(df["Quantity"] < low_q) | (df["Quantity"] > high_q)]

    lines = []
    lines.append("=" * 70)
    lines.append("OUTLIER ANALYSIS (IQR method, 1.5x IQR bounds)")
    lines.append("=" * 70)
    lines.append(f"Order Value (TotalPrice) normal range: {money(low_p)} - {money(high_p)}")
    lines.append(f"Order Value outliers found: {len(price_outliers)} ({len(price_outliers)/len(df)*100:.2f}% of orders)")
    lines.append("-" * 70)
    lines.append(f"Quantity normal range: {low_q:.2f} - {high_q:.2f} units")
    lines.append(f"Quantity outliers found: {len(qty_outliers)} ({len(qty_outliers)/len(df)*100:.2f}% of orders)")
    lines.append("-" * 70)
    if len(price_outliers) > 0:
        lines.append("Top 5 highest-value outlier orders:")
        lines.append(
            price_outliers.sort_values("TotalPrice", ascending=False)
            [["OrderID", "CustomerID", "Product", "Quantity", "TotalPrice"]]
            .head(5)
            .to_string(index=False)
        )
    lines.append("=" * 70)

    report = "\n".join(lines)
    print(report)
    save_text_report("11_outlier_analysis.txt", report)
    price_outliers.to_csv("../outputs/11_price_outliers.csv", index=False)
    qty_outliers.to_csv("../outputs/11_quantity_outliers.csv", index=False)


if __name__ == "__main__":
    run()
