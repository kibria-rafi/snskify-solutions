def count_equal_pairs(lst):
    count = 0
    n = len(lst)
    for i in range(n):
        for j in range(i + 1, n):
            if lst[i] == lst[j]:
                count += 1
    return count

# Take input from the user
numbers = input("Enter numbers separated by spaces: ").split()

# Convert the numbers from strings to integers
numbers = [int(num) for num in numbers]

print("Number of element pairs with the same value:", count_equal_pairs(numbers))
