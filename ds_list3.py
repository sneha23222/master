# Create an example multi-level Python List with a business scenario
# Let's say we have a company with multiple departments, and each department has multiple employees.
company = [
    ["Alice", "Bob", "Charlie"],
    ["David", "Eve"],
    ["Frank", "Grace", "Henry"]
]
# Accessing elements in the multi-level list
print(company[0])  # Output: ['Alice', 'Bob', 'Charlie'] (Accessing the first department)
print(company[1][0])  # Output: 'David' (Accessing the first employee in the second department)
# Iterating through the multi-level list
for department in company:
    print("Department:")
    for employee in department:
        print(f" - {employee}")
        