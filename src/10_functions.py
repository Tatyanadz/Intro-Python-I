# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE
def is_even(numToCheck):
    if(numToCheck % 2 == 0):
        print(str(numToCheck) + " is even")
    else:
        print(str(numToCheck) + " is odd")
# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)


# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE

is_even(num)