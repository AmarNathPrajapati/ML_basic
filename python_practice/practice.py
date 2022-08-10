# '''here I want to print a poem in same manner as written in books'''
# print('''Twinkle, twinkle, little star,
# How I wonder what you are!
# Up above the world so high,
# Like a diamond in the sky.''')
# from playsound import playsound
# playsound('music.mp3')
# import os
# print(os.listdir())

# a = int(input("Enter the first number "))
# sqr = str(a*a)
# print("the square of  number is:"+sqr)

# str = "Chandan"
# print(str[0:])
# print(str[:7])
# print(str[1:6])
# print(str[-7:-1])
# print(str[0:6:2])

# gname = input("Enter the name :")
# givenDate = input("enter the date")
# letter = '''De  ar <|NAME|>,
# Greetings  from ABC coding house. I am happy to tell you about your selection
# You are selected!
# Have a great day ahead!
# Thanks and regards,
# Bill
# Date: <|DATE|>'''
# # letter = letter.replace("<|NAME|>",gname)
# # letter = letter.replace("<|DATE|>",givenDate)
# # print(letter)
# # letter = letter.replace(" ","")
# # print(letter)
# newLetter  = " Dear \'Harry\',\n This python course is very nice.\n\t\t\t\tThanks!"
# print(newLetter)

# lst = [34,"Amar","chandan",None,True,23.23]
# lst.append("Prajapati")
# lst.insert(0,"jaunpur")
# lst.pop(4)
# lst.remove(23.23)
# # lst.sort()
# print(lst)

# tpl = ()
# tpl = (1,)
# tpl = (1,23.3,5,1,5,5,5,5,5,5,)
# print(type(tpl))
# print(tpl)
# print(tpl.count(5))
# print(tpl.index(1))

# marksStudent1 = int(input("Enter the  marksOfStudent1  : "))
# marksStudent2 = int(input("Enter the  marksOfStudent2  : "))
# marksStudent3 = int(input("Enter the  marksOfStudent3  : "))
# marksStudent4 = int(input("Enter the  marksOfStudent4  : "))
# marksStudent5 = int(input("Enter the  marksOfStudent5  : "))
# marksStudent6 = int(input("Enter the  marksOfStudent6  : "))
# lst = [marksStudent1,marksStudent2,marksStudent3,marksStudent4,marksStudent5,marksStudent6]
# print(lst)
# lst.sort()
# print(lst)

# tpl = (1,2,4,5,3,"Amar","Chandan",None,True)
# tpl.append("Prajapati")
# print(tpl)

# lst = [1,2,3,5]
# print(lst[0]+lst[1]+lst[2]+lst[3])

# a = (7,0,8,0,0,9)
# print(a.count(0))

# dict = {
#     "Name":"Amar Nath",
#     "lastName":"Prajapati",
#     "Age":19,
#     "Married":False,
#     "lst":[23,35,57,63,42],
#     "Name":"Chandan"#no duplicate key allowed ,here name has updated
# }
# dict.update({"role":"Programmar"})
# print(dict.get("Name1"))
# print(dict["Name1"])
# print(dict)

# set = {1,2,4,5,3,3,3,3.0,5,5,6,7}
# set.add(34)
# print(set)
# print(len(set))
# set.remove(34)
# print(set)
# set.pop()
# print(set)
# set = set.union({45,32,45})
# print(set)
# set = set.intersection({1,2,32,56,65})
# print(set)


# dict = {
#     "Summit":"Sikhar Sammenlan",
#     "floral":"Phoolo ki",
#     "Reverberates":"Gunjati hai",
#     "Homage":"Shradhda",
#     "Venue":"Sthan"
# }
# print(dict["Homage"])
# print(dict["Reverberates"])

# num1 = int(input("Enter the number"))
# num2 = int(input("Enter the number"))
# num3 = int(input("Enter the number"))
# num4 = int(input("Enter the number"))
# num5 = int(input("Enter the number"))
# num6 = int(input("Enter the number"))
# num7 = int(input("Enter the number"))
# num8 = int(input("Enter the number"))
# set = {num1,num2,num3,num4,num5,num6,num7,num8}
# print(set)

