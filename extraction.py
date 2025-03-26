import shopify
import os
import pandas as pd
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve environment variables
token = os.getenv("ADMINTOKEN")
merchant = os.getenv("MERCHANT")
api_version = os.getenv("API_VERSION")

# Set up Shopify API endpoint
base_url = f"https://{merchant}.myshopify.com/admin/api/{api_version}"

# Activate Shopify API session
api_session = shopify.Session(merchant, api_version, token)
shopify.ShopifyResource.activate_session(api_session)



def get_product_details():
    try:
        # Initialize list to store all products data
        products_data = []

        # Pagination loop
        page = 1
        while True:
            # Fetch products for the current page
            products = shopify.Product.find(limit=250)

            # If no products are returned, break the loop
            if not products:
                break

            # Iterate over products and collect data
            for product in products:
                product_data = {
                    'Title': product.title,
                    'Vendor': product.vendor,
                    'Product Type': product.product_type,
                    'Published': product.published_at,
                    'Created': product.created_at,
                    'Updated': product.updated_at,
                    'Tags': ','.join(product.tags) if product.tags else '',
                    'Inventory Quantity': product.inventory_quantity,
                    'Inventory Management': product.inventory_management,
                    'Requires Shipping': product.requires_shipping,
                    # Add more fields as needed
                }
                products_data.append(product_data)

            # Move to the next page
            page += 1

        # Convert products_data to DataFrame
        df = pd.DataFrame(products_data)

        # Store DataFrame in a CSV file
        csv_filename = 'shopify_products.csv'
        df.to_csv(csv_filename, index=False)

        print(f"Data successfully exported to {csv_filename}")
    except Exception as e:
        print(f"Error fetching or exporting products: {e}")



def get_order_details():
    orders_data = []

    try:

        
        # Fetch orders since the last fetched order ID (since_id)
        orders = shopify.Order.find()

        # Iterate over orders and collect data
        for order in orders:
            # Collect order data
            order_data = {
                'Order ID': order.id,
                'Created at': order.created_at,
                'Financial Status': order.financial_status,
                'Fulfillment Status': order.fulfillment_status,
                'Total Price': order.total_price,
                'Currency': order.currency,
                'Customer ID': order.customer.id if order.customer else None,
                'Email': order.email,
                'Billing Name': order.billing_address.name if order.billing_address else None,
                'Billing City': order.billing_address.city if order.billing_address else None,
                'Billing Country': order.billing_address.country if order.billing_address else None,
                'Billing Province': order.billing_address.province if order.billing_address else None,
                'Billing Zip': order.billing_address.zip if order.billing_address else None,
            }
            orders_data.append(order_data)

        # Convert orders_data to DataFrame
        orders_df = pd.DataFrame(orders_data)

        # Store DataFrame in a CSV file
        orders_csv_filename = 'shopify_orders.csv'
        orders_df.to_csv(orders_csv_filename, index=False)

        print(f"Order data successfully exported to {orders_csv_filename}")

    except Exception as e:
        print(f"Error fetching orders: {e}")

    




def get_customer_details():
    customers_data = []

    try:
        # Fetch customers
        customers = shopify.Customer.find()

        # Iterate over customers and collect data
        for customer in customers:
            customer_data = {
                'Customer ID': customer.id,
                'First Name': customer.first_name,
                'Last Name': customer.last_name,
                'Email': customer.email,
                'Phone': customer.phone,
                'Total Spent': customer.total_spent,
                'Orders Count': customer.orders_count,
                'Tags': ''.join(customer.tags) if customer.tags else '',
                'Accepts Marketing': customer.accepts_marketing,
                'Created at': customer.created_at,
                # Add more fields as needed
            }
            customers_data.append(customer_data)

    except Exception as e:
        print(f"Error fetching customers: {e}")

    # Convert customers_data to DataFrame
    customers_df = pd.DataFrame(customers_data)

    # Store DataFrame in a CSV file
    customers_csv_filename = 'shopify_customers.csv'
    customers_df.to_csv(customers_csv_filename, index=False)

    print(f"Customer data successfully exported to {customers_csv_filename}")



def get_discount_details():
    discounts_data = []

    try:
        # Fetch discounts
        discounts = shopify.Discount.find()

        # Iterate over discounts and collect data
        for discount in discounts:
            discount_data = {
                'Discount ID': discount.id,
                'Title': discount.title,
                'Code': discount.code,
                'Amount': discount.amount,
                'Type': discount.discount_type,
                'Starts at': discount.starts_at,
                'Ends at': discount.ends_at,
                # Add more fields as needed
            }
            discounts_data.append(discount_data)

    except Exception as e:
        print(f"Error fetching discounts: {e}")

    # Convert discounts_data to DataFrame
    discounts_df = pd.DataFrame(discounts_data)

    # Store DataFrame in a CSV file
    discounts_csv_filename = 'shopify_discounts.csv'
    discounts_df.to_csv(discounts_csv_filename, index=False)

    print(f"Discount data successfully exported to {discounts_csv_filename}")


if __name__ == "__main__":
    # get_product_details()
    # get_customer_details()
    get_order_details()