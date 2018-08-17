def diamond(n):
    stars = 1
    max_spaces = n // 2
    for blanks in range(max_spaces, -1, -1):
        print(blanks * ' ' + stars * '*')
        stars = stars + 2

        star = stars -4
    for blanks in range(1, max_spaces + 1):
        print(blanks * ' ' + star * '*')
        star = star - 2



required_number = int(input('Enter Number'))
diamond(required_number)
