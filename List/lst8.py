
numbers = input("Enter numbers separated by spaces: ").split()

numbers = [int(num) for num in numbers]

for i in range(1, len(numbers), 2):
    numbers[i], numbers[i - 1] = numbers[i - 1], numbers[i]

for num in numbers:
    print(num, end=' ')
