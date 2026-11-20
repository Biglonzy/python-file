# world = "I am ramon"
# print(world)

# myNameIs = True
# print(myNameIs)

# num = 43
# print(num)

# nume = (4.8)
# print(nume)f

#number =[1,2,3,4,5,6,7,8,9]
# print(Number[0])
# print(Number[1])

# Number.pop()
#number.append(10)
 
# Class = "Mr Ramon"
# print(Class.upper())


# Class = "Mr Ramon"
# print(Class.lower())

# print("----- Strip Method -----")
# course3 = "  Mr Ramon is my python instructor  "
# print(course3)
# print(course3.strip())

# print("----- Replace ------")
# print(course3.replace("python", "c++"))

# print("----- Join ------")
# print(course3.join(["First", "Second"]))

# course4 = "ramon"
# print(course4.join(["Mr","ramon"]))

# print("------- slicing method ---------")
# course4 = "Mr Ramon is my python and javascript instructor"
# print(course4[26])
# print(course4[-5])
# print(len(course4))
# name = "python"
# print(name)

# word = "programming"
# print(word[0])

# print("python"[-1])

# print("programming"[3:7])

# print("Hello World"[::-1])

# print("ABCDEFGH"[::2])

# print("hello".upper())

# print("PYTHON".lower())

# print(" Ada Lovelace ".strip())

# print("Ada Lovelace".replace("Ada","Grace"))


# print("apple,banana,cherry".split(","))

# name = "Alice"
# age = 25 
# print(f"My name is{name} and i am {age} years old.")


# number = 21.3358
# print(f"{number:1f}")

# print("Hello\nWorld")

# print("Name:\tAda")

# print("Hello")

# # print("\\")

# name = "Ramon"
# course = "python class"
# name = input("what is your name? ")
# course = input("what course are you learning?")
# print("Hello" + " " + name + " " + "you are learning" + " " + course)



 
 

#day = 7

#match day:
#  case 1:
#     print("Sunday")
#   case 2:
#     print("Monday")
#   case 3:
#     print("Tuesday")
#   case 4:
#     print("Wednesday")
#   case 5:
#     print("Thursday")
#   case 6:
#     print("Friday")
#   case 7:
#     print("Satuday")
#   case _:
#     print("Invalid day")

# #user_rule = "Admin"
#match user_rule:
  #case "Admin":
   # print("welcome Administrator")
  #case "Student":
    #print("welcome Administrator")
  #case "Teacher":
   # print("welcome Administrator")
  #case _:
    #print("Unknown user")

#day = "Sunday"
#match day:
 # case "Saturday" | "Sunday":
  #  print("It is the weekend")
  
  #case "Monday" | "Tusday" | "Wednesday"| "Thursday" | "Friday":
   
   # print("It is a working day")

  #case _: 
   # print("invalid day")
    # 1. Variable assignment
#age = 20
#status = "Adult" if age >= 18 else "Minor"
#print(status)  # Output: Adult

# 2. Direct use inside a function call
#number = 7
#print("Even" if number % 2 == 0 else "Odd")  # Output: Odd


# first_name = input("Enter first name: ")
# last_name = input("Enter last name: ")
# age = input("Enter age: ")
# gender = input("Enter gender: ")

# with open("students.txt", "w") as file:
#     file.write("First Name: " + first_name + "\n")
#     file.write("Last Name: " + last_name + "\n")
#     file.write("Age: " + age + "\n")
#     file.write("Gender: " + gender + "\n")

# print("a file handling in python is process creating,opening,reading,writing,appending to,and closing file using python.")
# print("Q2"),("Writing  mode w replaces the files existing content. If the file doesnt exist, Python creates it. Appending with mode a adds content to the end of the file while preserving its existing content.")

 
# print("- r — opens a file for reading.") 
# print("- w — opens a file for writing, replacing existing content or creating a new file.")
# print("- a — opens a file for appending, adding content to the end or creating the file if it doesnt exist.")
# print("- x — creates a new file and raises an error if the file already exists.")
# print("The `open()` function opens a file and returns a file object that Python can use to read or write the file.") 
# print("The `write()` method writes text to a file. The `close()` method closes the file, helping ensure changes are saved and resources are released.")
# print("Opening  existing file in w mode deletes its previous content before new content is written.")







# with open("student.txt", "w") as file:
#     file.write("Name: Alex Smith\n")
#     file.write("Age: 20\n")
#     file.write("Course: Computer Science\n")



# python
# with open("school.txt", "w") as file:
#     file.write("Welcome to Python Programming Class.")


# python
# with open("student.txt", "a") as file:
#     file.write("Department: Computing\n")
#     file.write("Level: 200\n")



# python
# name = input("Enter your name: ")
# age = input("Enter your age: ")
# address = input("Enter your home address: ")

# with open("details.txt", "w") as file:
#     file.write(f"Name: {name}\n")
#     file.write(f"Age: {age}\n")
#     file.write(f"Home address: {address}\n")




# python
# with open("my_biography.txt", "w") as file:
#     file.write("My name is Alex Smith.\n")
#     file.write("I am a student.\n")
#     file.write("I enjoy learning new things.\n")
#     file.write("My favourite subject is computer science.\n")
#     file.write("I hope to become a skilled programmer.\n")




# python
# subject = input("Enter your favourite subject: ")
# food = input("Enter your favourite food: ")

