
choice = input("Enter the choice (press q to quit): ")

while choice != "q":
    num = int(input("Enter the Number to get table of : "))

    for i in range(1,11):
        print(f"{num} x {i} = {num*i}")

    choice = input("Enter the choice (press q to quit): ")

