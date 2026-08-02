"""
03_sales_overview.py

Phase 3 - Exploratory Data Analysis
Produces the top-line sales KPIs for the business:
    - Total Orders
    - Total Revenue
    - Average Order Value
    - Total Quantity Sold
    - Average Quantity per Order
"""

from utils import load_data, save_text_report, money


def run():
    df = load_data()

    total_orders = len(df)
    total_revenue = df["TotalPrice"].sum()
    avg_order_value = df["TotalPrice"].mean()
    total_quantity = df["Quantity"].sum()
    avg_quantity_per_order = df["Quantity"].mean()

    lines = []
    lines.append("=" * 60)
    lines.append("SALES OVERVIEW")
    lines.append("=" * 60)
    lines.append(f"Total Orders:              {total_orders:,}")
    lines.append(f"Total Revenue:             {money(total_revenue)}")
    lines.append(f"Average Order Value:       {money(avg_order_value)}")
    lines.append(f"Total Quantity Sold:       {total_quantity:,} units")
    lines.append(f"Average Quantity/Order:    {avg_quantity_per_order:.2f} units")
    lines.append("=" * 60)

    report = "\n".join(lines)
    print(report)
    save_text_report("03_sales_overview.txt", report)


if __name__ == "__main__":
    run()
