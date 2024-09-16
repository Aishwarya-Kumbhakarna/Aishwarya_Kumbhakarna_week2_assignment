
'''Implement a program that takes a tuple of integers and returns a new tuple with even numbers only.'''

def filter_even_numbers(numbers):
    even_numbers = tuple(num for num in numbers if num % 2 == 0)
    return even_numbers

numbers_tuple = (12, 21, 3, 44, 5, 68, 79, 80, 9, 10)


even_tuple = filter_even_numbers(numbers_tuple)
print("Original tuple:", numbers_tuple)
print("Tuple with even numbers only:", even_tuple)
