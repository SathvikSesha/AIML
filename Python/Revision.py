# simple Python print statement
# print("Hii this is sathvik")

# How to reach the ascii value of a character using ord
# print(ord("a"))

# How to check the version of the system
# import sys
# print(sys.version)

# How to check the time
# import time
# print(time.ctime())

# python variables
# a = 10
# b = 20.0
# c = "sathvik"
# d = False
# e = [1,32,4,5,6,7,8]
# f = 1+5j
# print(f"{type(a)} , {type(b)} , {type(c)} , {type(d)} , {type(e)} , {type(f)}")

# Python Type Casting
# a = 20
# b = float(a)
# c = str(b)
# print(type(a))
# print(type(b))
# print(type(c))

# Assigning Multiple Values
# a,b = 10,20
# print(a,b)
# a,b = b,a
# print(a,b)

# Strings
# str = "sathvik"
# print(len(str))
# print(str[0:4])
# print(str[-4:-1])
# print(str.endswith("vik"))
# print(str.islower())
# print(str.capitalize())
# print(str)
# print(str.isupper())

# Operations
# a , b = 20,10
# print(a+b)
# print(a-b)
# print(a*b)
# print(a<b)
# print(a/b)
# print(a==b)
# print(type(a))
# print(a%b)
# print(5//3)
# print("sathvik" + "is a python programmer")

# Lists
# a = [1,4,2,7,3,5,8,9,6]
# b = ["sathvik","John","Biden","Trump","Obama"]
# print(a,type(a))
# a = [x+2 for x in a]
# print(a)
# c = ["Hi "+x for x in b]
# print(c)
# print(a[1])
# a.append(10)
# a.insert(9,9.5)
# a.sort()
# print(a)
# a.remove(10)
# print(a)

# tuple
# a = (1,2,3,4)
# print(a,type(a))
# print(a.index(3))

# Set 
# a = set()
# for i in range(10):
#     a.add(i)
#     a.add(i+1)
# print(a)
# print(type(a))
# print(a.remove(10))
# # print(a.pop(20))
# print(a.union({1,2,11,20}))
# print(a.intersection(5,1,7,12))
# print(a.difference(2,4,0,14))
# print(a.symmetric_difference(3,9,10,25))

# Dict
# dict1 = {"name":"sathvik","Age":18,"marks":[32,45,46,48,37]}
# print(dict1)
# print(dict1["name"])
# print(dict1["Age"])
# print(dict1['marks'])
# dict1['marks'] = [x+2 for x in dict1['marks']]
# print(dict1['marks'])
# print(dict1.keys())
# print(dict1.items())
# print(dict1.values())

# if - elif - else and short hand
# num = int(input("Enter the number:"))
# if num>18:
#     print("You can vote!!")
# else:
#     print("You cannot vote")

# a = int(input("Enter number-1:"))
# b = int(input("Enter number-2:"))
# c = int(input("Enter number-3:"))
# if a>b and a>c:
#     print(f"{a} is largest")
# elif b>c and b>a:
#     print(f"{b} is the largest")
# else:
#     print(f"{c} is the largest")

# num = int(input("Enter number to find even or odd:"))
# print("Is Evene number" if num%2==0 else "Is Odd number")

# Loops - While and for
# i = 100
# while i>0:
#     if(i%5==0 and i%3==0):
#         print(i)
#     i-=1

# num = int(input("Enter the number: "))
# flag = False
# if num <= 1:
#     print("Not a prime")
# else:
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             print("Not a prime")
#             flag = True
#             break
#     if not flag:
#         print("Yes a prime number")

# a = [1,2,53,77,5,33,22,19]
# print(sum(a))
# for i in a:
#     print(i+1,end=" ")

# functions
# def isPalindrome(n):
#     sum = 0
#     while(n>0):
#         sum = sum*10+n%10
#         n = n//10
#     return sum
# n = int(input("Enter the number: "))
# print(f"The reverse of the number is:{isPalindrome(n)}")

# Classes
# class animal:
#     def __init__(self,name):
#         self.name = name
#     def sound(self):
#         print(f"Hi i am {self.name}! how can i help you")
# dog = animal("dog")
# dog.sound()