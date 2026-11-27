list_of_num = [10,25,8,40,15,30]
largest_number = 0
second_largest_num = 0

for num in list_of_num:
    if num > largest_number:
        largest_number = num
    elif num > second_largest_num:
        second_largest_num = num
print(largest_number)        
print(second_largest_num)
    