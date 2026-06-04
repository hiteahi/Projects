# Starbucks Daily Sales Dashboard

## Overview

The Starbucks Daily Sales Dashboard is an interactive Power BI project designed to analyze daily sales performance across Starbucks stores. The dashboard provides insights into orders, customers, revenue, and quantity sold while allowing users to switch between multiple visual themes.

The project uses a simulated Starbucks dataset generated through Python and modeled in Power BI using DAX measures, calculated tables, and custom visual design techniques.

---

```text
Project_4/
│
├── Dashboard/
│   ├── Starbucks_Dashboard.pbix
│   └── Dashboard Screenshots/
│       ├── Home.jpg
│       ├── Overview.jpg
│       ├── Overview-filter.jpg
│       ├── Theme2.jpg
│       ├── Theme3.jpg
│       └── Theme4.jpg
│
├── images/
│       ├── coco.jpg
│       ├── red.jpg
│       └── logo.jpg
├── Data/
│   ├── data_generater/
│   │   └── orders.py
│   ├── orders.csv
│   ├── customers.csv
│   └── items.csv
│
│
└── README.md
```
--- 

## Dashboard Features

### Home Page
- Starbucks branded landing page
- Navigation menu for all dashboard views
- Interactive theme selection

### Overview Dashboard
- Total Orders KPI
- Total Customers KPI
- Total Revenue KPI
- Total Quantity KPI
- Hourly Orders Analysis
- Hourly Revenue Analysis
- Hourly Quantity Analysis
- Last Updated Timestamp
- Interactive Theme Switching

### Theme Pages
Multiple dashboard themes are available:

- Theme 1 
- Theme 2 
- Theme 3
- Theme 4

Each theme contains identical business insights while demonstrating different dashboard design styles.

---

## Data Model

### Orders Table

| Column | Description |
|----------|------------|
| order_id | Unique order identifier |
| store_id | Store identifier |
| datetime | Order timestamp |
| customer_id | Customer identifier |
| item_id | Product identifier |
| quantity | Quantity purchased |
| total_amount | Total order value |
| payment_mode | Payment method |
| customer_type | Walk-in or Mobile App customer |

---

### Customers Table

| Column | Description |
|----------|------------|
| customer_id | Unique customer identifier |
| customer_name | Customer information |

---

### Items Table

| Column | Description |
|----------|------------|
| item_id | Product identifier |
| item_name | Product name |
| category | Product category |
| price | Product price |

---

## Calendar Table

A custom calendar table is created from order timestamps.

### DAX

```DAX
calendar =
SUMMARIZE(
    orders,
    orders[datetime]
)
```

### Calendar Columns

```DAX
hour =
FORMAT(
    'calendar'[datetime],
    "h AM/PM"
)
```

```DAX
hour_sort =
HOUR(
    'calendar'[datetime]
)
```

The hour column is sorted using hour_sort to maintain chronological order in visuals.

---

## DAX Measures

### Last Updated

```DAX
last_update =
"Last Updated: "
&
FORMAT(
    LASTNONBLANK(
        orders[datetime],
        ""
    ),
    "dd mmm yy hh:mm AM/PM"
)
```

### Maximum Customers Per Hour

```DAX
Max customer Hourly =
MAXX(
    SUMMARIZE(
        'calendar',
        'calendar'[hour]
    ),
    CALCULATE(
        COUNT(
            orders[customer_id]
        )
    )
)
```

### Maximum Orders Per Hour

```DAX
Max Order Hourly =
MAXX(
    SUMMARIZE(
        'calendar',
        'calendar'[hour]
    ),
    CALCULATE(
        COUNT(
            orders[order_id]
        )
    )
)
```

### Maximum Quantity Per Hour

```DAX
Max quantity Hourly =
MAXX(
    SUMMARIZE(
        'calendar',
        'calendar'[hour]
    ),
    CALCULATE(
        SUM(
            orders[quantity]
        )
    )
)
```

### Maximum Revenue Per Hour

```DAX
Max Revenue Hourly =
MAXX(
    ALLSELECTED(
        'calendar'[hour]
    ),
    CALCULATE(
        SUM(
            orders[total_amount]
        )
    )
)
```

### Orders Target Remaining

```DAX
target_orders =
3000 -
COUNT(
    orders[order_id]
)
```

### Customers Target Remaining

```DAX
target_customers =
400 -
DISTINCTCOUNT(
    orders[customer_id]
)
```

### Quantity Target Remaining

```DAX
target_quantity =
5500 -
SUM(
    orders[quantity]
)
```

### Revenue Target Remaining

```DAX
target_revenue =
1800000 -
SUM(
    orders[total_amount]
)
```

---

## Visual Components

### KPI Cards
- Orders
- Customers
- Revenue
- Quantity

### Gauge Visuals
Progress indicators for target achievement.

### Sparkline Trends
Shows performance trends for key metrics.

### Column Charts
- Orders by Hour
- Revenue by Hour
- Quantity by Hour

### Dynamic Maximum Indicators
Displays peak hourly performance values.

### Dynamic Last Updated Timestamp
Shows latest data refresh time.

---

## Tools Used

- Power BI Desktop
- DAX
- Power Query
- Python
- CSV Data Sources

---

## Contributing

This is a personal learning portfolio, but suggestions and feedback are welcome!

*Built with ❤️*
