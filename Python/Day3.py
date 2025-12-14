# #Strings
# str = input("enter your name:")
# print(str)

# count = 0
# for ch in str:
#     if(ch=='a' or ch =='e' or ch == 'i' or ch == 'o' or ch == 'u'):
#         count+=1
# print(f"There are {count} vowels in your name")

# print(str[3:5])

# #List
# l = [43,54,23,17,39]
# print(l)
# l.append(27)
# print(l)
# l.insert(2,65)
# print(l)
# l.remove(27)
# print(l)
# l.pop(2)
# print(l)
# l.reverse()
# print(l)
# l.sort()
# print(l)
# for i in l:
#     print(i,end=" ")
# print("\n")
# print(l[1:5])
# print(list(range(10)))

# Tuple
# t = (1,3,2,4,2,5,2,6)
# print(t)
# print(type(t))
# print(t.count(2))
# print(t.index(3))

# Set
# s = {"Apple","Banana","papaya","Banana","Apple"}
# print(s)
# s1 = {1,2,5,6}
# s2 = {2,3,4,5}
# s1.update(s2)
# print(s1)
# s1.intersection(s2)
# print(s1)

# Dictionary
# dict = {
#     "name":"Sathvik",
#     "Age" : 19,
#     "Marks" : [55,65,75,85,95]
# }
# print(dict)
# print(type(dict))
# print(dict["Age"])
# print(dict.values())
# print(dict.keys())
# print(dict.items())

# info = [
#     ("Sathvik","Math"),
#     ("Alice","English"),
#     ("Alice","Math"),
#     ("Sathvik","Science"),
#     ("Holly","Math"),
#     ("Alice","Science"),
#     ("Holly","English")
# ]
# # print(info)
# course = set()
# for lst in info:
#     course.add(lst[1])
# print(course)

# for stu in info:
#     if(stu[1]=="English"):
#         print(stu[0],end=" ")
# print()

# dic = {}

# for name, course in info:
#     dic.setdefault(name, []).append(course)
# print(dic)

# Question - 1
# str = input("Enter your name:")
# i = 0
# j = len(str)-1
# flag = True
# while i<j :
#     if(str[i]!=str[j]):
#         flag = False
#         break
#     i+=1
#     j-=1
# if flag:
#     print(f"Yes {str} is a palindrome")
# else:
#     print("Not a palindrome")

# Question - 2
# import random
# lst = []
# for i in range(1,10):
#     x = int(random.randint(1,100))
#     lst.append(x)
# sum = 0
# for i in lst:
#     sum+=i
# print(lst)
# print(f"The average of the numbers in the list : {sum/len(lst):.2f}")

# Question - 3
# l1 = [1,2,7]
# l2 = [2,4,5]
# l1.extend(l2)
# l1.sort()
# print(l1)

# Question - 4
# lst = []
# n = int(input("Enter the number of veggies and fruits are you going to enter:"))
# print("enter the names:")
# for i in range(0,n):
#     x = input()
#     lst.append(x)
# dic = {}
# for item in lst:
#     dic[item] = len(item)
# print(dic)

# Question - 5
# str = input("Enter the string:")
# print(str.count(" "))

# Question - 6