# set = {18,"18",18.0}
# print(set)
# set = {}
# print(type(set))

# dict = {}
# dict.update({"Amar":"Python"})
# dict.update({"Chandan":"JavaScript"})
# dict.update({"Chandan":"Css"})
# dict.update({"Pandit":"Css"})
# print(dict)

# dict = {}
# dict["Amar"]="Python"
# dict["Chandan"]="Python"
# print(dict)

# if(True and True):
#     print("yes")
# else:
#     print("No")
# age = int(input("Enter your Age"))
# if(age>=18):
#     print("yes")
# else:
#     print("No")

# a = int(input("Enter the marks "))
# b = int(input("Enter the marks "))
# c = int(input("Enter the marks "))

# avg = (a+b+c)/3
# if(a>33 and b>33 and c>33 and avg>40):
#     print("You are Selected")
# else:
#     print("You are not selected")

# spamComment = input("Write your comment")
# if(spamComment.count("subscribe now!")):
#     print("this is spam comment don't click this")
# elif(spamComment.count("buy now!")):
#     print("this is spam comment don't click this")
# elif(spamComment.count("make a lot of money")):
#     print("this is spam comment don't click this")
# else:
#     print("this is not a  spam comment")


# if(len(userName)<10):
#     print(userName+" contain less than 10 character")
# else:
#     print("everything is OK")

# lst = ["Amar","Chandan","Prajapati","Golu"]
# userName = input("Enter your Name: ")
# if(lst.count(userName)):
#     print(userName+" is present in the list")
# else:
#     print("name is not found")

# per = int(input("Enter Your percentage : "))
# if(per> 90 and per<= 100):
#     print("Execellent")
# elif(per> 80 and per<= 90):
#     print("A")
# elif(per> 70 and per<= 80):
#     print("B")
# elif(per> 60 and per<= 70):
#     print("C")
# elif(per> 50 and per<= 60):
#     print("D")
# else:
#     print("Fail")

# post = input("write your post\n")
# if(post.count("Harry")):
#     print("this post is talking about Harry")
# else:
#     print("this post is not talking about harry")
# a=1
# while(a<=50):
#     print(a)
#     a +=1

# from os import pipe


# lst = ["False", 1, 2, 3, "Amar", "Chandan", True, 23232.2323]
# for item in lst:
#     print(item)
# for  i in range(0,200):
#     if(i==100):
#         continue
# #     print(i)
# for  i in range(0,200):
#     pass
# for  i in range(0,200):
#     print(i)
#     if(i==100):
#         break

# num = int(input("Enter the number whose table you want"))
# i = 1
# while(i<11):
#     print(f"{num}x{i}={num*i}")
#     i += 1
# for i in range(0,11):
#     print(f"{num}x{i}={num*i}")

# lst = ["Amar", "Sohan", "Sachin", "Rahul"]
# for name in lst:
#     if(name.startswith("S")):
#         print(name)


# num = int(input("Enter the number"))
# prime = True
# for i in range(2,num):
#     if (num%i==0):
#         prime = False
# if(prime):
#     print("This is a prime number")
# else:
#     print("This is not a prime number")

# num = int (input("Enter the number"))
# fact = 1
# for  i in range(1,num+1):
#     fact*=i
# print(fact)

# i = 1
# while(i<=num):
#     sum +=i
#     i +=1
# print(sum)

# num = int (input("Enter the number : "))
# for i in range(1,num+1):
#     print("*"*i)

# for i in range (100):
#     print(i)

# n=3
# for i in range(3):
#     print(" "*(n-i-1),end="")                             #important
#     print("*"*(2*i+1),end="")
#     print(" "*(n-i-1))


# for i in range(3):
#     print(" "*(3-i-1),end="")
#     print("*"*(2*i+1),end="fdfdd")
#     print(" "*(3-i-1))

