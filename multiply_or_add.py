# Create a program that will --

# Calculate the product if and only the product of two number is equal to or greater than 1000
# Else, add the two number to get their sum

# DEADLINE: JANUARY 26, 2024

# Assigning the given numbers and their expected output

# Given 1
number_1 = 20
number_2 = 30

# Expected output for Given 1
# The result is 600

# Given 2
number_3 = 30
number_4 = 40

# Expected output for Given 1
# The result is 70

# psuedocode
def multiply_or_add(first_number, second_number):
    product_of_two = first_number * second_number
    if product_of_two <= 1000:
        return print("The results is " + product_of_two)
    else:
        sum_of_two = first_number + second_number
        return print("The results is " + sum_of_two)
    
# The first given values
values_1 = multiply_or_add(20, 30)

# The second given values
values_2 = multiply_or_add(30, 40)