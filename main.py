

try:
    num = int(input("Enter a number : "))

    while num != 0:
        if num % 2 == 0:
            print(" even")
            num = int(input("Enter a number : "))

        elif num % 1 == 0:
            print(" odd")
            num = int(input("Enter a number : "))
except ValueError:
    print("it needs to be a number")
