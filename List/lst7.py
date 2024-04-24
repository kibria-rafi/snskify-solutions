def count_distinct_elements(lst):
    distinct_count = 0
    prev_element = None
    for element in lst:
        if element != prev_element:
            distinct_count += 1
        prev_element = element
    return distinct_count

numbers = input("Enter numbers separated by spaces (sorted in ascending order): ").split()

numbers = [int(num) for num in numbers]

print( count_distinct_elements(numbers))