# with open("personal.txt", "a") as file:
#     file.write(f"Favourite subject: {subject}\n")
#     file.write(f"Favourite food: {food}\n")


# def greet_student(name, age):
#     return(f"Hello student.{name},you are {age} years old.")

#     print(greet_student("victor ",20))
#     print(greet_student("john",25))
    



# def greet_student_by_name(name, age):
#     print(f"Hello student. {name}, you are {age} years old.")


# def welcome_student(name, country="Nigeria"):
#     print(f"Welcome {name} from {country}.")


# def create_profile(role, username):
#     return f"User: {username} Role: {role}"


# def add_scores(*scores):
#     return sum(scores)


# def total_for_student(name, *scores):
#     return f"{name}: {sum(scores)}"


# def greet_student_with_default_age(name, age=18):
#     print(f"Hello student. {name}, you are {age} years old.")


# def product_description(name, price):
#     return f"Product: {name}, Price: {price}"


# def highest_score(*scores):
#     if not scores:
#         raise ValueError("Provide at least one score.")
#     return max(scores)


# def report_student_scores(name, country, *scores):
#     print(f"{name} from {country} scored a total of {sum(scores)}")


# if __name__ == "__main__":
#     # 1
#     greet_student()

#     # 2
#     greet_student_by_name("Victor", 20)

#     # 3: defaults to Nigeria; pass country="Ghana" to use Ghana.
#     welcome_student("Victor")
#     welcome_student("Victor", "Ghana")

#     # 4: role is the first positional argument, username is second.
#     print(create_profile("Instructor", "Victor"))

#     # 5
#     print(add_scores(10, 20))
#     print(add_scores(10, 20, 30, 40, 50))
#     print(add_scores(10, 20, 30, 40, 50, 60, 70, 80, 90, 100))

#     # 6
#     print(total_for_student("Victor", 10, 20, 30))

#     # 7
#     greet_student_with_default_age("Victor")
#     greet_student_with_default_age("Victor", 20)

#     # 8: keyword arguments are supplied in reverse order.
#     print(product_description(price=5000, name="Book"))

#     # 9
#     print(highest_score(10, 20, 30, 25))

#     # 10
#     report_student_scores("Victor", "Nigeria", 40, 30, 30)



# def greet_student():
#     print("Hello student.")

# greet_student()  



# def greet_with_details(name, age):
#     print(f"Hello student. {name}, you are {age} years old.")

# greet_with_details("Victor", 20)



# def welcome_student(name, country="Nigeria"):
#     print(f"Welcome {name} from {country}!")

# welcome_student("Victor")            
# welcome_student("Victor", "Ghana")   



# def create_profile(username, role):
#     return f"User: {username} Role: {role}"


# print(create_profile(role="Instructor", username="Victor"))




# def add_scores(*scores):
#     return sum(scores)

# print(add_scores(10, 20))                          
# print(add_scores(10, 20, 30, 40, 50))              
# print(add_scores(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))   


# def total_for_student(name, *scores):
#     total = sum(scores)
#     return f"{name}'s total score is {total}"

# print(total_for_student("Victor", 10, 20, 30))




# def student_info(name, age=18):
#     print(f"Student: {name}, Age: {age}")

# student_info("Victor")       
# student_info("Victor", 20)   



# def product_info(name, price):
#     return f"Product: {name}, Price: {price}"

# print(product_info(price=5000, name="Book"))



# def highest_score(*scores):
#     return max(scores)

# print(highest_score(45, 78, 92, 60))   # 92


# # 10. Name, country, and any number of scores
# def student_summary(name, country, *scores):
#     print(f"{name} from {country} scored a total of {sum(scores)}")

# student_summary("Victor", "Nigeria", 40, 30, 30)
# # Victor from Nigeria scored a total of 100

# car= {
#     "brand": "Toyota", 
#     "year": 2027
#     }    

# print(car["year"])

# user = {
#     "name":"zainab"
# }

# print(user.get("name"))

# book = {
#     "title": "Clean code",
#     "author": "Robort c meartin"
# }
# book["page"] = 484
# print(book) 

    
# price = {
#     "apple": 200,
#     "banana": 150
# }
# print("apple" in price)
# print("mango" in price)

# person = {
#     "name": "david",
#     "city": "abuja"

# }
# print(list(person.keys()))
# print(list(person.values()))
# wallet = {
#     "balance": 5000
# }

# wallet["balance"] =  7500
# print(wallet["balance"])
# 1. Student dictionary
student = {"name": "Chidi", "age": 20, "track": "Python"}
print(student)



car = {"brand": "Toyota", "year": 2022}
print(car["brand"])




user = {"name": "Zainab"}
print(user.get("email", "No email provided"))




book = {"title": "Clean Code", "author": "Robert C. Martin"}
book["pages"] = 464
print(book)




wallet = {"balance": 5000}
wallet["balance"] = 7500
print(wallet["balance"])


settings = {"theme": "dark", "notifications": True}
settings.pop("notifications")
print(settings)




prices = {"apple": 200, "banana": 150}
print("apple" in prices)
print("mango" in prices)




person = {"name": "David", "city": "Abuja"}
print(list(person.keys()))
print(list(person.values()))






students = [
    {"name": "Amina", "score": 88},
    {"name": "Tunde", "score": 92}
]
print(students[1]["name"])




phone = {"brand": "Samsung", "model": "Galaxy S23", "price": 650000}

phone["color"] = "black"        
phone["price"] = 600000         
print(list(phone.keys()))