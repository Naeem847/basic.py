print("hello world")

# check Even or Odd
num=float(input("enter the number\n"))
if num%2==0:
    print("num is even")
else:
    print("num is odd")

# find the largest of two number
a=int(input("enter the num1\n"))
b=int(input("enter the num2\n"))
if a>b:
    print("a is greater then b")
else:
    print("b is greater then a")

# 5 swaping the two numbers
a=int(input("enter the num1\n"))
b=int(input("enter the num2\n"))
temp=int
temp=a
a=b
b=temp
print("swapping the numbers","a is",a,"and","b is",b)

# create a simple calculator
a=int(input("enter the 1st numb\n"))
b=int(input("enter the 2nd numb\n"))
choice=input("enter your choice\n")
if choice =='+':
    print("add",a+b)
elif choice=='-':
    print("sub",a-b)
elif choice=='*':
    print("multi",a*b)
elif choice=='%':
    print("divide",a%b)
else:
    print("invalid choice")
