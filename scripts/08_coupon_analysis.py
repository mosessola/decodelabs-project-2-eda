"""
08_coupon_analysis.py

Phase 3 - Exploratory Data Analysis
Analyzes coupon/discount code usage:
    - Coupon usage counts and share of orders
    - Revenue comparison: orders with a coupon vs without
"""

from utils import load_data, save_text_report, money


def run():
    df = load_data()
    total_orders = len(df)

    by_coupon = (
        df.groupby("CouponCode")
        .agg(
            Orders=("OrderID", "count"),
            Revenue=("TotalPrice", "sum"),
            Avg_Order_Value=("TotalPrice", "mean"),
        )
        .sort_values("Orders", ascending=False)
    )
    by_coupon["Order_Share_%"] = (by_coupon["Orders"] / total_orders * 100).round(2)

    df["Used_Coupon"] = df["CouponCode"].apply(lambda x: "No Coupon" if x == "No Coupon" else "Used Coupon")
    coupon_vs_no = (
        df.groupby("Used_Coupon")
        .agg(
            Orders=("OrderID", "count"),
            Total_Revenue=("TotalPrice", "sum"),
            Avg_Order_Value=("TotalPrice", "mean"),
        )
    )

    lines = []
    lines.append("=" * 70)
    lines.append("COUPON ANALYSIS")
    lines.append("=" * 70)
    lines.append("Usage by coupon code:")
    lines.append(by_coupon.round(2).to_string())
    lines.append("-" * 70)
    lines.append("Coupon vs No Coupon comparison:")
    lines.append(coupon_vs_no.round(2).to_string())
    lines.append("=" * 70)

    report = "\n".join(lines)
    print(report)
    save_text_report("08_coupon_analysis.txt", report)
    by_coupon.to_csv("../outputs/08_coupon_analysis.csv")


if __name__ == "__main__":
    run()
