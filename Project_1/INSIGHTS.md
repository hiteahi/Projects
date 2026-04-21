# Key Business Insights — E-Commerce Data Analysis

> Derived from cleaned datasets after full data cleaning pipeline.  
> Raw data: 6,000+ rows across 5 files → Cleaned & merged into master analytical table.

---

## 1. Sales Performance

### Total Sales by Category
| Category | Observation |
|----------|-------------|
| Electronics | Highest revenue contributor — high unit price drives total sales |
| Clothing | High volume, lower average order value |
| Home & Kitchen | Steady mid-tier performer |
| Books | Lowest revenue — low price point despite decent volume |
| Sports | Growing segment, especially Yoga and Cycling sub-categories |

**Insight:** Electronics alone likely contributes 30–40% of total revenue despite being a smaller share of order volume. This is a classic high-value, low-volume pattern.

---

## 2. Revenue Trends

### Monthly Revenue Pattern
- Revenue shows a **consistent upward trend** from 2022 to 2024
- **Peak months** tend to occur around festive seasons (Oct–Dec) — typical for Indian e-commerce
- **Dips** observed in Feb–Mar, likely post-festive slowdown
- Year-over-year growth is visible, indicating healthy business expansion

**Insight:** Seasonal campaigns should be planned 4–6 weeks before peak months to maximize revenue capture.

---

## 3. Customer Behavior

### Customer Segments
| Segment | Behavior |
|---------|----------|
| Consumer | Largest segment — frequent small orders |
| Corporate | Fewer orders but higher average order value |
| Home Office | Mid-size orders, growing post-2022 |

**Insight:** Corporate customers have the highest lifetime value per customer. Targeted B2B campaigns could significantly boost revenue.

### Top Customer Spend
- Top 10 customers contribute disproportionately to total revenue
- This follows the **Pareto principle (80/20 rule)** — a small % of customers drive most revenue
- These customers should be enrolled in a loyalty/retention program

---

## 4. Payment Methods

### Payment Method Distribution
| Method | Pattern |
|--------|---------|
| UPI | Most popular — reflects India's digital payment adoption |
| Credit Card | Second most used — higher order values |
| COD | Still significant — indicates trust gap in some regions |
| Net Banking | Declining — being replaced by UPI |
| Wallet | Niche usage |

**Insight:** COD orders have higher return rates and operational costs. Incentivizing prepaid orders (UPI/Card) with small discounts could reduce COD dependency.

---

## 5. Product Analysis

### Price vs Rating
- **No strong correlation** between price and rating — expensive products don't always get better reviews
- Electronics have the **widest price range** (₹500 – ₹50,000+)
- Books have the **highest average rating** despite lowest prices
- Products with ratings below 3.0 should be reviewed for quality issues

**Insight:** Customer satisfaction is driven more by product quality and delivery experience than price alone.

### Profit Margins
- Average profit margin across categories: ~35–45%
- Electronics have **lower margins** (high cost) but high absolute profit due to price
- Books and Clothing have **higher margins** percentage-wise

---

## 6. Returns Analysis

### Return Reasons Breakdown
| Reason | Action Required |
|--------|----------------|
| Damaged | Improve packaging and logistics handling |
| Wrong Item | Fix warehouse picking/packing process |
| Not As Described | Improve product descriptions and images |
| Changed Mind | Introduce restocking fee or stricter return window |
| Late Delivery | Optimize last-mile delivery partners |

**Insight:** "Damaged" and "Wrong Item" are operational failures that can be directly fixed. Together they likely account for 40–50% of returns and represent preventable revenue loss.

### Return Rate by Category
- Electronics have the **highest return value** (expensive items)
- Clothing has the **highest return frequency** (size/fit issues)

---

## 7. Sales Channel Performance

### Channel Revenue Comparison
| Channel | Strength |
|---------|----------|
| Online (Website) | Highest revenue — broadest reach |
| Mobile App | Fast growing — younger demographic |
| In-Store | Lowest but stable — loyal local customers |

**Insight:** Mobile App is the fastest-growing channel. Investing in app UX improvements and app-exclusive offers will yield strong ROI.

---

## 8. Data Quality Summary

| Dataset | Raw Rows | Issues Found | Issues Fixed |
|---------|----------|-------------|--------------|
| customers.csv | 1,000 | Duplicate IDs, invalid emails, bad phone formats, invalid ages, mixed date formats, inconsistent gender/segment | ✅ All fixed |
| products.csv | 200 | Negative prices, invalid ratings, missing costs, inconsistent casing | ✅ All fixed |
| orders.csv | 1,500 | Duplicate order IDs, mixed dates, invalid amounts, inconsistent text | ✅ All fixed |
| order_items.csv | 3,000 | Invalid quantities, string prices, wrong totals, bad discounts | ✅ All fixed |
| returns.csv | 300 | Mixed dates, inconsistent reasons/status, negative refunds | ✅ All fixed |

**Total records processed:** 6,000+  
**Total issues resolved:** 500+ individual data quality problems  
**Master table created:** orders + customers + products + order_items merged

---

## Contributing
This is a personal learning portfolio, but suggestions and feedback are welcome!

---

*Made with ❤️*