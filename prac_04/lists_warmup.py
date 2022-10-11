numbers = [3, 1, 4, 1, 5, 9, 2]

numbers[0]
# Value is 3
numbers[-1]
# Value is 2
numbers[3]
# Value is 1
numbers[:-1]
# Value is  begin from index 0 which is 3 to the end : 9 [3,1,4,1,5,9]
numbers[3:4]
# Value is [1]
5 in numbers
# Value is True
7 in numbers
# Value is False
"3" in numbers
# Value is False
numbers + [6, 5, 3]
# Value is [3,1,4,1,5,9,2,6,5,3]

"""1.Change the first element of numbers to "ten" (the string, not the number 10)
2.Change the last element of numbers to 1
3.Get all the elements from numbers except the first two (slice)
4.Check if 9 is an element of numbers
"""
# 1.
"""numbers.pop(0)
numbers.insert(0, "ten")"""
numbers[0] = "ten"
# 2.
"""numbers.pop(-1)
numbers.append(1)"""
numbers[-1] = 1
# 3.
new_numbers = slice(2, len(numbers))
print(numbers[new_numbers])
# 4.
"""for i in numbers:
    if i == 9:
        print("9 is an element of numbers at " + str(numbers.index(i))+" index")"""
print(9 in numbers)







