# Example: Simulating a simple inventory management system with nested loops

# Store fictitious product names in a list
products = ["Laptop", "Mouse", "Monitor"]

# Iterate through each product and display its name
for product_name in products:   # Python list products is an iterable, so we can use a for loop to iterate through it
    print(f"\nManaging Product: {product_name}")
    
    # Inner loop for managing stock levels of the current product
    stock_level = 5  # Initial stock level for the product
    while stock_level > 0:
        print(f"Current stock level for {product_name}: {stock_level}")
        
        # Simulate a sale
        sale_quantity = int(input(f"Enter quantity sold for {product_name} (or 0 to stop selling): "))
        if sale_quantity == 0:
            print(f"Stopping sales for {product_name}.")
            break
        
        if sale_quantity <= stock_level:
            stock_level -= sale_quantity
            print(f"Sold {sale_quantity} units. New stock level: {stock_level}")
        else:
            print("Not enough stock to fulfill the sale.")