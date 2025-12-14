# class student:
#     University = "Stanford"
#     def __init__(self,name,age,branch):
#         self.age = age
#         self.name = name
#         self.branch = branch
    
#     @classmethod
#     def get_University(cls):
#         print(f"The {cls.University} University")

#     def display(self):
#         print(f"Name : {self.name} Age : {self.age} Branch : {self.branch}")
# s = []
# s.append(student("Sathvik",20,"CSE"))
# s.append(student("Shiva",100,"Humanity and Worship"))
# s.append(student("Rama",80,"Ethics and values"))
# for i in s:
#     i.get_University()
#     i.display()

# class Store:
#     count = 0
#     def __init__(self,name,price):
#         self.name = name
#         self.price = price
#         Store.count+=1
    
#     @classmethod
#     def get_count(cls):
#         return cls.count
    
#     def display(self):
#         print(f"Name : {self.name} Price : {self.price}")
    
#     @staticmethod
#     def discount(price,per):
#         print(f"The final price : {price - (price*per/100):.2f}")

# p1 = Store("Iphone 16 pro max",10_0000)
# p2 = Store("Samsung Galaxy S24",12_0000)     
# p3 = Store("Google pixel",85_000)
# p1.display()
# p2.display()
# p3.display()

# print(f"There are {Store.get_count()} products in the cart")

# p1.discount(p1.price,17.5)
# p2.discount(p2.price,15)
# p3.discount(p3.price,18.4)


# Inheritence
# class employee:
#     def __init__(self,start,end):
#         self.start = start
#         self.end = end

# class grade1(employee):
#     def __init__(self, name,start, end):
#         super().__init__(start, end)
#         self.name = name
#         print(f"{self.name} is Grade 1 employee")
#     def display(self):
#         print(f"{self.name} started at {self.start} AM and ended work at {self.end} PM")
# class grade2(employee):
#     def __init__(self, name,start, end):
#         super().__init__(start, end)
#         self.name = name
#         print(f"{name} is Grade 2 employee")
    
#     def display(self):
#         print(f"{self.name} started at {self.start} AM and ended work at {self.end} PM")

# g1 = grade1("sathvik",10,7)
# g2 = grade2("Rohan",10,8)

# g1.display()
# g2.display()


# Abstraction
# from abc import ABC

# class Animal(ABC):
#     def sound(self):
#         pass

# class Dog(Animal):
#     def sound(self):
#         print("Bow! Bow! Bow!")
 
# class Cat(Animal):
#     def sound(self):
#         print("Meow! Meow! Meow!")
# dog = Dog()
# cat = Cat()
# dog.sound()
# cat.sound()

# Polymorphism
# class Employee:
#     def display(self):
#         print("This is employee of xyz company")

# class SoftwareDev(Employee):
#     def display(self):
#         print("I am the Software Developer in XYZ company")

# class Designer(Employee):
#     def display(self):
#         print("Hey this is designer from xyz!")
# s1 = SoftwareDev()
# s2 = Designer()
# s1.display()
# s2.display()


class User:
    def __init__(self,name):
        self.name = name
        self.chatroom = None
    
    def join(self,chatroom):
        if self.chatroom:
            print(f"{self.name} is already in the chat room.")
        else:
            chatroom.addUser(self)
            self.chatroom = chatroom
            print(f"{self.name} joined {chatroom.name}")
    def leave(self):
        if not self.chatroom:
            print(f"{self.name} is not in any chat room")
        else:
            self.chatroom.remove(self)
            print(f"{self.name} left from {self.chatroom.name}")
            self.chatroom = None
    def sendMessage(self,message):
        if not self.chatroom:
            print(f"You are not in any chat room")
        else:
            self.chatroom.broadcast(self,message)

class Message:
    count = 1
    def __init__(self,name,message):
        self.name = name
        self.message = message
        Message.count+=1
    
    def __str__(self):
        return f"{self.name}: {self.message}"

class ChatRoom:
    def __init__(self,name):
       self.name = name
       self.users = []
       self.messages = []
    
    def addUser(self,user):
        self.users.append(user)
    
    def remove(self,user):
        self.users.remove(user)
    
    def broadcast(self, user, message):
        mess = Message(user.name, message)
        self.messages.append(mess)
        print(mess.message)

    def history(self):
        print("The chat history:")
        for i in self.messages:
            print(i)
        print()

room = ChatRoom("Avengers")
u1 = User("sathvik")
u1.join(room)
u2 = User("Saddie")
u2.join(room)

u1.sendMessage("Hi this is sathvik")
u2.sendMessage("Hi i am saddie")
u1.sendMessage("Yeah! how are you?")
u2.sendMessage("Ha! I am good wau?")
u1.sendMessage("Okay then byeee!")
u2.sendMessage("Byee")

room.history()