# str = "Amar Nath"
# for i in str:
#     print(i)


# for i in range(10,0,-1):
#     print(5*i)
# def greet(name = "stranger"):
#     print("Good Day "+ name)
# greet("Amar Nath")

# def greatest(num1,num2,num3):
#     if(num1>num2):
#         greater = num1
#     else:
#         greater = num2
#     if(greater>num3):
#         print(f"{greater} is greatest number")
#     else:
#         print(f"{num3} is greatest number")
# greatest(1211,454,132)

# temp  = int(input("Enter your body Temperature : "))
# def CtoF(celcius):
#     return (9/5)*celcius + 32
# f=CtoF(temp)
# print(f"farenheight value is {f}")

# print("Amar nath prajapati " ,end="")
# print("I am from jaunpur uttar pradesh")

# def sum(n):
#     if(n==0):
#         return 0
#     else:
#         return n+sum(n-1)
# summation = sum(5)
# print(f" the summation of first 10 natural number is {summation}")

# def pic(n):
#     if(n==0):
#         return
#     else:
#         print("*"*n)
#         pic(n-1)
# pic(3)

# def inchToCms(inch):
#     return inch * 2.54
# cms = inchToCms(66)
# print(f"your height in cenimneter is :  {cms}")

# lst = ["Amar","Chandan","Golu"]
# def rem(name):
#         lst.remove(name)
#         print(lst)
# rem("Golu")

# def mulTable(i):
#     num = 5
#     if(i>10):
#         return
#     else:
#         print(num*i)
#         mulTable(i+1)
# mulTable(0)

# f = open("Amar.txt","w")
# f.write("Amar Nath is a good python programmar")
# f.close()
# with open ("Amar.txt","a") as f:
#     f.write("I am from Jaunpur uttar pradesh")

# with open ("poem.txt","r") as f:
#     poem = f.read()
#     print(poem.index("Twinkle"))
from functools import reduce
from typing import Dict, Text
# if(poem.index("Twinkle")):
#     print("the poem has word 'Twinkle'")
# else:
#     print("the poem has not word 'Twinkle'")

# def game():
#     return 45
# hiscore= game()
# with open("hiscore.txt","w") as f:
#     f.write(str(hiscore))

# for j in range(2,21):
#     with open (f"table/ Multiplication_table_of{j}","w") as f:
#         for i in range(1,11):
#             f.write((f"{j}x {i} = {j*i}\n"))
# lst = ["donkey","mote","kaddu","bhodu"]
# with open("donkey.txt","r+") as f:
#     text = f.read()
#     for word in lst:
#         text = text.replace(word,"######")
# with open("donkey.txt","w") as f:
#     f.write(text)
# content = True
# i = 1
# with open("Amar.txt","r+") as f:
#     while(content):
#         content = f.readline()
#         if "python" in content:
#             print(f"python is present in line number {i}")
#             print(content)
#         i+=1

# with open("Amar.txt","r+") as f:
#     text1 = f.read()
# with open("Chandan","r+") as g:
#     text2 = g.read()
# if(text1 == text2):
#     print("file are identical")
# else:
#     print("file are not identical")
# import os
# with open("Chandan","r+") as f:
#     text1 = f.read()
# with open("renamed_by_python","w") as g:
#     g.write(text1)
# os.remove("Chandan")
# os.rename("Golu.txt","Chandan.txt")

# class Employee:
#     def __init__(self):
#         print("You are selected")
#     company = "Google"
#     venue = "India"
#     def name(self):
#         print("what is your name?")
#     @staticmethod
#     def getSalary():
#         return print("your salary is 50k$")
# e = Employee()
# e.name()
# Amar.age = 19
# # print(Amar.company)
# # print(Amar.age)
# Amar.getSalary()
# Amar.getSalary() == Employee.getSalary(Amar)
# Amar.greet() == Employee.greet()

