# # # #starting to learn OOP
# # # class Aalu: 
# # #     def __init__(self, product):
# # #         self.product = product
    

# # #     def printint(self):
# # #         print(f"product name is :{self.product}")



# # # ramu = Aalu("ramesh")

# # # ramu.printint()
        

# # # #practice practice and practice

# # # class Books:
# # #     def __init__(self,title,  author, prices):
# # #         self.title = title
# # #         self.author = author
# # #         self.prices = prices

# # #     def applydiscounts (self, discount):
        
        
# # #         self.prices = self.prices - discount 
    
# # #     def displayinfo(self):
# # #         print(f"Name of the book is {self.title}")
# # #         print(f"Author of the book is {self.author}")
# # #         print(f"Price of the book is {self.prices}")


# # # book = Books("Subtle Art", "Shyam", 1000)
# # # book.applydiscounts(100)
# # # book.displayinfo()  

# # class BankAcc:
# #     def __init__(self, accountholder, balance):
# #         self.accountholder = accountholder
# #         self.balance = balance
    
# #     def deposite(self, deposite):
# #         self.balance = self.balance + deposite
    
# #     def withdraw (self, withdraw):
# #         if(self.balance < withdraw):
# #             print(f"insufficient funds! you only have {self.balance}")
        
# #         self.balance = self.balance - withdraw

# #     def display (self):
# #         print(f"Account Holder : {self.accountholder}")
# #         print(f"Current Balance : {self.balance}")
    

# # abishek = BankAcc("Abishek", 100000)
# # ramu = BankAcc ("Ramu", 14000)
# # abishek.withdraw(300000)
# # ramu.deposite(6050)
# # ramu.display()

# # abishek.display()


# # practice practice practice

# class Student:
#     def __init__(self, name, age, grade):
#         self.name = name
#         self.age = age
#         self.grades = [] 

#     def add_grade (self, grade):
#         self.grades.append(grade)
    
#     def average (self):
#         return sum(self.grades) / len(self.grades) if self.grades else 0
    
#     def ispassing (self):
#         avg =  self.average()
#         return avg >= 50
    
#     def displayinfo(self):
#         print(f"student name: {self.name}")
#         print(f"student age: {self.age}")
#         print(f"student grade: {self.grades}")
#         print("Pass" if self.ispassing() else "fail")

# Ramesh = Student("Ramesh", 18, 6)

# Ramesh.add_grade(40)
# Ramesh.add_grade(40)
# Ramesh.add_grade(90)
# Ramesh.add_grade(90)
# Ramesh.add_grade(40)
# Ramesh.displayinfo()

# practice practice practice
from datetime import datetime
class Cars:
    def __init__(self, name, milage, deriven, year):
        self.name = name
        self.milage = milage
        self.driven = deriven
        self.year = year


    def drive(self, km):
        self.driven += km

      

    
    def car_age(self):
        current = datetime.now().year
        return current - self.year
        
    
    def information(self):
        print(f"Car Name: {self.name}")
        print(f"Car Manufactured: {self.year}")
        print(f"Car Milage: {self.milage}")
        print(f"Car Age: {self.car_age()} years old")
        print(f"Car Driven: {self.driven} ")

Rolls = Cars("rolls royals", "50 KMPL", 5030, 2015)

Rolls.drive(500)
Rolls.car_age()
Rolls.information()
