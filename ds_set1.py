# Create examples of various Python Set operations

# Create a set
my_set = {1, 2, 3, 4, 5}    

# Add an element to the set
my_set.add(6)

# Remove an element from the set
my_set.remove(3)

print("Set after adding 6 and removing 3:", my_set)

# Check if an element is in the set
if 4 in my_set:
    print("4 is in the set")

# Get the length of the set
print("Length of the set:", len(my_set))

# Create another set
another_set = {4, 5, 6, 7, 8}

# Perform union operation using the | operator
union_set = my_set | another_set
print("Union of sets:", union_set)

# Perform intersection operation using the & operator
intersection_set = my_set & another_set
print("Intersection of sets:", intersection_set)

# Perform difference operation using the - operator
difference_set = my_set - another_set
print("Difference of sets:", difference_set)

# complex operations
# Create a set of strings   
string_set = {"apple", "banana", "cherry"}

# Add a string to the set
string_set.add("date")
print("String set after adding 'date':", string_set)    

# Remove a string from the set
string_set.remove("banana")
print("String set after removing 'banana':", string_set)


    