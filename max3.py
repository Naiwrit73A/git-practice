num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))
num3 = int(input("Enter 3rd number: "))

max(num1,num2,num3)

def max(num1,num2,num3):
    if num1 > num2 and num1 > num3:
        print("The largest number is:", num1)
    elif num2 > num3:
        print("The largest number is:", num2)
    else:
        print("The largest number is:", num3)

