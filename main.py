#
# age = input("Enter age: ")
# convert_age_to_int = int(age)
#
#
#
#
# def arithmetic():
#    passwords = []
#    password = input("Password: ")
#    password2 = input("Password: ")
#    passwords.append(password)
#    passwords.append(password2)
#    if convert_age_to_int >= 18:
#        print("Proceed to log in")
#    else:
#        print("Sorry, you are too young")
#
#    print(passwords)
#
# arithmetic()

# Program which takes 2 age using input function variables, and evaluate the age is above 18 and looks for average of their ages


# def average_age():
#     age1 = input("Enter age: ")
#     age2 = input("Enter age: ")
#     age3 = input("Enter age: ")
#     convert_age1 = int(age1)
#     convert_age2 = int(age2)
#     convert_age3 = int(age3)
#     if convert_age1 >= 18 and convert_age2 >= 18 and convert_age3 >= 18:
#         average = convert_age1 + convert_age2/3
#         print(average)
#     else:
#         print("Sorry, one or all the users are too young")
#
#
# average_age()


# # LOOPS
# for x in range(1,31):
#     z = x % 2
#     if z < 1:
#         print(x)

# name = input("Enter name: ")
# capitalized_name = name.capitalize()
# print(name)
# print(capitalized_name)

class Students:
    def __init__(bbb, firstname, lastname, registration, course, birth):
        bbb.fname = firstname
        bbb.lname = lastname
        bbb.regno = registration
        bbb.course = course
        bbb.yearBirth = birth

    def insert(bbb):
        bbb.fname = input("Enter your first name: ")
        bbb.lname = input("Enter your last name: ")
        bbb.regno = input("Enter your registration number: ")
        bbb.course = input("Enter the course you do: ")
        bbb.yearBirth = input("Enter your birth year: ")

    def confirmation(self):
        studentdetails = dict()
        print("........Confirmation........\n")
        print("Your name is " + self.fname + " " + self.lname + "\n")
        print("Your registration number is " + self.regno + "\n")
        print("Your course is " + self.course + "\n")
        print("Your birth year is " + self.yearBirth + "\n")
        confirmation = input("Press Y/y if the above is true and N/n if false: ")
        if confirmation == "y" or confirmation == "Y":
            studentdetails.update({"first name" : f"{self.fname}", "last name": f"{self.lname}",
                                   "Registration number": f"{self.regno}", "course" : f"{self.course}",
                                   "year of birth": f"{self.yearBirth}"})
            print("Your details have been saved")
            print(studentdetails)
        else:
            self.insert(Students)



s1 = Students
s1.insert(s1)
s1.confirmation(s1)

# lists
# accessing list items
# if "apple" in myList:
#     print("Yes apple is in the list")
# else:
#     print("No apple is not in the list, do you want to add? Yes or No")
#     user_decision = input("Enter y for yes or n for no: ")
#     if user_decision == "y" or user_decision == "Y":
#         myList.insert(1,"apple")
#         print("Apple has been added")
#         print(myList)
#     else:
#         print("Apple was not added")

# connecting two lists
# looping though a list
# x = 0
# while x < len(myList):
#     print(myList[x])
#     x += 1
# [print(x) for x in myList]

# list2 = [1,2,3,4,5]
# for x in list2:
#     myList.append(x)
# print(myList)

#
# dictionary = {
#     "child1": {
#         "name": "Bruno",
#         "age": 3,
#         "school": False
#     },
#     "child2": {
#         "name": "Jason",
#         "age": "15",
#         "school": True
#     }
# }
# dictionary.clear()
# print(dictionary)

# x = dict(dictionary)
# print(x)

# dict2 = dict(name="John Reese", occupation="Unknown")
# print(dict2)
#
# myList = ["apple", "banana", "mango", "passion", "pineapple", "monkey"]
# # for x in myList:
# #     if x == "pineapple":
# #         break
# #     print(x)
# x = 0
# while x < len(myList):
#     print(myList[x])
#     x += 1

# divisor = int(input("Enter number you want to test divisor: "))
#
# # for x in range(1,101):
# #     if x % divisor == 0:
# #         print(x)
# x = 1
# while x <= 100:
#     x += 1
#     if x % divisor == 0:
#         print(x)

