def print_greater_than_previous(lst):
    if len(lst) <= 1:
        return  # There are no elements to compare

    for i in range(1, len(lst)):
        if lst[i] > lst[i - 1]:
            print(lst[i])


numbers = input("Enter numbers separated by spaces: ").split()

numbers = [int(num) for num in numbers]

print_greater_than_previous(numbers)
