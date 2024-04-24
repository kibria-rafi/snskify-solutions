def print_unique_elements(lst):
    element_count = {}
    for num in lst:
        if num in element_count:
            element_count[num] += 1
        else:
            element_count[num] = 1
    
    for num in lst:
        if element_count[num] == 1:
            print(num, end=' ')
numbers = input("Enter numbers separated by spaces: ").split()
numbers = [int(num) for num in numbers]

print_unique_elements(numbers)
