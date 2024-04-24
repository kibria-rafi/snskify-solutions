def print_even_index_elements(lst):
    for i in range(len(lst)):
        if i % 2 == 0:
            print(lst[i])

numbers = [4, 5, 3, 4, 2, 3]
print("Elements with even index numbers:")
print_even_index_elements(numbers)