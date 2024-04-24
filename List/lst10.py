def count_equal_pairs(lst):
    count = 0
    n = len(lst)
    for i in range(n):
        for j in range(i + 1, n):
            if lst[i] == lst[j]:
                count += 1
    return count
numbers = input("Enter numbers separated by spaces: ").split()
numbers = [int(num) for num in numbers]

print( count_equal_pairs(numbers))
