# def hello():
#     print("hello")
# function declaration
# write a program to add two numbers using user input and a funtion

# def add():
#     a=int(input("enter the first number:"))
#     b=int(input("enter the second number:"))
#     print("sum =",a+b)

# LOCAL VARIABLES
# variables declared inside a funtion are called local variables

# def add():
#     a=int(input("enter the first number:"))
#     b=int(input("enter the second number:"))
#     print("sum=",a+b)
# add()

# print(a+b)
# we cannot access 'a'and 'b' outside the funtion because they are local variables

# B. GLOBAL VARIABLES
# A variable decleared outside a function is called a global variable
# num=10
# def add():
#     a=int(input("enter the first number:"))
#     b=int(input("enter the second number:"))
#     print("sum=",a+b)
#     print("global variable:",num)
# add()
# print(num)
# print("global variable:",num)

# FUNCTIONS WITH ARGUMENTDS
# def add(a,b):
#     print(a+b)
# add(10,20)

# 1.write a program to find the product of three numbers using and
# def product(a,b,c):
#     print(a*b*c)
# product(10,20,30)

# Arbritrary psitional arguments(*args)
# def values(*num)
#     print(num)
# values(1,12,8,3,5,100,200,200,100)
# write a program to find the sum of all numbers passed to a function.
# def total_sum(*sum):
#     print("numbers=",num)
#     total=0
#     for i in num:
#         total+=i
#     print("sum=",total)
#     total_sum(2,3,5,10,20,15,100,1000)
#     total_sum(2,3)


# 6)
# def reverse_number (num):
#     reverse= 0
#     while num > 0:
#     digit = num% 10
#     reverse = reverse * 10 + digit
#     num = num 
# print("reversed number is:", reverse)
# number = int(input("enter a number:"))
# 5)
# def multiplication_table(num):
#     print("multiplication table of",num)
#     for i in range(1,11):
#         print(num,"x",i,"=",num*i)
# number=int(input("enter a number:"))
# multiplication_table(number)
# 1)
# def add_numbers(a,b):
#     return a+b
# num1=float(input("enter the first number:"))
# num2=float(input("enter the second number"))
# result=add_numbers(num1,num2)
# print("the sum is:",result)

# # 7)
# def check_palindrome(text):
#     if text==text[::-1]:
#         print("the string is a palindrome.")
#     else:
#         print("the string is not a palindrome.")
# string=input("enter a string:")
# check_palindrome(string)

# 17)
# def count_even_odd(*numbers):
#     even=0
#     odd=0
#     for num in numbers:
#         if num%2==0:
#             even+=1
#         else:
#             odd+=1
#      print("number of even numbers:",even)
#      print("number of odd numbers:",odd)
#     nums=list(int,(input("enter numbers separated by space:").split()))
#     count_even_odd(*num)

# # 24)
# def check_divisible(num):
#     if num % 2==0 and num % 3==0:
#         return True
#     else:
#         return False
# number=int(input("enter a number:"))
# if check_divisible (number):
#     print(number,"is divisible by both 2 and 3.")
# else:
#     print(number,"is not divisible by both 2 and 3.")
    
# for i in range(0,3):
#     for j in range(i+3):
#         print("*",end='')
#     print()

# for i in range(0,3):
#     for k in range(2-i):
#         print('',end=' ')
#     for j in range(i+1):
#         print('*',end=' ')
#     print()

# for i in range(0,3):
#     for j in range(3):
#         print('*',end=' ')
#     print()



#1 Custom exception-even number

# class Evennumberexception(Exception):
#     pass
# try:
#     num=int(input("enter a number:"))
#     if num % 2==0:
#         raise Evennumberexception
#     else:
#         print('odd')

# except Evennumberexception :
#     print('even number')

# 2 custom exception-password validation

#  class ShortPasswordException(Exception):
#     pass
#  class NoDigitException(Exception):
#     pass
#  try:
#     password=input("enter a password:")
#     if len(password)<8:
#        raise
#     ShortPasswordException
#     for char in password:
#         raise
#     NoDigitException
#       print("password created successfully")
#  except as e:
#    print(e)

# 3 student marks validation

# class NegativeMarksException(Exception):
#     pass
# class MarksLimitException(Exception):
#     pass
# try:
#     Marks = int(input("enter Marks:"))
#     if Marks<0:
#         raise
#     NegativeMarksException
#     if marks>100:
#         raise
#     MarksLimitException
#     print("valid Marks entered")
# except  e:
#     print(e)  

#   4 Email validation

# class MissingAtSymbolException(Exception):
#     pass
# class MissingDotException(Exception):
#     pass
# try:
#     email=input("enter email address:")
#     if"@" not in email:
#         raise
#     MissingAtSymbolException
#     at_index=email.index("@")
#     if"."not in email[at_index:]:
#         raise
#     MissingDotException
#     print("valid email address")
# except MissingAtSymbolException as e:
#     print(e)
# except MissingDotException as e:
#     print(e)

# 5 ATM Withdrawal 

# class insufficientBalanceException(Exception):
#     pass
# class InvalidAmountException(Exception):
#     pass
# balance=10000
# try:
#     amount=float(input("enter withdrawal amount:"))
#     if amount <= 0:
#         raise
#     InvalidAmountException
#     if amount > balance:
#         raise
#     insufficientBalanceException
#     balance-=amount
#     print("Remaing balance:",balance)
# except InvalidAmountException as e:
#     print("InvalidAmountException:",e)
# except InsufficientBalanceException as e:
#     print("InsufficientBalanceException:",e)

# 6 Handle multiple Exception

# try:
#     num1=int(input("enter first number:"))
#     num2=int(input("enter second number:"))
#     result=num1/num2
#     print("result=",result)
# except ValueError:
#     print("Invalid input! please enter integers only.")
# except ZeroDivisionError:
#     print("cannot divide by zero.")
# finally:
#     print("program completed")

# 7 List index

# languages=["Python","Java","C++","SQL"]
# try:
#     index=int(input("enter the index:"))
#     print("selected languages:",languages[index])
# except ValueError:
#     print("Invalid input! please enter an integer.")
# except IndexError:
#     print("Index out of range.")

# 8 Username validation 

# class ShortUsernameException(Exception):
#     pass
# class SpecialCharacterException(Exception):
#     pass
# try:
#     username=input("enter username:")
#     if len(username) < 5:
#         raise
#     ShortUsernameException
#     if not username.isalnum():
#         raise
#     SpecialCharacterException
#     print("Username accepted")
# except ShortUsernameException as e:
#     print("ShortUsernameException:")
# except SpecialCharacterException as e:
#     print("SpecialCharactersException:")

# 9 Employee age verification

# class UnderAgeException(Exception):
#     pass
# class OverAgeException(Exception):
#     pass
# try:
#     age=int(input("enter age:"))
#     if age < 18:
#         raise
#     elif age >60:
#         raise
#     else:
#         print("Employee is eligible")
# except UnderAgeException as e:
#     print("UnderAgeException:")
# except OverAgeException as e:
#     print("OverAgeException:)
