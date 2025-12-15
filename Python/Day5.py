# f = open("sample.txt","r")
# data = f.read()
# print(data)
# f.close()

# f = open("sample.txt",'w')
# f.write("New data is written")

# f = open("sample2.txt","x")
# f.write("Random text")
# f1 = open("sample2.txt","r")
# print(f1.read())
# f1.close()

# with open(r"d:\AIML\Python\sample.txt", "r") as f:
#     print(f.read())

# data = True
# with open(r"d:\AIML\Python\sample.txt", "r") as f:
#     while data:
#         data = f.readline()
#         if("python" in data):
#             print("word found")
#             break
#         print(data)

#List Comprehensions
# l = [x*2 for x in range(1,10)]
# print(l)

# a = [x**2 for x in l]
# print(a)

# b = [x for x in a if x%3==0]
# print(b)