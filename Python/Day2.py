# # Question - 1
# salary = float(input("Enter your salary:"))
# finalTaxRate = 0
# if(salary<30000):
#     finalTaxRate = salary*0.05
# elif(salary>=30000 and salary<=70000):
#     finalTaxRate = salary*0.15
# else:
#     finalTaxRate = salary*0.25
# print(f"the tax for salary {salary} is {finalTaxRate:.3f}")

# # Question - 2
# a = int(input("Enter the start:"))
# b = int(input("enter the end:"))
# for i in range(a,b+1):
#     if(i&1==0):
#         print(i,end=" ")

# #Question - 3,4,5
# n = int(input("Enter the number:"))
# count = 0 
# sum = 0
# dup = n
# print("The digits in the number are:")
# while(n>0):
#     print(n%10,end=" ")
#     count+=1
#     sum+=n%10
#     n = n//10
# print("\n")
# print(f"There are {count} digits in number {dup}")
# print(f"The sum of digits in number {dup} is {sum}")

# # Question - 6
# for i in range(1,101):
#     if(i%3==0 and i%5==0):
#         print(i,end=" ")

# #Question - 7
# while True:
#     n = input("Enter the number:")
#     if(n=="Quit" or n =="quit"):
#         print("Thank you!")
#         break
#     n = int(n)
#     if(n>0):
#         print(f"{n} is a positive number")
#     elif(n<0):
#         print(f"{n} is a negative number")

# # Question - 8
# def calculator(a,b,op):
#     if(op=='+'):
#         return a+b
#     elif(op=='-'):
#         return a-b
#     elif(op=='*'):
#         return a*b
#     elif(op=='/'):
#         return a/b
#     else:
#         print("Check the operator properly...")
# a = int(input("Enter the number-1:"))
# b = int(input("Enter the number-2:"))
# op = input("Enter the operation you want to perform (+,-,*,/):")
# print(f"{a} {op} {b} = {calculator(a,b,op)}")

# # Question - 9     
# def is_prime(n):
#     if(n<2):
#         return False
#     i = 2
#     while(i*i<=n):
#         if(n%i==0):
#             return False
#         i+=1
#     return True
# n = int(input("Enter the number:"))
# s = "prime" if is_prime(n) else "not prime"
# print(f"{n} is {s}")

# # Question - 10
# import random
# def numGuessGame(n,target):
#     if(n==target):
#         print(f"Yes you guessed it right!! \n the number is {target}")
#         return True
#     elif(abs(n-target)<10):
#         print(f"{n} is close to target")
#     elif(n>target):
#         print(f"{n} is larger than target")
#     else:
#         print(f"{n} is smaller than target")
#     return False
# target = random.randint(0,101)
# while True:
#     n = int(input("Enter your guess:"))
#     if(numGuessGame(n,target)):
#         break
