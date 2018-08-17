def filled_square(n):
    for i in range(1, n + 1):
        print("*" * n)

required_number = int(input("Enter Number:"))
result = filled_square(required_number)
