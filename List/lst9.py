
numbers = input("Enter unique numbers separated by spaces: ").split()
numbers = [int(num) for num in numbers]
min_index = numbers.index(min(numbers))
max_index = numbers.index(max(numbers))

numbers[min_index], numbers[max_index] = numbers[max_index], numbers[min_index]

for num in numbers:
    print(num, end=' ')
