import pandas as pd

## TABLES
customers = pd.read_csv("olist-brazilian-e-commerce-dataset/olist_customers_dataset.csv")
orders = pd.read_csv("olist-brazilian-e-commerce-dataset/olist_orders_dataset.csv")
order_items = pd.read_csv("olist-brazilian-e-commerce-dataset/olist_order_items_dataset.csv")
order_payments = pd.read_csv("olist-brazilian-e-commerce-dataset/olist_order_payments_dataset.csv")
order_reviews = pd.read_csv("olist-brazilian-e-commerce-dataset/olist_order_reviews_dataset.csv")
products = pd.read_csv("olist-brazilian-e-commerce-dataset/olist_products_dataset.csv")
sellers = pd.read_csv("olist-brazilian-e-commerce-dataset/olist_sellers_dataset.csv")
geolocation = pd.read_csv("olist-brazilian-e-commerce-dataset/olist_geolocation_dataset.csv")
category_translation = pd.read_csv("olist-brazilian-e-commerce-dataset/product_category_name_translation.csv")

def data_overview(df, name):
    print(f"\n===== {name.upper()} =====")
    print("Shape:", df.shape) # (jumlah baris, jumlah kolom)
    print("\nInfo:")
    df.info()
    print("\nMissing Values:")
    print(df.isnull().sum())
    print("\nDuplicates:", df.duplicated().sum(),"\n")

data_overview(customers, "customers")
data_overview(orders, "orders")
data_overview(order_items, "order items")
data_overview(order_payments, "order payments")
data_overview(order_reviews, "order reviews")
data_overview(products, "products")
data_overview(sellers, "sellers")
data_overview(geolocation, "geolocation")
data_overview(category_translation, "category translation")

### Data Cleaning

## CUSTOMERS TABLE
# 1. Change the customer_zip_code_prefix column type to string because it is not a numeric value.
customers['customer_zip_code_prefix'] = customers['customer_zip_code_prefix'].astype(str)

## ORDERS TABLE
# 2. Change several columns with data type: object to datetime
date_cols = [
    'order_purchase_timestamp',
    'order_approved_at',
    'order_delivered_carrier_date',
    'order_delivered_customer_date',
    'order_estimated_delivery_date'
]
for col in date_cols:
    orders[col] = pd.to_datetime(orders[col])

# 3. Check whether missing delivered_customer_date is only on non-delivered orders

