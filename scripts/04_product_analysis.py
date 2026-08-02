"""
04_product_analysis.py

Phase 3 - Exploratory Data Analysis
Analyzes performance at the product level:
    - Best-selling products (by quantity)
    - Revenue by product
    - Average quantity sold per order, by product
    - Each product's % contribution to total revenue
"""

from utils import load_data, save_text_report, money


def run():
    df = load_data()
    total_revenue = df["TotalPrice"].sum()

    by_product = (
        df.groupby("Product")
        .agg(
            Orders=("OrderID", "count"),
            Total_Quantity=("Quantity", "sum"),
            Avg_Quantity_Per_Order=("Quantity", "mean"),
            Total_Revenue=("TotalPrice", "sum"),
        )
        .sort_values("Total_Revenue", ascending=False)
    )
    by_product["Revenue_Share_%"] = (by_product["Total_Revenue"] / total_revenue * 100).round(2)

    best_seller_by_qty = by_product["Total_Quantity"].idxmax()
    top_revenue_product = by_product["Total_Revenue"].idxmax()

    lines = []
    lines.append("=" * 70)
    lines.append("PRODUCT ANALYSIS")
    lines.append("=" * 70)
    lines.append(by_product.round(2).to_string())
    lines.append("-" * 70)
    lines.append(f"Best-selling product (by units): {best_seller_by_qty}")
    lines.append(f"Top revenue-generating product:  {top_revenue_product}")
    lines.append("=" * 70)

    report = "\n".join(lines)
    print(report)
    save_text_report("04_product_analysis.txt", report)
    by_product.to_csv("../outputs/04_product_analysis.csv")


if __name__ == "__main__":
    run()
