# Example: Simulating a simple inventory management system with nested loops

# Outer loop for managing multiple products

product_count = 3
product_index = 0

while product_index < product_count:
    print(f"\nManaging Product {product_index + 1}")
    
    # Inner loop for managing stock levels of the current product
    stock_level = 5  # Initial stock level for the product
    while stock_level > 0:
        print(f"Current stock level: {stock_level}")
        
        # Simulate a sale
        sale_quantity = int(input("Enter quantity sold (or 0 to stop selling): "))
        if sale_quantity == 0:
            print("Stopping sales for this product.")
            break
        
        if sale_quantity <= stock_level:
            stock_level -= sale_quantity
            print(f"Sold {sale_quantity} units. New stock level: {stock_level}")
        else:
            print("Not enough stock to fulfill the sale.")
    
    product_index += 1