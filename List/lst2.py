def print_even_elements(lst):
    for num in lst:
        if num % 2 == 0:
            print(num)

# Take input from the user
numbers = input("Enter numbers separated by spaces: ").split()

# Convert the numbers from strings to integers
numbers = [int(num) for num in numbers]

print_even_elements(numbers)
