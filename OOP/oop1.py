# # # # # learning my first OOP Program.


# # # # class person:
# # # #     def __init__(self, name, age):
# # # #         self.name = name
# # # #         self.age = age

# # # #     def greet(self):
# # # #         print(f"hi {name} yo whats up")


# # # # person1 = person("ravi", 34)


# # # class cars:
# # #     def __init__(self, name, price):
# # #         self.name = name
# # #         self.price = price


# # # car1 = cars("sujuki", 40000)

# # # print(car1.name)
# # # print(type(car1))


# # class sounds:
# #     def __init__(self, names, sound):
# #         self.names = names
# #         self.sound = sound

# #     def iwillprint(self):
# #         print(f"{self.names} : {self.sound}")


# # animals = sounds("monkey", "chauchau")


# # print(animals.sound)
# # print(animals.iwillprint())


# # {Requirements:
# # The class should be called Student.

# # When creating a student, you should pass:

# # Their name

# # Their grade

# # Their school name }#


# class student:
#     def __init__(self, name, grade, school_name):
#         self.name = name
#         self.grade = grade
#         self.school_name = school_name

#     def introduce(self):
#         print(
#             f"Hi my name is {self.name} & i study at grade {self.grade}. i am a student at {self.school_name}")

#     def change_grade(self, grade):
#         self.grade = grade


# abishek = student("abishek", 8, "deneb")

# abishek.introduce()


# abishek.change_grade(9)

# abishek.introduce()


# class school:
#     def __init__(self, name):
#         self.name = name
#         self.students = []

#     def add_student(self, student):
#         self.students.append(student)

#     def list_student(self):
#         for student in self.students:
#             student.introduce()


# deneb_school = school("Deneb Academy")
# student = ("baihav")

# deneb_school.add_student("ramu")
# deneb_school.list_student()
