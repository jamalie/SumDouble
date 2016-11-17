#   codingbat code practice
#   Given two int values, return their sum.
#   **Unless the two values are the same, then return double their sum.


def sum_double(a, b):
    if a == b:
        return (a+b)*2
    return a+b

print sum_double(1,2) #Print 3
print sum_double(3,2) #Print 5
print sum_double(2,2) #Print 8

#Solution:
#def sum_double(a, b):
# Store the sum in a local variable
# sum = a + b
#
# Double it if a and b are the same
# if a == b:
#   sum = sum * 2
# return sum