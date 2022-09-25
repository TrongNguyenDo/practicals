num_item = int(input("Enter number of items: "))
sum_item = 0
if num_item <= 0:
    print("Wrong number of items!")
    print()
    num_item = int(input("Enter number of items: "))

elif num_item > 0:
    for i in range(num_item):
        price = float(input("Enter price: $"))
        while price <= 0:
            print("Please enter the price again!")
            price = float(input("Enter price: $"))

        if price > 0:
            sum_item += price

if sum_item > 100:
    sum_item *= 0.9
    # print("Total price for ", num_item, " item is $", sum_item, sep='')
    print(f"Total price for {num_item} item is ${sum_item:.2f}")
