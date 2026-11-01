# Create a demo program to create examples of list assignment, insertion, index based access, deletion, and iteration using indexes

# List assignment
my_list = [1, 2, 3, 4, 5]

# List insertion
my_list.append(6)
my_list.insert(0, 0)

# Index based access
print(my_list[0])  # Access first element
print(my_list[-1])  # Access last element

# List deletion
my_list.remove(3)  # Remove specific element
print(my_list)

del my_list[0]  # Delete element at index 0
print(my_list)

print(list(range(len(my_list))))

# Iteration using indexes
for i in range(len(my_list)):
    print(f"Element at index {i}: {my_list[i]}")
    
# Show an example of extracting part of a list using slicing
# Slicing the list to get elements from index 1 to 3 (exclusive)
sliced_list = my_list[1:3]
print(f"Sliced list (index 1 to 3): {sliced_list}")

    