# Write a program that takes a range of numbers as input and outputs the Prime
# Numbers in that range.

num = int(input("Enter the number : "))
try:
    if num == 0:
        print("This is whole number  ")
    elif num == 1:
        print("This is not a prime number")
    elif num >= 2:
        for i in range (2,num):
            if (num%i) == 0:
                print(num, "the number is not a prime number ")
                

    
except NameError:
    print("Invalid input , Please Enter interger number only")
    