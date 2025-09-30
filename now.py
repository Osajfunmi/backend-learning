# Numbers and loops
numbers = [3, 7, 12, 18, 5, 21]

for number in numbers:
    # Task 2: print only numbers greater than 10
    if number > 10:
        print(number)
    if number>10:
        print(number)
    # Task 3: check if even or odd
    if number % 2 == 0:
        print(number, "is even")
    else:
        print(number, "is odd")

numbers = [3, 7, 12, 18, 5, 21]

for number in numbers:
    if number > 10:
        if number % 2 == 0:
            print(number, "is greater than 10 and even")
        else:
            print(number, "is greater than 10 and odd")
    else:
        print(number, "is 10 or less")

