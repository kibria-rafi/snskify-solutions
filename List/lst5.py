def count_elements_greater_than_neighbors(lst):
    count = 0
    for i in range(1, len(lst) - 1):  # Exclude first and last elements
        if lst[i] > lst[i - 1] and lst[i] > lst[i + 1]:
            count += 1
    return count

numbers = input("Enter numbers separated by spaces: ").split()

numbers = [int(num) for num in numbers]

print( count_elements_greater_than_neighbors(numbers))
