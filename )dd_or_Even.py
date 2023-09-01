"""
Program: Odd_or_Even.py
Author: Allen Whittenbury
Date: 02/09/2023
Purpose: This script will ask the user to enter a whole number and
will then tell the user if that number is odd or even

"""


def odd_even():
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


odd_even()
