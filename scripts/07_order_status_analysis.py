"""
07_order_status_analysis.py

Phase 3 - Exploratory Data Analysis
Analyzes order fulfillment status:
    - Delivered / Pending / Cancelled / Returned / Shipped breakdown
    - Revenue lost to Cancelled and Returned orders
"""

from utils import load_data, save_text_report, money


def run():
    df = load_data()
    total_orders = len(df)
    total_revenue = df["TotalPrice"].sum()

    by_status = (
        df.groupby("OrderStatus")
        .agg(Orders=("OrderID", "count"), Revenue=("TotalPrice", "sum"))
        .sort_values("Orders", ascending=False)
    )
    by_status["Order_Share_%"] = (by_status["Orders"] / total_orders * 100).round(2)

    lost_statuses = ["Cancelled", "Returned"]
    revenue_lost = df[df["OrderStatus"].isin(lost_statuses)]["TotalPrice"].sum()
    revenue_lost_pct = revenue_lost / total_revenue * 100

    delivered_orders = by_status.loc["Delivered", "Orders"] if "Delivered" in by_status.index else 0
    delivered_pct = delivered_orders / total_orders * 100

    lines = []
    lines.append("=" * 70)
    lines.append("ORDER STATUS ANALYSIS")
    lines.append("=" * 70)
    lines.append(by_status.round(2).to_string())
    lines.append("-" * 70)
    lines.append(f"Delivered order rate:        {delivered_pct:.2f}%")
    lines.append(f"Revenue lost (Cancelled+Returned): {money(revenue_lost)} ({revenue_lost_pct:.2f}% of total revenue)")
    lines.append("=" * 70)

    report = "\n".join(lines)
    print(report)
    save_text_report("07_order_status_analysis.txt", report)
    by_status.to_csv("../outputs/07_order_status_analysis.csv")


if __name__ == "__main__":
    run()
