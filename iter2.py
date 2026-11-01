# show an example of while loop in python using a numeric variable and a condition. 
# The loop should run until the variable reaches a certain value, and in each iteration, it should print the current value 
# of the variable and then increment it by 1.

i = 0
while i < 5:
    print(i)
    if i == 2:
        # exit the loop if the variable reaches 2
        break
    i += 1
    
print("Loop exited. Final value of i:", i)

    
