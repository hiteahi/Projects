# E-Commerce Analytics Dashboard (Power BI)

## Overview

An interactive multi-page Power BI dashboard built using cleaned e-commerce datasets processed with Python and Pandas.

This project focuses on:
- Sales performance analysis
- Customer insights
- Product analysis
- Returns & operational insights
- KPI tracking
- Time intelligence analysis

The dashboard was created after a complete data cleaning pipeline using Python + Pandas.

---

# Tools & Technologies

- Power BI
- DAX
- Python
- Pandas
- Matplotlib
- Seaborn
- CSV Data Modeling

---

# Dashboard Pages

## 1. Overview Dashboard

Tracks high-level business KPIs:

- Total Revenue
- Total Orders
- Average Order Value
- Total Customers
- Return Rate %

### Visuals Included
- Monthly Revenue Trend
- Sales by Category
- Revenue by Sales Channel
- Date Range Slicer

---

## 2. Customer & Product Analysis

Analyzes customer behavior and product performance.

### Visuals Included
- Revenue by Customer Segment
- Top 10 Customers
- Top Products by Revenue
- Price vs Rating Analysis

### Key Insights
- Corporate customers generate the highest revenue
- Electronics is the top-performing category
- No strong correlation between price and customer ratings

---

## 3. Returns & Operations Dashboard

Focuses on operational efficiency and return analysis.

### Visuals Included
- Return Rate by Category
- Return Reasons Breakdown
- Order Status Distribution
- Monthly Return Trends
- Payment Method Analysis

### Key Insights
- Damaged products are the leading return reason
- COD orders contribute significantly to returns
- Returns peak during high-sales periods

---

# Data Model

The dashboard follows a relational data model using:

- Customers Table
- Orders Table
- Order Items Table
- Products Table
- Returns Table
- Custom Date Table

A custom DateTable was created using DAX for time intelligence calculations.

---

# DAX Measures Used

## Revenue Metrics
- Total Revenue
- Avg Order Value
- Revenue YTD
- Revenue MoM %

## Customer Metrics
- Total Customers
- New Customers

## Returns Metrics
- Return Rate %
- Refund Amount

## Product Metrics
- Total Items Sold
- Avg Profit Margin

---

# Data Cleaning Process

Before building the dashboard, the raw datasets were cleaned using Python + Pandas.

### Cleaning Included
- Removing duplicates
- Handling missing values
- Standardizing dates
- Fixing invalid prices and ratings
- Cleaning phone/email formats
- Recalculating totals
- Validating business rules

---

# Key Skills Demonstrated

- Data Cleaning
- Data Modeling
- DAX Calculations
- Power BI Dashboard Design
- Time Intelligence
- Business Analysis
- KPI Reporting
- Data Visualization

---

# Project Files

```
ecommerce-dashboard/
│
├── dashboards/
│   ├── ecommerce_dashboard.pbix
│   └── powerBI_readme.md
│   
│
├── cleaned_data/
│   ├── customers_clean.csv
│   ├── orders_clean.csv
│   ├── order_items_clean.csv
│   ├── products_clean.csv
│   └── returns_clean.csv
│
├── notebooks/
│   └── data_cleaning.ipynb
│
├── visualizations/
│   └── dashboard_screenshots/
│
└── README.md
```


---

## Contributing
This is a personal learning portfolio, but suggestions and feedback are welcome!

---

*Made with ❤️*