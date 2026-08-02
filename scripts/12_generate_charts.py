"""
12_generate_charts.py

Phase 4 - Visualization
Generates professional Matplotlib charts and saves them as PNG files
for use in the executive report:
    - Revenue trend (monthly)
    - Product sales (revenue by product)
    - Payment methods (revenue share)
    - Order status breakdown
    - Referral source performance
    - Customer spending distribution
    - Boxplot of order values (outlier visualization)
    - Histogram of order values
"""

import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
from utils import load_data

CHART_DIR = os.path.join(os.path.dirname(__file__), "..", "charts")
os.makedirs(CHART_DIR, exist_ok=True)

# Consistent professional style
plt.rcParams.update({
    "figure.figsize": (10, 6),
    "font.size": 11,
    "axes.titlesize": 14,
    "axes.titleweight": "bold",
    "axes.spines.top": False,
    "axes.spines.right": False,
    "axes.grid": True,
    "grid.alpha": 0.3,
    "figure.dpi": 150,
})

COLOR_PRIMARY = "#2E5EAA"
COLOR_PALETTE = ["#2E5EAA", "#4C9F70", "#E8A33D", "#C1443C", "#7C5CBF", "#3AA6A6", "#D46FA5"]


def save(fig, name):
    path = os.path.join(CHART_DIR, name)
    fig.savefig(path, bbox_inches="tight")
    plt.close(fig)
    print(f"Saved chart -> {path}")


def chart_revenue_trend(df):
    df["YearMonth"] = df["Date"].dt.to_period("M").astype(str)
    monthly = df.groupby("YearMonth")["TotalPrice"].sum()

    fig, ax = plt.subplots()
    ax.plot(monthly.index, monthly.values, marker="o", color=COLOR_PRIMARY, linewidth=2)
    ax.set_title("Monthly Revenue Trend")
    ax.set_xlabel("Month")
    ax.set_ylabel("Revenue ($)")
    ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"${x:,.0f}"))
    plt.xticks(rotation=90)
    fig.tight_layout()
    save(fig, "01_revenue_trend.png")


def chart_product_sales(df):
    by_product = df.groupby("Product")["TotalPrice"].sum().sort_values(ascending=False)

    fig, ax = plt.subplots()
    bars = ax.bar(by_product.index, by_product.values, color=COLOR_PALETTE)
    ax.set_title("Revenue by Product")
    ax.set_xlabel("Product")
    ax.set_ylabel("Revenue ($)")
    ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"${x:,.0f}"))
    for b in bars:
        ax.annotate(f"${b.get_height():,.0f}", (b.get_x() + b.get_width() / 2, b.get_height()),
                    ha="center", va="bottom", fontsize=9)
    fig.tight_layout()
    save(fig, "02_product_sales.png")


def chart_payment_methods(df):
    by_payment = df.groupby("PaymentMethod")["TotalPrice"].sum().sort_values(ascending=False)

    fig, ax = plt.subplots()
    ax.pie(
        by_payment.values,
        labels=by_payment.index,
        autopct="%1.1f%%",
        colors=COLOR_PALETTE,
        startangle=90,
        wedgeprops={"edgecolor": "white", "linewidth": 1},
    )
    ax.set_title("Revenue Share by Payment Method")
    fig.tight_layout()
    save(fig, "03_payment_methods.png")


def chart_order_status(df):
    by_status = df.groupby("OrderStatus")["OrderID"].count().sort_values(ascending=False)

    fig, ax = plt.subplots()
    bars = ax.barh(by_status.index, by_status.values, color=COLOR_PALETTE)
    ax.set_title("Order Count by Status")
    ax.set_xlabel("Number of Orders")
    for b in bars:
        ax.annotate(f"{int(b.get_width())}", (b.get_width(), b.get_y() + b.get_height() / 2),
                    ha="left", va="center", fontsize=9, xytext=(5, 0), textcoords="offset points")
    fig.tight_layout()
    save(fig, "04_order_status.png")


def chart_referral_sources(df):
    by_ref = df.groupby("ReferralSource")["TotalPrice"].sum().sort_values(ascending=False)

    fig, ax = plt.subplots()
    bars = ax.bar(by_ref.index, by_ref.values, color=COLOR_PALETTE)
    ax.set_title("Revenue by Referral Source")
    ax.set_xlabel("Referral Source")
    ax.set_ylabel("Revenue ($)")
    ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"${x:,.0f}"))
    for b in bars:
        ax.annotate(f"${b.get_height():,.0f}", (b.get_x() + b.get_width() / 2, b.get_height()),
                    ha="center", va="bottom", fontsize=9)
    fig.tight_layout()
    save(fig, "05_referral_sources.png")


def chart_customer_spending(df):
    spend = df.groupby("CustomerID")["TotalPrice"].sum().sort_values(ascending=False).head(15)

    fig, ax = plt.subplots()
    bars = ax.barh(spend.index[::-1], spend.values[::-1], color=COLOR_PRIMARY)
    ax.set_title("Top 15 Customers by Spend")
    ax.set_xlabel("Total Spend ($)")
    ax.xaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"${x:,.0f}"))
    fig.tight_layout()
    save(fig, "06_customer_spending.png")


def chart_boxplot_order_value(df):
    fig, ax = plt.subplots()
    bp = ax.boxplot(df["TotalPrice"], vert=False, patch_artist=True,
                     boxprops=dict(facecolor=COLOR_PRIMARY, alpha=0.6),
                     medianprops=dict(color="#C1443C", linewidth=2))
    ax.set_title("Order Value Distribution (Boxplot)")
    ax.set_xlabel("Order Value ($)")
    ax.set_yticks([])
    ax.xaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"${x:,.0f}"))
    fig.tight_layout()
    save(fig, "07_boxplot_order_value.png")


def chart_histogram_order_value(df):
    fig, ax = plt.subplots()
    ax.hist(df["TotalPrice"], bins=30, color=COLOR_PRIMARY, edgecolor="white", alpha=0.85)
    ax.set_title("Distribution of Order Values (Histogram)")
    ax.set_xlabel("Order Value ($)")
    ax.set_ylabel("Number of Orders")
    ax.xaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"${x:,.0f}"))
    fig.tight_layout()
    save(fig, "08_histogram_order_value.png")


def run():
    df = load_data()
    chart_revenue_trend(df)
    chart_product_sales(df)
    chart_payment_methods(df)
    chart_order_status(df)
    chart_referral_sources(df)
    chart_customer_spending(df)
    chart_boxplot_order_value(df)
    chart_histogram_order_value(df)


if __name__ == "__main__":
    run()