# class programmer:
#     company = "Microsoft"
#     vunue = "India"
#     def slogan(slf):
#         print("This is the best company for operating System")
#         print(f"The age of programmer is {slf.age} ")
# Amar = programmer()
# Amar.age = 19
# Amar.slogan()
# Chandan = programmer()
# Chandan.salary = "Salary is 100"
# print(Amar.company)
# Amar.slogan()
# print(Amar.age)
# print(Chandan.salary)

# import math
# class Calculator:
#     @staticmethod
#     def greet():
#         print("Hello")
#     def square(self,num):
#         return num*num
#     def cub(self,num):
#         return num*num*num
#     def squareRoot(self,num):
#         return math.sqrt(num)
# cal = Calculator()
# print(cal.square(5))
# print(cal.cub(5))
# print(cal.squareRoot(676))
# print(cal.greet())

# class sample:
#     a = "Amar"
# obj=sample()
# obj.a = "Chandan"
# sample.a="Chandan"
# obj2=sample()
# print(obj2.a)
# print(obj.a)
# print(sample.a)

# class Train:
#     def __init__(self,name,fare,seats):
#         self.name = name
#         self.fare = fare
#         self.seats= seats
#     def getStatus(self):
#         print(f"The name of the train is {self.name}")
#         print(f"The number of seats available in the train is {self.seats}")
#     def fareInfo(self):
#         print(f"The fare of the train is {self.fare}")
#     def bookTicket(self):
#         if(self.seats>0):
#             print("your ticket has booked successfully")
#             self.seats = self.seats-1
#             print(f"your ticket number is {self.seats} ")
#         else:
#             print("Train is full")
# train1 = Train("Godan",100,1000)
# train1.getStatus()
# train1.fareInfo()
# train1.bookTicket()

# class v2d:
#     def __init__(self,i,j):
#         self.i = i
#         self.j = j
#     def __str__(self):
#         return (f"{self.i}i + {self.j}j ")
# class v3d(v2d):
#     def __init__(self, i, j,k):
#         super().__init__(i, j)
#         self.k = k
#     def __str__(self):
#         return (f"{self.i}i + {self.j}j + {self.k}k ")
# vect1 = v2d(3,4)
# print(vect1)
# vect2 = v3d(5,4,3)
# print(vect2)


# class animal:
#     def __init__(self):
#         print("This is a animal")
# class pets(animal):
#     def __init__(self):
#         super().__init__()
#         print("This animal is a pet animal")
# class dogs(pets):
#     def __init__(self):
#         super().__init__()
#         print("This is a dog and the variety of dog is labradoor")
#     barks = "The dog is barking"
# tommy = dogs()
# print(tommy.barks)

# class vector:
#     def __init__(self, i, j, k):
#         self.i = i
#         self.j = j
#         self.k = k
#     def __str__(self):
#         return(f"{self.i}i + {self.j}j + {self.k}k")
#     def __len__(self):
#         return 1000
# vect = vector(45,34,23)
# print(vect)
# print(len(vect))


# while(True):
#     num =(input("Enter the number: "))
#     try:
#         if(num=="q"):
#             break
#         if(int(num)>10):
#             print("you win")
#         else:
#             print("you lose")
#     except Exception as e:
#         print("Your error is ",e)
# print("Thanks for playing this game")


# while(True):
#     num =(input("Enter the number: "))
#     try:
#         if(num=="q"):
#             break
#         val = 1/int(num)
#         if(val>0):
#             print("you win")
#         else:
#             print("you lose")
#     except ZeroDivisionError as e:
#         print("you can't enter zero because ",e)
#     except ValueError as e:
#         print("you can not enter string because ",e)
#     except Exception as e:
#         print("Your error is ",e)
# print("Thanks for playing this game")

# while(True):
#     num =(input("Enter the number: "))
#     try:
#         if(num=="q"):
#             break
#         val = 1/int(num)
#         if(val>0):
#             print("you win")
#         else:
#             print("you lose")
#     except :
#         raise ZeroDivisionError("you can't enter zero ")
# print("Thanks for playing this game")
# while (True):
#     try:
#         a = input("Enter the number")
#         val = 1/int(a)
#     except Exception as e:
#         print(e)
#     else:
#         print("we are successful")

