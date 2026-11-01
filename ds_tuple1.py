model_details = ("gpt-model", 128000, True, "xyz")

print(model_details[0])  # gpt-model
print(model_details[1])  # 128000

# Unpacking the tuple into separate variables
model_name, model_size, is_active, dummyx = model_details
print(model_name)  # gpt-model
print(model_size)  # 128000
print(is_active)   # True
print(dummyx)      # xyz
#model_details[0] = "another-model"  # This will raise a TypeError since tuples are immutable
