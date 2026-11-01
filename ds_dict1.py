# Demo of Python dictionary data structure using a business example

# A dictionary is a collection of key-value pairs, where each key is unique and maps to a specific value.

# In this example, we will create a dictionary to represent a simple inventory system for a small business.

# Define the inventory dictionary
inventory = {
    "item1": 10000,
    "item2": 20000,
    "xyx": 30000
}

# Adding a new key-value pair to the dictionary
inventory["item3"] = [5000, 6000, 7000]
print(inventory)

# Example of a nested dictionary: product details stored in a dictionary
inventory["item4"] = {
    "name": "Laptop",
    "price": 60000,
    "stock": 10
}
print(inventory["item4"])  # Output: {'name': 'Laptop', 'price': 60000, 'stock': 10}
print(inventory["item4"]["price"])  # Output: 60000

# Changing an existing key's value
inventory["item2"] = 25000
print(inventory["item2"])  # Output: 25000

# Changing another key's value using assignment
inventory["xyx"] = 35000
print(inventory["xyx"])  # Output: 35000

# Accessing values in the dictionary using the get() method
print(inventory.get("item1"))  # Output: 10000
print(inventory.get("item2"))  # Output: 25000
print(inventory.get("xyx"))  # Output: 35000
print(inventory.get("item3"))  # Output: [5000, 6000, 7000]

# Iterating through the dictionary
for item, quantity in inventory.items():
    print(f"{item}: {quantity}")
