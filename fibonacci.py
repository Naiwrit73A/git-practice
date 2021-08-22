#This code helps in generating fibonacci numbers upto a certain range given as user input

# f1 = 0
# f2 = 1
# n = int(input("Enter the range: "))
# print(f1,f2,end=' ')

# for count in range(2,n):
#     f3 = f1 + f2
#     print(f3,end=' ')
#     f1 = f2
#     f2 = f3

f1 = 0
f2 = 1
num = int(input("Enter the number: "))
#print(a,b,end =' ') #end is basically for formatting used in the print fucntion to input space instead of next line

count = sum = 0

if num <= 0:
    print("wrong")
elif num == 1:
    print("Fibonacci series: ",num)
    print(f1)
else:
    print("Fibonacci series")
    while count < num:
        print(f1)
        sum = f1 + f2
        f1 = f2
        f2 = sum
        count = count + 1
