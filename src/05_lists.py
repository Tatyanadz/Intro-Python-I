# For the exercise, look up the methods and functions that are available for use
# with Python lists.

x = [1, 2, 3]
y = [8, 9, 10]

# For the following, DO NOT USE AN ASSIGNMENT (=).

# Change x so that it is [1, 2, 3, 4]
# YOUR CODE HERE
x.append(4)
print(x)

# Using y, change x so that it is [1, 2, 3, 4, 8, 9, 10]
# YOUR CODE HERE
<<<<<<< HEAD
x.extend(y)
print(x)

# Change x so that it is [1, 2, 3, 4, 9, 10]
# YOUR CODE HERE
x.pop(4)
print(x)

# Change x so that it is [1, 2, 3, 4, 9, 99, 10]
# YOUR CODE HERE
x.insert(5, 99)
print(x)

# Print the length of list x
# YOUR CODE HERE
print(len(x))
# Print all the values in x multiplied by 1000
# YOUR CODE HERE
print([element * 1000 for element in x])
=======
print(x + y)

# Change x so that it is [1, 2, 3, 4, 9, 10]
# YOUR CODE HERE
y.pop(0)
print(x + y)

# Change x so that it is [1, 2, 3, 4, 9, 99, 10]
# YOUR CODE HERE
y.insert(1, 99)
print(x + y)

# Print the length of list x
# YOUR CODE HERE
print("length", len(x))

# Print all the values in x multiplied by 1000
# YOUR CODE HERE
multiplied = [element * 1000 for element in x]
print(multiplied)
>>>>>>> f0bd116467bbcf5011333d0d528bc42c70155368
