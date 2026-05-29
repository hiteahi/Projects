# Uber Performance Insights Dashboard

## Overview

The Uber Performance Insights Dashboard is an interactive Power BI project designed to analyze ride bookings, revenue performance, customer behavior, vehicle utilization, and location-based trends.

The dashboard provides business stakeholders with a comprehensive view of operational performance through multiple analytical pages, dynamic filtering, bookmarks, and KPI tracking.

---

## Dashboard Pages

### Home
Landing page providing navigation to all analytical sections of the dashboard.

### Overview
Provides a high-level summary of business performance including:

- Completed Bookings
- Revenue
- Total Distance
- Average Ride Distance
- Lost Bookings
- Booking Trends
- Revenue Trends
- Customer Ratings
- Driver Ratings

### Vehicle Analysis
Analyzes vehicle category performance.

Features:

- Vehicle-wise Customer Count
- Completed Bookings
- Contribution Percentage
- Monthly Booking Trends
- Vehicle Comparison

### Revenue Analysis
Revenue-focused insights including:

- Revenue by Vehicle Type
- Revenue by Payment Method
- Top Revenue Generating Customers
- Monthly Revenue Trends

### Rider Analysis
Customer behavior and retention analysis.

Features:

- First-Time Riders
- Second-Time Riders
- Regular Riders
- Customer Revenue Contribution
- Cancellation Analysis
- Average Ride Distance

### Location Analysis
Geographical and operational insights.

Features:

- Location-wise Bookings
- Total Distance Analysis
- Time Slot Analysis
- Peak Booking Hours
- High Performing Areas

---

## Dataset Information

The dashboard is built using Uber ride booking data containing:

- Booking ID
- Customer ID
- Vehicle Type
- Booking Status
- Booking Value
- Ride Distance
- Payment Method
- Pickup Location
- Drop Location
- Customer Rating
- Driver Rating
- Date
- Time
- Cancellation Reasons

---

## Data Model

### Fact Table

**data**

Contains all ride-level transactional information.

### Calendar Table

Custom calendar table created for time intelligence calculations.

```DAX
calender =
SUMMARIZE(
    data,
    data[Date]
)
```

---

## Calculated Columns

### Time Slot

```DAX
Time Slot =
VAR _hour = HOUR(data[Time])
RETURN
SWITCH(
    TRUE(),
    _hour >= 9 && _hour < 12, "09 AM - 12 PM",
    _hour >= 12 && _hour < 15, "12 PM - 03 PM",
    _hour >= 15 && _hour < 18, "03 PM - 06 PM",
    _hour >= 18 && _hour < 21, "06 PM - 09 PM",
    _hour >= 21 && _hour < 24, "09 PM - 12 AM",
    _hour >= 0 && _hour < 3, "12 AM - 03 AM",
    _hour >= 3 && _hour < 6, "03 AM - 06 AM",
    _hour >= 6 && _hour < 9, "06 AM - 09 AM"
)
```

### Vehicle Type Standardization

```DAX
vehicleType =
IF(
    CONTAINSSTRING(data[Vehicle Type], "Bike"),
    "Bike",
    data[Vehicle Type]
)
```

---

## Key Measures

### Booking Count

```DAX
bookingCount =
DISTINCTCOUNT(data[Booking ID])
```

### Revenue

```DAX
bookingValue =
SUM(data[Booking Value])
```

### Customer Count

```DAX
custCount =
DISTINCTCOUNT(data[Customer ID])
```

### Completed Bookings

```DAX
completedBookings =
CALCULATE(
    [bookingCount],
    data[Booking Status] = "Completed"
)
```

### Average Distance

```DAX
avgDistance =
AVERAGE(data[Ride Distance])
```

### Total Distance

```DAX
totalDistance =
SUM(data[Ride Distance])
```
### Lost Bookings

```DAX
lostBookings =
CALCULATE(
    [bookingCount],
    data[Booking Status] <> "Completed"
)
```

---

## Features

- Multi-page dashboard architecture
- Dynamic navigation using bookmarks
- Interactive filter panel
- Month and Quarter analysis
- Vehicle-wise performance tracking
- Revenue analysis
- Customer segmentation
- Cancellation insights
- Time-slot analysis
- Responsive layout design

---

## Dashboard Screenshots

### Home

![Home](Dashboard-Screenshots/Home.jpg)

### Overview

![Overview](Dashboard-Screenshots/Overview.jpg)

### Overview Filter Panel

![Overview Filter](Dashboard-Screenshots/Overview-filter.jpg)

### Vehicle Analysis

![Vehicle](Dashboard-Screenshots/Vehicle.jpg)

### Revenue Analysis

![Revenue](Dashboard-Screenshots/Revenue.jpg)

### Rider Analysis

![Rider](Dashboard-Screenshots/Rider.jpg)

### Location Analysis

![Location](Dashboard-Screenshots/Location.jpg)

---

## Tools & Technologies

- Power BI Desktop
- DAX
- Power Query
- Data Modeling
- Bookmarks
- Field Parameters
- Interactive Visualizations

---

## Structure

```text
├── Dashboard-Screenshots
│   ├── Home.jpg
│   ├── Overview.jpg
│   ├── Overview-filter.jpg
│   ├── Vehicle.jpg
│   ├── Revenue.jpg
│   ├── Rider.jpg
│   └── Location.jpg
│
├── data
│   └── uber.xlsx
│
├── Icons
│
├── Images
│
├── p3.pbix
│
└── README.md
```

---

## Business Insights Generated

- Auto generates the highest revenue among vehicle categories.
- UPI is the most preferred payment method.
- Revenue and bookings show seasonal fluctuations.
- Customer retention can be analyzed through rider segmentation.
- Peak demand periods can be identified using time-slot analysis.
- Cancellation trends help uncover operational challenges.

---

## Contributing

This is a personal learning portfolio, but suggestions and feedback are welcome!

*Built with ❤️*