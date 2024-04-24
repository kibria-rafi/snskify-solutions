def find_largest_element(lst):
    max_value = lst[0]
    max_index = 0
    for i in range(1, len(lst)):
        if lst[i] > max_value:
            max_value = lst[i]
            max_index = i
    return max_value, max_index

numbers = input("Enter numbers separated by spaces: ").split()

numbers = [int(num) for num in numbers]

max_value, max_index = find_largest_element(numbers)
print( max_value)
print( max_index)
