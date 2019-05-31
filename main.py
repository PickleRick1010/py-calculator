import sys
from py_funcs import functions as func

while True:

    print("""
    1 => To add two numbers
    2 => To subtract two numbers
    3 => To divide two numbers
    4 => To multiply two numbers
    5 => To take out the power a number to any degree

    0 => Exit
    """)
    try:
        answer = int(input("Enter one of the options: " ))
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))

        if answer == 1:
            print(num1,"+",num2,"=",func.add(num1,num2))

        elif answer == 2:
            print(num1,"-",num2,"=",func.sub(num1,num2))

        elif answer == 3:
            print(num1,"/",num2,"=",func.div(num1,num2))

        elif answer == 4:
            print(num1,"*",num2,"=",func.mul(num1,num2))

        elif answer == 5:
            print(num1,"^",num2,"=",func.power(num1,num2))

        elif answer == 0:
            sys.exit()



    except(ValueError):
        print("OOPS! WRITE A NUMBER")

