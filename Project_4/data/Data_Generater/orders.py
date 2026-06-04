import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

def generate_starbucks_orders(customers_file, items_file, output_file="orders.csv", num_days=7, avg_orders_per_day=300):
    # 1. Load existing tables to use real IDs
    try:
        customers_df = pd.read_csv(customers_file)
        items_df = pd.read_csv(items_file)
    except FileNotFoundError as e:
        print(f"Error: {e}. Please ensure the paths to customers.csv and items.csv are correct.")
        return

    customer_ids = customers_df['customer_id'].tolist()
    
    # Check if items uses 'ID' or 'item_id' based on the snippet provided
    item_id_col = 'ID' if 'ID' in items_df.columns else 'item_id'
    # Map item IDs to their respective prices for easy lookup
    item_price_map = dict(zip(items_df[item_id_col], items_df['price']))
    item_ids = list(item_price_map.keys())


    # 2. Setup Configuration & Distributions
    stores = [101, 102, 103, 104, 105]
    
    # Quantities: higher weight for 1, 2, 3; lower weight for 4 through 9
    qty_options = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    qty_weights = [0.45, 0.30, 0.13, 0.04, 0.03, 0.02, 0.01, 0.01, 0.01] 
    
    # Payment modes and customer types with exact specified probabilities
    pay_modes = ['UPI', 'Cash', 'Card']
    pay_weights = [0.42, 0.53, 0.05]
    
    cust_types = ['walk-in', 'mobile-app']
    cust_weights = [0.35, 0.65]

    # Time frame calculation (Last 'num_days' up to today)
    end_date = datetime.now()
    start_date = end_date - timedelta(days=num_days)
    
    orders_data = []
    order_counter = 1

    print(f"Generating orders from {start_date.strftime('%Y-%m-%d')} to {end_date.strftime('%Y-%m-%d')}...")

    # 3. Generate Daily Transactions
    for day_offset in range(num_days + 1):
        current_day = start_date + timedelta(days=day_offset)
        
        # Add slight randomness to daily order volumes so it looks natural
        daily_orders = int(np.random.normal(avg_orders_per_day, scale=30))
        
        for _ in range(daily_orders):
            # Format order ID (e.g., ORD00001)
            order_id = f"ORD{order_counter:05d}"
            store_id = random.choice(stores)
            
            # Generate realistic timestamps (Starbucks operating hours: 7 AM to 10 PM)
            hour = random.randint(7, 21)
            minute = random.randint(0, 59)
            second = random.randint(0, 59)
            # Handle edge case for current day so we don't generate orders in the future
            order_time = current_day.replace(hour=hour, minute=minute, second=second)
            if order_time > end_date:
                continue
                
            customer_id = random.choice(customer_ids)
            item_id = random.choice(item_ids)
            
            # Apply weights to match desired distributions
            quantity = np.random.choice(qty_options, p=qty_weights)
            payment_mode = np.random.choice(pay_modes, p=pay_weights)
            customer_type = np.random.choice(cust_types, p=cust_weights)
            
            # Calculate total amount based on the item's price
            price = item_price_map[item_id]
            total_amount = int(price * quantity)  # kept as integer matching your items.csv price format
            
            orders_data.append({
                "order_id": order_id,
                "store_id": store_id,
                "datetime": order_time.strftime("%Y-%m-%d %H:%M:%S"),
                "customer_id": customer_id,
                "item_id": item_id,
                "quantity": quantity,
                "total_amount": total_amount,
                "payment_mode": payment_mode,
                "customer_type": customer_type
            })
            
            order_counter += 1

    # 4. Convert to DataFrame and Save
    orders_df = pd.DataFrame(orders_data)
    orders_df.to_csv(output_file, index=False)
    print(f"Successfully generated {len(orders_df)} orders saved into '{output_file}'!")

# Run the generator using your uploaded files
generate_starbucks_orders(
    customers_file='customers.csv', 
    items_file='items.csv', 
    output_file='starbucks_orders.csv'
)