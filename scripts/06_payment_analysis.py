"""
06_payment_analysis.py

Phase 3 - Exploratory Data Analysis
Analyzes payment method usage:
    - Order count / share by payment method
    - Revenue by payment method
"""

from utils import load_data, save_text_report, money


def run():
    df = load_data()
    total_revenue = df["TotalPrice"].sum()
    total_orders = len(df)

    by_payment = (
        df.groupby("PaymentMethod")
        .agg(Orders=("OrderID", "count"), Revenue=("TotalPrice", "sum"))
        .sort_values("Revenue", ascending=False)
    )
    by_payment["Order_Share_%"] = (by_payment["Orders"] / total_orders * 100).round(2)
    by_payment["Revenue_Share_%"] = (by_payment["Revenue"] / total_revenue * 100).round(2)

    most_used = by_payment["Orders"].idxmax()
    top_revenue_method = by_payment["Revenue"].idxmax()

    lines = []
    lines.append("=" * 70)
    lines.append("PAYMENT METHOD ANALYSIS")
    lines.append("=" * 70)
    lines.append(by_payment.round(2).to_string())
    lines.append("-" * 70)
    lines.append(f"Most used payment method:        {most_used}")
    lines.append(f"Highest revenue payment method:  {top_revenue_method}")
    lines.append("=" * 70)

    report = "\n".join(lines)
    print(report)
    save_text_report("06_payment_analysis.txt", report)
    by_payment.to_csv("../outputs/06_payment_analysis.csv")


if __name__ == "__main__":
    run()
