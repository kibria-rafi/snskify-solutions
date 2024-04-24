def find_same_sign_adjacent_elements(lst):
    for i in range(len(lst) - 1):
        if lst[i] * lst[i + 1] > 0:
            print(lst[i], lst[i + 1])
            return

numbers = input("Enter numbers separated by spaces: ").split()

numbers = [int(num) for num in numbers]

find_same_sign_adjacent_elements(numbers)
