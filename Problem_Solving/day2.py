numbers = [15, 8, 25, 3, 40, 12, 6]
smallest_num = float('inf')
second_smallest_num = float('inf')

for num in numbers:
    if num < smallest_num:
        # second_smallest_num = smallest_num
        smallest_num = num
    elif smallest_num > second_smallest_num:    
        smallest_num = second_smallest_num
print(smallest_num)
print(second_smallest_num)        