# while (True):
# try:
#     a = input("Enter the number: ")
#     val = 1/int(a)
# except Exception as e:
#     print(e)
#     exit()
# else:
#     print("we are successful")
# finally:
#     print("Eventhough your program stopped , it will have to excute")

# def greet(name):
#     print(f"Good Morning, {name}")
# if(__name__=="__main__"):
#     print(__name__)
#     greet("Amar")
#     print("Amar Nath is good python programmer")

# a = 12
# def sum():
#     b =10
#     #a =8
#     global a
#     print("The sum of a and b is : ",a +b)
# sum()

# list = ["Amar","Chandan","Golu",23,434,True]
# for i , item in enumerate(list):
#     print(i,item)

# lst = [1,2,34,3,5,56,577,678,78,78,5,3,43]
# lst2 =[ i for i in lst if i>5]
# print(lst2)

# try:
#     with open ("golu.txt","r") as f:
#         print(f.read())
#     with open ("Amar.txt","r") as f:
#         print(f.read())
# except Exception as e:
#     print(e)

# def read(fileName):
#     try:
#         with open(fileName,"r") as f:
#             print(f.read())
#     except FileNotFoundError:
#         print("File is not find")
# read("Amar.txt")
# read("Golu.txt")
# read("Chandan.txt")
# try:
#     lst = ["Amar","Chandan",12,34,"Amar",True,232]
#     for i , item in enumerate(lst):
#         if(i==2 or i == 4 or i==6):
#             print(i+1,item)
# except Exception as e:
#     print(e)

# num = int(input("Enter the number: "))
# lst2 = [ num*i for i in range(1,11) ]
# print(lst2)
# with open("Chandan.txt","w") as f:
#     f.write(str(lst2))

# while(True):
#     try:
#         b = input("Enter a number: ")
#         val = 12/int(b)
#         print(val)
#     except ZeroDivisionError:
#         print("infinite")

# square= lambda a:a*a
# print(square(5))
# sum = lambda a,b,c:a+b+c
# print(sum(23,54,2))

# lst = ["Amar Nath","Chandan","Golu"]
# lst = [str(i*7 for i in range(1,11))]
# print(str(" \n ".join(lst)))

# name = "Amar Nath "
# place = "Jaunpur U.P."
# print("My Name is {} and I am from {}".format(name,place))
# print("My Name is {} ,{} and {} ".format(lst[0],lst[1],lst[2]))
# print("My Name is {1} ,{2} and {0} ".format(lst[0],lst[1],lst[2]))

# lst = [1,2,4]
# square= lambda a:a*a
# print(list(map(square,lst)))

# lst = [1, 2, 3, 4]
# def greater(a):
#     if(a>10):
#         return True
#     else:
#         return False
# print(list(filter(greater,lst)))
# def sum(a, b): return a+b


# val = reduce(sum, lst)
# print(val)

# name  = input("Enter your name: ")
# marks = int(input("Enter your marks: "))
# phoneNumber = int(input("Enter your phone number : "))
# print("The name of the student is {} , and his marks are {}  and phone number is {} ".format(name,marks,phoneNumber))

# lst = [7,14,21,28,35,42,49,56,63,70]
# print(" a ".join(lst))

# lst = [str(i*7) for i in range ( 1,11)]
# print("\n".join(lst))

# def divisibleBy5(a):
#     if(a%5==0):
#         return True
#     else:
#         return False
# lst = [12,34,23,4,10,15,35,56,4565,45,4,34,50]
# print(list(filter(divisibleBy5,lst)))

# from functools import reduce
# lst = [12,34,23,4,10,15,35,56,4565,45,4,34,50]
# print(reduce(max,lst))


a = []
for i in range(10):
    a.append(i*++i)
for a[i] in a:
    print(a[i])



