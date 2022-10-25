# a
for i in range(0, 101, 10):
    print(i, end=' ')
print()
# b
for i in range(20, 0, -1):
    print(i, end=' ')
print()

# c
starss = int(input("Number of stars: "))
for i in range(1, starss + 1):
    print('*', end=' ')

# d
print()
starss = int(input("Number of stars: "))
for i in range(1, starss + 1):
    print('*' * i)