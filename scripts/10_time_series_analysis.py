"""
10_time_series_analysis.py

Phase 3 - Exploratory Data Analysis
Analyzes trends over time:
    - Orders by month
    - Revenue by month
    - Daily order/revenue trends
"""

from utils import load_data, save_text_report, money


def run():
    df = load_data()
    df["YearMonth"] = df["Date"].dt.to_period("M").astype(str)
    df["DayOfWeek"] = df["Date"].dt.day_name()

    by_month = (
        df.groupby("YearMonth")
        .agg(Orders=("OrderID", "count"), Revenue=("TotalPrice", "sum"))
    )

    by_day_of_week = (
        df.groupby("DayOfWeek")
        .agg(Orders=("OrderID", "count"), Revenue=("TotalPrice", "sum"))
        .reindex(["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])
    )

    best_month = by_month["Revenue"].idxmax()
    best_day = by_day_of_week["Revenue"].idxmax()

    lines = []
    lines.append("=" * 70)
    lines.append("TIME SERIES ANALYSIS")
    lines.append("=" * 70)
    lines.append("Orders & Revenue by Month:")
    lines.append(by_month.round(2).to_string())
    lines.append("-" * 70)
    lines.append("Orders & Revenue by Day of Week:")
    lines.append(by_day_of_week.round(2).to_string())
    lines.append("-" * 70)
    lines.append(f"Best month by revenue: {best_month}")
    lines.append(f"Best day of week by revenue: {best_day}")
    lines.append("=" * 70)

    report = "\n".join(lines)
    print(report)
    save_text_report("10_time_series_analysis.txt", report)
    by_month.to_csv("../outputs/10_monthly_trend.csv")
    by_day_of_week.to_csv("../outputs/10_day_of_week_trend.csv")


if __name__ == "__main__":
    run()
