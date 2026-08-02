"""
05_customer_analysis.py

Phase 3 - Exploratory Data Analysis
Analyzes customer behavior:
    - Unique customers
    - Top customers by spend
    - Repeat customers (customers with more than one order)
    - Overall customer spending distribution
"""

from utils import load_data, save_text_report, money


def run():
    df = load_data()

    unique_customers = df["CustomerID"].nunique()

    spend_by_customer = (
        df.groupby("CustomerID")
        .agg(Orders=("OrderID", "count"), Total_Spend=("TotalPrice", "sum"))
        .sort_values("Total_Spend", ascending=False)
    )

    top_10 = spend_by_customer.head(10)

    repeat_customers = spend_by_customer[spend_by_customer["Orders"] > 1]
    repeat_customer_count = len(repeat_customers)
    repeat_rate = repeat_customer_count / unique_customers * 100

    avg_spend_per_customer = spend_by_customer["Total_Spend"].mean()

    lines = []
    lines.append("=" * 70)
    lines.append("CUSTOMER ANALYSIS")
    lines.append("=" * 70)
    lines.append(f"Unique Customers:            {unique_customers:,}")
    lines.append(f"Repeat Customers:            {repeat_customer_count:,} ({repeat_rate:.2f}% of customer base)")
    lines.append(f"Average Spend per Customer:  {money(avg_spend_per_customer)}")
    lines.append("-" * 70)
    lines.append("Top 10 Customers by Spend:")
    lines.append(top_10.round(2).to_string())
    lines.append("=" * 70)

    report = "\n".join(lines)
    print(report)
    save_text_report("05_customer_analysis.txt", report)
    spend_by_customer.to_csv("../outputs/05_customer_spend_full.csv")


if __name__ == "__main__":
    run()
