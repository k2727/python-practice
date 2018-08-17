def square(n):
    spaces = n -2
    for i in range(1, n + 1):
        if i == 1:
            print('*' * n)
        elif i<n:
            print("*" + ' ' * spaces + "*")
        else: print('*'  *  n)


required_number = int(input("Enter Number:"))
result = square(required_number)
