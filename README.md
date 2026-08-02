Project 2 — Exploratory Data Analysis (EDA)

DecodeLabs Data Analytics Internship

Goal

Analyze a cleaned e-commerce order dataset to understand patterns, trends, and distributions — calculating descriptive statistics, identifying trends and outliers, and summarizing findings into an actionable business report.

Dataset

Dataset_for_Data_Analytics_CLEANED.xlsx — 1,200 orders  with columns: OrderID, Date, CustomerID, Product, Quantity, UnitPrice, ShippingAddress, PaymentMethod, OrderStatus, TrackingNumber, ItemsInCart, CouponCode, ReferralSource, TotalPrice.

Project Structure
Executive_Report.docx   Full narrative report: findings, business impact, recommendations
scripts/                9 analysis scripts (Python/pandas) + 1 charting script + shared utils.py
outputs/                .txt (readable) + .csv (raw) results for every analysis
charts/                 8 PNG visualizations
Scripts & What They Answer
Script	Business Question
03_sales_overview.py	What's the overall size and health of the business?
04_product_analysis.py	Which products sell best, by volume and revenue?
05_customer_analysis.py	Who are the top customers, and how loyal is the customer base?
06_payment_analysis.py	How is revenue split across payment methods?
07_order_status_analysis.py	How much revenue is lost to cancellations/returns?
08_coupon_analysis.py	Are coupons changing customer behavior?
09_referral_analysis.py	Which acquisition channels perform best?
10_time_series_analysis.py	Are there monthly or day-of-week sales trends?
11_outlier_analysis.py	Which orders are statistical outliers, and why?
12_generate_charts.py	Produces all 8 charts in charts/ from the analyses above


Key Findings
1,200 orders, $1,264,761.96 total revenue, average order value $1,053.97, 3,535 units sold.
Revenue is evenly spread across products — Chair leads at 15.47% of revenue, Phone trails at 12.00%; no single product dominates or drags down the business.
41.09% of revenue ($519,673.91) is tied up in Cancelled or Returned orders — the single biggest lever for improving the bottom line without acquiring a single new customer.
Only 19.25% of orders reach "Delivered" status — fulfillment/logistics is worth investigating as a root cause.
8 orders (0.67%) are statistical price outliers (IQR method) — all high-value, multi-unit purchases ($3,300–$3,456), which read as legitimate large orders rather than data errors.
Payment methods, referral sources, and coupon usage are all fairly evenly distributed — no channel or promotion is currently over- or under-performing dramatically.
Portfolio Checklist
 Narrative structure (problem → methodology → findings → recommendations) — see Executive_Report.docx
 Technical evidence — clean, modular scripts with shared utils.py
 Data forensics — outlier detection (IQR method) documented in 11_outlier_analysis
 Business impact — quantified findings above (revenue at risk, delivery rate, etc.)
 README — this file
