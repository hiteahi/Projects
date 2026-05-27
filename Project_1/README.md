# E-Commerce Data Cleaning Project
### Python + Pandas + Matplotlib + Seaborn

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![Pandas](https://img.shields.io/badge/Pandas-2.x-green?logo=pandas)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange?logo=jupyter)
![PowerBI](https://img.shields.io/badge/Power%20BI-Ready-yellow?logo=powerbi)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen)

---

## Project Overview

A real-world style **end-to-end data cleaning project** using 5 messy e-commerce datasets with 6,000+ rows. The project covers the full data analyst workflow — from raw dirty data to cleaned, merged, analyzed, and visualized output — ready for Power BI dashboards.

---

## Structure

```
ecommerce-data-cleaning/
│
├── cleaned_data/                       # Processed, clean datasets ready for modeling
│   ├── customers_clean.csv
│   ├── master_table.csv
│   ├── order_items_clean.csv
│   ├── orders_clean.csv
│   ├── products_clean.csv
│   └── returns_clean.csv
│
├── dashboard/                          # Power BI assets and documentation
│   ├── dashboard screenshots/          # Embedded dashboard interface views
│   │   ├── 6086750725191963289.jpg
│   │   ├── 6086750725191963290.jpg
│   │   └── 6086750725191963291.jpg
│   ├── dashboard_readme.md             # Detailed documentation for the dashboard
│   └── p1.pbix                         # Main Power BI Desktop file
│
├── raw_data/                           # Original, uncleaned source datasets
│   ├── customers.csv
│   ├── order_items.csv
│   ├── orders.csv
│   ├── products.csv
│   └── returns.csv
│
├── visualizations/                     # Static EDA charts generated via Python
│   ├── .ipynb_checkpoints/
│   ├── 01_sales_by_category.png
│   ├── 02_monthly_revenue_trend.png
│   ├── 03_payment_method_pie.png
│   ├── 04_heatmap_monthly_category.png
│   ├── 05_boxplot_segment_orders.png
│   ├── 06_scatter_price_vs_rating.png
│   ├── 07_return_reasons.png
│   └── 08_revenue_by_channel.png
│
├── data_cleaning.ipynb                 # Jupyter Notebook containing ETL pipeline
├── INSIGHTS.md                         # Business intelligence findings and takeaways
└── README.md                           # Project overview documentation (this file)
```

---

## Data Problems in Raw Files

Each raw file contains intentional real-world data quality issues:

### customers.csv
| Problem | Example |
|---------|---------|
| Duplicate customer IDs | CUST0003 appears twice |
| Invalid emails | `ALICE@GMAIL.COM`, extra spaces, missing |
| Phone number formats | `+91-98765-43210`, `0987654321`, `N/A` |
| Invalid age | `-5`, `200`, missing |
| Inconsistent gender | `male`, `MALE`, `M`, `m`, `Female` |
| Mixed date formats | `2024-01-15`, `15/01/2024`, `01-15-2024` |
| Inconsistent segment | `consumer`, `CORPORATE`, `Home Office` |

### products.csv
| Problem | Example |
|---------|---------|
| Negative/zero prices | `-99`, `0` |
| Invalid ratings | `6.5`, `-1`, missing |
| Inconsistent category casing | `electronics`, `CLOTHING` |
| Missing cost_price | NaN |

### orders.csv
| Problem | Example |
|---------|---------|
| Duplicate order IDs | ORD00015 appears twice |
| Mixed date formats | `2024-01-15`, `15/01/2024` |
| Negative order amounts | `-500` |
| Discount > order amount | Invalid business logic |
| Inconsistent status | `delivered`, `SHIPPED`, `Pending` |
| Extra spaces in payment | `UPI `, `  COD` |

### order_items.csv
| Problem | Example |
|---------|---------|
| Zero/negative quantity | `0`, `-1` |
| Price stored as string | `"N/A"` |
| Wrong item_total | Doesn't match qty × price |
| Invalid discount | `150%`, `-10%` |

### returns.csv
| Problem | Example |
|---------|---------|
| Mixed date formats | `2024-01-15`, `15/01/2024` |
| Inconsistent reasons | `damaged`, `WRONG ITEM`, `  Late Delivery  ` |
| Negative refund amounts | `-500` |

---

## Cleaning Steps (Notebook Walkthrough)

```
Step 1  → Import libraries (pandas, numpy, matplotlib, seaborn, re)
Step 2  → Load all 5 CSV files
Step 3  → Data audit — find ALL problems across all files
Step 4  → Clean customers.csv
           - drop_duplicates(subset=['customer_id'])
           - regex email validation
           - regex phone standardization → 10-digit
           - fix invalid age with median fill
           - standardize gender and segment with mapping dict
           - pd.to_datetime() for mixed date formats
Step 5  → Clean products.csv
           - fix negative prices → median fill
           - fix invalid ratings → clip to 1–5
           - recalculate cost_price where missing
           - add profit_margin column
Step 6  → Clean orders.csv
           - drop_duplicates(subset=['order_id'])
           - pd.to_datetime() for mixed formats
           - fill missing ship_date = order_date + 3 days
           - remove negative order amounts
           - fix discount > order_amount
           - add net_amount and order_month columns
Step 7  → Clean order_items.csv
           - remove invalid quantities
           - fix string unit_price
           - recalculate item_total from scratch
           - clip discount_pct to 0–100
Step 8  → Clean returns.csv
           - parse mixed dates
           - standardize return_reason and return_status
           - fix negative refund amounts
Step 9  → Merge all DataFrames
           - orders + customers (LEFT JOIN on customer_id)
           - + order_items (LEFT JOIN on order_id)
           - + products (LEFT JOIN on product_id)
           → master_table.csv
Step 10 → GroupBy analysis
           - Sales by category
           - Monthly revenue trend
           - Top 10 customers by spend
           - Return reasons breakdown
           - Orders by payment method
Step 11 → Save all cleaned CSVs
Step 12 → Generate 8 visualizations
Step 13 → Before vs After summary
```

---

## Visualizations Generated

| # | Chart | Type | Insight |
|---|-------|------|---------|
| 1 | Sales by Category | Bar | Electronics leads revenue |
| 2 | Monthly Revenue Trend | Line | Upward trend 2022–2024 |
| 3 | Payment Method Share | Pie | UPI dominates |
| 4 | Monthly Sales by Category | Heatmap | Seasonal patterns visible |
| 5 | Order Amount by Segment | Box Plot | Corporate has highest median |
| 6 | Price vs Rating | Scatter | No strong price-rating correlation |
| 7 | Return Reasons | Horizontal Bar | Damaged items top reason |
| 8 | Revenue by Channel | Bar | Online channel leads |

---

## Skills Demonstrated

| Skill | Code Used |
|-------|-----------|
| Load multiple CSVs | `pd.read_csv()` in a loop |
| Full data audit | `isnull()`, `duplicated()`, `dtypes`, `unique()` |
| Regex text cleaning | `re.match()`, `re.sub()`, custom `apply()` |
| Phone standardization | Regex extract 10-digit numbers |
| Email validation | Regex pattern matching |
| Mixed date parsing | `pd.to_datetime(dayfirst=False, errors='coerce')` |
| Smart missing value fill | `fillna(median)`, `fillna(method='ffill')` |
| Business logic validation | Boolean masking + `.loc[]` |
| Recalculate derived columns | `qty × price × (1 - disc/100)` |
| Merge multiple DataFrames | `df.merge(on=..., how='left')` chained |
| GroupBy aggregations | `groupby().sum()`, `groupby().value_counts()` |
| 8 chart types | `matplotlib` + `seaborn` |
| Export cleaned data | `df.to_csv()` |

---

## Before vs After Summary

| Dataset | Raw Rows | Clean Rows | Issues Fixed |
|---------|----------|------------|-------------|
| customers.csv | 1,000 | ~950 | Duplicates, invalid emails/phones/ages, mixed dates, inconsistent text |
| products.csv | 200 | 200 | Negative prices, invalid ratings, missing costs |
| orders.csv | 1,500 | ~1,450 | Duplicates, mixed dates, negative amounts, bad discounts |
| order_items.csv | 3,000 | ~2,850 | Invalid qty, string prices, wrong totals |
| returns.csv | 300 | 300 | Mixed dates, inconsistent text, negative refunds |
| **master_table.csv** | — | **All merged** | Single analytical table |

---

## Contributing
This is a personal learning portfolio, but suggestions and feedback are welcome!

---

*Made with ❤️*