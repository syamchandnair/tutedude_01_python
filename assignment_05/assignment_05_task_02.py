# Assignment 5:
# Module 6: Data Structures and Strings in Python
# Task 2: Demonstrate List Slicing

my_lst = list(range(1, 11))

# extracting first 5 elements
my_lst_5 = my_lst[:5]

print ("Original list: {}".format(my_lst))
print ("Extracted first five elements: {}".format(my_lst))

# reversing extracted list
my_lst_5.reverse()
print ("Reversed extracted elements: {}".format(my_lst_5))

