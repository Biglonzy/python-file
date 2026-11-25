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
# student = {"name": "Chidi", "age": 20, "track": "Python"}
# print(student)



# car = {"brand": "Toyota", "year": 2022}
# print(car["brand"])




# user = {"name": "Zainab"}
# print(user.get("email", "No email provided"))




# book = {"title": "Clean Code", "author": "Robert C. Martin"}
# book["pages"] = 464
# print(book)




# wallet = {"balance": 5000}
# wallet["balance"] = 7500
# print(wallet["balance"])


# settings = {"theme": "dark", "notifications": True}
# settings.pop("notifications")
# print(settings)




# prices = {"apple": 200, "banana": 150}
# print("apple" in prices)
# print("mango" in prices)




# person = {"name": "David", "city": "Abuja"}
# print(list(person.keys()))
# print(list(person.values()))






# students = [
#     {"name": "Amina", "score": 88},
#     {"name": "Tunde", "score": 92}
# ]
# print(students[1]["name"])




# phone = {"brand": "Samsung", "model": "Galaxy S23", "price": 650000}

# phone["color"] = "black"        
# phone["price"] = 600000         
# print(list(phone.keys()))

# remove method
# fruit = {"Apple","Mango","Orange"}
# print(fruit)

# fruit.remove("Mango")

# print(fruit)

# discard method
# fruit = {"Apple","Mango","Orange"}
# fruit.discard("Pineapple")
# print(fruit)

# uinon method
# math_students = {"john", "victor", "mary", "david"}

# english_students = {"mary", "david", "peter", "james"}

# result = math_students.union(english_students)

# print(result)

# result = math_students.intersection(english_students)

# print(result)

# result = math_students.difference(english_students)
# print(result)

# result = math_students.symmetric_difference(english_students)
# print(result)

# TUPLE
# student = ("Victor", 25, "python", "Nigeria")
# print(student)


# students = ("john", "mary", "victor", "david")

# print(students[0])
# print(students[1])
# print(students[2])
# print(students[3])

# #negative indexing
# print(students[-1])
# print(students[-2])
# print(students[-3])
# print(students[-4])

# number = (10,20,30,40,50,60)

# print(number[1:4])
# print(number[:3])
# print(number[2:])

# fruits = ("Apple", "Mango", "Orange")
# print(fruits)

# temporary = list(fruits)
# print(temporary)

# temporary[1] = "Banana"

# fruits = tuple(temporary)

# print(frui 



name = "ramon"
age = 21
height = "6ft"
status = "student"

print(name)
print(age)
print(height)
print(status)


z, y = 3, 10
m, o = 5.3, 1.1
print("Addition:", z+y, m+o)
print("subrtract:", z-y, m-o)
print("multiplication:", z*y, m*o)
print("division:", z/y, m/o)


Name = input("Enter your name:")
Age = int(input("Enter your age:"))
Colour = input("Enter your favourite colour:")

print(f"My name is {Name}, I am {Age} years old and my faveourite coloue is {Colour}")


num = 10
num2 = 20.29
name = "Max"
Value = True

print("Q4",num, type(num), num2, type(num2), (name, type(name), (Value, type(Value))))

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Q5","Sum:", a + b)
print("Q5","Product:", a * b)
print("Q5","Difference:", a - b)

name = "Chidi"
s1, s2, s3, s4, s5 = 70, 65, 80, 55, 90
status = "Passed"
total = s1 + s2 + s3 + s4 + s5
average = total / 5
print("Q6","Name:", name)
print("Q6","Scores:", s1, s2, s3, s4, s5)
print("Q6","Status:", status)
print("Q6","Total:", total)
print("Q6","Average:", average)

fruits = ["apple", "banana", "mango", "orange", "pear", "grape", "pineapple", "guava", "lemon", "papaya"]
print("Q7","First:", fruits[0])
print("Q7","Last:", fruits[-1])
print("Q7","Total items:", len(fruits))

students = ["Ade", "Bola", "Chidi", "Dayo", "Emeka"]
students.append(input("Enter another student's name: "))
print("Q8","Updated list:", students)

Number =[1,2,3,4,5,6,7,8,9,10]
print("Q9","Even numbers:", [n for n in Number if n % 2 == 0])

nums = [15, 8, 25, 40, 12, 30, 5, 18]
largest = nums[0]
smallest = nums[0]
total = 0
for n in nums:
  if n > largest:
        largest = n
  if n < smallest:
       smallest = n
total += n
print("Q10","Largest:", largest)
print("Q10","Smallest:", smallest)
print("Q10","Sum:", total)

shopping = ["bread", "milk", "eggs", "rice", "sugar"]
for _ in range(2):
shopping.append(input("Add a product: "))
item = input("Enter a product to remove: ")
if item in shopping:
  shopping.remove(item)
else:
print("Product not found.")
print("Q11","Final shopping list:", shopping)


numbers = [5, 12, 18, 23, 7, 30, 41, 9, 15, 2]
n = int(input("Enter a number: "))
if n in numbers:
print(f"{n} exists at position (index) {numbers.index(n)}")
else:
print("Q12", f"{n} is not in the list.")

student = {"name": "Ada", "age": 20, "gender": "Female","department": "Computer Science", "matric_no": "CSC/2024/001"}
for key, value in student.items():
print("Q13", f"{key}: {value}")

products = {"Bread": 800, "Milk": 1200, "Rice": 5000, "Eggs": 2500, "Sugar": 1500}
for name, price in products.items():
print("Q14", f"{name}: {price}")

student = {"name": "Ada", "age": 20, "score": 65}
student["score"] = int(input("Enter the new score: "))
print("Q15", "Updated information:", student)

scores = {"Ade": 67, "Bola": 82, "Chidi": 75, "Dayo": 90, "Emeka": 58}
top_name, top_score = None, -1
for name, score in scores.items():
if score > top_score:
top_name, top_score = name, score
print("Q16", f"Highest score: {top_name} with {top_score}")

account = {"account_name": "Ada Obi", "account_number": "1234567890", "balance": 10000.0}
choice = input("Type 'deposit' or 'withdraw': ").strip().lower()
amount = float(input("Enter amount: "))
if choice == "deposit":
account["balance"] += amount
elif choice == "withdraw":
if amount <= account["balance"]:
account["balance"] -= amount
else:
    print("Insufficient funds.")
else:
    print("Invalid choice.")
print("Q17","Current balance:", account["balance"])

numbers = {10, 20, 30, 10, 40, 20, 50, 30}
print("Q18",numbers)

class_a = {"Ade", "Bola", "Chidi", "Dayo"}
class_b = {"Chidi", "Emeka", "Dayo", "Funke"}
print("Q19","Students in both classes:", class_a & class_b)

a = set(range(1, 11))
b = set(range(5, 16))
print("Q20","All elements:", a | b)
print("Q20","Common elements:", a & b)
print("Q20", "In first but not second:", a - b)

days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
print("Q21","First day:", days[0])
print("Q21","Last day:", days[-1])
print("Q21","Number of days:", len(days))
print("Q21","Saturday exists:", "Saturday" in days)

students = ("Ade", "Bola", "Chidi", "Dayo", "Emeka")
lst = list(students)
lst.append("Funke")
lst.append("Gozie")
lst.remove("Bola")
students = tuple(lst)
print("Q22",students)


with open("students.txt", "w") as f:
   f.write("Name: Ada\nAge: 20\nDepartment: Computer Science\n")
print("Q23","students.txt created.")


names = ["Ade", "Bola", "Chidi", "Dayo", "Emeka"]
with open("students.txt", "w") as f:  # "w" replaces previous content
for n in names:
     f.write(n + "\n")
print("Q24","students.txt overwritten with five names.")


with open("students.txt", "a") as f:  # "a" keeps previous content
for n in ["Funke", "Gozie", "Hauwa"]:
     f.write(n + "\n")
print("Q25","Three names appended.")


try:
with open("students.txt", "r") as f:
   print(f.read())
except FileNotFoundError:
print("Q26","students.txt not found. Run q23 first.")


sentences = ["Today was a good day.", "I learned about Python files.", "I wrote some code.", "I fixed a few bugs.", "Tomorrow I will practise more."]
with open("diary.txt", "w") as f:
for s in sentences:
f.write(s + "\n")
with open("diary.txt", "r") as f:
print("Q27:", f.read())

name = input("Enter your name: ")
language = input("Enter your favourite programming language: ")
with open("profile.txt", "a") as f:
f.write(f"{name} - {language}\n")
print("Q28","Saved to profile.txt.")


if not os.path.exists("numbers.txt"):  # create sample data if missing
with open("numbers.txt", "w") as f:
f.write("10\n20\n30\n40\n")
total = 0
with open("numbers.txt", "r") as f:
for line in f:
line = line.strip()
if line:
total += float(line)
print("Q29","Sum of numbers:", total)

    while True:
        print("\n1. Add student record\n2. View all records\n3. Count records\n4. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            name = input("Name: ")
            age = input("Age: ")
            score = input("Exam score: ")
            with open("records.txt", "a") as f:
                f.write(f"{name},{age},{score}\n")
            print("Record saved.")
        elif choice == "2":
            if os.path.exists("records.txt"):
                with open("records.txt", "r") as f:
                    for line in f:
                        name, age, score = line.strip().split(",")
                        print(f"Name: {name} | Age: {age} | Score: {score}")
            else:
                print("No records yet.")
        elif choice == "3":
            count = 0
            if os.path.exists("records.txt"):
                with open("records.txt", "r") as f:
                    count = sum(1 for line in f if line.strip())
            print("Total records:", count)
        elif choice == "4":
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    choice = input("Enter question number (1-30) or 'all': ").strip().lower()
    if choice == "all":
        for i in range(1, 31):
            print(f"\n--- Question {i} ---")
            globals()[f"q{i}"]()
    elif choice.isdigit() and 1 <= int(choice) <= 30:
        globals()[f"q{choice}"]()
    else:
        print("Invalid choice.")Name = "Moses"
Age = 19
Height = "6ft"
Status = "Student"

print("Q1",Name)
print("Q1",Age)
print("Q1",Height)
print("Q1",Status)

a, b = 10, 3
x, y = 4.5, 1.5
print("Q2","Addition:", a + b, x + y)
print("Q2","Subtraction:", a - b, x - y)
print("Q2","Multiplication:", a * b, x * y)
print("Q2","Division:", a / b, x / y)

Name = input("Enter your name: ")
Age = int(input("Enter your age: "))
colour = input("Enter your favourite colour: ")

print("Q3",f"My name is {Name}, I am {Age} years old and my favourite colour is {colour}.")

num = 10
num2 = 20.29
name = "Ada"
Value = True

print("Q4",num, type(num), num2, type(num2), (name, type(name), (Value, type(Value))))

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Q5","Sum:", a + b)
print("Q5","Product:", a * b)
print("Q5","Difference:", a - b)

name = "Chidi"
s1, s2, s3, s4, s5 = 70, 65, 80, 55, 90
status = "Passed"
total = s1 + s2 + s3 + s4 + s5
average = total / 5
print("Q6","Name:", name)
print("Q6","Scores:", s1, s2, s3, s4, s5)
print("Q6","Status:", status)
print("Q6","Total:", total)
print("Q6","Average:", average)

fruits = ["apple", "banana", "mango", "orange", "pear", "grape", "pineapple", "guava", "lemon", "papaya"]
print("Q7","First:", fruits[0])
print("Q7","Last:", fruits[-1])
print("Q7","Total items:", len(fruits))

students = ["Ade", "Bola", "Chidi", "Dayo", "Emeka"]
students.append(input("Enter another student's name: "))
print("Q8","Updated list:", students)

Number =[1,2,3,4,5,6,7,8,9,10]
print("Q9","Even numbers:", [n for n in Number if n % 2 == 0])

nums = [15, 8, 25, 40, 12, 30, 5, 18]
largest = nums[0]
smallest = nums[0]
total = 0
for n in nums:
  if n > largest:
        largest = n
  if n < smallest:
       smallest = n
total += n
print("Q10","Largest:", largest)
print("Q10","Smallest:", smallest)
print("Q10","Sum:", total)

shopping = ["bread", "milk", "eggs", "rice", "sugar"]
for _ in range(2):
shopping.append(input("Add a product: "))
item = input("Enter a product to remove: ")
if item in shopping:
  shopping.remove(item)
else:
print("Product not found.")
print("Q11","Final shopping list:", shopping)


numbers = [5, 12, 18, 23, 7, 30, 41, 9, 15, 2]
n = int(input("Enter a number: "))
if n in numbers:
print(f"{n} exists at position (index) {numbers.index(n)}")
else:
print("Q12", f"{n} is not in the list.")

student = {"name": "Ada", "age": 20, "gender": "Female","department": "Computer Science", "matric_no": "CSC/2024/001"}
for key, value in student.items():
print("Q13", f"{key}: {value}")

products = {"Bread": 800, "Milk": 1200, "Rice": 5000, "Eggs": 2500, "Sugar": 1500}
for name, price in products.items():
print("Q14", f"{name}: {price}")

student = {"name": "Ada", "age": 20, "score": 65}
student["score"] = int(input("Enter the new score: "))
print("Q15", "Updated information:", student)

scores = {"Ade": 67, "Bola": 82, "Chidi": 75, "Dayo": 90, "Emeka": 58}
top_name, top_score = None, -1
for name, score in scores.items():
if score > top_score:
top_name, top_score = name, score
print("Q16", f"Highest score: {top_name} with {top_score}")

account = {"account_name": "Ada Obi", "account_number": "1234567890", "balance": 10000.0}
choice = input("Type 'deposit' or 'withdraw': ").strip().lower()
amount = float(input("Enter amount: "))
if choice == "deposit":
account["balance"] += amount
elif choice == "withdraw":
if amount <= account["balance"]:
account["balance"] -= amount
else:
    print("Insufficient funds.")
else:
    print("Invalid choice.")
print("Q17","Current balance:", account["balance"])

numbers = {10, 20, 30, 10, 40, 20, 50, 30}
print("Q18",numbers)

class_a = {"Ade", "Bola", "Chidi", "Dayo"}
class_b = {"Chidi", "Emeka", "Dayo", "Funke"}
print("Q19","Students in both classes:", class_a & class_b)

a = set(range(1, 11))
b = set(range(5, 16))
print("Q20","All elements:", a | b)
print("Q20","Common elements:", a & b)
print("Q20", "In first but not second:", a - b)

days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
print("Q21","First day:", days[0])
print("Q21","Last day:", days[-1])
print("Q21","Number of days:", len(days))
print("Q21","Saturday exists:", "Saturday" in days)

students = ("Ade", "Bola", "Chidi", "Dayo", "Emeka")
lst = list(students)
lst.append("Funke")
lst.append("Gozie")
lst.remove("Bola")
students = tuple(lst)
print("Q22",students)


with open("students.txt", "w") as f:
   f.write("Name: Ada\nAge: 20\nDepartment: Computer Science\n")
print("Q23","students.txt created.")


names = ["Ade", "Bola", "Chidi", "Dayo", "Emeka"]
with open("students.txt", "w") as f:  # "w" replaces previous content
for n in names:
     f.write(n + "\n")
print("Q24","students.txt overwritten with five names.")


with open("students.txt", "a") as f:  # "a" keeps previous content
for n in ["Funke", "Gozie", "Hauwa"]:
     f.write(n + "\n")
print("Q25","Three names appended.")


try:
with open("students.txt", "r") as f:
   print(f.read())
except FileNotFoundError:
print("Q26","students.txt not found. Run q23 first.")


sentences = ["Today was a good day.", "I learned about Python files.", "I wrote some code.", "I fixed a few bugs.", "Tomorrow I will practise more."]
with open("diary.txt", "w") as f:
for s in sentences:
f.write(s + "\n")
with open("diary.txt", "r") as f:
print("Q27:", f.read())

name = input("Enter your name: ")
language = input("Enter your favourite programming language: ")
with open("profile.txt", "a") as f:
f.write(f"{name} - {language}\n")
print("Q28","Saved to profile.txt.")


if not os.path.exists("numbers.txt"):  # create sample data if missing
with open("numbers.txt", "w") as f:
f.write("10\n20\n30\n40\n")
total = 0
with open("numbers.txt", "r") as f:
for line in f:
line = line.strip()
if line:
total += float(line)
print("Q29","Sum of numbers:", total)

    while True:
        print("\n1. Add student record\n2. View all records\n3. Count records\n4. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            name = input("Name: ")
            age = input("Age: ")
            score = input("Exam score: ")
            with open("records.txt", "a") as f:
                f.write(f"{name},{age},{score}\n")
            print("Record saved.")
        elif choice == "2":
            if os.path.exists("records.txt"):
                with open("records.txt", "r") as f:
                    for line in f:
                        name, age, score = line.strip().split(",")
                        print(f"Name: {name} | Age: {age} | Score: {score}")
            else:
                print("No records yet.")
        elif choice == "3":
            count = 0
            if os.path.exists("records.txt"):
                with open("records.txt", "r") as f:
                    count = sum(1 for line in f if line.strip())
            print("Total records:", count)
        elif choice == "4":
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    choice = input("Enter question number (1-30) or 'all': ").strip().lower()
    if choice == "all":
        for i in range(1, 31):
            print(f"\n--- Question {i} ---")
            globals()[f"q{i}"]()
    elif choice.isdigit() and 1 <= int(choice) <= 30:
        globals()[f"q{choice}"]()
    else:
        print("Invalid choice.")Name = "Moses"
Age = 19
Height = "6ft"
Status = "Student"

print("Q1",Name)
print("Q1",Age)
print("Q1",Height)
print("Q1",Status)

a, b = 10, 3
x, y = 4.5, 1.5
print("Q2","Addition:", a + b, x + y)
print("Q2","Subtraction:", a - b, x - y)
print("Q2","Multiplication:", a * b, x * y)
print("Q2","Division:", a / b, x / y)

Name = input("Enter your name: ")
Age = int(input("Enter your age: "))
colour = input("Enter your favourite colour: ")

print("Q3",f"My name is {Name}, I am {Age} years old and my favourite colour is {colour}.")

num = 10
num2 = 20.29
name = "Ada"
Value = True

print("Q4",num, type(num), num2, type(num2), (name, type(name), (Value, type(Value))))

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Q5","Sum:", a + b)
print("Q5","Product:", a * b)
print("Q5","Difference:", a - b)

name = "Chidi"
s1, s2, s3, s4, s5 = 70, 65, 80, 55, 90
status = "Passed"
total = s1 + s2 + s3 + s4 + s5
average = total / 5
print("Q6","Name:", name)
print("Q6","Scores:", s1, s2, s3, s4, s5)
print("Q6","Status:", status)
print("Q6","Total:", total)
print("Q6","Average:", average)

fruits = ["apple", "banana", "mango", "orange", "pear", "grape", "pineapple", "guava", "lemon", "papaya"]
print("Q7","First:", fruits[0])
print("Q7","Last:", fruits[-1])
print("Q7","Total items:", len(fruits))

students = ["Ade", "Bola", "Chidi", "Dayo", "Emeka"]
students.append(input("Enter another student's name: "))
print("Q8","Updated list:", students)

Number =[1,2,3,4,5,6,7,8,9,10]
print("Q9","Even numbers:", [n for n in Number if n % 2 == 0])

nums = [15, 8, 25, 40, 12, 30, 5, 18]
largest = nums[0]
smallest = nums[0]
total = 0
for n in nums:
  if n > largest:
        largest = n
  if n < smallest:
       smallest = n
total += n
print("Q10","Largest:", largest)
print("Q10","Smallest:", smallest)
print("Q10","Sum:", total)

shopping = ["bread", "milk", "eggs", "rice", "sugar"]
for _ in range(2):
shopping.append(input("Add a product: "))
item = input("Enter a product to remove: ")
if item in shopping:
  shopping.remove(item)
else:
print("Product not found.")
print("Q11","Final shopping list:", shopping)


numbers = [5, 12, 18, 23, 7, 30, 41, 9, 15, 2]
n = int(input("Enter a number: "))
if n in numbers:
print(f"{n} exists at position (index) {numbers.index(n)}")
else:
print("Q12", f"{n} is not in the list.")

student = {"name": "Ada", "age": 20, "gender": "Female","department": "Computer Science", "matric_no": "CSC/2024/001"}
for key, value in student.items():
print("Q13", f"{key}: {value}")

products = {"Bread": 800, "Milk": 1200, "Rice": 5000, "Eggs": 2500, "Sugar": 1500}
for name, price in products.items():
print("Q14", f"{name}: {price}")

student = {"name": "Ada", "age": 20, "score": 65}
student["score"] = int(input("Enter the new score: "))
print("Q15", "Updated information:", student)

scores = {"Ade": 67, "Bola": 82, "Chidi": 75, "Dayo": 90, "Emeka": 58}
top_name, top_score = None, -1
for name, score in scores.items():
if score > top_score:
top_name, top_score = name, score
print("Q16", f"Highest score: {top_name} with {top_score}")

account = {"account_name": "Ada Obi", "account_number": "1234567890", "balance": 10000.0}
choice = input("Type 'deposit' or 'withdraw': ").strip().lower()
amount = float(input("Enter amount: "))
if choice == "deposit":
account["balance"] += amount
elif choice == "withdraw":
if amount <= account["balance"]:
account["balance"] -= amount
else:
    print("Insufficient funds.")
else:
    print("Invalid choice.")
print("Q17","Current balance:", account["balance"])

numbers = {10, 20, 30, 10, 40, 20, 50, 30}
print("Q18",numbers)

class_a = {"Ade", "Bola", "Chidi", "Dayo"}
class_b = {"Chidi", "Emeka", "Dayo", "Funke"}
print("Q19","Students in both classes:", class_a & class_b)

a = set(range(1, 11))
b = set(range(5, 16))
print("Q20","All elements:", a | b)
print("Q20","Common elements:", a & b)
print("Q20", "In first but not second:", a - b)

days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
print("Q21","First day:", days[0])
print("Q21","Last day:", days[-1])
print("Q21","Number of days:", len(days))
print("Q21","Saturday exists:", "Saturday" in days)

students = ("Ade", "Bola", "Chidi", "Dayo", "Emeka")
lst = list(students)
lst.append("Funke")
lst.append("Gozie")
lst.remove("Bola")
students = tuple(lst)
print("Q22",students)


with open("students.txt", "w") as f:
   f.write("Name: Ada\nAge: 20\nDepartment: Computer Science\n")
print("Q23","students.txt created.")


names = ["Ade", "Bola", "Chidi", "Dayo", "Emeka"]
with open("students.txt", "w") as f:  # "w" replaces previous content
for n in names:
     f.write(n + "\n")
print("Q24","students.txt overwritten with five names.")


with open("students.txt", "a") as f:  # "a" keeps previous content
for n in ["Funke", "Gozie", "Hauwa"]:
     f.write(n + "\n")
print("Q25","Three names appended.")


try:
with open("students.txt", "r") as f:
   print(f.read())
except FileNotFoundError:
print("Q26","students.txt not found. Run q23 first.")


sentences = ["Today was a good day.", "I learned about Python files.", "I wrote some code.", "I fixed a few bugs.", "Tomorrow I will practise more."]
with open("diary.txt", "w") as f:
for s in sentences:
f.write(s + "\n")
with open("diary.txt", "r") as f:
print("Q27:", f.read())

name = input("Enter your name: ")
language = input("Enter your favourite programming language: ")
with open("profile.txt", "a") as f:
f.write(f"{name} - {language}\n")
print("Q28","Saved to profile.txt.")


if not os.path.exists("numbers.txt"):  # create sample data if missing
with open("numbers.txt", "w") as f:
f.write("10\n20\n30\n40\n")
total = 0
with open("numbers.txt", "r") as f:
for line in f:
line = line.strip()
if line:
total += float(line)
print("Q29","Sum of numbers:", total)

    while True:
        print("\n1. Add student record\n2. View all records\n3. Count records\n4. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            name = input("Name: ")
            age = input("Age: ")
            score = input("Exam score: ")
            with open("records.txt", "a") as f:
                f.write(f"{name},{age},{score}\n")
            print("Record saved.")
        elif choice == "2":
            if os.path.exists("records.txt"):
                with open("records.txt", "r") as f:
                    for line in f:
                        name, age, score = line.strip().split(",")
                        print(f"Name: {name} | Age: {age} | Score: {score}")
            else:
                print("No records yet.")
        elif choice == "3":
            count = 0
            if os.path.exists("records.txt"):
                with open("records.txt", "r") as f:
                    count = sum(1 for line in f if line.strip())
            print("Total records:", count)
        elif choice == "4":
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    choice = input("Enter question number (1-30) or 'all': ").strip().lower()
    if choice == "all":
        for i in range(1, 31):
            print(f"\n--- Question {i} ---")
            globals()[f"q{i}"]()
    elif choice.isdigit() and 1 <= int(choice) <= 30:
        globals()[f"q{choice}"]()
    else:
        print("Invalid choice.")Name = "Moses"
Age = 19
Height = "6ft"
Status = "Student"

print("Q1",Name)
print("Q1",Age)
print("Q1",Height)
print("Q1",Status)

a, b = 10, 3
x, y = 4.5, 1.5
print("Q2","Addition:", a + b, x + y)
print("Q2","Subtraction:", a - b, x - y)
print("Q2","Multiplication:", a * b, x * y)
print("Q2","Division:", a / b, x / y)

Name = input("Enter your name: ")
Age = int(input("Enter your age: "))
colour = input("Enter your favourite colour: ")

print("Q3",f"My name is {Name}, I am {Age} years old and my favourite colour is {colour}.")

num = 10
num2 = 20.29
name = "Ada"
Value = True

print("Q4",num, type(num), num2, type(num2), (name, type(name), (Value, type(Value))))

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Q5","Sum:", a + b)
print("Q5","Product:", a * b)
print("Q5","Difference:", a - b)

name = "Chidi"
s1, s2, s3, s4, s5 = 70, 65, 80, 55, 90
status = "Passed"
total = s1 + s2 + s3 + s4 + s5
average = total / 5
print("Q6","Name:", name)
print("Q6","Scores:", s1, s2, s3, s4, s5)
print("Q6","Status:", status)
print("Q6","Total:", total)
print("Q6","Average:", average)

fruits = ["apple", "banana", "mango", "orange", "pear", "grape", "pineapple", "guava", "lemon", "papaya"]
print("Q7","First:", fruits[0])
print("Q7","Last:", fruits[-1])
print("Q7","Total items:", len(fruits))

students = ["Ade", "Bola", "Chidi", "Dayo", "Emeka"]
students.append(input("Enter another student's name: "))
print("Q8","Updated list:", students)

Number =[1,2,3,4,5,6,7,8,9,10]
print("Q9","Even numbers:", [n for n in Number if n % 2 == 0])

nums = [15, 8, 25, 40, 12, 30, 5, 18]
largest = nums[0]
smallest = nums[0]
total = 0
for n in nums:
  if n > largest:
        largest = n
  if n < smallest:
       smallest = n
total += n
print("Q10","Largest:", largest)
print("Q10","Smallest:", smallest)
print("Q10","Sum:", total)

shopping = ["bread", "milk", "eggs", "rice", "sugar"]
for _ in range(2):
shopping.append(input("Add a product: "))
item = input("Enter a product to remove: ")
if item in shopping:
  shopping.remove(item)
else:
print("Product not found.")
print("Q11","Final shopping list:", shopping)


numbers = [5, 12, 18, 23, 7, 30, 41, 9, 15, 2]
n = int(input("Enter a number: "))
if n in numbers:
print(f"{n} exists at position (index) {numbers.index(n)}")
else:
print("Q12", f"{n} is not in the list.")

student = {"name": "Ada", "age": 20, "gender": "Female","department": "Computer Science", "matric_no": "CSC/2024/001"}
for key, value in student.items():
print("Q13", f"{key}: {value}")

products = {"Bread": 800, "Milk": 1200, "Rice": 5000, "Eggs": 2500, "Sugar": 1500}
for name, price in products.items():
print("Q14", f"{name}: {price}")

student = {"name": "Ada", "age": 20, "score": 65}
student["score"] = int(input("Enter the new score: "))
print("Q15", "Updated information:", student)

scores = {"Ade": 67, "Bola": 82, "Chidi": 75, "Dayo": 90, "Emeka": 58}
top_name, top_score = None, -1
for name, score in scores.items():
if score > top_score:
top_name, top_score = name, score
print("Q16", f"Highest score: {top_name} with {top_score}")

account = {"account_name": "Ada Obi", "account_number": "1234567890", "balance": 10000.0}
choice = input("Type 'deposit' or 'withdraw': ").strip().lower()
amount = float(input("Enter amount: "))
if choice == "deposit":
account["balance"] += amount
elif choice == "withdraw":
if amount <= account["balance"]:
account["balance"] -= amount
else:
    print("Insufficient funds.")
else:
    print("Invalid choice.")
print("Q17","Current balance:", account["balance"])

numbers = {10, 20, 30, 10, 40, 20, 50, 30}
print("Q18",numbers)

class_a = {"Ade", "Bola", "Chidi", "Dayo"}
class_b = {"Chidi", "Emeka", "Dayo", "Funke"}
print("Q19","Students in both classes:", class_a & class_b)

a = set(range(1, 11))
b = set(range(5, 16))
print("Q20","All elements:", a | b)
print("Q20","Common elements:", a & b)
print("Q20", "In first but not second:", a - b)

days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
print("Q21","First day:", days[0])
print("Q21","Last day:", days[-1])
print("Q21","Number of days:", len(days))
print("Q21","Saturday exists:", "Saturday" in days)

students = ("Ade", "Bola", "Chidi", "Dayo", "Emeka")
lst = list(students)
lst.append("Funke")
lst.append("Gozie")
lst.remove("Bola")
students = tuple(lst)
print("Q22",students)


with open("students.txt", "w") as f:
   f.write("Name: Ada\nAge: 20\nDepartment: Computer Science\n")
print("Q23","students.txt created.")


names = ["Ade", "Bola", "Chidi", "Dayo", "Emeka"]
with open("students.txt", "w") as f:  # "w" replaces previous content
for n in names:
     f.write(n + "\n")
print("Q24","students.txt overwritten with five names.")


with open("students.txt", "a") as f:  # "a" keeps previous content
for n in ["Funke", "Gozie", "Hauwa"]:
     f.write(n + "\n")
print("Q25","Three names appended.")


try:
with open("students.txt", "r") as f:
   print(f.read())
except FileNotFoundError:
print("Q26","students.txt not found. Run q23 first.")


sentences = ["Today was a good day.", "I learned about Python files.", "I wrote some code.", "I fixed a few bugs.", "Tomorrow I will practise more."]
with open("diary.txt", "w") as f:
for s in sentences:
f.write(s + "\n")
with open("diary.txt", "r") as f:
print("Q27:", f.read())

name = input("Enter your name: ")
language = input("Enter your favourite programming language: ")
with open("profile.txt", "a") as f:
f.write(f"{name} - {language}\n")
print("Q28","Saved to profile.txt.")


if not os.path.exists("numbers.txt"):  # create sample data if missing
with open("numbers.txt", "w") as f:
f.write("10\n20\n30\n40\n")
total = 0
with open("numbers.txt", "r") as f:
for line in f:
line = line.strip()
if line:
total += float(line)
print("Q29","Sum of numbers:", total)

    while True:
        print("\n1. Add student record\n2. View all records\n3. Count records\n4. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            name = input("Name: ")
            age = input("Age: ")
            score = input("Exam score: ")
            with open("records.txt", "a") as f:
                f.write(f"{name},{age},{score}\n")
            print("Record saved.")
        elif choice == "2":
            if os.path.exists("records.txt"):
                with open("records.txt", "r") as f:
                    for line in f:
                        name, age, score = line.strip().split(",")
                        print(f"Name: {name} | Age: {age} | Score: {score}")
            else:
                print("No records yet.")
        elif choice == "3":
            count = 0
            if os.path.exists("records.txt"):
                with open("records.txt", "r") as f:
                    count = sum(1 for line in f if line.strip())
            print("Total records:", count)
        elif choice == "4":
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    choice = input("Enter question number (1-30) or 'all': ").strip().lower()
    if choice == "all":
        for i in range(1, 31):
            print(f"\n--- Question {i} ---")
            globals()[f"q{i}"]()
    elif choice.isdigit() and 1 <= int(choice) <= 30:
        globals()[f"q{choice}"]()
    else:
        print("Invalid choice.")Name = "Moses"
Age = 19
Height = "6ft"
Status = "Student"

print("Q1",Name)
print("Q1",Age)
print("Q1",Height)
print("Q1",Status)

a, b = 10, 3
x, y = 4.5, 1.5
print("Q2","Addition:", a + b, x + y)
print("Q2","Subtraction:", a - b, x - y)
print("Q2","Multiplication:", a * b, x * y)
print("Q2","Division:", a / b, x / y)

Name = input("Enter your name: ")
Age = int(input("Enter your age: "))
colour = input("Enter your favourite colour: ")

print("Q3",f"My name is {Name}, I am {Age} years old and my favourite colour is {colour}.")

num = 10
num2 = 20.29
name = "Ada"
Value = True

print("Q4",num, type(num), num2, type(num2), (name, type(name), (Value, type(Value))))

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Q5","Sum:", a + b)
print("Q5","Product:", a * b)
print("Q5","Difference:", a - b)

name = "Chidi"
s1, s2, s3, s4, s5 = 70, 65, 80, 55, 90
status = "Passed"
total = s1 + s2 + s3 + s4 + s5
average = total / 5
print("Q6","Name:", name)
print("Q6","Scores:", s1, s2, s3, s4, s5)
print("Q6","Status:", status)
print("Q6","Total:", total)
print("Q6","Average:", average)

fruits = ["apple", "banana", "mango", "orange", "pear", "grape", "pineapple", "guava", "lemon", "papaya"]
print("Q7","First:", fruits[0])
print("Q7","Last:", fruits[-1])
print("Q7","Total items:", len(fruits))

students = ["Ade", "Bola", "Chidi", "Dayo", "Emeka"]
students.append(input("Enter another student's name: "))
print("Q8","Updated list:", students)

Number =[1,2,3,4,5,6,7,8,9,10]
print("Q9","Even numbers:", [n for n in Number if n % 2 == 0])

nums = [15, 8, 25, 40, 12, 30, 5, 18]
largest = nums[0]
smallest = nums[0]
total = 0
for n in nums:
  if n > largest:
        largest = n
  if n < smallest:
       smallest = n
total += n
print("Q10","Largest:", largest)
print("Q10","Smallest:", smallest)
print("Q10","Sum:", total)

shopping = ["bread", "milk", "eggs", "rice", "sugar"]
for _ in range(2):
shopping.append(input("Add a product: "))
item = input("Enter a product to remove: ")
if item in shopping:
  shopping.remove(item)
else:
print("Product not found.")
print("Q11","Final shopping list:", shopping)


numbers = [5, 12, 18, 23, 7, 30, 41, 9, 15, 2]
n = int(input("Enter a number: "))
if n in numbers:
print(f"{n} exists at position (index) {numbers.index(n)}")
else:
print("Q12", f"{n} is not in the list.")

student = {"name": "Ada", "age": 20, "gender": "Female","department": "Computer Science", "matric_no": "CSC/2024/001"}
for key, value in student.items():
print("Q13", f"{key}: {value}")

products = {"Bread": 800, "Milk": 1200, "Rice": 5000, "Eggs": 2500, "Sugar": 1500}
for name, price in products.items():
print("Q14", f"{name}: {price}")

student = {"name": "Ada", "age": 20, "score": 65}
student["score"] = int(input("Enter the new score: "))
print("Q15", "Updated information:", student)

scores = {"Ade": 67, "Bola": 82, "Chidi": 75, "Dayo": 90, "Emeka": 58}
top_name, top_score = None, -1
for name, score in scores.items():
if score > top_score:
top_name, top_score = name, score
print("Q16", f"Highest score: {top_name} with {top_score}")

account = {"account_name": "Ada Obi", "account_number": "1234567890", "balance": 10000.0}
choice = input("Type 'deposit' or 'withdraw': ").strip().lower()
amount = float(input("Enter amount: "))
if choice == "deposit":
account["balance"] += amount
elif choice == "withdraw":
if amount <= account["balance"]:
account["balance"] -= amount
else:
    print("Insufficient funds.")
else:
    print("Invalid choice.")
print("Q17","Current balance:", account["balance"])

numbers = {10, 20, 30, 10, 40, 20, 50, 30}
print("Q18",numbers)

class_a = {"Ade", "Bola", "Chidi", "Dayo"}
class_b = {"Chidi", "Emeka", "Dayo", "Funke"}
print("Q19","Students in both classes:", class_a & class_b)

a = set(range(1, 11))
b = set(range(5, 16))
print("Q20","All elements:", a | b)
print("Q20","Common elements:", a & b)
print("Q20", "In first but not second:", a - b)

days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
print("Q21","First day:", days[0])
print("Q21","Last day:", days[-1])
print("Q21","Number of days:", len(days))
print("Q21","Saturday exists:", "Saturday" in days)

students = ("Ade", "Bola", "Chidi", "Dayo", "Emeka")
lst = list(students)
lst.append("Funke")
lst.append("Gozie")
lst.remove("Bola")
students = tuple(lst)
print("Q22",students)


with open("students.txt", "w") as f:
   f.write("Name: Ada\nAge: 20\nDepartment: Computer Science\n")
print("Q23","students.txt created.")


names = ["Ade", "Bola", "Chidi", "Dayo", "Emeka"]
with open("students.txt", "w") as f:  # "w" replaces previous content
for n in names:
     f.write(n + "\n")
print("Q24","students.txt overwritten with five names.")


with open("students.txt", "a") as f:  # "a" keeps previous content
for n in ["Funke", "Gozie", "Hauwa"]:
     f.write(n + "\n")
print("Q25","Three names appended.")


try:
with open("students.txt", "r") as f:
   print(f.read())
except FileNotFoundError:
print("Q26","students.txt not found. Run q23 first.")


sentences = ["Today was a good day.", "I learned about Python files.", "I wrote some code.", "I fixed a few bugs.", "Tomorrow I will practise more."]
with open("diary.txt", "w") as f:
for s in sentences:
f.write(s + "\n")
with open("diary.txt", "r") as f:
print("Q27:", f.read())

name = input("Enter your name: ")
language = input("Enter your favourite programming language: ")
with open("profile.txt", "a") as f:
f.write(f"{name} - {language}\n")
print("Q28","Saved to profile.txt.")


if not os.path.exists("numbers.txt"):  # create sample data if missing
with open("numbers.txt", "w") as f:
f.write("10\n20\n30\n40\n")
total = 0
with open("numbers.txt", "r") as f:
for line in f:
line = line.strip()
if line:
total += float(line)
print("Q29","Sum of numbers:", total)

    while True:
        print("\n1. Add student record\n2. View all records\n3. Count records\n4. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            name = input("Name: ")
            age = input("Age: ")
            score = input("Exam score: ")
            with open("records.txt", "a") as f:
                f.write(f"{name},{age},{score}\n")
            print("Record saved.")
        elif choice == "2":
            if os.path.exists("records.txt"):
                with open("records.txt", "r") as f:
                    for line in f:
                        name, age, score = line.strip().split(",")
                        print(f"Name: {name} | Age: {age} | Score: {score}")
            else:
                print("No records yet.")
        elif choice == "3":
            count = 0
            if os.path.exists("records.txt"):
                with open("records.txt", "r") as f:
                    count = sum(1 for line in f if line.strip())
            print("Total records:", count)
        elif choice == "4":
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    choice = input("Enter question number (1-30) or 'all': ").strip().lower()
    if choice == "all":
        for i in range(1, 31):
            print(f"\n--- Question {i} ---")
            globals()[f"q{i}"]()
    elif choice.isdigit() and 1 <= int(choice) <= 30:
        globals()[f"q{choice}"]()
    else:
        print("Invalid choice.")Name = "Moses"
Age = 19
Height = "6ft"
Status = "Student"

print("Q1",Name)
print("Q1",Age)
print("Q1",Height)
print("Q1",Status)

a, b = 10, 3
x, y = 4.5, 1.5
print("Q2","Addition:", a + b, x + y)
print("Q2","Subtraction:", a - b, x - y)
print("Q2","Multiplication:", a * b, x * y)
print("Q2","Division:", a / b, x / y)

Name = input("Enter your name: ")
Age = int(input("Enter your age: "))
colour = input("Enter your favourite colour: ")

print("Q3",f"My name is {Name}, I am {Age} years old and my favourite colour is {colour}.")

num = 10
num2 = 20.29
name = "Ada"
Value = True

print("Q4",num, type(num), num2, type(num2), (name, type(name), (Value, type(Value))))

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Q5","Sum:", a + b)
print("Q5","Product:", a * b)
print("Q5","Difference:", a - b)

name = "Chidi"
s1, s2, s3, s4, s5 = 70, 65, 80, 55, 90
status = "Passed"
total = s1 + s2 + s3 + s4 + s5
average = total / 5
print("Q6","Name:", name)
print("Q6","Scores:", s1, s2, s3, s4, s5)
print("Q6","Status:", status)
print("Q6","Total:", total)
print("Q6","Average:", average)

fruits = ["apple", "banana", "mango", "orange", "pear", "grape", "pineapple", "guava", "lemon", "papaya"]
print("Q7","First:", fruits[0])
print("Q7","Last:", fruits[-1])
print("Q7","Total items:", len(fruits))

students = ["Ade", "Bola", "Chidi", "Dayo", "Emeka"]
students.append(input("Enter another student's name: "))
print("Q8","Updated list:", students)

Number =[1,2,3,4,5,6,7,8,9,10]
print("Q9","Even numbers:", [n for n in Number if n % 2 == 0])

nums = [15, 8, 25, 40, 12, 30, 5, 18]
largest = nums[0]
smallest = nums[0]
total = 0
for n in nums:
  if n > largest:
        largest = n
  if n < smallest:
       smallest = n
total += n
print("Q10","Largest:", largest)
print("Q10","Smallest:", smallest)
print("Q10","Sum:", total)

shopping = ["bread", "milk", "eggs", "rice", "sugar"]
for _ in range(2):
shopping.append(input("Add a product: "))
item = input("Enter a product to remove: ")
if item in shopping:
  shopping.remove(item)
else:
print("Product not found.")
print("Q11","Final shopping list:", shopping)


numbers = [5, 12, 18, 23, 7, 30, 41, 9, 15, 2]
n = int(input("Enter a number: "))
if n in numbers:
print(f"{n} exists at position (index) {numbers.index(n)}")
else:
print("Q12", f"{n} is not in the list.")

student = {"name": "Ada", "age": 20, "gender": "Female","department": "Computer Science", "matric_no": "CSC/2024/001"}
for key, value in student.items():
print("Q13", f"{key}: {value}")

products = {"Bread": 800, "Milk": 1200, "Rice": 5000, "Eggs": 2500, "Sugar": 1500}
for name, price in products.items():
print("Q14", f"{name}: {price}")

student = {"name": "Ada", "age": 20, "score": 65}
student["score"] = int(input("Enter the new score: "))
print("Q15", "Updated information:", student)

scores = {"Ade": 67, "Bola": 82, "Chidi": 75, "Dayo": 90, "Emeka": 58}
top_name, top_score = None, -1
for name, score in scores.items():
if score > top_score:
top_name, top_score = name, score
print("Q16", f"Highest score: {top_name} with {top_score}")

account = {"account_name": "Ada Obi", "account_number": "1234567890", "balance": 10000.0}
choice = input("Type 'deposit' or 'withdraw': ").strip().lower()
amount = float(input("Enter amount: "))
if choice == "deposit":
account["balance"] += amount
elif choice == "withdraw":
if amount <= account["balance"]:
account["balance"] -= amount
else:
    print("Insufficient funds.")
else:
    print("Invalid choice.")
print("Q17","Current balance:", account["balance"])

numbers = {10, 20, 30, 10, 40, 20, 50, 30}
print("Q18",numbers)

class_a = {"Ade", "Bola", "Chidi", "Dayo"}
class_b = {"Chidi", "Emeka", "Dayo", "Funke"}
print("Q19","Students in both classes:", class_a & class_b)

a = set(range(1, 11))
b = set(range(5, 16))
print("Q20","All elements:", a | b)
print("Q20","Common elements:", a & b)
print("Q20", "In first but not second:", a - b)

days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
print("Q21","First day:", days[0])
print("Q21","Last day:", days[-1])
print("Q21","Number of days:", len(days))
print("Q21","Saturday exists:", "Saturday" in days)

students = ("Ade", "Bola", "Chidi", "Dayo", "Emeka")
lst = list(students)
lst.append("Funke")
lst.append("Gozie")
lst.remove("Bola")
students = tuple(lst)
print("Q22",students)


with open("students.txt", "w") as f:
   f.write("Name: Ada\nAge: 20\nDepartment: Computer Science\n")
print("Q23","students.txt created.")


names = ["Ade", "Bola", "Chidi", "Dayo", "Emeka"]
with open("students.txt", "w") as f:  # "w" replaces previous content
for n in names:
     f.write(n + "\n")
print("Q24","students.txt overwritten with five names.")


with open("students.txt", "a") as f:  # "a" keeps previous content
for n in ["Funke", "Gozie", "Hauwa"]:
     f.write(n + "\n")
print("Q25","Three names appended.")


try:
with open("students.txt", "r") as f:
   print(f.read())
except FileNotFoundError:
print("Q26","students.txt not found. Run q23 first.")


sentences = ["Today was a good day.", "I learned about Python files.", "I wrote some code.", "I fixed a few bugs.", "Tomorrow I will practise more."]
with open("diary.txt", "w") as f:
for s in sentences:
f.write(s + "\n")
with open("diary.txt", "r") as f:
print("Q27:", f.read())

name = input("Enter your name: ")
language = input("Enter your favourite programming language: ")
with open("profile.txt", "a") as f:
f.write(f"{name} - {language}\n")
print("Q28","Saved to profile.txt.")


if not os.path.exists("numbers.txt"):  # create sample data if missing
with open("numbers.txt", "w") as f:
f.write("10\n20\n30\n40\n")
total = 0
with open("numbers.txt", "r") as f:
for line in f:
line = line.strip()
if line:
total += float(line)
print("Q29","Sum of numbers:", total)

    while True:
        print("\n1. Add student record\n2. View all records\n3. Count records\n4. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            name = input("Name: ")
            age = input("Age: ")
            score = input("Exam score: ")
            with open("records.txt", "a") as f:
                f.write(f"{name},{age},{score}\n")
            print("Record saved.")
        elif choice == "2":
            if os.path.exists("records.txt"):
                with open("records.txt", "r") as f:
                    for line in f:
                        name, age, score = line.strip().split(",")
                        print(f"Name: {name} | Age: {age} | Score: {score}")
            else:
                print("No records yet.")
        elif choice == "3":
            count = 0
            if os.path.exists("records.txt"):
                with open("records.txt", "r") as f:
                    count = sum(1 for line in f if line.strip())
            print("Total records:", count)
        elif choice == "4":
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    choice = input("Enter question number (1-30) or 'all': ").strip().lower()
    if choice == "all":
        for i in range(1, 31):
            print(f"\n--- Question {i} ---")
            globals()[f"q{i}"]()
    elif choice.isdigit() and 1 <= int(choice) <= 30:
        globals()[f"q{choice}"]()
    else:
        print("Invalid choice.")vName = "Moses"
Age = 19
Height = "6ft"
Status = "Student"

print("Q1",Name)
print("Q1",Age)
print("Q1",Height)
print("Q1",Status)

a, b = 10, 3
x, y = 4.5, 1.5
print("Q2","Addition:", a + b, x + y)
print("Q2","Subtraction:", a - b, x - y)
print("Q2","Multiplication:", a * b, x * y)
print("Q2","Division:", a / b, x / y)

Name = input("Enter your name: ")
Age = int(input("Enter your age: "))
colour = input("Enter your favourite colour: ")

print("Q3",f"My name is {Name}, I am {Age} years old and my favourite colour is {colour}.")

num = 10
num2 = 20.29
name = "Ada"
Value = True

print("Q4",num, type(num), num2, type(num2), (name, type(name), (Value, type(Value))))

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Q5","Sum:", a + b)
print("Q5","Product:", a * b)
print("Q5","Difference:", a - b)

name = "Chidi"
s1, s2, s3, s4, s5 = 70, 65, 80, 55, 90
status = "Passed"
total = s1 + s2 + s3 + s4 + s5
average = total / 5
print("Q6","Name:", name)
print("Q6","Scores:", s1, s2, s3, s4, s5)
print("Q6","Status:", status)
print("Q6","Total:", total)
print("Q6","Average:", average)

fruits = ["apple", "banana", "mango", "orange", "pear", "grape", "pineapple", "guava", "lemon", "papaya"]
print("Q7","First:", fruits[0])
print("Q7","Last:", fruits[-1])
print("Q7","Total items:", len(fruits))

students = ["Ade", "Bola", "Chidi", "Dayo", "Emeka"]
students.append(input("Enter another student's name: "))
print("Q8","Updated list:", students)

Number =[1,2,3,4,5,6,7,8,9,10]
print("Q9","Even numbers:", [n for n in Number if n % 2 == 0])

nums = [15, 8, 25, 40, 12, 30, 5, 18]
largest = nums[0]
smallest = nums[0]
total = 0
for n in nums:
  if n > largest:
        largest = n
  if n < smallest:
       smallest = n
total += n
print("Q10","Largest:", largest)
print("Q10","Smallest:", smallest)
print("Q10","Sum:", total)

shopping = ["bread", "milk", "eggs", "rice", "sugar"]
for _ in range(2):
shopping.append(input("Add a product: "))
item = input("Enter a product to remove: ")
if item in shopping:
  shopping.remove(item)
else:
print("Product not found.")
print("Q11","Final shopping list:", shopping)


numbers = [5, 12, 18, 23, 7, 30, 41, 9, 15, 2]
n = int(input("Enter a number: "))
if n in numbers:
print(f"{n} exists at position (index) {numbers.index(n)}")
else:
print("Q12", f"{n} is not in the list.")

student = {"name": "Ada", "age": 20, "gender": "Female","department": "Computer Science", "matric_no": "CSC/2024/001"}
for key, value in student.items():
print("Q13", f"{key}: {value}")

products = {"Bread": 800, "Milk": 1200, "Rice": 5000, "Eggs": 2500, "Sugar": 1500}
for name, price in products.items():
print("Q14", f"{name}: {price}")

student = {"name": "Ada", "age": 20, "score": 65}
student["score"] = int(input("Enter the new score: "))
print("Q15", "Updated information:", student)

scores = {"Ade": 67, "Bola": 82, "Chidi": 75, "Dayo": 90, "Emeka": 58}
top_name, top_score = None, -1
for name, score in scores.items():
if score > top_score:
top_name, top_score = name, score
print("Q16", f"Highest score: {top_name} with {top_score}")

account = {"account_name": "Ada Obi", "account_number": "1234567890", "balance": 10000.0}
choice = input("Type 'deposit' or 'withdraw': ").strip().lower()
amount = float(input("Enter amount: "))
if choice == "deposit":
account["balance"] += amount
elif choice == "withdraw":
if amount <= account["balance"]:
account["balance"] -= amount
else:
    print("Insufficient funds.")
else:
    print("Invalid choice.")
print("Q17","Current balance:", account["balance"])

numbers = {10, 20, 30, 10, 40, 20, 50, 30}
print("Q18",numbers)

class_a = {"Ade", "Bola", "Chidi", "Dayo"}
class_b = {"Chidi", "Emeka", "Dayo", "Funke"}
print("Q19","Students in both classes:", class_a & class_b)

a = set(range(1, 11))
b = set(range(5, 16))
print("Q20","All elements:", a | b)
print("Q20","Common elements:", a & b)
print("Q20", "In first but not second:", a - b)

days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
print("Q21","First day:", days[0])
print("Q21","Last day:", days[-1])
print("Q21","Number of days:", len(days))
print("Q21","Saturday exists:", "Saturday" in days)

students = ("Ade", "Bola", "Chidi", "Dayo", "Emeka")
lst = list(students)
lst.append("Funke")
lst.append("Gozie")
lst.remove("Bola")
students = tuple(lst)
print("Q22",students)


with open("students.txt", "w") as f:
   f.write("Name: Ada\nAge: 20\nDepartment: Computer Science\n")
print("Q23","students.txt created.")


names = ["Ade", "Bola", "Chidi", "Dayo", "Emeka"]
with open("students.txt", "w") as f:  # "w" replaces previous content
for n in names:
     f.write(n + "\n")
print("Q24","students.txt overwritten with five names.")


with open("students.txt", "a") as f:  # "a" keeps previous content
for n in ["Funke", "Gozie", "Hauwa"]:
     f.write(n + "\n")
print("Q25","Three names appended.")


try:
with open("students.txt", "r") as f:
   print(f.read())
except FileNotFoundError:
print("Q26","students.txt not found. Run q23 first.")


sentences = ["Today was a good day.", "I learned about Python files.", "I wrote some code.", "I fixed a few bugs.", "Tomorrow I will practise more."]
with open("diary.txt", "w") as f:
for s in sentences:
f.write(s + "\n")
with open("diary.txt", "r") as f:
print("Q27:", f.read())

name = input("Enter your name: ")
language = input("Enter your favourite programming language: ")
with open("profile.txt", "a") as f:
f.write(f"{name} - {language}\n")
print("Q28","Saved to profile.txt.")


if not os.path.exists("numbers.txt"):  # create sample data if missing
with open("numbers.txt", "w") as f:
f.write("10\n20\n30\n40\n")
total = 0
with open("numbers.txt", "r") as f:
for line in f:
line = line.strip()
if line:
total += float(line)
print("Q29","Sum of numbers:", total)

    while True:
        print("\n1. Add student record\n2. View all records\n3. Count records\n4. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            name = input("Name: ")
            age = input("Age: ")
            score = input("Exam score: ")
            with open("records.txt", "a") as f:
                f.write(f"{name},{age},{score}\n")
            print("Record saved.")
        elif choice == "2":
            if os.path.exists("records.txt"):
                with open("records.txt", "r") as f:
                    for line in f:
                        name, age, score = line.strip().split(",")
                        print(f"Name: {name} | Age: {age} | Score: {score}")
            else:
                print("No records yet.")
        elif choice == "3":
            count = 0
            if os.path.exists("records.txt"):
                with open("records.txt", "r") as f:
                    count = sum(1 for line in f if line.strip())
            print("Total records:", count)
        elif choice == "4":
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    choice = input("Enter question number (1-30) or 'all': ").strip().lower()
    if choice == "all":
        for i in range(1, 31):
            print(f"\n--- Question {i} ---")
            globals()[f"q{i}"]()
    elif choice.isdigit() and 1 <= int(choice) <= 30:
        globals()[f"q{choice}"]()
    else:
        print("Invalid choice.")Name = "Moses"
Age = 19
Height = "6ft"
Status = "Student"

print("Q1",Name)
print("Q1",Age)
print("Q1",Height)
print("Q1",Status)

a, b = 10, 3
x, y = 4.5, 1.5
print("Q2","Addition:", a + b, x + y)
print("Q2","Subtraction:", a - b, x - y)
print("Q2","Multiplication:", a * b, x * y)
print("Q2","Division:", a / b, x / y)

Name = input("Enter your name: ")
Age = int(input("Enter your age: "))
colour = input("Enter your favourite colour: ")

print("Q3",f"My name is {Name}, I am {Age} years old and my favourite colour is {colour}.")

num = 10
num2 = 20.29
name = "Ada"
Value = True

print("Q4",num, type(num), num2, type(num2), (name, type(name), (Value, type(Value))))

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Q5","Sum:", a + b)
print("Q5","Product:", a * b)
print("Q5","Difference:", a - b)

name = "Chidi"
s1, s2, s3, s4, s5 = 70, 65, 80, 55, 90
status = "Passed"
total = s1 + s2 + s3 + s4 + s5
average = total / 5
print("Q6","Name:", name)
print("Q6","Scores:", s1, s2, s3, s4, s5)
print("Q6","Status:", status)
print("Q6","Total:", total)
print("Q6","Average:", average)

fruits = ["apple", "banana", "mango", "orange", "pear", "grape", "pineapple", "guava", "lemon", "papaya"]
print("Q7","First:", fruits[0])
print("Q7","Last:", fruits[-1])
print("Q7","Total items:", len(fruits))

students = ["Ade", "Bola", "Chidi", "Dayo", "Emeka"]
students.append(input("Enter another student's name: "))
print("Q8","Updated list:", students)

Number =[1,2,3,4,5,6,7,8,9,10]
print("Q9","Even numbers:", [n for n in Number if n % 2 == 0])

nums = [15, 8, 25, 40, 12, 30, 5, 18]
largest = nums[0]
smallest = nums[0]
total = 0
for n in nums:
  if n > largest:
        largest = n
  if n < smallest:
       smallest = n
total += n
print("Q10","Largest:", largest)
print("Q10","Smallest:", smallest)
print("Q10","Sum:", total)

shopping = ["bread", "milk", "eggs", "rice", "sugar"]
for _ in range(2):
shopping.append(input("Add a product: "))
item = input("Enter a product to remove: ")
if item in shopping:
  shopping.remove(item)
else:
print("Product not found.")
print("Q11","Final shopping list:", shopping)


numbers = [5, 12, 18, 23, 7, 30, 41, 9, 15, 2]
n = int(input("Enter a number: "))
if n in numbers:
print(f"{n} exists at position (index) {numbers.index(n)}")
else:
print("Q12", f"{n} is not in the list.")

student = {"name": "Ada", "age": 20, "gender": "Female","department": "Computer Science", "matric_no": "CSC/2024/001"}
for key, value in student.items():
print("Q13", f"{key}: {value}")

products = {"Bread": 800, "Milk": 1200, "Rice": 5000, "Eggs": 2500, "Sugar": 1500}
for name, price in products.items():
print("Q14", f"{name}: {price}")

student = {"name": "Ada", "age": 20, "score": 65}
student["score"] = int(input("Enter the new score: "))
print("Q15", "Updated information:", student)

scores = {"Ade": 67, "Bola": 82, "Chidi": 75, "Dayo": 90, "Emeka": 58}
top_name, top_score = None, -1
for name, score in scores.items():
if score > top_score:
top_name, top_score = name, score
print("Q16", f"Highest score: {top_name} with {top_score}")

account = {"account_name": "Ada Obi", "account_number": "1234567890", "balance": 10000.0}
choice = input("Type 'deposit' or 'withdraw': ").strip().lower()
amount = float(input("Enter amount: "))
if choice == "deposit":
account["balance"] += amount
elif choice == "withdraw":
if amount <= account["balance"]:
account["balance"] -= amount
else:
    print("Insufficient funds.")
else:
    print("Invalid choice.")
print("Q17","Current balance:", account["balance"])

numbers = {10, 20, 30, 10, 40, 20, 50, 30}
print("Q18",numbers)

class_a = {"Ade", "Bola", "Chidi", "Dayo"}
class_b = {"Chidi", "Emeka", "Dayo", "Funke"}
print("Q19","Students in both classes:", class_a & class_b)

a = set(range(1, 11))
b = set(range(5, 16))
print("Q20","All elements:", a | b)
print("Q20","Common elements:", a & b)
print("Q20", "In first but not second:", a - b)

days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
print("Q21","First day:", days[0])
print("Q21","Last day:", days[-1])
print("Q21","Number of days:", len(days))
print("Q21","Saturday exists:", "Saturday" in days)

students = ("Ade", "Bola", "Chidi", "Dayo", "Emeka")
lst = list(students)
lst.append("Funke")
lst.append("Gozie")
lst.remove("Bola")
students = tuple(lst)
print("Q22",students)


with open("students.txt", "w") as f:
   f.write("Name: Ada\nAge: 20\nDepartment: Computer Science\n")
print("Q23","students.txt created.")


names = ["Ade", "Bola", "Chidi", "Dayo", "Emeka"]
with open("students.txt", "w") as f:  # "w" replaces previous content
for n in names:
     f.write(n + "\n")
print("Q24","students.txt overwritten with five names.")


with open("students.txt", "a") as f:  # "a" keeps previous content
for n in ["Funke", "Gozie", "Hauwa"]:
     f.write(n + "\n")
print("Q25","Three names appended.")


try:
with open("students.txt", "r") as f:
   print(f.read())
except FileNotFoundError:
print("Q26","students.txt not found. Run q23 first.")


sentences = ["Today was a good day.", "I learned about Python files.", "I wrote some code.", "I fixed a few bugs.", "Tomorrow I will practise more."]
with open("diary.txt", "w") as f:
for s in sentences:
f.write(s + "\n")
with open("diary.txt", "r") as f:
print("Q27:", f.read())

name = input("Enter your name: ")
language = input("Enter your favourite programming language: ")
with open("profile.txt", "a") as f:
f.write(f"{name} - {language}\n")
print("Q28","Saved to profile.txt.")


if not os.path.exists("numbers.txt"):  # create sample data if missing
with open("numbers.txt", "w") as f:
f.write("10\n20\n30\n40\n")
total = 0
with open("numbers.txt", "r") as f:
for line in f:
line = line.strip()
if line:
total += float(line)
print("Q29","Sum of numbers:", total)

    while True:
        print("\n1. Add student record\n2. View all records\n3. Count records\n4. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            name = input("Name: ")
            age = input("Age: ")
            score = input("Exam score: ")
            with open("records.txt", "a") as f:
                f.write(f"{name},{age},{score}\n")
            print("Record saved.")
        elif choice == "2":
            if os.path.exists("records.txt"):
                with open("records.txt", "r") as f:
                    for line in f:
                        name, age, score = line.strip().split(",")
                        print(f"Name: {name} | Age: {age} | Score: {score}")
            else:
                print("No records yet.")
        elif choice == "3":
            count = 0
            if os.path.exists("records.txt"):
                with open("records.txt", "r") as f:
                    count = sum(1 for line in f if line.strip())
            print("Total records:", count)
        elif choice == "4":
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    choice = input("Enter question number (1-30) or 'all': ").strip().lower()
    if choice == "all":
        for i in range(1, 31):
            print(f"\n--- Question {i} ---")
            globals()[f"q{i}"]()
    elif choice.isdigit() and 1 <= int(choice) <= 30:
        globals()[f"q{choice}"]()
    else:
        print("Invalid choice.")Name = "Moses"
Age = 19
Height = "6ft"
Status = "Student"

print("Q1",Name)
print("Q1",Age)
print("Q1",Height)
print("Q1",Status)

a, b = 10, 3
x, y = 4.5, 1.5
print("Q2","Addition:", a + b, x + y)
print("Q2","Subtraction:", a - b, x - y)
print("Q2","Multiplication:", a * b, x * y)
print("Q2","Division:", a / b, x / y)

Name = input("Enter your name: ")
Age = int(input("Enter your age: "))
colour = input("Enter your favourite colour: ")

print("Q3",f"My name is {Name}, I am {Age} years old and my favourite colour is {colour}.")

num = 10
num2 = 20.29
name = "Ada"
Value = True

print("Q4",num, type(num), num2, type(num2), (name, type(name), (Value, type(Value))))

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Q5","Sum:", a + b)
print("Q5","Product:", a * b)
print("Q5","Difference:", a - b)

name = "Chidi"
s1, s2, s3, s4, s5 = 70, 65, 80, 55, 90
status = "Passed"
total = s1 + s2 + s3 + s4 + s5
average = total / 5
print("Q6","Name:", name)
print("Q6","Scores:", s1, s2, s3, s4, s5)
print("Q6","Status:", status)
print("Q6","Total:", total)
print("Q6","Average:", average)

fruits = ["apple", "banana", "mango", "orange", "pear", "grape", "pineapple", "guava", "lemon", "papaya"]
print("Q7","First:", fruits[0])
print("Q7","Last:", fruits[-1])
print("Q7","Total items:", len(fruits))

students = ["Ade", "Bola", "Chidi", "Dayo", "Emeka"]
students.append(input("Enter another student's name: "))
print("Q8","Updated list:", students)

Number =[1,2,3,4,5,6,7,8,9,10]
print("Q9","Even numbers:", [n for n in Number if n % 2 == 0])

nums = [15, 8, 25, 40, 12, 30, 5, 18]
largest = nums[0]
smallest = nums[0]
total = 0
for n in nums:
  if n > largest:
        largest = n
  if n < smallest:
       smallest = n
total += n
print("Q10","Largest:", largest)
print("Q10","Smallest:", smallest)
print("Q10","Sum:", total)

shopping = ["bread", "milk", "eggs", "rice", "sugar"]
for _ in range(2):
shopping.append(input("Add a product: "))
item = input("Enter a product to remove: ")
if item in shopping:
  shopping.remove(item)
else:
print("Product not found.")
print("Q11","Final shopping list:", shopping)


numbers = [5, 12, 18, 23, 7, 30, 41, 9, 15, 2]
n = int(input("Enter a number: "))
if n in numbers:
print(f"{n} exists at position (index) {numbers.index(n)}")
else:
print("Q12", f"{n} is not in the list.")

student = {"name": "Ada", "age": 20, "gender": "Female","department": "Computer Science", "matric_no": "CSC/2024/001"}
for key, value in student.items():
print("Q13", f"{key}: {value}")

products = {"Bread": 800, "Milk": 1200, "Rice": 5000, "Eggs": 2500, "Sugar": 1500}
for name, price in products.items():
print("Q14", f"{name}: {price}")

student = {"name": "Ada", "age": 20, "score": 65}
student["score"] = int(input("Enter the new score: "))
print("Q15", "Updated information:", student)

scores = {"Ade": 67, "Bola": 82, "Chidi": 75, "Dayo": 90, "Emeka": 58}
top_name, top_score = None, -1
for name, score in scores.items():
if score > top_score:
top_name, top_score = name, score
print("Q16", f"Highest score: {top_name} with {top_score}")

account = {"account_name": "Ada Obi", "account_number": "1234567890", "balance": 10000.0}
choice = input("Type 'deposit' or 'withdraw': ").strip().lower()
amount = float(input("Enter amount: "))
if choice == "deposit":
account["balance"] += amount
elif choice == "withdraw":
if amount <= account["balance"]:
account["balance"] -= amount
else:
    print("Insufficient funds.")
else:
    print("Invalid choice.")
print("Q17","Current balance:", account["balance"])

numbers = {10, 20, 30, 10, 40, 20, 50, 30}
print("Q18",numbers)

class_a = {"Ade", "Bola", "Chidi", "Dayo"}
class_b = {"Chidi", "Emeka", "Dayo", "Funke"}
print("Q19","Students in both classes:", class_a & class_b)

a = set(range(1, 11))
b = set(range(5, 16))
print("Q20","All elements:", a | b)
print("Q20","Common elements:", a & b)
print("Q20", "In first but not second:", a - b)

days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
print("Q21","First day:", days[0])
print("Q21","Last day:", days[-1])
print("Q21","Number of days:", len(days))
print("Q21","Saturday exists:", "Saturday" in days)

students = ("Ade", "Bola", "Chidi", "Dayo", "Emeka")
lst = list(students)
lst.append("Funke")
lst.append("Gozie")
lst.remove("Bola")
students = tuple(lst)
print("Q22",students)


with open("students.txt", "w") as f:
   f.write("Name: Ada\nAge: 20\nDepartment: Computer Science\n")
print("Q23","students.txt created.")


names = ["Ade", "Bola", "Chidi", "Dayo", "Emeka"]
with open("students.txt", "w") as f:  # "w" replaces previous content
for n in names:
     f.write(n + "\n")
print("Q24","students.txt overwritten with five names.")


with open("students.txt", "a") as f:  # "a" keeps previous content
for n in ["Funke", "Gozie", "Hauwa"]:
     f.write(n + "\n")
print("Q25","Three names appended.")


try:
with open("students.txt", "r") as f:
   print(f.read())
except FileNotFoundError:
print("Q26","students.txt not found. Run q23 first.")


sentences = ["Today was a good day.", "I learned about Python files.", "I wrote some code.", "I fixed a few bugs.", "Tomorrow I will practise more."]
with open("diary.txt", "w") as f:
for s in sentences:
f.write(s + "\n")
with open("diary.txt", "r") as f:
print("Q27:", f.read())

name = input("Enter your name: ")
language = input("Enter your favourite programming language: ")
with open("profile.txt", "a") as f:
f.write(f"{name} - {language}\n")
print("Q28","Saved to profile.txt.")


if not os.path.exists("numbers.txt"):  # create sample data if missing
with open("numbers.txt", "w") as f:
f.write("10\n20\n30\n40\n")
total = 0
with open("numbers.txt", "r") as f:
for line in f:
line = line.strip()
if line:
total += float(line)
print("Q29","Sum of numbers:", total)

    while True:
        print("\n1. Add student record\n2. View all records\n3. Count records\n4. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            name = input("Name: ")
            age = input("Age: ")
            score = input("Exam score: ")
            with open("records.txt", "a") as f:
                f.write(f"{name},{age},{score}\n")
            print("Record saved.")
        elif choice == "2":
            if os.path.exists("records.txt"):
                with open("records.txt", "r") as f:
                    for line in f:
                        name, age, score = line.strip().split(",")
                        print(f"Name: {name} | Age: {age} | Score: {score}")
            else:
                print("No records yet.")
        elif choice == "3":
            count = 0
            if os.path.exists("records.txt"):
                with open("records.txt", "r") as f:
                    count = sum(1 for line in f if line.strip())
            print("Total records:", count)
        elif choice == "4":
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    choice = input("Enter question number (1-30) or 'all': ").strip().lower()
    if choice == "all":
        for i in range(1, 31):
            print(f"\n--- Question {i} ---")
            globals()[f"q{i}"]()
    elif choice.isdigit() and 1 <= int(choice) <= 30:
        globals()[f"q{choice}"]()
    else:
        print("Invalid choice.")vName = "Moses"
Age = 19
Height = "6ft"
Status = "Student"

print("Q1",Name)
print("Q1",Age)
print("Q1",Height)
print("Q1",Status)

a, b = 10, 3
x, y = 4.5, 1.5
print("Q2","Addition:", a + b, x + y)
print("Q2","Subtraction:", a - b, x - y)
print("Q2","Multiplication:", a * b, x * y)
print("Q2","Division:", a / b, x / y)

Name = input("Enter your name: ")
Age = int(input("Enter your age: "))
colour = input("Enter your favourite colour: ")

print("Q3",f"My name is {Name}, I am {Age} years old and my favourite colour is {colour}.")

num = 10
num2 = 20.29
name = "Ada"
Value = True

print("Q4",num, type(num), num2, type(num2), (name, type(name), (Value, type(Value))))

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Q5","Sum:", a + b)
print("Q5","Product:", a * b)
print("Q5","Difference:", a - b)

name = "Chidi"
s1, s2, s3, s4, s5 = 70, 65, 80, 55, 90
status = "Passed"
total = s1 + s2 + s3 + s4 + s5
average = total / 5
print("Q6","Name:", name)
print("Q6","Scores:", s1, s2, s3, s4, s5)
print("Q6","Status:", status)
print("Q6","Total:", total)
print("Q6","Average:", average)

fruits = ["apple", "banana", "mango", "orange", "pear", "grape", "pineapple", "guava", "lemon", "papaya"]
print("Q7","First:", fruits[0])
print("Q7","Last:", fruits[-1])
print("Q7","Total items:", len(fruits))

students = ["Ade", "Bola", "Chidi", "Dayo", "Emeka"]
students.append(input("Enter another student's name: "))
print("Q8","Updated list:", students)

Number =[1,2,3,4,5,6,7,8,9,10]
print("Q9","Even numbers:", [n for n in Number if n % 2 == 0])

nums = [15, 8, 25, 40, 12, 30, 5, 18]
largest = nums[0]
smallest = nums[0]
total = 0
for n in nums:
  if n > largest:
        largest = n
  if n < smallest:
       smallest = n
total += n
print("Q10","Largest:", largest)
print("Q10","Smallest:", smallest)
print("Q10","Sum:", total)

shopping = ["bread", "milk", "eggs", "rice", "sugar"]
for _ in range(2):
shopping.append(input("Add a product: "))
item = input("Enter a product to remove: ")
if item in shopping:
  shopping.remove(item)
else:
print("Product not found.")
print("Q11","Final shopping list:", shopping)


numbers = [5, 12, 18, 23, 7, 30, 41, 9, 15, 2]
n = int(input("Enter a number: "))
if n in numbers:
print(f"{n} exists at position (index) {numbers.index(n)}")
else:
print("Q12", f"{n} is not in the list.")

student = {"name": "Ada", "age": 20, "gender": "Female","department": "Computer Science", "matric_no": "CSC/2024/001"}
for key, value in student.items():
print("Q13", f"{key}: {value}")

products = {"Bread": 800, "Milk": 1200, "Rice": 5000, "Eggs": 2500, "Sugar": 1500}
for name, price in products.items():
print("Q14", f"{name}: {price}")

student = {"name": "Ada", "age": 20, "score": 65}
student["score"] = int(input("Enter the new score: "))
print("Q15", "Updated information:", student)

scores = {"Ade": 67, "Bola": 82, "Chidi": 75, "Dayo": 90, "Emeka": 58}
top_name, top_score = None, -1
for name, score in scores.items():
if score > top_score:
top_name, top_score = name, score
print("Q16", f"Highest score: {top_name} with {top_score}")

account = {"account_name": "Ada Obi", "account_number": "1234567890", "balance": 10000.0}
choice = input("Type 'deposit' or 'withdraw': ").strip().lower()
amount = float(input("Enter amount: "))
if choice == "deposit":
account["balance"] += amount
elif choice == "withdraw":
if amount <= account["balance"]:
account["balance"] -= amount
else:
    print("Insufficient funds.")
else:
    print("Invalid choice.")
print("Q17","Current balance:", account["balance"])

numbers = {10, 20, 30, 10, 40, 20, 50, 30}
print("Q18",numbers)

class_a = {"Ade", "Bola", "Chidi", "Dayo"}
class_b = {"Chidi", "Emeka", "Dayo", "Funke"}
print("Q19","Students in both classes:", class_a & class_b)

a = set(range(1, 11))
b = set(range(5, 16))
print("Q20","All elements:", a | b)
print("Q20","Common elements:", a & b)
print("Q20", "In first but not second:", a - b)

days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
print("Q21","First day:", days[0])
print("Q21","Last day:", days[-1])
print("Q21","Number of days:", len(days))
print("Q21","Saturday exists:", "Saturday" in days)

students = ("Ade", "Bola", "Chidi", "Dayo", "Emeka")
lst = list(students)
lst.append("Funke")
lst.append("Gozie")
lst.remove("Bola")
students = tuple(lst)
print("Q22",students)


with open("students.txt", "w") as f:
   f.write("Name: Ada\nAge: 20\nDepartment: Computer Science\n")
print("Q23","students.txt created.")


names = ["Ade", "Bola", "Chidi", "Dayo", "Emeka"]
with open("students.txt", "w") as f:  # "w" replaces previous content
for n in names:
     f.write(n + "\n")
print("Q24","students.txt overwritten with five names.")


with open("students.txt", "a") as f:  # "a" keeps previous content
for n in ["Funke", "Gozie", "Hauwa"]:
     f.write(n + "\n")
print("Q25","Three names appended.")


try:
with open("students.txt", "r") as f:
   print(f.read())
except FileNotFoundError:
print("Q26","students.txt not found. Run q23 first.")


sentences = ["Today was a good day.", "I learned about Python files.", "I wrote some code.", "I fixed a few bugs.", "Tomorrow I will practise more."]
with open("diary.txt", "w") as f:
for s in sentences:
f.write(s + "\n")
with open("diary.txt", "r") as f:
print("Q27:", f.read())

name = input("Enter your name: ")
language = input("Enter your favourite programming language: ")
with open("profile.txt", "a") as f:
f.write(f"{name} - {language}\n")
print("Q28","Saved to profile.txt.")


if not os.path.exists("numbers.txt"):  # create sample data if missing
with open("numbers.txt", "w") as f:
f.write("10\n20\n30\n40\n")
total = 0
with open("numbers.txt", "r") as f:
for line in f:
line = line.strip()
if line:
total += float(line)
print("Q29","Sum of numbers:", total)

    while True:
        print("\n1. Add student record\n2. View all records\n3. Count records\n4. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            name = input("Name: ")
            age = input("Age: ")
            score = input("Exam score: ")
            with open("records.txt", "a") as f:
                f.write(f"{name},{age},{score}\n")
            print("Record saved.")
        elif choice == "2":
            if os.path.exists("records.txt"):
                with open("records.txt", "r") as f:
                    for line in f:
                        name, age, score = line.strip().split(",")
                        print(f"Name: {name} | Age: {age} | Score: {score}")
            else:
                print("No records yet.")
        elif choice == "3":
            count = 0
            if os.path.exists("records.txt"):
                with open("records.txt", "r") as f:
                    count = sum(1 for line in f if line.strip())
            print("Total records:", count)
        elif choice == "4":
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    choice = input("Enter question number (1-30) or 'all': ").strip().lower()
    if choice == "all":
        for i in range(1, 31):
            print(f"\n--- Question {i} ---")
            globals()[f"q{i}"]()
    elif choice.isdigit() and 1 <= int(choice) <= 30:
        globals()[f"q{choice}"]()
    else:
        print("Invalid choice.")Name = "Moses"
Age = 19
Height = "6ft"
Status = "Student"

print("Q1",Name)
print("Q1",Age)
print("Q1",Height)
print("Q1",Status)

a, b = 10, 3
x, y = 4.5, 1.5
print("Q2","Addition:", a + b, x + y)
print("Q2","Subtraction:", a - b, x - y)
print("Q2","Multiplication:", a * b, x * y)
print("Q2","Division:", a / b, x / y)

Name = input("Enter your name: ")
Age = int(input("Enter your age: "))
colour = input("Enter your favourite colour: ")

print("Q3",f"My name is {Name}, I am {Age} years old and my favourite colour is {colour}.")

num = 10
num2 = 20.29
name = "Ada"
Value = True

print("Q4",num, type(num), num2, type(num2), (name, type(name), (Value, type(Value))))

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Q5","Sum:", a + b)
print("Q5","Product:", a * b)
print("Q5","Difference:", a - b)

name = "Chidi"
s1, s2, s3, s4, s5 = 70, 65, 80, 55, 90
status = "Passed"
total = s1 + s2 + s3 + s4 + s5
average = total / 5
print("Q6","Name:", name)
print("Q6","Scores:", s1, s2, s3, s4, s5)
print("Q6","Status:", status)
print("Q6","Total:", total)
print("Q6","Average:", average)

fruits = ["apple", "banana", "mango", "orange", "pear", "grape", "pineapple", "guava", "lemon", "papaya"]
print("Q7","First:", fruits[0])
print("Q7","Last:", fruits[-1])
print("Q7","Total items:", len(fruits))

students = ["Ade", "Bola", "Chidi", "Dayo", "Emeka"]
students.append(input("Enter another student's name: "))
print("Q8","Updated list:", students)

Number =[1,2,3,4,5,6,7,8,9,10]
print("Q9","Even numbers:", [n for n in Number if n % 2 == 0])

nums = [15, 8, 25, 40, 12, 30, 5, 18]
largest = nums[0]
smallest = nums[0]
total = 0
for n in nums:
  if n > largest:
        largest = n
  if n < smallest:
       smallest = n
total += n
print("Q10","Largest:", largest)
print("Q10","Smallest:", smallest)
print("Q10","Sum:", total)

shopping = ["bread", "milk", "eggs", "rice", "sugar"]
for _ in range(2):
shopping.append(input("Add a product: "))
item = input("Enter a product to remove: ")
if item in shopping:
  shopping.remove(item)
else:
print("Product not found.")
print("Q11","Final shopping list:", shopping)


numbers = [5, 12, 18, 23, 7, 30, 41, 9, 15, 2]
n = int(input("Enter a number: "))
if n in numbers:
print(f"{n} exists at position (index) {numbers.index(n)}")
else:
print("Q12", f"{n} is not in the list.")

student = {"name": "Ada", "age": 20, "gender": "Female","department": "Computer Science", "matric_no": "CSC/2024/001"}
for key, value in student.items():
print("Q13", f"{key}: {value}")

products = {"Bread": 800, "Milk": 1200, "Rice": 5000, "Eggs": 2500, "Sugar": 1500}
for name, price in products.items():
print("Q14", f"{name}: {price}")

student = {"name": "Ada", "age": 20, "score": 65}
student["score"] = int(input("Enter the new score: "))
print("Q15", "Updated information:", student)

scores = {"Ade": 67, "Bola": 82, "Chidi": 75, "Dayo": 90, "Emeka": 58}
top_name, top_score = None, -1
for name, score in scores.items():
if score > top_score:
top_name, top_score = name, score
print("Q16", f"Highest score: {top_name} with {top_score}")

account = {"account_name": "Ada Obi", "account_number": "1234567890", "balance": 10000.0}
choice = input("Type 'deposit' or 'withdraw': ").strip().lower()
amount = float(input("Enter amount: "))
if choice == "deposit":
account["balance"] += amount
elif choice == "withdraw":
if amount <= account["balance"]:
account["balance"] -= amount
else:
    print("Insufficient funds.")
else:
    print("Invalid choice.")
print("Q17","Current balance:", account["balance"])

numbers = {10, 20, 30, 10, 40, 20, 50, 30}
print("Q18",numbers)

class_a = {"Ade", "Bola", "Chidi", "Dayo"}
class_b = {"Chidi", "Emeka", "Dayo", "Funke"}
print("Q19","Students in both classes:", class_a & class_b)

a = set(range(1, 11))
b = set(range(5, 16))
print("Q20","All elements:", a | b)
print("Q20","Common elements:", a & b)
print("Q20", "In first but not second:", a - b)

days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
print("Q21","First day:", days[0])
print("Q21","Last day:", days[-1])
print("Q21","Number of days:", len(days))
print("Q21","Saturday exists:", "Saturday" in days)

students = ("Ade", "Bola", "Chidi", "Dayo", "Emeka")
lst = list(students)
lst.append("Funke")
lst.append("Gozie")
lst.remove("Bola")
students = tuple(lst)
print("Q22",students)


with open("students.txt", "w") as f:
   f.write("Name: Ada\nAge: 20\nDepartment: Computer Science\n")
print("Q23","students.txt created.")


names = ["Ade", "Bola", "Chidi", "Dayo", "Emeka"]
with open("students.txt", "w") as f:  # "w" replaces previous content
for n in names:
     f.write(n + "\n")
print("Q24","students.txt overwritten with five names.")


with open("students.txt", "a") as f:  # "a" keeps previous content
for n in ["Funke", "Gozie", "Hauwa"]:
     f.write(n + "\n")
print("Q25","Three names appended.")


try:
with open("students.txt", "r") as f:
   print(f.read())
except FileNotFoundError:
print("Q26","students.txt not found. Run q23 first.")


sentences = ["Today was a good day.", "I learned about Python files.", "I wrote some code.", "I fixed a few bugs.", "Tomorrow I will practise more."]
with open("diary.txt", "w") as f:
for s in sentences:
f.write(s + "\n")
with open("diary.txt", "r") as f:
print("Q27:", f.read())

name = input("Enter your name: ")
language = input("Enter your favourite programming language: ")
with open("profile.txt", "a") as f:
f.write(f"{name} - {language}\n")
print("Q28","Saved to profile.txt.")


if not os.path.exists("numbers.txt"):  # create sample data if missing
with open("numbers.txt", "w") as f:
f.write("10\n20\n30\n40\n")
total = 0
with open("numbers.txt", "r") as f:
for line in f:
line = line.strip()
if line:
total += float(line)
print("Q29","Sum of numbers:", total)

    while True:
        print("\n1. Add student record\n2. View all records\n3. Count records\n4. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            name = input("Name: ")
            age = input("Age: ")
            score = input("Exam score: ")
            with open("records.txt", "a") as f:
                f.write(f"{name},{age},{score}\n")
            print("Record saved.")
        elif choice == "2":
            if os.path.exists("records.txt"):
                with open("records.txt", "r") as f:
                    for line in f:
                        name, age, score = line.strip().split(",")
                        print(f"Name: {name} | Age: {age} | Score: {score}")
            else:
                print("No records yet.")
        elif choice == "3":
            count = 0
            if os.path.exists("records.txt"):
                with open("records.txt", "r") as f:
                    count = sum(1 for line in f if line.strip())
            print("Total records:", count)
        elif choice == "4":
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    choice = input("Enter question number (1-30) or 'all': ").strip().lower()
    if choice == "all":
        for i in range(1, 31):
            print(f"\n--- Question {i} ---")
            globals()[f"q{i}"]()
    elif choice.isdigit() and 1 <= int(choice) <= 30:
        globals()[f"q{choice}"]()
    else:
        print("Invalid choice.")Name = "Moses"
Age = 19
Height = "6ft"
Status = "Student"

print("Q1",Name)
print("Q1",Age)
print("Q1",Height)
print("Q1",Status)

a, b = 10, 3
x, y = 4.5, 1.5
print("Q2","Addition:", a + b, x + y)
print("Q2","Subtraction:", a - b, x - y)
print("Q2","Multiplication:", a * b, x * y)
print("Q2","Division:", a / b, x / y)

Name = input("Enter your name: ")
Age = int(input("Enter your age: "))
colour = input("Enter your favourite colour: ")

print("Q3",f"My name is {Name}, I am {Age} years old and my favourite colour is {colour}.")

num = 10
num2 = 20.29
name = "Ada"
Value = True

print("Q4",num, type(num), num2, type(num2), (name, type(name), (Value, type(Value))))

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Q5","Sum:", a + b)
print("Q5","Product:", a * b)
print("Q5","Difference:", a - b)

name = "Chidi"
s1, s2, s3, s4, s5 = 70, 65, 80, 55, 90
status = "Passed"
total = s1 + s2 + s3 + s4 + s5
average = total / 5
print("Q6","Name:", name)
print("Q6","Scores:", s1, s2, s3, s4, s5)
print("Q6","Status:", status)
print("Q6","Total:", total)
print("Q6","Average:", average)

fruits = ["apple", "banana", "mango", "orange", "pear", "grape", "pineapple", "guava", "lemon", "papaya"]
print("Q7","First:", fruits[0])
print("Q7","Last:", fruits[-1])
print("Q7","Total items:", len(fruits))

students = ["Ade", "Bola", "Chidi", "Dayo", "Emeka"]
students.append(input("Enter another student's name: "))
print("Q8","Updated list:", students)

Number =[1,2,3,4,5,6,7,8,9,10]
print("Q9","Even numbers:", [n for n in Number if n % 2 == 0])

nums = [15, 8, 25, 40, 12, 30, 5, 18]
largest = nums[0]
smallest = nums[0]
total = 0
for n in nums:
  if n > largest:
        largest = n
  if n < smallest:
       smallest = n
total += n
print("Q10","Largest:", largest)
print("Q10","Smallest:", smallest)
print("Q10","Sum:", total)

shopping = ["bread", "milk", "eggs", "rice", "sugar"]
for _ in range(2):
shopping.append(input("Add a product: "))
item = input("Enter a product to remove: ")
if item in shopping:
  shopping.remove(item)
else:
print("Product not found.")
print("Q11","Final shopping list:", shopping)


numbers = [5, 12, 18, 23, 7, 30, 41, 9, 15, 2]
n = int(input("Enter a number: "))
if n in numbers:
print(f"{n} exists at position (index) {numbers.index(n)}")
else:
print("Q12", f"{n} is not in the list.")

student = {"name": "Ada", "age": 20, "gender": "Female","department": "Computer Science", "matric_no": "CSC/2024/001"}
for key, value in student.items():
print("Q13", f"{key}: {value}")

products = {"Bread": 800, "Milk": 1200, "Rice": 5000, "Eggs": 2500, "Sugar": 1500}
for name, price in products.items():
print("Q14", f"{name}: {price}")

student = {"name": "Ada", "age": 20, "score": 65}
student["score"] = int(input("Enter the new score: "))
print("Q15", "Updated information:", student)

scores = {"Ade": 67, "Bola": 82, "Chidi": 75, "Dayo": 90, "Emeka": 58}
top_name, top_score = None, -1
for name, score in scores.items():
if score > top_score:
top_name, top_score = name, score
print("Q16", f"Highest score: {top_name} with {top_score}")

account = {"account_name": "Ada Obi", "account_number": "1234567890", "balance": 10000.0}
choice = input("Type 'deposit' or 'withdraw': ").strip().lower()
amount = float(input("Enter amount: "))
if choice == "deposit":
account["balance"] += amount
elif choice == "withdraw":
if amount <= account["balance"]:
account["balance"] -= amount
else:
    print("Insufficient funds.")
else:
    print("Invalid choice.")
print("Q17","Current balance:", account["balance"])

numbers = {10, 20, 30, 10, 40, 20, 50, 30}
print("Q18",numbers)

class_a = {"Ade", "Bola", "Chidi", "Dayo"}
class_b = {"Chidi", "Emeka", "Dayo", "Funke"}
print("Q19","Students in both classes:", class_a & class_b)

a = set(range(1, 11))
b = set(range(5, 16))
print("Q20","All elements:", a | b)
print("Q20","Common elements:", a & b)
print("Q20", "In first but not second:", a - b)

days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
print("Q21","First day:", days[0])
print("Q21","Last day:", days[-1])
print("Q21","Number of days:", len(days))
print("Q21","Saturday exists:", "Saturday" in days)

students = ("Ade", "Bola", "Chidi", "Dayo", "Emeka")
lst = list(students)
lst.append("Funke")
lst.append("Gozie")
lst.remove("Bola")
students = tuple(lst)
print("Q22",students)


with open("students.txt", "w") as f:
   f.write("Name: Ada\nAge: 20\nDepartment: Computer Science\n")
print("Q23","students.txt created.")


names = ["Ade", "Bola", "Chidi", "Dayo", "Emeka"]
with open("students.txt", "w") as f:  # "w" replaces previous content
for n in names:
     f.write(n + "\n")
print("Q24","students.txt overwritten with five names.")


with open("students.txt", "a") as f:  # "a" keeps previous content
for n in ["Funke", "Gozie", "Hauwa"]:
     f.write(n + "\n")
print("Q25","Three names appended.")


try:
with open("students.txt", "r") as f:
   print(f.read())
except FileNotFoundError:
print("Q26","students.txt not found. Run q23 first.")


sentences = ["Today was a good day.", "I learned about Python files.", "I wrote some code.", "I fixed a few bugs.", "Tomorrow I will practise more."]
with open("diary.txt", "w") as f:
for s in sentences:
f.write(s + "\n")
with open("diary.txt", "r") as f:
print("Q27:", f.read())

name = input("Enter your name: ")
language = input("Enter your favourite programming language: ")
with open("profile.txt", "a") as f:
f.write(f"{name} - {language}\n")
print("Q28","Saved to profile.txt.")


if not os.path.exists("numbers.txt"):  # create sample data if missing
with open("numbers.txt", "w") as f:
f.write("10\n20\n30\n40\n")
total = 0
with open("numbers.txt", "r") as f:
for line in f:
line = line.strip()
if line:
total += float(line)
print("Q29","Sum of numbers:", total)

    while True:
        print("\n1. Add student record\n2. View all records\n3. Count records\n4. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            name = input("Name: ")
            age = input("Age: ")
            score = input("Exam score: ")
            with open("records.txt", "a") as f:
                f.write(f"{name},{age},{score}\n")
            print("Record saved.")
        elif choice == "2":
            if os.path.exists("records.txt"):
                with open("records.txt", "r") as f:
                    for line in f:
                        name, age, score = line.strip().split(",")
                        print(f"Name: {name} | Age: {age} | Score: {score}")
            else:
                print("No records yet.")
        elif choice == "3":
            count = 0
            if os.path.exists("records.txt"):
                with open("records.txt", "r") as f:
                    count = sum(1 for line in f if line.strip())
            print("Total records:", count)
        elif choice == "4":
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    choice = input("Enter question number (1-30) or 'all': ").strip().lower()
    if choice == "all":
        for i in range(1, 31):
            print(f"\n--- Question {i} ---")
            globals()[f"q{i}"]()
    elif choice.isdigit() and 1 <= int(choice) <= 30:
        globals()[f"q{choice}"]()
    else:
        print("Invalid choice.")Name = "Moses"
Age = 19
Height = "6ft"
Status = "Student"

print("Q1",Name)
print("Q1",Age)
print("Q1",Height)
print("Q1",Status)

a, b = 10, 3
x, y = 4.5, 1.5
print("Q2","Addition:", a + b, x + y)
print("Q2","Subtraction:", a - b, x - y)
print("Q2","Multiplication:", a * b, x * y)
print("Q2","Division:", a / b, x / y)

Name = input("Enter your name: ")
Age = int(input("Enter your age: "))
colour = input("Enter your favourite colour: ")

print("Q3",f"My name is {Name}, I am {Age} years old and my favourite colour is {colour}.")

num = 10
num2 = 20.29
name = "Ada"
Value = True

print("Q4",num, type(num), num2, type(num2), (name, type(name), (Value, type(Value))))

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Q5","Sum:", a + b)
print("Q5","Product:", a * b)
print("Q5","Difference:", a - b)

name = "Chidi"
s1, s2, s3, s4, s5 = 70, 65, 80, 55, 90
status = "Passed"
total = s1 + s2 + s3 + s4 + s5
average = total / 5
print("Q6","Name:", name)
print("Q6","Scores:", s1, s2, s3, s4, s5)
print("Q6","Status:", status)
print("Q6","Total:", total)
print("Q6","Average:", average)

fruits = ["apple", "banana", "mango", "orange", "pear", "grape", "pineapple", "guava", "lemon", "papaya"]
print("Q7","First:", fruits[0])
print("Q7","Last:", fruits[-1])
print("Q7","Total items:", len(fruits))

students = ["Ade", "Bola", "Chidi", "Dayo", "Emeka"]
students.append(input("Enter another student's name: "))
print("Q8","Updated list:", students)

Number =[1,2,3,4,5,6,7,8,9,10]
print("Q9","Even numbers:", [n for n in Number if n % 2 == 0])

nums = [15, 8, 25, 40, 12, 30, 5, 18]
largest = nums[0]
smallest = nums[0]
total = 0
for n in nums:
  if n > largest:
        largest = n
  if n < smallest:
       smallest = n
total += n
print("Q10","Largest:", largest)
print("Q10","Smallest:", smallest)
print("Q10","Sum:", total)

shopping = ["bread", "milk", "eggs", "rice", "sugar"]
for _ in range(2):
shopping.append(input("Add a product: "))
item = input("Enter a product to remove: ")
if item in shopping:
  shopping.remove(item)
else:
print("Product not found.")
print("Q11","Final shopping list:", shopping)


numbers = [5, 12, 18, 23, 7, 30, 41, 9, 15, 2]
n = int(input("Enter a number: "))
if n in numbers:
print(f"{n} exists at position (index) {numbers.index(n)}")
else:
print("Q12", f"{n} is not in the list.")

student = {"name": "Ada", "age": 20, "gender": "Female","department": "Computer Science", "matric_no": "CSC/2024/001"}
for key, value in student.items():
print("Q13", f"{key}: {value}")

products = {"Bread": 800, "Milk": 1200, "Rice": 5000, "Eggs": 2500, "Sugar": 1500}
for name, price in products.items():
print("Q14", f"{name}: {price}")

student = {"name": "Ada", "age": 20, "score": 65}
student["score"] = int(input("Enter the new score: "))
print("Q15", "Updated information:", student)

scores = {"Ade": 67, "Bola": 82, "Chidi": 75, "Dayo": 90, "Emeka": 58}
top_name, top_score = None, -1
for name, score in scores.items():
if score > top_score:
top_name, top_score = name, score
print("Q16", f"Highest score: {top_name} with {top_score}")

account = {"account_name": "Ada Obi", "account_number": "1234567890", "balance": 10000.0}
choice = input("Type 'deposit' or 'withdraw': ").strip().lower()
amount = float(input("Enter amount: "))
if choice == "deposit":
account["balance"] += amount
elif choice == "withdraw":
if amount <= account["balance"]:
account["balance"] -= amount
else:
    print("Insufficient funds.")
else:
    print("Invalid choice.")
print("Q17","Current balance:", account["balance"])

numbers = {10, 20, 30, 10, 40, 20, 50, 30}
print("Q18",numbers)

class_a = {"Ade", "Bola", "Chidi", "Dayo"}
class_b = {"Chidi", "Emeka", "Dayo", "Funke"}
print("Q19","Students in both classes:", class_a & class_b)

a = set(range(1, 11))
b = set(range(5, 16))
print("Q20","All elements:", a | b)
print("Q20","Common elements:", a & b)
print("Q20", "In first but not second:", a - b)

days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
print("Q21","First day:", days[0])
print("Q21","Last day:", days[-1])
print("Q21","Number of days:", len(days))
print("Q21","Saturday exists:", "Saturday" in days)

students = ("Ade", "Bola", "Chidi", "Dayo", "Emeka")
lst = list(students)
lst.append("Funke")
lst.append("Gozie")
lst.remove("Bola")
students = tuple(lst)
print("Q22",students)


with open("students.txt", "w") as f:
   f.write("Name: Ada\nAge: 20\nDepartment: Computer Science\n")
print("Q23","students.txt created.")


names = ["Ade", "Bola", "Chidi", "Dayo", "Emeka"]
with open("students.txt", "w") as f:  # "w" replaces previous content
for n in names:
     f.write(n + "\n")
print("Q24","students.txt overwritten with five names.")


with open("students.txt", "a") as f:  # "a" keeps previous content
for n in ["Funke", "Gozie", "Hauwa"]:
     f.write(n + "\n")
print("Q25","Three names appended.")


try:
with open("students.txt", "r") as f:
   print(f.read())
except FileNotFoundError:
print("Q26","students.txt not found. Run q23 first.")


sentences = ["Today was a good day.", "I learned about Python files.", "I wrote some code.", "I fixed a few bugs.", "Tomorrow I will practise more."]
with open("diary.txt", "w") as f:
for s in sentences:
f.write(s + "\n")
with open("diary.txt", "r") as f:
print("Q27:", f.read())

name = input("Enter your name: ")
language = input("Enter your favourite programming language: ")
with open("profile.txt", "a") as f:
f.write(f"{name} - {language}\n")
print("Q28","Saved to profile.txt.")


if not os.path.exists("numbers.txt"):  # create sample data if missing
with open("numbers.txt", "w") as f:
f.write("10\n20\n30\n40\n")
total = 0
with open("numbers.txt", "r") as f:
for line in f:
line = line.strip()
if line:
total += float(line)
print("Q29","Sum of numbers:", total)

    while True:
        print("\n1. Add student record\n2. View all records\n3. Count records\n4. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            name = input("Name: ")
            age = input("Age: ")
            score = input("Exam score: ")
            with open("records.txt", "a") as f:
                f.write(f"{name},{age},{score}\n")
            print("Record saved.")
        elif choice == "2":
            if os.path.exists("records.txt"):
                with open("records.txt", "r") as f:
                    for line in f:
                        name, age, score = line.strip().split(",")
                        print(f"Name: {name} | Age: {age} | Score: {score}")
            else:
                print("No records yet.")
        elif choice == "3":
            count = 0
            if os.path.exists("records.txt"):
                with open("records.txt", "r") as f:
                    count = sum(1 for line in f if line.strip())
            print("Total records:", count)
        elif choice == "4":
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    choice = input("Enter question number (1-30) or 'all': ").strip().lower()
    if choice == "all":
        for i in range(1, 31):
            print(f"\n--- Question {i} ---")
            globals()[f"q{i}"]()
    elif choice.isdigit() and 1 <= int(choice) <= 30:
        globals()[f"q{choice}"]()
    else:
        print("Invalid choice.")Name = "Moses"
Age = 19
Height = "6ft"
Status = "Student"

print("Q1",Name)
print("Q1",Age)
print("Q1",Height)
print("Q1",Status)

a, b = 10, 3
x, y = 4.5, 1.5
print("Q2","Addition:", a + b, x + y)
print("Q2","Subtraction:", a - b, x - y)
print("Q2","Multiplication:", a * b, x * y)
print("Q2","Division:", a / b, x / y)

Name = input("Enter your name: ")
Age = int(input("Enter your age: "))
colour = input("Enter your favourite colour: ")

print("Q3",f"My name is {Name}, I am {Age} years old and my favourite colour is {colour}.")

num = 10
num2 = 20.29
name = "Ada"
Value = True

print("Q4",num, type(num), num2, type(num2), (name, type(name), (Value, type(Value))))

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Q5","Sum:", a + b)
print("Q5","Product:", a * b)
print("Q5","Difference:", a - b)

name = "Chidi"
s1, s2, s3, s4, s5 = 70, 65, 80, 55, 90
status = "Passed"
total = s1 + s2 + s3 + s4 + s5
average = total / 5
print("Q6","Name:", name)
print("Q6","Scores:", s1, s2, s3, s4, s5)
print("Q6","Status:", status)
print("Q6","Total:", total)
print("Q6","Average:", average)

fruits = ["apple", "banana", "mango", "orange", "pear", "grape", "pineapple", "guava", "lemon", "papaya"]
print("Q7","First:", fruits[0])
print("Q7","Last:", fruits[-1])
print("Q7","Total items:", len(fruits))

students = ["Ade", "Bola", "Chidi", "Dayo", "Emeka"]
students.append(input("Enter another student's name: "))
print("Q8","Updated list:", students)

Number =[1,2,3,4,5,6,7,8,9,10]
print("Q9","Even numbers:", [n for n in Number if n % 2 == 0])

nums = [15, 8, 25, 40, 12, 30, 5, 18]
largest = nums[0]
smallest = nums[0]
total = 0
for n in nums:
  if n > largest:
        largest = n
  if n < smallest:
       smallest = n
total += n
print("Q10","Largest:", largest)
print("Q10","Smallest:", smallest)
print("Q10","Sum:", total)

shopping = ["bread", "milk", "eggs", "rice", "sugar"]
for _ in range(2):
shopping.append(input("Add a product: "))
item = input("Enter a product to remove: ")
if item in shopping:
  shopping.remove(item)
else:
print("Product not found.")
print("Q11","Final shopping list:", shopping)


numbers = [5, 12, 18, 23, 7, 30, 41, 9, 15, 2]
n = int(input("Enter a number: "))
if n in numbers:
print(f"{n} exists at position (index) {numbers.index(n)}")
else:
print("Q12", f"{n} is not in the list.")

student = {"name": "Ada", "age": 20, "gender": "Female","department": "Computer Science", "matric_no": "CSC/2024/001"}
for key, value in student.items():
print("Q13", f"{key}: {value}")

products = {"Bread": 800, "Milk": 1200, "Rice": 5000, "Eggs": 2500, "Sugar": 1500}
for name, price in products.items():
print("Q14", f"{name}: {price}")

student = {"name": "Ada", "age": 20, "score": 65}
student["score"] = int(input("Enter the new score: "))
print("Q15", "Updated information:", student)

scores = {"Ade": 67, "Bola": 82, "Chidi": 75, "Dayo": 90, "Emeka": 58}
top_name, top_score = None, -1
for name, score in scores.items():
if score > top_score:
top_name, top_score = name, score
print("Q16", f"Highest score: {top_name} with {top_score}")

account = {"account_name": "Ada Obi", "account_number": "1234567890", "balance": 10000.0}
choice = input("Type 'deposit' or 'withdraw': ").strip().lower()
amount = float(input("Enter amount: "))
if choice == "deposit":
account["balance"] += amount
elif choice == "withdraw":
if amount <= account["balance"]:
account["balance"] -= amount
else:
    print("Insufficient funds.")
else:
    print("Invalid choice.")
print("Q17","Current balance:", account["balance"])

numbers = {10, 20, 30, 10, 40, 20, 50, 30}
print("Q18",numbers)

class_a = {"Ade", "Bola", "Chidi", "Dayo"}
class_b = {"Chidi", "Emeka", "Dayo", "Funke"}
print("Q19","Students in both classes:", class_a & class_b)

a = set(range(1, 11))
b = set(range(5, 16))
print("Q20","All elements:", a | b)
print("Q20","Common elements:", a & b)
print("Q20", "In first but not second:", a - b)

days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
print("Q21","First day:", days[0])
print("Q21","Last day:", days[-1])
print("Q21","Number of days:", len(days))
print("Q21","Saturday exists:", "Saturday" in days)

students = ("Ade", "Bola", "Chidi", "Dayo", "Emeka")
lst = list(students)
lst.append("Funke")
lst.append("Gozie")
lst.remove("Bola")
students = tuple(lst)
print("Q22",students)


with open("students.txt", "w") as f:
   f.write("Name: Ada\nAge: 20\nDepartment: Computer Science\n")
print("Q23","students.txt created.")


names = ["Ade", "Bola", "Chidi", "Dayo", "Emeka"]
with open("students.txt", "w") as f:  # "w" replaces previous content
for n in names:
     f.write(n + "\n")
print("Q24","students.txt overwritten with five names.")


with open("students.txt", "a") as f:  # "a" keeps previous content
for n in ["Funke", "Gozie", "Hauwa"]:
     f.write(n + "\n")
print("Q25","Three names appended.")


try:
with open("students.txt", "r") as f:
   print(f.read())
except FileNotFoundError:
print("Q26","students.txt not found. Run q23 first.")


sentences = ["Today was a good day.", "I learned about Python files.", "I wrote some code.", "I fixed a few bugs.", "Tomorrow I will practise more."]
with open("diary.txt", "w") as f:
for s in sentences:
f.write(s + "\n")
with open("diary.txt", "r") as f:
print("Q27:", f.read())

name = input("Enter your name: ")
language = input("Enter your favourite programming language: ")
with open("profile.txt", "a") as f:
f.write(f"{name} - {language}\n")
print("Q28","Saved to profile.txt.")


if not os.path.exists("numbers.txt"):  # create sample data if missing
with open("numbers.txt", "w") as f:
f.write("10\n20\n30\n40\n")
total = 0
with open("numbers.txt", "r") as f:
for line in f:
line = line.strip()
if line:
total += float(line)
print("Q29","Sum of numbers:", total)

    while True:
        print("\n1. Add student record\n2. View all records\n3. Count records\n4. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            name = input("Name: ")
            age = input("Age: ")
            score = input("Exam score: ")
            with open("records.txt", "a") as f:
                f.write(f"{name},{age},{score}\n")
            print("Record saved.")
        elif choice == "2":
            if os.path.exists("records.txt"):
                with open("records.txt", "r") as f:
                    for line in f:
                        name, age, score = line.strip().split(",")
                        print(f"Name: {name} | Age: {age} | Score: {score}")
            else:
                print("No records yet.")
        elif choice == "3":
            count = 0
            if os.path.exists("records.txt"):
                with open("records.txt", "r") as f:
                    count = sum(1 for line in f if line.strip())
            print("Total records:", count)
        elif choice == "4":
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    choice = input("Enter question number (1-30) or 'all': ").strip().lower()
    if choice == "all":
        for i in range(1, 31):
            print(f"\n--- Question {i} ---")
            globals()[f"q{i}"]()
    elif choice.isdigit() and 1 <= int(choice) <= 30:
        globals()[f"q{choice}"]()
    else:
        print("Invalid choice.")Name = "Moses"
Age = 19
Height = "6ft"
Status = "Student"

print("Q1",Name)
print("Q1",Age)
print("Q1",Height)
print("Q1",Status)

a, b = 10, 3
x, y = 4.5, 1.5
print("Q2","Addition:", a + b, x + y)
print("Q2","Subtraction:", a - b, x - y)
print("Q2","Multiplication:", a * b, x * y)
print("Q2","Division:", a / b, x / y)

Name = input("Enter your name: ")
Age = int(input("Enter your age: "))
colour = input("Enter your favourite colour: ")

print("Q3",f"My name is {Name}, I am {Age} years old and my favourite colour is {colour}.")

num = 10
num2 = 20.29
name = "Ada"
Value = True

print("Q4",num, type(num), num2, type(num2), (name, type(name), (Value, type(Value))))

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Q5","Sum:", a + b)
print("Q5","Product:", a * b)
print("Q5","Difference:", a - b)

name = "Chidi"
s1, s2, s3, s4, s5 = 70, 65, 80, 55, 90
status = "Passed"
total = s1 + s2 + s3 + s4 + s5
average = total / 5
print("Q6","Name:", name)
print("Q6","Scores:", s1, s2, s3, s4, s5)
print("Q6","Status:", status)
print("Q6","Total:", total)
print("Q6","Average:", average)

fruits = ["apple", "banana", "mango", "orange", "pear", "grape", "pineapple", "guava", "lemon", "papaya"]
print("Q7","First:", fruits[0])
print("Q7","Last:", fruits[-1])
print("Q7","Total items:", len(fruits))

students = ["Ade", "Bola", "Chidi", "Dayo", "Emeka"]
students.append(input("Enter another student's name: "))
print("Q8","Updated list:", students)

Number =[1,2,3,4,5,6,7,8,9,10]
print("Q9","Even numbers:", [n for n in Number if n % 2 == 0])

nums = [15, 8, 25, 40, 12, 30, 5, 18]
largest = nums[0]
smallest = nums[0]
total = 0
for n in nums:
  if n > largest:
        largest = n
  if n < smallest:
       smallest = n
total += n
print("Q10","Largest:", largest)
print("Q10","Smallest:", smallest)
print("Q10","Sum:", total)

shopping = ["bread", "milk", "eggs", "rice", "sugar"]
for _ in range(2):
shopping.append(input("Add a product: "))
item = input("Enter a product to remove: ")
if item in shopping:
  shopping.remove(item)
else:
print("Product not found.")
print("Q11","Final shopping list:", shopping)


numbers = [5, 12, 18, 23, 7, 30, 41, 9, 15, 2]
n = int(input("Enter a number: "))
if n in numbers:
print(f"{n} exists at position (index) {numbers.index(n)}")
else:
print("Q12", f"{n} is not in the list.")

student = {"name": "Ada", "age": 20, "gender": "Female","department": "Computer Science", "matric_no": "CSC/2024/001"}
for key, value in student.items():
print("Q13", f"{key}: {value}")

products = {"Bread": 800, "Milk": 1200, "Rice": 5000, "Eggs": 2500, "Sugar": 1500}
for name, price in products.items():
print("Q14", f"{name}: {price}")

student = {"name": "Ada", "age": 20, "score": 65}
student["score"] = int(input("Enter the new score: "))
print("Q15", "Updated information:", student)

scores = {"Ade": 67, "Bola": 82, "Chidi": 75, "Dayo": 90, "Emeka": 58}
top_name, top_score = None, -1
for name, score in scores.items():
if score > top_score:
top_name, top_score = name, score
print("Q16", f"Highest score: {top_name} with {top_score}")

account = {"account_name": "Ada Obi", "account_number": "1234567890", "balance": 10000.0}
choice = input("Type 'deposit' or 'withdraw': ").strip().lower()
amount = float(input("Enter amount: "))
if choice == "deposit":
account["balance"] += amount
elif choice == "withdraw":
if amount <= account["balance"]:
account["balance"] -= amount
else:
    print("Insufficient funds.")
else:
    print("Invalid choice.")
print("Q17","Current balance:", account["balance"])

numbers = {10, 20, 30, 10, 40, 20, 50, 30}
print("Q18",numbers)

class_a = {"Ade", "Bola", "Chidi", "Dayo"}
class_b = {"Chidi", "Emeka", "Dayo", "Funke"}
print("Q19","Students in both classes:", class_a & class_b)

a = set(range(1, 11))
b = set(range(5, 16))
print("Q20","All elements:", a | b)
print("Q20","Common elements:", a & b)
print("Q20", "In first but not second:", a - b)

days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
print("Q21","First day:", days[0])
print("Q21","Last day:", days[-1])
print("Q21","Number of days:", len(days))
print("Q21","Saturday exists:", "Saturday" in days)

students = ("Ade", "Bola", "Chidi", "Dayo", "Emeka")
lst = list(students)
lst.append("Funke")
lst.append("Gozie")
lst.remove("Bola")
students = tuple(lst)
print("Q22",students)


with open("students.txt", "w") as f:
   f.write("Name: Ada\nAge: 20\nDepartment: Computer Science\n")
print("Q23","students.txt created.")


names = ["Ade", "Bola", "Chidi", "Dayo", "Emeka"]
with open("students.txt", "w") as f:  # "w" replaces previous content
for n in names:
     f.write(n + "\n")
print("Q24","students.txt overwritten with five names.")


with open("students.txt", "a") as f:  # "a" keeps previous content
for n in ["Funke", "Gozie", "Hauwa"]:
     f.write(n + "\n")
print("Q25","Three names appended.")


try:
with open("students.txt", "r") as f:
   print(f.read())
except FileNotFoundError:
print("Q26","students.txt not found. Run q23 first.")


sentences = ["Today was a good day.", "I learned about Python files.", "I wrote some code.", "I fixed a few bugs.", "Tomorrow I will practise more."]
with open("diary.txt", "w") as f:
for s in sentences:
f.write(s + "\n")
with open("diary.txt", "r") as f:
print("Q27:", f.read())

name = input("Enter your name: ")
language = input("Enter your favourite programming language: ")
with open("profile.txt", "a") as f:
f.write(f"{name} - {language}\n")
print("Q28","Saved to profile.txt.")


if not os.path.exists("numbers.txt"):  # create sample data if missing
with open("numbers.txt", "w") as f:
f.write("10\n20\n30\n40\n")
total = 0
with open("numbers.txt", "r") as f:
for line in f:
line = line.strip()
if line:
total += float(line)
print("Q29","Sum of numbers:", total)

    while True:
        print("\n1. Add student record\n2. View all records\n3. Count records\n4. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            name = input("Name: ")
            age = input("Age: ")
            score = input("Exam score: ")
            with open("records.txt", "a") as f:
                f.write(f"{name},{age},{score}\n")
            print("Record saved.")
        elif choice == "2":
            if os.path.exists("records.txt"):
                with open("records.txt", "r") as f:
                    for line in f:
                        name, age, score = line.strip().split(",")
                        print(f"Name: {name} | Age: {age} | Score: {score}")
            else:
                print("No records yet.")
        elif choice == "3":
            count = 0
            if os.path.exists("records.txt"):
                with open("records.txt", "r") as f:
                    count = sum(1 for line in f if line.strip())
            print("Total records:", count)
        elif choice == "4":
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    choice = input("Enter question number (1-30) or 'all': ").strip().lower()
    if choice == "all":
        for i in range(1, 31):
            print(f"\n--- Question {i} ---")
            globals()[f"q{i}"]()
    elif choice.isdigit() and 1 <= int(choice) <= 30:
        globals()[f"q{choice}"]()
    else:
        print("Invalid choice.")Name = "Moses"
Age = 19
Height = "6ft"
Status = "Student"

print("Q1",Name)
print("Q1",Age)
print("Q1",Height)
print("Q1",Status)

a, b = 10, 3
x, y = 4.5, 1.5
print("Q2","Addition:", a + b, x + y)
print("Q2","Subtraction:", a - b, x - y)
print("Q2","Multiplication:", a * b, x * y)
print("Q2","Division:", a / b, x / y)

Name = input("Enter your name: ")
Age = int(input("Enter your age: "))
colour = input("Enter your favourite colour: ")

print("Q3",f"My name is {Name}, I am {Age} years old and my favourite colour is {colour}.")

num = 10
num2 = 20.29
name = "Ada"
Value = True

print("Q4",num, type(num), num2, type(num2), (name, type(name), (Value, type(Value))))

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Q5","Sum:", a + b)
print("Q5","Product:", a * b)
print("Q5","Difference:", a - b)

name = "Chidi"
s1, s2, s3, s4, s5 = 70, 65, 80, 55, 90
status = "Passed"
total = s1 + s2 + s3 + s4 + s5
average = total / 5
print("Q6","Name:", name)
print("Q6","Scores:", s1, s2, s3, s4, s5)
print("Q6","Status:", status)
print("Q6","Total:", total)
print("Q6","Average:", average)

fruits = ["apple", "banana", "mango", "orange", "pear", "grape", "pineapple", "guava", "lemon", "papaya"]
print("Q7","First:", fruits[0])
print("Q7","Last:", fruits[-1])
print("Q7","Total items:", len(fruits))

students = ["Ade", "Bola", "Chidi", "Dayo", "Emeka"]
students.append(input("Enter another student's name: "))
print("Q8","Updated list:", students)

Number =[1,2,3,4,5,6,7,8,9,10]
print("Q9","Even numbers:", [n for n in Number if n % 2 == 0])

nums = [15, 8, 25, 40, 12, 30, 5, 18]
largest = nums[0]
smallest = nums[0]
total = 0
for n in nums:
  if n > largest:
        largest = n
  if n < smallest:
       smallest = n
total += n
print("Q10","Largest:", largest)
print("Q10","Smallest:", smallest)
print("Q10","Sum:", total)

shopping = ["bread", "milk", "eggs", "rice", "sugar"]
for _ in range(2):
shopping.append(input("Add a product: "))
item = input("Enter a product to remove: ")
if item in shopping:
  shopping.remove(item)
else:
print("Product not found.")
print("Q11","Final shopping list:", shopping)


numbers = [5, 12, 18, 23, 7, 30, 41, 9, 15, 2]
n = int(input("Enter a number: "))
if n in numbers:
print(f"{n} exists at position (index) {numbers.index(n)}")
else:
print("Q12", f"{n} is not in the list.")

student = {"name": "Ada", "age": 20, "gender": "Female","department": "Computer Science", "matric_no": "CSC/2024/001"}
for key, value in student.items():
print("Q13", f"{key}: {value}")

products = {"Bread": 800, "Milk": 1200, "Rice": 5000, "Eggs": 2500, "Sugar": 1500}
for name, price in products.items():
print("Q14", f"{name}: {price}")

student = {"name": "Ada", "age": 20, "score": 65}
student["score"] = int(input("Enter the new score: "))
print("Q15", "Updated information:", student)

scores = {"Ade": 67, "Bola": 82, "Chidi": 75, "Dayo": 90, "Emeka": 58}
top_name, top_score = None, -1
for name, score in scores.items():
if score > top_score:
top_name, top_score = name, score
print("Q16", f"Highest score: {top_name} with {top_score}")

account = {"account_name": "Ada Obi", "account_number": "1234567890", "balance": 10000.0}
choice = input("Type 'deposit' or 'withdraw': ").strip().lower()
amount = float(input("Enter amount: "))
if choice == "deposit":
account["balance"] += amount
elif choice == "withdraw":
if amount <= account["balance"]:
account["balance"] -= amount
else:
    print("Insufficient funds.")
else:
    print("Invalid choice.")
print("Q17","Current balance:", account["balance"])

numbers = {10, 20, 30, 10, 40, 20, 50, 30}
print("Q18",numbers)

class_a = {"Ade", "Bola", "Chidi", "Dayo"}
class_b = {"Chidi", "Emeka", "Dayo", "Funke"}
print("Q19","Students in both classes:", class_a & class_b)

a = set(range(1, 11))
b = set(range(5, 16))
print("Q20","All elements:", a | b)
print("Q20","Common elements:", a & b)
print("Q20", "In first but not second:", a - b)

days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
print("Q21","First day:", days[0])
print("Q21","Last day:", days[-1])
print("Q21","Number of days:", len(days))
print("Q21","Saturday exists:", "Saturday" in days)

students = ("Ade", "Bola", "Chidi", "Dayo", "Emeka")
lst = list(students)
lst.append("Funke")
lst.append("Gozie")
lst.remove("Bola")
students = tuple(lst)
print("Q22",students)


with open("students.txt", "w") as f:
   f.write("Name: Ada\nAge: 20\nDepartment: Computer Science\n")
print("Q23","students.txt created.")


names = ["Ade", "Bola", "Chidi", "Dayo", "Emeka"]
with open("students.txt", "w") as f:  # "w" replaces previous content
for n in names:
     f.write(n + "\n")
print("Q24","students.txt overwritten with five names.")


with open("students.txt", "a") as f:  # "a" keeps previous content
for n in ["Funke", "Gozie", "Hauwa"]:
     f.write(n + "\n")
print("Q25","Three names appended.")


try:
with open("students.txt", "r") as f:
   print(f.read())
except FileNotFoundError:
print("Q26","students.txt not found. Run q23 first.")


sentences = ["Today was a good day.", "I learned about Python files.", "I wrote some code.", "I fixed a few bugs.", "Tomorrow I will practise more."]
with open("diary.txt", "w") as f:
for s in sentences:
f.write(s + "\n")
with open("diary.txt", "r") as f:
print("Q27:", f.read())

name = input("Enter your name: ")
language = input("Enter your favourite programming language: ")
with open("profile.txt", "a") as f:
f.write(f"{name} - {language}\n")
print("Q28","Saved to profile.txt.")


if not os.path.exists("numbers.txt"):  # create sample data if missing
with open("numbers.txt", "w") as f:
f.write("10\n20\n30\n40\n")
total = 0
with open("numbers.txt", "r") as f:
for line in f:
line = line.strip()
if line:
total += float(line)
print("Q29","Sum of numbers:", total)

    while True:
        print("\n1. Add student record\n2. View all records\n3. Count records\n4. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            name = input("Name: ")
            age = input("Age: ")
            score = input("Exam score: ")
            with open("records.txt", "a") as f:
                f.write(f"{name},{age},{score}\n")
            print("Record saved.")
        elif choice == "2":
            if os.path.exists("records.txt"):
                with open("records.txt", "r") as f:
                    for line in f:
                        name, age, score = line.strip().split(",")
                        print(f"Name: {name} | Age: {age} | Score: {score}")
            else:
                print("No records yet.")
        elif choice == "3":
            count = 0
            if os.path.exists("records.txt"):
                with open("records.txt", "r") as f:
                    count = sum(1 for line in f if line.strip())
            print("Total records:", count)
        elif choice == "4":
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    choice = input("Enter question number (1-30) or 'all': ").strip().lower()
    if choice == "all":
        for i in range(1, 31):
            print(f"\n--- Question {i} ---")
            globals()[f"q{i}"]()
    elif choice.isdigit() and 1 <= int(choice) <= 30:
        globals()[f"q{choice}"]()
    else:
        print("Invalid choice.")Name = "Moses"
Age = 19
Height = "6ft"
Status = "Student"

print("Q1",Name)
print("Q1",Age)
print("Q1",Height)
print("Q1",Status)

a, b = 10, 3
x, y = 4.5, 1.5
print("Q2","Addition:", a + b, x + y)
print("Q2","Subtraction:", a - b, x - y)
print("Q2","Multiplication:", a * b, x * y)
print("Q2","Division:", a / b, x / y)

Name = input("Enter your name: ")
Age = int(input("Enter your age: "))
colour = input("Enter your favourite colour: ")

print("Q3",f"My name is {Name}, I am {Age} years old and my favourite colour is {colour}.")

num = 10
num2 = 20.29
name = "Ada"
Value = True

print("Q4",num, type(num), num2, type(num2), (name, type(name), (Value, type(Value))))

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Q5","Sum:", a + b)
print("Q5","Product:", a * b)
print("Q5","Difference:", a - b)

name = "Chidi"
s1, s2, s3, s4, s5 = 70, 65, 80, 55, 90
status = "Passed"
total = s1 + s2 + s3 + s4 + s5
average = total / 5
print("Q6","Name:", name)
print("Q6","Scores:", s1, s2, s3, s4, s5)
print("Q6","Status:", status)
print("Q6","Total:", total)
print("Q6","Average:", average)

fruits = ["apple", "banana", "mango", "orange", "pear", "grape", "pineapple", "guava", "lemon", "papaya"]
print("Q7","First:", fruits[0])
print("Q7","Last:", fruits[-1])
print("Q7","Total items:", len(fruits))

students = ["Ade", "Bola", "Chidi", "Dayo", "Emeka"]
students.append(input("Enter another student's name: "))
print("Q8","Updated list:", students)

Number =[1,2,3,4,5,6,7,8,9,10]
print("Q9","Even numbers:", [n for n in Number if n % 2 == 0])

nums = [15, 8, 25, 40, 12, 30, 5, 18]
largest = nums[0]
smallest = nums[0]
total = 0
for n in nums:
  if n > largest:
        largest = n
  if n < smallest:
       smallest = n
total += n
print("Q10","Largest:", largest)
print("Q10","Smallest:", smallest)
print("Q10","Sum:", total)

shopping = ["bread", "milk", "eggs", "rice", "sugar"]
for _ in range(2):
shopping.append(input("Add a product: "))
item = input("Enter a product to remove: ")
if item in shopping:
  shopping.remove(item)
else:
print("Product not found.")
print("Q11","Final shopping list:", shopping)


numbers = [5, 12, 18, 23, 7, 30, 41, 9, 15, 2]
n = int(input("Enter a number: "))
if n in numbers:
print(f"{n} exists at position (index) {numbers.index(n)}")
else:
print("Q12", f"{n} is not in the list.")

student = {"name": "Ada", "age": 20, "gender": "Female","department": "Computer Science", "matric_no": "CSC/2024/001"}
for key, value in student.items():
print("Q13", f"{key}: {value}")

products = {"Bread": 800, "Milk": 1200, "Rice": 5000, "Eggs": 2500, "Sugar": 1500}
for name, price in products.items():
print("Q14", f"{name}: {price}")

student = {"name": "Ada", "age": 20, "score": 65}
student["score"] = int(input("Enter the new score: "))
print("Q15", "Updated information:", student)

scores = {"Ade": 67, "Bola": 82, "Chidi": 75, "Dayo": 90, "Emeka": 58}
top_name, top_score = None, -1
for name, score in scores.items():
if score > top_score:
top_name, top_score = name, score
print("Q16", f"Highest score: {top_name} with {top_score}")

account = {"account_name": "Ada Obi", "account_number": "1234567890", "balance": 10000.0}
choice = input("Type 'deposit' or 'withdraw': ").strip().lower()
amount = float(input("Enter amount: "))
if choice == "deposit":
account["balance"] += amount
elif choice == "withdraw":
if amount <= account["balance"]:
account["balance"] -= amount
else:
    print("Insufficient funds.")
else:
    print("Invalid choice.")
print("Q17","Current balance:", account["balance"])

numbers = {10, 20, 30, 10, 40, 20, 50, 30}
print("Q18",numbers)

class_a = {"Ade", "Bola", "Chidi", "Dayo"}
class_b = {"Chidi", "Emeka", "Dayo", "Funke"}
print("Q19","Students in both classes:", class_a & class_b)

a = set(range(1, 11))
b = set(range(5, 16))
print("Q20","All elements:", a | b)
print("Q20","Common elements:", a & b)
print("Q20", "In first but not second:", a - b)

days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
print("Q21","First day:", days[0])
print("Q21","Last day:", days[-1])
print("Q21","Number of days:", len(days))
print("Q21","Saturday exists:", "Saturday" in days)

students = ("Ade", "Bola", "Chidi", "Dayo", "Emeka")
lst = list(students)
lst.append("Funke")
lst.append("Gozie")
lst.remove("Bola")
students = tuple(lst)
print("Q22",students)


with open("students.txt", "w") as f:
   f.write("Name: Ada\nAge: 20\nDepartment: Computer Science\n")
print("Q23","students.txt created.")


names = ["Ade", "Bola", "Chidi", "Dayo", "Emeka"]
with open("students.txt", "w") as f:  # "w" replaces previous content
for n in names:
     f.write(n + "\n")
print("Q24","students.txt overwritten with five names.")


with open("students.txt", "a") as f:  # "a" keeps previous content
for n in ["Funke", "Gozie", "Hauwa"]:
     f.write(n + "\n")
print("Q25","Three names appended.")


try:
with open("students.txt", "r") as f:
   print(f.read())
except FileNotFoundError:
print("Q26","students.txt not found. Run q23 first.")


sentences = ["Today was a good day.", "I learned about Python files.", "I wrote some code.", "I fixed a few bugs.", "Tomorrow I will practise more."]
with open("diary.txt", "w") as f:
for s in sentences:
f.write(s + "\n")
with open("diary.txt", "r") as f:
print("Q27:", f.read())

name = input("Enter your name: ")
language = input("Enter your favourite programming language: ")
with open("profile.txt", "a") as f:
f.write(f"{name} - {language}\n")
print("Q28","Saved to profile.txt.")


if not os.path.exists("numbers.txt"):  # create sample data if missing
with open("numbers.txt", "w") as f:
f.write("10\n20\n30\n40\n")
total = 0
with open("numbers.txt", "r") as f:
for line in f:
line = line.strip()
if line:
total += float(line)
print("Q29","Sum of numbers:", total)

    while True:
        print("\n1. Add student record\n2. View all records\n3. Count records\n4. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            name = input("Name: ")
            age = input("Age: ")
            score = input("Exam score: ")
            with open("records.txt", "a") as f:
                f.write(f"{name},{age},{score}\n")
            print("Record saved.")
        elif choice == "2":
            if os.path.exists("records.txt"):
                with open("records.txt", "r") as f:
                    for line in f:
                        name, age, score = line.strip().split(",")
                        print(f"Name: {name} | Age: {age} | Score: {score}")
            else:
                print("No records yet.")
        elif choice == "3":
            count = 0
            if os.path.exists("records.txt"):
                with open("records.txt", "r") as f:
                    count = sum(1 for line in f if line.strip())
            print("Total records:", count)
        elif choice == "4":
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    choice = input("Enter question number (1-30) or 'all': ").strip().lower()
    if choice == "all":
        for i in range(1, 31):
            print(f"\n--- Question {i} ---")
            globals()[f"q{i}"]()
    elif choice.isdigit() and 1 <= int(choice) <= 30:
        globals()[f"q{choice}"]()
    else:
        print("Invalid choice.")Name = "Moses"
Age = 19
Height = "6ft"
Status = "Student"

print("Q1",Name)
print("Q1",Age)
print("Q1",Height)
print("Q1",Status)

a, b = 10, 3
x, y = 4.5, 1.5
print("Q2","Addition:", a + b, x + y)
print("Q2","Subtraction:", a - b, x - y)
print("Q2","Multiplication:", a * b, x * y)
print("Q2","Division:", a / b, x / y)

Name = input("Enter your name: ")
Age = int(input("Enter your age: "))
colour = input("Enter your favourite colour: ")

print("Q3",f"My name is {Name}, I am {Age} years old and my favourite colour is {colour}.")

num = 10
num2 = 20.29
name = "Ada"
Value = True

print("Q4",num, type(num), num2, type(num2), (name, type(name), (Value, type(Value))))

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Q5","Sum:", a + b)
print("Q5","Product:", a * b)
print("Q5","Difference:", a - b)

name = "Chidi"
s1, s2, s3, s4, s5 = 70, 65, 80, 55, 90
status = "Passed"
total = s1 + s2 + s3 + s4 + s5
average = total / 5
print("Q6","Name:", name)
print("Q6","Scores:", s1, s2, s3, s4, s5)
print("Q6","Status:", status)
print("Q6","Total:", total)
print("Q6","Average:", average)

fruits = ["apple", "banana", "mango", "orange", "pear", "grape", "pineapple", "guava", "lemon", "papaya"]
print("Q7","First:", fruits[0])
print("Q7","Last:", fruits[-1])
print("Q7","Total items:", len(fruits))

students = ["Ade", "Bola", "Chidi", "Dayo", "Emeka"]
students.append(input("Enter another student's name: "))
print("Q8","Updated list:", students)

Number =[1,2,3,4,5,6,7,8,9,10]
print("Q9","Even numbers:", [n for n in Number if n % 2 == 0])

nums = [15, 8, 25, 40, 12, 30, 5, 18]
largest = nums[0]
smallest = nums[0]
total = 0
for n in nums:
  if n > largest:
        largest = n
  if n < smallest:
       smallest = n
total += n
print("Q10","Largest:", largest)
print("Q10","Smallest:", smallest)
print("Q10","Sum:", total)

shopping = ["bread", "milk", "eggs", "rice", "sugar"]
for _ in range(2):
shopping.append(input("Add a product: "))
item = input("Enter a product to remove: ")
if item in shopping:
  shopping.remove(item)
else:
print("Product not found.")
print("Q11","Final shopping list:", shopping)


numbers = [5, 12, 18, 23, 7, 30, 41, 9, 15, 2]
n = int(input("Enter a number: "))
if n in numbers:
print(f"{n} exists at position (index) {numbers.index(n)}")
else:
print("Q12", f"{n} is not in the list.")

student = {"name": "Ada", "age": 20, "gender": "Female","department": "Computer Science", "matric_no": "CSC/2024/001"}
for key, value in student.items():
print("Q13", f"{key}: {value}")

products = {"Bread": 800, "Milk": 1200, "Rice": 5000, "Eggs": 2500, "Sugar": 1500}
for name, price in products.items():
print("Q14", f"{name}: {price}")

student = {"name": "Ada", "age": 20, "score": 65}
student["score"] = int(input("Enter the new score: "))
print("Q15", "Updated information:", student)

scores = {"Ade": 67, "Bola": 82, "Chidi": 75, "Dayo": 90, "Emeka": 58}
top_name, top_score = None, -1
for name, score in scores.items():
if score > top_score:
top_name, top_score = name, score
print("Q16", f"Highest score: {top_name} with {top_score}")

account = {"account_name": "Ada Obi", "account_number": "1234567890", "balance": 10000.0}
choice = input("Type 'deposit' or 'withdraw': ").strip().lower()
amount = float(input("Enter amount: "))
if choice == "deposit":
account["balance"] += amount
elif choice == "withdraw":
if amount <= account["balance"]:
account["balance"] -= amount
else:
    print("Insufficient funds.")
else:
    print("Invalid choice.")
print("Q17","Current balance:", account["balance"])

numbers = {10, 20, 30, 10, 40, 20, 50, 30}
print("Q18",numbers)

class_a = {"Ade", "Bola", "Chidi", "Dayo"}
class_b = {"Chidi", "Emeka", "Dayo", "Funke"}
print("Q19","Students in both classes:", class_a & class_b)

a = set(range(1, 11))
b = set(range(5, 16))
print("Q20","All elements:", a | b)
print("Q20","Common elements:", a & b)
print("Q20", "In first but not second:", a - b)

days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
print("Q21","First day:", days[0])
print("Q21","Last day:", days[-1])
print("Q21","Number of days:", len(days))
print("Q21","Saturday exists:", "Saturday" in days)

students = ("Ade", "Bola", "Chidi", "Dayo", "Emeka")
lst = list(students)
lst.append("Funke")
lst.append("Gozie")
lst.remove("Bola")
students = tuple(lst)
print("Q22",students)


with open("students.txt", "w") as f:
   f.write("Name: Ada\nAge: 20\nDepartment: Computer Science\n")
print("Q23","students.txt created.")


names = ["Ade", "Bola", "Chidi", "Dayo", "Emeka"]
with open("students.txt", "w") as f:  # "w" replaces previous content
for n in names:
     f.write(n + "\n")
print("Q24","students.txt overwritten with five names.")


with open("students.txt", "a") as f:  # "a" keeps previous content
for n in ["Funke", "Gozie", "Hauwa"]:
     f.write(n + "\n")
print("Q25","Three names appended.")


try:
with open("students.txt", "r") as f:
   print(f.read())
except FileNotFoundError:
print("Q26","students.txt not found. Run q23 first.")


sentences = ["Today was a good day.", "I learned about Python files.", "I wrote some code.", "I fixed a few bugs.", "Tomorrow I will practise more."]
with open("diary.txt", "w") as f:
for s in sentences:
f.write(s + "\n")
with open("diary.txt", "r") as f:
print("Q27:", f.read())

name = input("Enter your name: ")
language = input("Enter your favourite programming language: ")
with open("profile.txt", "a") as f:
f.write(f"{name} - {language}\n")
print("Q28","Saved to profile.txt.")


if not os.path.exists("numbers.txt"):  # create sample data if missing
with open("numbers.txt", "w") as f:
f.write("10\n20\n30\n40\n")
total = 0
with open("numbers.txt", "r") as f:
for line in f:
line = line.strip()
if line:
total += float(line)
print("Q29","Sum of numbers:", total)

    while True:
        print("\n1. Add student record\n2. View all records\n3. Count records\n4. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            name = input("Name: ")
            age = input("Age: ")
            score = input("Exam score: ")
            with open("records.txt", "a") as f:
                f.write(f"{name},{age},{score}\n")
            print("Record saved.")
        elif choice == "2":
            if os.path.exists("records.txt"):
                with open("records.txt", "r") as f:
                    for line in f:
                        name, age, score = line.strip().split(",")
                        print(f"Name: {name} | Age: {age} | Score: {score}")
            else:
                print("No records yet.")
        elif choice == "3":
            count = 0
            if os.path.exists("records.txt"):
                with open("records.txt", "r") as f:
                    count = sum(1 for line in f if line.strip())
            print("Total records:", count)
        elif choice == "4":
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    choice = input("Enter question number (1-30) or 'all': ").strip().lower()
    if choice == "all":
        for i in range(1, 31):
            print(f"\n--- Question {i} ---")
            globals()[f"q{i}"]()
    elif choice.isdigit() and 1 <= int(choice) <= 30:
        globals()[f"q{choice}"]()
    else:
        print("Invalid choice.")Name = "Moses"
Age = 19
Height = "6ft"
Status = "Student"

print("Q1",Name)
print("Q1",Age)
print("Q1",Height)
print("Q1",Status)

a, b = 10, 3
x, y = 4.5, 1.5
print("Q2","Addition:", a + b, x + y)
print("Q2","Subtraction:", a - b, x - y)
print("Q2","Multiplication:", a * b, x * y)
print("Q2","Division:", a / b, x / y)

Name = input("Enter your name: ")
Age = int(input("Enter your age: "))
colour = input("Enter your favourite colour: ")

print("Q3",f"My name is {Name}, I am {Age} years old and my favourite colour is {colour}.")

num = 10
num2 = 20.29
name = "Ada"
Value = True

print("Q4",num, type(num), num2, type(num2), (name, type(name), (Value, type(Value))))

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Q5","Sum:", a + b)
print("Q5","Product:", a * b)
print("Q5","Difference:", a - b)

name = "Chidi"
s1, s2, s3, s4, s5 = 70, 65, 80, 55, 90
status = "Passed"
total = s1 + s2 + s3 + s4 + s5
average = total / 5
print("Q6","Name:", name)
print("Q6","Scores:", s1, s2, s3, s4, s5)
print("Q6","Status:", status)
print("Q6","Total:", total)
print("Q6","Average:", average)

fruits = ["apple", "banana", "mango", "orange", "pear", "grape", "pineapple", "guava", "lemon", "papaya"]
print("Q7","First:", fruits[0])
print("Q7","Last:", fruits[-1])
print("Q7","Total items:", len(fruits))

students = ["Ade", "Bola", "Chidi", "Dayo", "Emeka"]
students.append(input("Enter another student's name: "))
print("Q8","Updated list:", students)

Number =[1,2,3,4,5,6,7,8,9,10]
print("Q9","Even numbers:", [n for n in Number if n % 2 == 0])

nums = [15, 8, 25, 40, 12, 30, 5, 18]
largest = nums[0]
smallest = nums[0]
total = 0
for n in nums:
  if n > largest:
        largest = n
  if n < smallest:
       smallest = n
total += n
print("Q10","Largest:", largest)
print("Q10","Smallest:", smallest)
print("Q10","Sum:", total)

shopping = ["bread", "milk", "eggs", "rice", "sugar"]
for _ in range(2):
shopping.append(input("Add a product: "))
item = input("Enter a product to remove: ")
if item in shopping:
  shopping.remove(item)
else:
print("Product not found.")
print("Q11","Final shopping list:", shopping)


numbers = [5, 12, 18, 23, 7, 30, 41, 9, 15, 2]
n = int(input("Enter a number: "))
if n in numbers:
print(f"{n} exists at position (index) {numbers.index(n)}")
else:
print("Q12", f"{n} is not in the list.")

student = {"name": "Ada", "age": 20, "gender": "Female","department": "Computer Science", "matric_no": "CSC/2024/001"}
for key, value in student.items():
print("Q13", f"{key}: {value}")

products = {"Bread": 800, "Milk": 1200, "Rice": 5000, "Eggs": 2500, "Sugar": 1500}
for name, price in products.items():
print("Q14", f"{name}: {price}")

student = {"name": "Ada", "age": 20, "score": 65}
student["score"] = int(input("Enter the new score: "))
print("Q15", "Updated information:", student)

scores = {"Ade": 67, "Bola": 82, "Chidi": 75, "Dayo": 90, "Emeka": 58}
top_name, top_score = None, -1
for name, score in scores.items():
if score > top_score:
top_name, top_score = name, score
print("Q16", f"Highest score: {top_name} with {top_score}")

account = {"account_name": "Ada Obi", "account_number": "1234567890", "balance": 10000.0}
choice = input("Type 'deposit' or 'withdraw': ").strip().lower()
amount = float(input("Enter amount: "))
if choice == "deposit":
account["balance"] += amount
elif choice == "withdraw":
if amount <= account["balance"]:
account["balance"] -= amount
else:
    print("Insufficient funds.")
else:
    print("Invalid choice.")
print("Q17","Current balance:", account["balance"])

numbers = {10, 20, 30, 10, 40, 20, 50, 30}
print("Q18",numbers)

class_a = {"Ade", "Bola", "Chidi", "Dayo"}
class_b = {"Chidi", "Emeka", "Dayo", "Funke"}
print("Q19","Students in both classes:", class_a & class_b)

a = set(range(1, 11))
b = set(range(5, 16))
print("Q20","All elements:", a | b)
print("Q20","Common elements:", a & b)
print("Q20", "In first but not second:", a - b)

days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
print("Q21","First day:", days[0])
print("Q21","Last day:", days[-1])
print("Q21","Number of days:", len(days))
print("Q21","Saturday exists:", "Saturday" in days)

students = ("Ade", "Bola", "Chidi", "Dayo", "Emeka")
lst = list(students)
lst.append("Funke")
lst.append("Gozie")
lst.remove("Bola")
students = tuple(lst)
print("Q22",students)


with open("students.txt", "w") as f:
   f.write("Name: Ada\nAge: 20\nDepartment: Computer Science\n")
print("Q23","students.txt created.")


names = ["Ade", "Bola", "Chidi", "Dayo", "Emeka"]
with open("students.txt", "w") as f:  # "w" replaces previous content
for n in names:
     f.write(n + "\n")
print("Q24","students.txt overwritten with five names.")


with open("students.txt", "a") as f:  # "a" keeps previous content
for n in ["Funke", "Gozie", "Hauwa"]:
     f.write(n + "\n")
print("Q25","Three names appended.")


try:
with open("students.txt", "r") as f:
   print(f.read())
except FileNotFoundError:
print("Q26","students.txt not found. Run q23 first.")


sentences = ["Today was a good day.", "I learned about Python files.", "I wrote some code.", "I fixed a few bugs.", "Tomorrow I will practise more."]
with open("diary.txt", "w") as f:
for s in sentences:
f.write(s + "\n")
with open("diary.txt", "r") as f:
print("Q27:", f.read())

name = input("Enter your name: ")
language = input("Enter your favourite programming language: ")
with open("profile.txt", "a") as f:
f.write(f"{name} - {language}\n")
print("Q28","Saved to profile.txt.")


if not os.path.exists("numbers.txt"):  # create sample data if missing
with open("numbers.txt", "w") as f:
f.write("10\n20\n30\n40\n")
total = 0
with open("numbers.txt", "r") as f:
for line in f:
line = line.strip()
if line:
total += float(line)
print("Q29","Sum of numbers:", total)

    while True:
        print("\n1. Add student record\n2. View all records\n3. Count records\n4. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            name = input("Name: ")
            age = input("Age: ")
            score = input("Exam score: ")
            with open("records.txt", "a") as f:
                f.write(f"{name},{age},{score}\n")
            print("Record saved.")
        elif choice == "2":
            if os.path.exists("records.txt"):
                with open("records.txt", "r") as f:
                    for line in f:
                        name, age, score = line.strip().split(",")
                        print(f"Name: {name} | Age: {age} | Score: {score}")
            else:
                print("No records yet.")
        elif choice == "3":
            count = 0
            if os.path.exists("records.txt"):
                with open("records.txt", "r") as f:
                    count = sum(1 for line in f if line.strip())
            print("Total records:", count)
        elif choice == "4":
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    choice = input("Enter question number (1-30) or 'all': ").strip().lower()
    if choice == "all":
        for i in range(1, 31):
            print(f"\n--- Question {i} ---")
            globals()[f"q{i}"]()
    elif choice.isdigit() and 1 <= int(choice) <= 30:
        globals()[f"q{choice}"]()
    else:
        print("Invalid choice.")Name = "Moses"
Age = 19
Height = "6ft"
Status = "Student"

print("Q1",Name)
print("Q1",Age)
print("Q1",Height)
print("Q1",Status)

a, b = 10, 3
x, y = 4.5, 1.5
print("Q2","Addition:", a + b, x + y)
print("Q2","Subtraction:", a - b, x - y)
print("Q2","Multiplication:", a * b, x * y)
print("Q2","Division:", a / b, x / y)

Name = input("Enter your name: ")
Age = int(input("Enter your age: "))
colour = input("Enter your favourite colour: ")

print("Q3",f"My name is {Name}, I am {Age} years old and my favourite colour is {colour}.")

num = 10
num2 = 20.29
name = "Ada"
Value = True

print("Q4",num, type(num), num2, type(num2), (name, type(name), (Value, type(Value))))

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Q5","Sum:", a + b)
print("Q5","Product:", a * b)
print("Q5","Difference:", a - b)

name = "Chidi"
s1, s2, s3, s4, s5 = 70, 65, 80, 55, 90
status = "Passed"
total = s1 + s2 + s3 + s4 + s5
average = total / 5
print("Q6","Name:", name)
print("Q6","Scores:", s1, s2, s3, s4, s5)
print("Q6","Status:", status)
print("Q6","Total:", total)
print("Q6","Average:", average)

fruits = ["apple", "banana", "mango", "orange", "pear", "grape", "pineapple", "guava", "lemon", "papaya"]
print("Q7","First:", fruits[0])
print("Q7","Last:", fruits[-1])
print("Q7","Total items:", len(fruits))

students = ["Ade", "Bola", "Chidi", "Dayo", "Emeka"]
students.append(input("Enter another student's name: "))
print("Q8","Updated list:", students)

Number =[1,2,3,4,5,6,7,8,9,10]
print("Q9","Even numbers:", [n for n in Number if n % 2 == 0])

nums = [15, 8, 25, 40, 12, 30, 5, 18]
largest = nums[0]
smallest = nums[0]
total = 0
for n in nums:
  if n > largest:
        largest = n
  if n < smallest:
       smallest = n
total += n
print("Q10","Largest:", largest)
print("Q10","Smallest:", smallest)
print("Q10","Sum:", total)

shopping = ["bread", "milk", "eggs", "rice", "sugar"]
for _ in range(2):
shopping.append(input("Add a product: "))
item = input("Enter a product to remove: ")
if item in shopping:
  shopping.remove(item)
else:
print("Product not found.")
print("Q11","Final shopping list:", shopping)


numbers = [5, 12, 18, 23, 7, 30, 41, 9, 15, 2]
n = int(input("Enter a number: "))
if n in numbers:
print(f"{n} exists at position (index) {numbers.index(n)}")
else:
print("Q12", f"{n} is not in the list.")

student = {"name": "Ada", "age": 20, "gender": "Female","department": "Computer Science", "matric_no": "CSC/2024/001"}
for key, value in student.items():
print("Q13", f"{key}: {value}")

products = {"Bread": 800, "Milk": 1200, "Rice": 5000, "Eggs": 2500, "Sugar": 1500}
for name, price in products.items():
print("Q14", f"{name}: {price}")

student = {"name": "Ada", "age": 20, "score": 65}
student["score"] = int(input("Enter the new score: "))
print("Q15", "Updated information:", student)

scores = {"Ade": 67, "Bola": 82, "Chidi": 75, "Dayo": 90, "Emeka": 58}
top_name, top_score = None, -1
for name, score in scores.items():
if score > top_score:
top_name, top_score = name, score
print("Q16", f"Highest score: {top_name} with {top_score}")

account = {"account_name": "Ada Obi", "account_number": "1234567890", "balance": 10000.0}
choice = input("Type 'deposit' or 'withdraw': ").strip().lower()
amount = float(input("Enter amount: "))
if choice == "deposit":
account["balance"] += amount
elif choice == "withdraw":
if amount <= account["balance"]:
account["balance"] -= amount
else:
    print("Insufficient funds.")
else:
    print("Invalid choice.")
print("Q17","Current balance:", account["balance"])

numbers = {10, 20, 30, 10, 40, 20, 50, 30}
print("Q18",numbers)

class_a = {"Ade", "Bola", "Chidi", "Dayo"}
class_b = {"Chidi", "Emeka", "Dayo", "Funke"}
print("Q19","Students in both classes:", class_a & class_b)

a = set(range(1, 11))
b = set(range(5, 16))
print("Q20","All elements:", a | b)
print("Q20","Common elements:", a & b)
print("Q20", "In first but not second:", a - b)

days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
print("Q21","First day:", days[0])
print("Q21","Last day:", days[-1])
print("Q21","Number of days:", len(days))
print("Q21","Saturday exists:", "Saturday" in days)

students = ("Ade", "Bola", "Chidi", "Dayo", "Emeka")
lst = list(students)
lst.append("Funke")
lst.append("Gozie")
lst.remove("Bola")
students = tuple(lst)
print("Q22",students)


with open("students.txt", "w") as f:
   f.write("Name: Ada\nAge: 20\nDepartment: Computer Science\n")
print("Q23","students.txt created.")


names = ["Ade", "Bola", "Chidi", "Dayo", "Emeka"]
with open("students.txt", "w") as f:  # "w" replaces previous content
for n in names:
     f.write(n + "\n")
print("Q24","students.txt overwritten with five names.")


with open("students.txt", "a") as f:  # "a" keeps previous content
for n in ["Funke", "Gozie", "Hauwa"]:
     f.write(n + "\n")
print("Q25","Three names appended.")


try:
with open("students.txt", "r") as f:
   print(f.read())
except FileNotFoundError:
print("Q26","students.txt not found. Run q23 first.")


sentences = ["Today was a good day.", "I learned about Python files.", "I wrote some code.", "I fixed a few bugs.", "Tomorrow I will practise more."]
with open("diary.txt", "w") as f:
for s in sentences:
f.write(s + "\n")
with open("diary.txt", "r") as f:
print("Q27:", f.read())

name = input("Enter your name: ")
language = input("Enter your favourite programming language: ")
with open("profile.txt", "a") as f:
f.write(f"{name} - {language}\n")
print("Q28","Saved to profile.txt.")


if not os.path.exists("numbers.txt"):  # create sample data if missing
with open("numbers.txt", "w") as f:
f.write("10\n20\n30\n40\n")
total = 0
with open("numbers.txt", "r") as f:
for line in f:
line = line.strip()
if line:
total += float(line)
print("Q29","Sum of numbers:", total)

    while True:
        print("\n1. Add student record\n2. View all records\n3. Count records\n4. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            name = input("Name: ")
            age = input("Age: ")
            score = input("Exam score: ")
            with open("records.txt", "a") as f:
                f.write(f"{name},{age},{score}\n")
            print("Record saved.")
        elif choice == "2":
            if os.path.exists("records.txt"):
                with open("records.txt", "r") as f:
                    for line in f:
                        name, age, score = line.strip().split(",")
                        print(f"Name: {name} | Age: {age} | Score: {score}")
            else:
                print("No records yet.")
        elif choice == "3":
            count = 0
            if os.path.exists("records.txt"):
                with open("records.txt", "r") as f:
                    count = sum(1 for line in f if line.strip())
            print("Total records:", count)
        elif choice == "4":
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    choice = input("Enter question number (1-30) or 'all': ").strip().lower()
    if choice == "all":
        for i in range(1, 31):
            print(f"\n--- Question {i} ---")
            globals()[f"q{i}"]()
    elif choice.isdigit() and 1 <= int(choice) <= 30:
        globals()[f"q{choice}"]()
    else:
        print("Invalid choice.")Name = "Moses"
Age = 19
Height = "6ft"
Status = "Student"

print("Q1",Name)
print("Q1",Age)
print("Q1",Height)
print("Q1",Status)

a, b = 10, 3
x, y = 4.5, 1.5
print("Q2","Addition:", a + b, x + y)
print("Q2","Subtraction:", a - b, x - y)
print("Q2","Multiplication:", a * b, x * y)
print("Q2","Division:", a / b, x / y)

Name = input("Enter your name: ")
Age = int(input("Enter your age: "))
colour = input("Enter your favourite colour: ")

print("Q3",f"My name is {Name}, I am {Age} years old and my favourite colour is {colour}.")

num = 10
num2 = 20.29
name = "Ada"
Value = True

print("Q4",num, type(num), num2, type(num2), (name, type(name), (Value, type(Value))))

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Q5","Sum:", a + b)
print("Q5","Product:", a * b)
print("Q5","Difference:", a - b)

name = "Chidi"
s1, s2, s3, s4, s5 = 70, 65, 80, 55, 90
status = "Passed"
total = s1 + s2 + s3 + s4 + s5
average = total / 5
print("Q6","Name:", name)
print("Q6","Scores:", s1, s2, s3, s4, s5)
print("Q6","Status:", status)
print("Q6","Total:", total)
print("Q6","Average:", average)

fruits = ["apple", "banana", "mango", "orange", "pear", "grape", "pineapple", "guava", "lemon", "papaya"]
print("Q7","First:", fruits[0])
print("Q7","Last:", fruits[-1])
print("Q7","Total items:", len(fruits))

students = ["Ade", "Bola", "Chidi", "Dayo", "Emeka"]
students.append(input("Enter another student's name: "))
print("Q8","Updated list:", students)

Number =[1,2,3,4,5,6,7,8,9,10]
print("Q9","Even numbers:", [n for n in Number if n % 2 == 0])

nums = [15, 8, 25, 40, 12, 30, 5, 18]
largest = nums[0]
smallest = nums[0]
total = 0
for n in nums:
  if n > largest:
        largest = n
  if n < smallest:
       smallest = n
total += n
print("Q10","Largest:", largest)
print("Q10","Smallest:", smallest)
print("Q10","Sum:", total)

shopping = ["bread", "milk", "eggs", "rice", "sugar"]
for _ in range(2):
shopping.append(input("Add a product: "))
item = input("Enter a product to remove: ")
if item in shopping:
  shopping.remove(item)
else:
print("Product not found.")
print("Q11","Final shopping list:", shopping)


numbers = [5, 12, 18, 23, 7, 30, 41, 9, 15, 2]
n = int(input("Enter a number: "))
if n in numbers:
print(f"{n} exists at position (index) {numbers.index(n)}")
else:
print("Q12", f"{n} is not in the list.")

student = {"name": "Ada", "age": 20, "gender": "Female","department": "Computer Science", "matric_no": "CSC/2024/001"}
for key, value in student.items():
print("Q13", f"{key}: {value}")

products = {"Bread": 800, "Milk": 1200, "Rice": 5000, "Eggs": 2500, "Sugar": 1500}
for name, price in products.items():
print("Q14", f"{name}: {price}")

student = {"name": "Ada", "age": 20, "score": 65}
student["score"] = int(input("Enter the new score: "))
print("Q15", "Updated information:", student)

scores = {"Ade": 67, "Bola": 82, "Chidi": 75, "Dayo": 90, "Emeka": 58}
top_name, top_score = None, -1
for name, score in scores.items():
if score > top_score:
top_name, top_score = name, score
print("Q16", f"Highest score: {top_name} with {top_score}")

account = {"account_name": "Ada Obi", "account_number": "1234567890", "balance": 10000.0}
choice = input("Type 'deposit' or 'withdraw': ").strip().lower()
amount = float(input("Enter amount: "))
if choice == "deposit":
account["balance"] += amount
elif choice == "withdraw":
if amount <= account["balance"]:
account["balance"] -= amount
else:
    print("Insufficient funds.")
else:
    print("Invalid choice.")
print("Q17","Current balance:", account["balance"])

numbers = {10, 20, 30, 10, 40, 20, 50, 30}
print("Q18",numbers)

class_a = {"Ade", "Bola", "Chidi", "Dayo"}
class_b = {"Chidi", "Emeka", "Dayo", "Funke"}
print("Q19","Students in both classes:", class_a & class_b)

a = set(range(1, 11))
b = set(range(5, 16))
print("Q20","All elements:", a | b)
print("Q20","Common elements:", a & b)
print("Q20", "In first but not second:", a - b)

days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
print("Q21","First day:", days[0])
print("Q21","Last day:", days[-1])
print("Q21","Number of days:", len(days))
print("Q21","Saturday exists:", "Saturday" in days)

students = ("Ade", "Bola", "Chidi", "Dayo", "Emeka")
lst = list(students)
lst.append("Funke")
lst.append("Gozie")
lst.remove("Bola")
students = tuple(lst)
print("Q22",students)


with open("students.txt", "w") as f:
   f.write("Name: Ada\nAge: 20\nDepartment: Computer Science\n")
print("Q23","students.txt created.")


names = ["Ade", "Bola", "Chidi", "Dayo", "Emeka"]
with open("students.txt", "w") as f:  # "w" replaces previous content
for n in names:
     f.write(n + "\n")
print("Q24","students.txt overwritten with five names.")


with open("students.txt", "a") as f:  # "a" keeps previous content
for n in ["Funke", "Gozie", "Hauwa"]:
     f.write(n + "\n")
print("Q25","Three names appended.")


try:
with open("students.txt", "r") as f:
   print(f.read())
except FileNotFoundError:
print("Q26","students.txt not found. Run q23 first.")


sentences = ["Today was a good day.", "I learned about Python files.", "I wrote some code.", "I fixed a few bugs.", "Tomorrow I will practise more."]
with open("diary.txt", "w") as f:
for s in sentences:
f.write(s + "\n")
with open("diary.txt", "r") as f:
print("Q27:", f.read())

name = input("Enter your name: ")
language = input("Enter your favourite programming language: ")
with open("profile.txt", "a") as f:
f.write(f"{name} - {language}\n")
print("Q28","Saved to profile.txt.")


if not os.path.exists("numbers.txt"):  # create sample data if missing
with open("numbers.txt", "w") as f:
f.write("10\n20\n30\n40\n")
total = 0
with open("numbers.txt", "r") as f:
for line in f:
line = line.strip()
if line:
total += float(line)
print("Q29","Sum of numbers:", total)

    while True:
        print("\n1. Add student record\n2. View all records\n3. Count records\n4. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            name = input("Name: ")
            age = input("Age: ")
            score = input("Exam score: ")
            with open("records.txt", "a") as f:
                f.write(f"{name},{age},{score}\n")
            print("Record saved.")
        elif choice == "2":
            if os.path.exists("records.txt"):
                with open("records.txt", "r") as f:
                    for line in f:
                        name, age, score = line.strip().split(",")
                        print(f"Name: {name} | Age: {age} | Score: {score}")
            else:
                print("No records yet.")
        elif choice == "3":
            count = 0
            if os.path.exists("records.txt"):
                with open("records.txt", "r") as f:
                    count = sum(1 for line in f if line.strip())
            print("Total records:", count)
        elif choice == "4":
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    choice = input("Enter question number (1-30) or 'all': ").strip().lower()
    if choice == "all":
        for i in range(1, 31):
            print(f"\n--- Question {i} ---")
            globals()[f"q{i}"]()
    elif choice.isdigit() and 1 <= int(choice) <= 30:
        globals()[f"q{choice}"]()
    else:
        print("Invalid choice.")Name = "Moses"
Age = 19
Height = "6ft"
Status = "Student"

print("Q1",Name)
print("Q1",Age)
print("Q1",Height)
print("Q1",Status)

a, b = 10, 3
x, y = 4.5, 1.5
print("Q2","Addition:", a + b, x + y)
print("Q2","Subtraction:", a - b, x - y)
print("Q2","Multiplication:", a * b, x * y)
print("Q2","Division:", a / b, x / y)

Name = input("Enter your name: ")
Age = int(input("Enter your age: "))
colour = input("Enter your favourite colour: ")

print("Q3",f"My name is {Name}, I am {Age} years old and my favourite colour is {colour}.")

num = 10
num2 = 20.29
name = "Ada"
Value = True

print("Q4",num, type(num), num2, type(num2), (name, type(name), (Value, type(Value))))

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Q5","Sum:", a + b)
print("Q5","Product:", a * b)
print("Q5","Difference:", a - b)

name = "Chidi"
s1, s2, s3, s4, s5 = 70, 65, 80, 55, 90
status = "Passed"
total = s1 + s2 + s3 + s4 + s5
average = total / 5
print("Q6","Name:", name)
print("Q6","Scores:", s1, s2, s3, s4, s5)
print("Q6","Status:", status)
print("Q6","Total:", total)
print("Q6","Average:", average)

fruits = ["apple", "banana", "mango", "orange", "pear", "grape", "pineapple", "guava", "lemon", "papaya"]
print("Q7","First:", fruits[0])
print("Q7","Last:", fruits[-1])
print("Q7","Total items:", len(fruits))

students = ["Ade", "Bola", "Chidi", "Dayo", "Emeka"]
students.append(input("Enter another student's name: "))
print("Q8","Updated list:", students)

Number =[1,2,3,4,5,6,7,8,9,10]
print("Q9","Even numbers:", [n for n in Number if n % 2 == 0])

nums = [15, 8, 25, 40, 12, 30, 5, 18]
largest = nums[0]
smallest = nums[0]
total = 0
for n in nums:
  if n > largest:
        largest = n
  if n < smallest:
       smallest = n
total += n
print("Q10","Largest:", largest)
print("Q10","Smallest:", smallest)
print("Q10","Sum:", total)

shopping = ["bread", "milk", "eggs", "rice", "sugar"]
for _ in range(2):
shopping.append(input("Add a product: "))
item = input("Enter a product to remove: ")
if item in shopping:
  shopping.remove(item)
else:
print("Product not found.")
print("Q11","Final shopping list:", shopping)


numbers = [5, 12, 18, 23, 7, 30, 41, 9, 15, 2]
n = int(input("Enter a number: "))
if n in numbers:
print(f"{n} exists at position (index) {numbers.index(n)}")
else:
print("Q12", f"{n} is not in the list.")

student = {"name": "Ada", "age": 20, "gender": "Female","department": "Computer Science", "matric_no": "CSC/2024/001"}
for key, value in student.items():
print("Q13", f"{key}: {value}")

products = {"Bread": 800, "Milk": 1200, "Rice": 5000, "Eggs": 2500, "Sugar": 1500}
for name, price in products.items():
print("Q14", f"{name}: {price}")

student = {"name": "Ada", "age": 20, "score": 65}
student["score"] = int(input("Enter the new score: "))
print("Q15", "Updated information:", student)

scores = {"Ade": 67, "Bola": 82, "Chidi": 75, "Dayo": 90, "Emeka": 58}
top_name, top_score = None, -1
for name, score in scores.items():
if score > top_score:
top_name, top_score = name, score
print("Q16", f"Highest score: {top_name} with {top_score}")

account = {"account_name": "Ada Obi", "account_number": "1234567890", "balance": 10000.0}
choice = input("Type 'deposit' or 'withdraw': ").strip().lower()
amount = float(input("Enter amount: "))
if choice == "deposit":
account["balance"] += amount
elif choice == "withdraw":
if amount <= account["balance"]:
account["balance"] -= amount
else:
    print("Insufficient funds.")
else:
    print("Invalid choice.")
print("Q17","Current balance:", account["balance"])

numbers = {10, 20, 30, 10, 40, 20, 50, 30}
print("Q18",numbers)

class_a = {"Ade", "Bola", "Chidi", "Dayo"}
class_b = {"Chidi", "Emeka", "Dayo", "Funke"}
print("Q19","Students in both classes:", class_a & class_b)

a = set(range(1, 11))
b = set(range(5, 16))
print("Q20","All elements:", a | b)
print("Q20","Common elements:", a & b)
print("Q20", "In first but not second:", a - b)

days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
print("Q21","First day:", days[0])
print("Q21","Last day:", days[-1])
print("Q21","Number of days:", len(days))
print("Q21","Saturday exists:", "Saturday" in days)

students = ("Ade", "Bola", "Chidi", "Dayo", "Emeka")
lst = list(students)
lst.append("Funke")
lst.append("Gozie")
lst.remove("Bola")
students = tuple(lst)
print("Q22",students)


with open("students.txt", "w") as f:
   f.write("Name: Ada\nAge: 20\nDepartment: Computer Science\n")
print("Q23","students.txt created.")


names = ["Ade", "Bola", "Chidi", "Dayo", "Emeka"]
with open("students.txt", "w") as f:  # "w" replaces previous content
for n in names:
     f.write(n + "\n")
print("Q24","students.txt overwritten with five names.")


with open("students.txt", "a") as f:  # "a" keeps previous content
for n in ["Funke", "Gozie", "Hauwa"]:
     f.write(n + "\n")
print("Q25","Three names appended.")


try:
with open("students.txt", "r") as f:
   print(f.read())
except FileNotFoundError:
print("Q26","students.txt not found. Run q23 first.")


sentences = ["Today was a good day.", "I learned about Python files.", "I wrote some code.", "I fixed a few bugs.", "Tomorrow I will practise more."]
with open("diary.txt", "w") as f:
for s in sentences:
f.write(s + "\n")
with open("diary.txt", "r") as f:
print("Q27:", f.read())

name = input("Enter your name: ")
language = input("Enter your favourite programming language: ")
with open("profile.txt", "a") as f:
f.write(f"{name} - {language}\n")
print("Q28","Saved to profile.txt.")


if not os.path.exists("numbers.txt"):  # create sample data if missing
with open("numbers.txt", "w") as f:
f.write("10\n20\n30\n40\n")
total = 0
with open("numbers.txt", "r") as f:
for line in f:
line = line.strip()
if line:
total += float(line)
print("Q29","Sum of numbers:", total)

    while True:
        print("\n1. Add student record\n2. View all records\n3. Count records\n4. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            name = input("Name: ")
            age = input("Age: ")
            score = input("Exam score: ")
            with open("records.txt", "a") as f:
                f.write(f"{name},{age},{score}\n")
            print("Record saved.")
        elif choice == "2":
            if os.path.exists("records.txt"):
                with open("records.txt", "r") as f:
                    for line in f:
                        name, age, score = line.strip().split(",")
                        print(f"Name: {name} | Age: {age} | Score: {score}")
            else:
                print("No records yet.")
        elif choice == "3":
            count = 0
            if os.path.exists("records.txt"):
                with open("records.txt", "r") as f:
                    count = sum(1 for line in f if line.strip())
            print("Total records:", count)
        elif choice == "4":
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    choice = input("Enter question number (1-30) or 'all': ").strip().lower()
    if choice == "all":
        for i in range(1, 31):
            print(f"\n--- Question {i} ---")
            globals()[f"q{i}"]()
    elif choice.isdigit() and 1 <= int(choice) <= 30:
        globals()[f"q{choice}"]()
    else:
        print("Invalid choice.")Name = "Moses"
Age = 19
Height = "6ft"
Status = "Student"

print("Q1",Name)
print("Q1",Age)
print("Q1",Height)
print("Q1",Status)

a, b = 10, 3
x, y = 4.5, 1.5
print("Q2","Addition:", a + b, x + y)
print("Q2","Subtraction:", a - b, x - y)
print("Q2","Multiplication:", a * b, x * y)
print("Q2","Division:", a / b, x / y)

Name = input("Enter your name: ")
Age = int(input("Enter your age: "))
colour = input("Enter your favourite colour: ")

print("Q3",f"My name is {Name}, I am {Age} years old and my favourite colour is {colour}.")

num = 10
num2 = 20.29
name = "Ada"
Value = True

print("Q4",num, type(num), num2, type(num2), (name, type(name), (Value, type(Value))))

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Q5","Sum:", a + b)
print("Q5","Product:", a * b)
print("Q5","Difference:", a - b)

name = "Chidi"
s1, s2, s3, s4, s5 = 70, 65, 80, 55, 90
status = "Passed"
total = s1 + s2 + s3 + s4 + s5
average = total / 5
print("Q6","Name:", name)
print("Q6","Scores:", s1, s2, s3, s4, s5)
print("Q6","Status:", status)
print("Q6","Total:", total)
print("Q6","Average:", average)

fruits = ["apple", "banana", "mango", "orange", "pear", "grape", "pineapple", "guava", "lemon", "papaya"]
print("Q7","First:", fruits[0])
print("Q7","Last:", fruits[-1])
print("Q7","Total items:", len(fruits))

students = ["Ade", "Bola", "Chidi", "Dayo", "Emeka"]
students.append(input("Enter another student's name: "))
print("Q8","Updated list:", students)

Number =[1,2,3,4,5,6,7,8,9,10]
print("Q9","Even numbers:", [n for n in Number if n % 2 == 0])

nums = [15, 8, 25, 40, 12, 30, 5, 18]
largest = nums[0]
smallest = nums[0]
total = 0
for n in nums:
  if n > largest:
        largest = n
  if n < smallest:
       smallest = n
total += n
print("Q10","Largest:", largest)
print("Q10","Smallest:", smallest)
print("Q10","Sum:", total)

shopping = ["bread", "milk", "eggs", "rice", "sugar"]
for _ in range(2):
shopping.append(input("Add a product: "))
item = input("Enter a product to remove: ")
if item in shopping:
  shopping.remove(item)
else:
print("Product not found.")
print("Q11","Final shopping list:", shopping)


numbers = [5, 12, 18, 23, 7, 30, 41, 9, 15, 2]
n = int(input("Enter a number: "))
if n in numbers:
print(f"{n} exists at position (index) {numbers.index(n)}")
else:
print("Q12", f"{n} is not in the list.")

student = {"name": "Ada", "age": 20, "gender": "Female","department": "Computer Science", "matric_no": "CSC/2024/001"}
for key, value in student.items():
print("Q13", f"{key}: {value}")

products = {"Bread": 800, "Milk": 1200, "Rice": 5000, "Eggs": 2500, "Sugar": 1500}
for name, price in products.items():
print("Q14", f"{name}: {price}")

student = {"name": "Ada", "age": 20, "score": 65}
student["score"] = int(input("Enter the new score: "))
print("Q15", "Updated information:", student)

scores = {"Ade": 67, "Bola": 82, "Chidi": 75, "Dayo": 90, "Emeka": 58}
top_name, top_score = None, -1
for name, score in scores.items():
if score > top_score:
top_name, top_score = name, score
print("Q16", f"Highest score: {top_name} with {top_score}")

account = {"account_name": "Ada Obi", "account_number": "1234567890", "balance": 10000.0}
choice = input("Type 'deposit' or 'withdraw': ").strip().lower()
amount = float(input("Enter amount: "))
if choice == "deposit":
account["balance"] += amount
elif choice == "withdraw":
if amount <= account["balance"]:
account["balance"] -= amount
else:
    print("Insufficient funds.")
else:
    print("Invalid choice.")
print("Q17","Current balance:", account["balance"])

numbers = {10, 20, 30, 10, 40, 20, 50, 30}
print("Q18",numbers)

class_a = {"Ade", "Bola", "Chidi", "Dayo"}
class_b = {"Chidi", "Emeka", "Dayo", "Funke"}
print("Q19","Students in both classes:", class_a & class_b)

a = set(range(1, 11))
b = set(range(5, 16))
print("Q20","All elements:", a | b)
print("Q20","Common elements:", a & b)
print("Q20", "In first but not second:", a - b)

days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
print("Q21","First day:", days[0])
print("Q21","Last day:", days[-1])
print("Q21","Number of days:", len(days))
print("Q21","Saturday exists:", "Saturday" in days)

students = ("Ade", "Bola", "Chidi", "Dayo", "Emeka")
lst = list(students)
lst.append("Funke")
lst.append("Gozie")
lst.remove("Bola")
students = tuple(lst)
print("Q22",students)


with open("students.txt", "w") as f:
   f.write("Name: Ada\nAge: 20\nDepartment: Computer Science\n")
print("Q23","students.txt created.")


names = ["Ade", "Bola", "Chidi", "Dayo", "Emeka"]
with open("students.txt", "w") as f:  # "w" replaces previous content
for n in names:
     f.write(n + "\n")
print("Q24","students.txt overwritten with five names.")


with open("students.txt", "a") as f:  # "a" keeps previous content
for n in ["Funke", "Gozie", "Hauwa"]:
     f.write(n + "\n")
print("Q25","Three names appended.")


try:
with open("students.txt", "r") as f:
   print(f.read())
except FileNotFoundError:
print("Q26","students.txt not found. Run q23 first.")


sentences = ["Today was a good day.", "I learned about Python files.", "I wrote some code.", "I fixed a few bugs.", "Tomorrow I will practise more."]
with open("diary.txt", "w") as f:
for s in sentences:
f.write(s + "\n")
with open("diary.txt", "r") as f:
print("Q27:", f.read())

name = input("Enter your name: ")
language = input("Enter your favourite programming language: ")
with open("profile.txt", "a") as f:
f.write(f"{name} - {language}\n")
print("Q28","Saved to profile.txt.")


if not os.path.exists("numbers.txt"):  # create sample data if missing
with open("numbers.txt", "w") as f:
f.write("10\n20\n30\n40\n")
total = 0
with open("numbers.txt", "r") as f:
for line in f:
line = line.strip()
if line:
total += float(line)
print("Q29","Sum of numbers:", total)

    while True:
        print("\n1. Add student record\n2. View all records\n3. Count records\n4. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            name = input("Name: ")
            age = input("Age: ")
            score = input("Exam score: ")
            with open("records.txt", "a") as f:
                f.write(f"{name},{age},{score}\n")
            print("Record saved.")
        elif choice == "2":
            if os.path.exists("records.txt"):
                with open("records.txt", "r") as f:
                    for line in f:
                        name, age, score = line.strip().split(",")
                        print(f"Name: {name} | Age: {age} | Score: {score}")
            else:
                print("No records yet.")
        elif choice == "3":
            count = 0
            if os.path.exists("records.txt"):
                with open("records.txt", "r") as f:
                    count = sum(1 for line in f if line.strip())
            print("Total records:", count)
        elif choice == "4":
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    choice = input("Enter question number (1-30) or 'all': ").strip().lower()
    if choice == "all":
        for i in range(1, 31):
            print(f"\n--- Question {i} ---")
            globals()[f"q{i}"]()
    elif choice.isdigit() and 1 <= int(choice) <= 30:
        globals()[f"q{choice}"]()
    else:
        print("Invalid choice.")Name = "Moses"
Age = 19
Height = "6ft"
Status = "Student"

print("Q1",Name)
print("Q1",Age)
print("Q1",Height)
print("Q1",Status)

a, b = 10, 3
x, y = 4.5, 1.5
print("Q2","Addition:", a + b, x + y)
print("Q2","Subtraction:", a - b, x - y)
print("Q2","Multiplication:", a * b, x * y)
print("Q2","Division:", a / b, x / y)

Name = input("Enter your name: ")
Age = int(input("Enter your age: "))
colour = input("Enter your favourite colour: ")

print("Q3",f"My name is {Name}, I am {Age} years old and my favourite colour is {colour}.")

num = 10
num2 = 20.29
name = "Ada"
Value = True

print("Q4",num, type(num), num2, type(num2), (name, type(name), (Value, type(Value))))

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Q5","Sum:", a + b)
print("Q5","Product:", a * b)
print("Q5","Difference:", a - b)

name = "Chidi"
s1, s2, s3, s4, s5 = 70, 65, 80, 55, 90
status = "Passed"
total = s1 + s2 + s3 + s4 + s5
average = total / 5
print("Q6","Name:", name)
print("Q6","Scores:", s1, s2, s3, s4, s5)
print("Q6","Status:", status)
print("Q6","Total:", total)
print("Q6","Average:", average)

fruits = ["apple", "banana", "mango", "orange", "pear", "grape", "pineapple", "guava", "lemon", "papaya"]
print("Q7","First:", fruits[0])
print("Q7","Last:", fruits[-1])
print("Q7","Total items:", len(fruits))

students = ["Ade", "Bola", "Chidi", "Dayo", "Emeka"]
students.append(input("Enter another student's name: "))
print("Q8","Updated list:", students)

Number =[1,2,3,4,5,6,7,8,9,10]
print("Q9","Even numbers:", [n for n in Number if n % 2 == 0])

nums = [15, 8, 25, 40, 12, 30, 5, 18]
largest = nums[0]
smallest = nums[0]
total = 0
for n in nums:
  if n > largest:
        largest = n
  if n < smallest:
       smallest = n
total += n
print("Q10","Largest:", largest)
print("Q10","Smallest:", smallest)
print("Q10","Sum:", total)

shopping = ["bread", "milk", "eggs", "rice", "sugar"]
for _ in range(2):
shopping.append(input("Add a product: "))
item = input("Enter a product to remove: ")
if item in shopping:
  shopping.remove(item)
else:
print("Product not found.")
print("Q11","Final shopping list:", shopping)


numbers = [5, 12, 18, 23, 7, 30, 41, 9, 15, 2]
n = int(input("Enter a number: "))
if n in numbers:
print(f"{n} exists at position (index) {numbers.index(n)}")
else:
print("Q12", f"{n} is not in the list.")

student = {"name": "Ada", "age": 20, "gender": "Female","department": "Computer Science", "matric_no": "CSC/2024/001"}
for key, value in student.items():
print("Q13", f"{key}: {value}")

products = {"Bread": 800, "Milk": 1200, "Rice": 5000, "Eggs": 2500, "Sugar": 1500}
for name, price in products.items():
print("Q14", f"{name}: {price}")

student = {"name": "Ada", "age": 20, "score": 65}
student["score"] = int(input("Enter the new score: "))
print("Q15", "Updated information:", student)

scores = {"Ade": 67, "Bola": 82, "Chidi": 75, "Dayo": 90, "Emeka": 58}
top_name, top_score = None, -1
for name, score in scores.items():
if score > top_score:
top_name, top_score = name, score
print("Q16", f"Highest score: {top_name} with {top_score}")

account = {"account_name": "Ada Obi", "account_number": "1234567890", "balance": 10000.0}
choice = input("Type 'deposit' or 'withdraw': ").strip().lower()
amount = float(input("Enter amount: "))
if choice == "deposit":
account["balance"] += amount
elif choice == "withdraw":
if amount <= account["balance"]:
account["balance"] -= amount
else:
    print("Insufficient funds.")
else:
    print("Invalid choice.")
print("Q17","Current balance:", account["balance"])

numbers = {10, 20, 30, 10, 40, 20, 50, 30}
print("Q18",numbers)

class_a = {"Ade", "Bola", "Chidi", "Dayo"}
class_b = {"Chidi", "Emeka", "Dayo", "Funke"}
print("Q19","Students in both classes:", class_a & class_b)

a = set(range(1, 11))
b = set(range(5, 16))
print("Q20","All elements:", a | b)
print("Q20","Common elements:", a & b)
print("Q20", "In first but not second:", a - b)

days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
print("Q21","First day:", days[0])
print("Q21","Last day:", days[-1])
print("Q21","Number of days:", len(days))
print("Q21","Saturday exists:", "Saturday" in days)

students = ("Ade", "Bola", "Chidi", "Dayo", "Emeka")
lst = list(students)
lst.append("Funke")
lst.append("Gozie")
lst.remove("Bola")
students = tuple(lst)
print("Q22",students)


with open("students.txt", "w") as f:
   f.write("Name: Ada\nAge: 20\nDepartment: Computer Science\n")
print("Q23","students.txt created.")


names = ["Ade", "Bola", "Chidi", "Dayo", "Emeka"]
with open("students.txt", "w") as f:  # "w" replaces previous content
for n in names:
     f.write(n + "\n")
print("Q24","students.txt overwritten with five names.")


with open("students.txt", "a") as f:  # "a" keeps previous content
for n in ["Funke", "Gozie", "Hauwa"]:
     f.write(n + "\n")
print("Q25","Three names appended.")


try:
with open("students.txt", "r") as f:
   print(f.read())
except FileNotFoundError:
print("Q26","students.txt not found. Run q23 first.")


sentences = ["Today was a good day.", "I learned about Python files.", "I wrote some code.", "I fixed a few bugs.", "Tomorrow I will practise more."]
with open("diary.txt", "w") as f:
for s in sentences:
f.write(s + "\n")
with open("diary.txt", "r") as f:
print("Q27:", f.read())

name = input("Enter your name: ")
language = input("Enter your favourite programming language: ")
with open("profile.txt", "a") as f:
f.write(f"{name} - {language}\n")
print("Q28","Saved to profile.txt.")


if not os.path.exists("numbers.txt"):  # create sample data if missing
with open("numbers.txt", "w") as f:
f.write("10\n20\n30\n40\n")
total = 0
with open("numbers.txt", "r") as f:
for line in f:
line = line.strip()
if line:
total += float(line)
print("Q29","Sum of numbers:", total)

    while True:
        print("\n1. Add student record\n2. View all records\n3. Count records\n4. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            name = input("Name: ")
            age = input("Age: ")
            score = input("Exam score: ")
            with open("records.txt", "a") as f:
                f.write(f"{name},{age},{score}\n")
            print("Record saved.")
        elif choice == "2":
            if os.path.exists("records.txt"):
                with open("records.txt", "r") as f:
                    for line in f:
                        name, age, score = line.strip().split(",")
                        print(f"Name: {name} | Age: {age} | Score: {score}")
            else:
                print("No records yet.")
        elif choice == "3":
            count = 0
            if os.path.exists("records.txt"):
                with open("records.txt", "r") as f:
                    count = sum(1 for line in f if line.strip())
            print("Total records:", count)
        elif choice == "4":
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    choice = input("Enter question number (1-30) or 'all': ").strip().lower()
    if choice == "all":
        for i in range(1, 31):
            print(f"\n--- Question {i} ---")
            globals()[f"q{i}"]()
    elif choice.isdigit() and 1 <= int(choice) <= 30:
        globals()[f"q{choice}"]()
    else:
        print("Invalid choice.")Name = "Moses"
Age = 19
Height = "6ft"
Status = "Student"

print("Q1",Name)
print("Q1",Age)
print("Q1",Height)
print("Q1",Status)

a, b = 10, 3
x, y = 4.5, 1.5
print("Q2","Addition:", a + b, x + y)
print("Q2","Subtraction:", a - b, x - y)
print("Q2","Multiplication:", a * b, x * y)
print("Q2","Division:", a / b, x / y)

Name = input("Enter your name: ")
Age = int(input("Enter your age: "))
colour = input("Enter your favourite colour: ")

print("Q3",f"My name is {Name}, I am {Age} years old and my favourite colour is {colour}.")

num = 10
num2 = 20.29
name = "Ada"
Value = True

print("Q4",num, type(num), num2, type(num2), (name, type(name), (Value, type(Value))))

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Q5","Sum:", a + b)
print("Q5","Product:", a * b)
print("Q5","Difference:", a - b)

name = "Chidi"
s1, s2, s3, s4, s5 = 70, 65, 80, 55, 90
status = "Passed"
total = s1 + s2 + s3 + s4 + s5
average = total / 5
print("Q6","Name:", name)
print("Q6","Scores:", s1, s2, s3, s4, s5)
print("Q6","Status:", status)
print("Q6","Total:", total)
print("Q6","Average:", average)

fruits = ["apple", "banana", "mango", "orange", "pear", "grape", "pineapple", "guava", "lemon", "papaya"]
print("Q7","First:", fruits[0])
print("Q7","Last:", fruits[-1])
print("Q7","Total items:", len(fruits))

students = ["Ade", "Bola", "Chidi", "Dayo", "Emeka"]
students.append(input("Enter another student's name: "))
print("Q8","Updated list:", students)

Number =[1,2,3,4,5,6,7,8,9,10]
print("Q9","Even numbers:", [n for n in Number if n % 2 == 0])

nums = [15, 8, 25, 40, 12, 30, 5, 18]
largest = nums[0]
smallest = nums[0]
total = 0
for n in nums:
  if n > largest:
        largest = n
  if n < smallest:
       smallest = n
total += n
print("Q10","Largest:", largest)
print("Q10","Smallest:", smallest)
print("Q10","Sum:", total)

shopping = ["bread", "milk", "eggs", "rice", "sugar"]
for _ in range(2):
shopping.append(input("Add a product: "))
item = input("Enter a product to remove: ")
if item in shopping:
  shopping.remove(item)
else:
print("Product not found.")
print("Q11","Final shopping list:", shopping)


numbers = [5, 12, 18, 23, 7, 30, 41, 9, 15, 2]
n = int(input("Enter a number: "))
if n in numbers:
print(f"{n} exists at position (index) {numbers.index(n)}")
else:
print("Q12", f"{n} is not in the list.")

student = {"name": "Ada", "age": 20, "gender": "Female","department": "Computer Science", "matric_no": "CSC/2024/001"}
for key, value in student.items():
print("Q13", f"{key}: {value}")

products = {"Bread": 800, "Milk": 1200, "Rice": 5000, "Eggs": 2500, "Sugar": 1500}
for name, price in products.items():
print("Q14", f"{name}: {price}")

student = {"name": "Ada", "age": 20, "score": 65}
student["score"] = int(input("Enter the new score: "))
print("Q15", "Updated information:", student)

scores = {"Ade": 67, "Bola": 82, "Chidi": 75, "Dayo": 90, "Emeka": 58}
top_name, top_score = None, -1
for name, score in scores.items():
if score > top_score:
top_name, top_score = name, score
print("Q16", f"Highest score: {top_name} with {top_score}")

account = {"account_name": "Ada Obi", "account_number": "1234567890", "balance": 10000.0}
choice = input("Type 'deposit' or 'withdraw': ").strip().lower()
amount = float(input("Enter amount: "))
if choice == "deposit":
account["balance"] += amount
elif choice == "withdraw":
if amount <= account["balance"]:
account["balance"] -= amount
else:
    print("Insufficient funds.")
else:
    print("Invalid choice.")
print("Q17","Current balance:", account["balance"])

numbers = {10, 20, 30, 10, 40, 20, 50, 30}
print("Q18",numbers)

class_a = {"Ade", "Bola", "Chidi", "Dayo"}
class_b = {"Chidi", "Emeka", "Dayo", "Funke"}
print("Q19","Students in both classes:", class_a & class_b)

a = set(range(1, 11))
b = set(range(5, 16))
print("Q20","All elements:", a | b)
print("Q20","Common elements:", a & b)
print("Q20", "In first but not second:", a - b)

days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
print("Q21","First day:", days[0])
print("Q21","Last day:", days[-1])
print("Q21","Number of days:", len(days))
print("Q21","Saturday exists:", "Saturday" in days)

students = ("Ade", "Bola", "Chidi", "Dayo", "Emeka")
lst = list(students)
lst.append("Funke")
lst.append("Gozie")
lst.remove("Bola")
students = tuple(lst)
print("Q22",students)


with open("students.txt", "w") as f:
   f.write("Name: Ada\nAge: 20\nDepartment: Computer Science\n")
print("Q23","students.txt created.")


names = ["Ade", "Bola", "Chidi", "Dayo", "Emeka"]
with open("students.txt", "w") as f:  # "w" replaces previous content
for n in names:
     f.write(n + "\n")
print("Q24","students.txt overwritten with five names.")


with open("students.txt", "a") as f:  # "a" keeps previous content
for n in ["Funke", "Gozie", "Hauwa"]:
     f.write(n + "\n")
print("Q25","Three names appended.")


try:
with open("students.txt", "r") as f:
   print(f.read())
except FileNotFoundError:
print("Q26","students.txt not found. Run q23 first.")


sentences = ["Today was a good day.", "I learned about Python files.", "I wrote some code.", "I fixed a few bugs.", "Tomorrow I will practise more."]
with open("diary.txt", "w") as f:
for s in sentences:
f.write(s + "\n")
with open("diary.txt", "r") as f:
print("Q27:", f.read())

name = input("Enter your name: ")
language = input("Enter your favourite programming language: ")
with open("profile.txt", "a") as f:
f.write(f"{name} - {language}\n")
print("Q28","Saved to profile.txt.")


if not os.path.exists("numbers.txt"):  # create sample data if missing
with open("numbers.txt", "w") as f:
f.write("10\n20\n30\n40\n")
total = 0
with open("numbers.txt", "r") as f:
for line in f:
line = line.strip()
if line:
total += float(line)
print("Q29","Sum of numbers:", total)

    while True:
        print("\n1. Add student record\n2. View all records\n3. Count records\n4. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            name = input("Name: ")
            age = input("Age: ")
            score = input("Exam score: ")
            with open("records.txt", "a") as f:
                f.write(f"{name},{age},{score}\n")
            print("Record saved.")
        elif choice == "2":
            if os.path.exists("records.txt"):
                with open("records.txt", "r") as f:
                    for line in f:
                        name, age, score = line.strip().split(",")
                        print(f"Name: {name} | Age: {age} | Score: {score}")
            else:
                print("No records yet.")
        elif choice == "3":
            count = 0
            if os.path.exists("records.txt"):
                with open("records.txt", "r") as f:
                    count = sum(1 for line in f if line.strip())
            print("Total records:", count)
        elif choice == "4":
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    choice = input("Enter question number (1-30) or 'all': ").strip().lower()
    if choice == "all":
        for i in range(1, 31):
            print(f"\n--- Question {i} ---")
            globals()[f"q{i}"]()
    elif choice.isdigit() and 1 <= int(choice) <= 30:
        globals()[f"q{choice}"]()
    else:
        print("Invalid choice.")Name = "Moses"
Age = 19
Height = "6ft"
Status = "Student"

print("Q1",Name)
print("Q1",Age)
print("Q1",Height)
print("Q1",Status)

a, b = 10, 3
x, y = 4.5, 1.5
print("Q2","Addition:", a + b, x + y)
print("Q2","Subtraction:", a - b, x - y)
print("Q2","Multiplication:", a * b, x * y)
print("Q2","Division:", a / b, x / y)

Name = input("Enter your name: ")
Age = int(input("Enter your age: "))
colour = input("Enter your favourite colour: ")

print("Q3",f"My name is {Name}, I am {Age} years old and my favourite colour is {colour}.")

num = 10
num2 = 20.29
name = "Ada"
Value = True

print("Q4",num, type(num), num2, type(num2), (name, type(name), (Value, type(Value))))

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Q5","Sum:", a + b)
print("Q5","Product:", a * b)
print("Q5","Difference:", a - b)

name = "Chidi"
s1, s2, s3, s4, s5 = 70, 65, 80, 55, 90
status = "Passed"
total = s1 + s2 + s3 + s4 + s5
average = total / 5
print("Q6","Name:", name)
print("Q6","Scores:", s1, s2, s3, s4, s5)
print("Q6","Status:", status)
print("Q6","Total:", total)
print("Q6","Average:", average)

fruits = ["apple", "banana", "mango", "orange", "pear", "grape", "pineapple", "guava", "lemon", "papaya"]
print("Q7","First:", fruits[0])
print("Q7","Last:", fruits[-1])
print("Q7","Total items:", len(fruits))

students = ["Ade", "Bola", "Chidi", "Dayo", "Emeka"]
students.append(input("Enter another student's name: "))
print("Q8","Updated list:", students)

Number =[1,2,3,4,5,6,7,8,9,10]
print("Q9","Even numbers:", [n for n in Number if n % 2 == 0])

nums = [15, 8, 25, 40, 12, 30, 5, 18]
largest = nums[0]
smallest = nums[0]
total = 0
for n in nums:
  if n > largest:
        largest = n
  if n < smallest:
       smallest = n
total += n
print("Q10","Largest:", largest)
print("Q10","Smallest:", smallest)
print("Q10","Sum:", total)

shopping = ["bread", "milk", "eggs", "rice", "sugar"]
for _ in range(2):
shopping.append(input("Add a product: "))
item = input("Enter a product to remove: ")
if item in shopping:
  shopping.remove(item)
else:
print("Product not found.")
print("Q11","Final shopping list:", shopping)


numbers = [5, 12, 18, 23, 7, 30, 41, 9, 15, 2]
n = int(input("Enter a number: "))
if n in numbers:
print(f"{n} exists at position (index) {numbers.index(n)}")
else:
print("Q12", f"{n} is not in the list.")

student = {"name": "Ada", "age": 20, "gender": "Female","department": "Computer Science", "matric_no": "CSC/2024/001"}
for key, value in student.items():
print("Q13", f"{key}: {value}")

products = {"Bread": 800, "Milk": 1200, "Rice": 5000, "Eggs": 2500, "Sugar": 1500}
for name, price in products.items():
print("Q14", f"{name}: {price}")

student = {"name": "Ada", "age": 20, "score": 65}
student["score"] = int(input("Enter the new score: "))
print("Q15", "Updated information:", student)

scores = {"Ade": 67, "Bola": 82, "Chidi": 75, "Dayo": 90, "Emeka": 58}
top_name, top_score = None, -1
for name, score in scores.items():
if score > top_score:
top_name, top_score = name, score
print("Q16", f"Highest score: {top_name} with {top_score}")

account = {"account_name": "Ada Obi", "account_number": "1234567890", "balance": 10000.0}
choice = input("Type 'deposit' or 'withdraw': ").strip().lower()
amount = float(input("Enter amount: "))
if choice == "deposit":
account["balance"] += amount
elif choice == "withdraw":
if amount <= account["balance"]:
account["balance"] -= amount
else:
    print("Insufficient funds.")
else:
    print("Invalid choice.")
print("Q17","Current balance:", account["balance"])

numbers = {10, 20, 30, 10, 40, 20, 50, 30}
print("Q18",numbers)

class_a = {"Ade", "Bola", "Chidi", "Dayo"}
class_b = {"Chidi", "Emeka", "Dayo", "Funke"}
print("Q19","Students in both classes:", class_a & class_b)

a = set(range(1, 11))
b = set(range(5, 16))
print("Q20","All elements:", a | b)
print("Q20","Common elements:", a & b)
print("Q20", "In first but not second:", a - b)

days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
print("Q21","First day:", days[0])
print("Q21","Last day:", days[-1])
print("Q21","Number of days:", len(days))
print("Q21","Saturday exists:", "Saturday" in days)

students = ("Ade", "Bola", "Chidi", "Dayo", "Emeka")
lst = list(students)
lst.append("Funke")
lst.append("Gozie")
lst.remove("Bola")
students = tuple(lst)
print("Q22",students)


with open("students.txt", "w") as f:
   f.write("Name: Ada\nAge: 20\nDepartment: Computer Science\n")
print("Q23","students.txt created.")


names = ["Ade", "Bola", "Chidi", "Dayo", "Emeka"]
with open("students.txt", "w") as f:  # "w" replaces previous content
for n in names:
     f.write(n + "\n")
print("Q24","students.txt overwritten with five names.")


with open("students.txt", "a") as f:  # "a" keeps previous content
for n in ["Funke", "Gozie", "Hauwa"]:
     f.write(n + "\n")
print("Q25","Three names appended.")


try:
with open("students.txt", "r") as f:
   print(f.read())
except FileNotFoundError:
print("Q26","students.txt not found. Run q23 first.")


sentences = ["Today was a good day.", "I learned about Python files.", "I wrote some code.", "I fixed a few bugs.", "Tomorrow I will practise more."]
with open("diary.txt", "w") as f:
for s in sentences:
f.write(s + "\n")
with open("diary.txt", "r") as f:
print("Q27:", f.read())

name = input("Enter your name: ")
language = input("Enter your favourite programming language: ")
with open("profile.txt", "a") as f:
f.write(f"{name} - {language}\n")
print("Q28","Saved to profile.txt.")


if not os.path.exists("numbers.txt"):  # create sample data if missing
with open("numbers.txt", "w") as f:
f.write("10\n20\n30\n40\n")
total = 0
with open("numbers.txt", "r") as f:
for line in f:
line = line.strip()
if line:
total += float(line)
print("Q29","Sum of numbers:", total)

    while True:
        print("\n1. Add student record\n2. View all records\n3. Count records\n4. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            name = input("Name: ")
            age = input("Age: ")
            score = input("Exam score: ")
            with open("records.txt", "a") as f:
                f.write(f"{name},{age},{score}\n")
            print("Record saved.")
        elif choice == "2":
            if os.path.exists("records.txt"):
                with open("records.txt", "r") as f:
                    for line in f:
                        name, age, score = line.strip().split(",")
                        print(f"Name: {name} | Age: {age} | Score: {score}")
            else:
                print("No records yet.")
        elif choice == "3":
            count = 0
            if os.path.exists("records.txt"):
                with open("records.txt", "r") as f:
                    count = sum(1 for line in f if line.strip())
            print("Total records:", count)
        elif choice == "4":
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    choice = input("Enter question number (1-30) or 'all': ").strip().lower()
    if choice == "all":
        for i in range(1, 31):
            print(f"\n--- Question {i} ---")
            globals()[f"q{i}"]()
    elif choice.isdigit() and 1 <= int(choice) <= 30:
        globals()[f"q{choice}"]()
    else:
        print("Invalid choice.")Name = "Moses"
Age = 19
Height = "6ft"
Status = "Student"

print("Q1",Name)
print("Q1",Age)
print("Q1",Height)
print("Q1",Status)

a, b = 10, 3
x, y = 4.5, 1.5
print("Q2","Addition:", a + b, x + y)
print("Q2","Subtraction:", a - b, x - y)
print("Q2","Multiplication:", a * b, x * y)
print("Q2","Division:", a / b, x / y)

Name = input("Enter your name: ")
Age = int(input("Enter your age: "))
colour = input("Enter your favourite colour: ")

print("Q3",f"My name is {Name}, I am {Age} years old and my favourite colour is {colour}.")

num = 10
num2 = 20.29
name = "Ada"
Value = True

print("Q4",num, type(num), num2, type(num2), (name, type(name), (Value, type(Value))))

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Q5","Sum:", a + b)
print("Q5","Product:", a * b)
print("Q5","Difference:", a - b)

name = "Chidi"
s1, s2, s3, s4, s5 = 70, 65, 80, 55, 90
status = "Passed"
total = s1 + s2 + s3 + s4 + s5
average = total / 5
print("Q6","Name:", name)
print("Q6","Scores:", s1, s2, s3, s4, s5)
print("Q6","Status:", status)
print("Q6","Total:", total)
print("Q6","Average:", average)

fruits = ["apple", "banana", "mango", "orange", "pear", "grape", "pineapple", "guava", "lemon", "papaya"]
print("Q7","First:", fruits[0])
print("Q7","Last:", fruits[-1])
print("Q7","Total items:", len(fruits))

students = ["Ade", "Bola", "Chidi", "Dayo", "Emeka"]
students.append(input("Enter another student's name: "))
print("Q8","Updated list:", students)

Number =[1,2,3,4,5,6,7,8,9,10]
print("Q9","Even numbers:", [n for n in Number if n % 2 == 0])

nums = [15, 8, 25, 40, 12, 30, 5, 18]
largest = nums[0]
smallest = nums[0]
total = 0
for n in nums:
  if n > largest:
        largest = n
  if n < smallest:
       smallest = n
total += n
print("Q10","Largest:", largest)
print("Q10","Smallest:", smallest)
print("Q10","Sum:", total)

shopping = ["bread", "milk", "eggs", "rice", "sugar"]
for _ in range(2):
shopping.append(input("Add a product: "))
item = input("Enter a product to remove: ")
if item in shopping:
  shopping.remove(item)
else:
print("Product not found.")
print("Q11","Final shopping list:", shopping)


numbers = [5, 12, 18, 23, 7, 30, 41, 9, 15, 2]
n = int(input("Enter a number: "))
if n in numbers:
print(f"{n} exists at position (index) {numbers.index(n)}")
else:
print("Q12", f"{n} is not in the list.")

student = {"name": "Ada", "age": 20, "gender": "Female","department": "Computer Science", "matric_no": "CSC/2024/001"}
for key, value in student.items():
print("Q13", f"{key}: {value}")

products = {"Bread": 800, "Milk": 1200, "Rice": 5000, "Eggs": 2500, "Sugar": 1500}
for name, price in products.items():
print("Q14", f"{name}: {price}")

student = {"name": "Ada", "age": 20, "score": 65}
student["score"] = int(input("Enter the new score: "))
print("Q15", "Updated information:", student)

scores = {"Ade": 67, "Bola": 82, "Chidi": 75, "Dayo": 90, "Emeka": 58}
top_name, top_score = None, -1
for name, score in scores.items():
if score > top_score:
top_name, top_score = name, score
print("Q16", f"Highest score: {top_name} with {top_score}")

account = {"account_name": "Ada Obi", "account_number": "1234567890", "balance": 10000.0}
choice = input("Type 'deposit' or 'withdraw': ").strip().lower()
amount = float(input("Enter amount: "))
if choice == "deposit":
account["balance"] += amount
elif choice == "withdraw":
if amount <= account["balance"]:
account["balance"] -= amount
else:
    print("Insufficient funds.")
else:
    print("Invalid choice.")
print("Q17","Current balance:", account["balance"])

numbers = {10, 20, 30, 10, 40, 20, 50, 30}
print("Q18",numbers)

class_a = {"Ade", "Bola", "Chidi", "Dayo"}
class_b = {"Chidi", "Emeka", "Dayo", "Funke"}
print("Q19","Students in both classes:", class_a & class_b)

a = set(range(1, 11))
b = set(range(5, 16))
print("Q20","All elements:", a | b)
print("Q20","Common elements:", a & b)
print("Q20", "In first but not second:", a - b)

days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
print("Q21","First day:", days[0])
print("Q21","Last day:", days[-1])
print("Q21","Number of days:", len(days))
print("Q21","Saturday exists:", "Saturday" in days)

students = ("Ade", "Bola", "Chidi", "Dayo", "Emeka")
lst = list(students)
lst.append("Funke")
lst.append("Gozie")
lst.remove("Bola")
students = tuple(lst)
print("Q22",students)


with open("students.txt", "w") as f:
   f.write("Name: Ada\nAge: 20\nDepartment: Computer Science\n")
print("Q23","students.txt created.")


names = ["Ade", "Bola", "Chidi", "Dayo", "Emeka"]
with open("students.txt", "w") as f:  # "w" replaces previous content
for n in names:
     f.write(n + "\n")
print("Q24","students.txt overwritten with five names.")


with open("students.txt", "a") as f:  # "a" keeps previous content
for n in ["Funke", "Gozie", "Hauwa"]:
     f.write(n + "\n")
print("Q25","Three names appended.")


try:
with open("students.txt", "r") as f:
   print(f.read())
except FileNotFoundError:
print("Q26","students.txt not found. Run q23 first.")


sentences = ["Today was a good day.", "I learned about Python files.", "I wrote some code.", "I fixed a few bugs.", "Tomorrow I will practise more."]
with open("diary.txt", "w") as f:
for s in sentences:
f.write(s + "\n")
with open("diary.txt", "r") as f:
print("Q27:", f.read())

name = input("Enter your name: ")
language = input("Enter your favourite programming language: ")
with open("profile.txt", "a") as f:
f.write(f"{name} - {language}\n")
print("Q28","Saved to profile.txt.")


if not os.path.exists("numbers.txt"):  # create sample data if missing
with open("numbers.txt", "w") as f:
f.write("10\n20\n30\n40\n")
total = 0
with open("numbers.txt", "r") as f:
for line in f:
line = line.strip()
if line:
total += float(line)
print("Q29","Sum of numbers:", total)

    while True:
        print("\n1. Add student record\n2. View all records\n3. Count records\n4. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            name = input("Name: ")
            age = input("Age: ")
            score = input("Exam score: ")
            with open("records.txt", "a") as f:
                f.write(f"{name},{age},{score}\n")
            print("Record saved.")
        elif choice == "2":
            if os.path.exists("records.txt"):
                with open("records.txt", "r") as f:
                    for line in f:
                        name, age, score = line.strip().split(",")
                        print(f"Name: {name} | Age: {age} | Score: {score}")
            else:
                print("No records yet.")
        elif choice == "3":
            count = 0
            if os.path.exists("records.txt"):
                with open("records.txt", "r") as f:
                    count = sum(1 for line in f if line.strip())
            print("Total records:", count)
        elif choice == "4":
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    choice = input("Enter question number (1-30) or 'all': ").strip().lower()
    if choice == "all":
        for i in range(1, 31):
            print(f"\n--- Question {i} ---")
            globals()[f"q{i}"]()
    elif choice.isdigit() and 1 <= int(choice) <= 30:
        globals()[f"q{choice}"]()
    else:
        print("Invalid choice.")Name = "Moses"
Age = 19
Height = "6ft"
Status = "Student"

print("Q1",Name)
print("Q1",Age)
print("Q1",Height)
print("Q1",Status)

a, b = 10, 3
x, y = 4.5, 1.5
print("Q2","Addition:", a + b, x + y)
print("Q2","Subtraction:", a - b, x - y)
print("Q2","Multiplication:", a * b, x * y)
print("Q2","Division:", a / b, x / y)

Name = input("Enter your name: ")
Age = int(input("Enter your age: "))
colour = input("Enter your favourite colour: ")

print("Q3",f"My name is {Name}, I am {Age} years old and my favourite colour is {colour}.")

num = 10
num2 = 20.29
name = "Ada"
Value = True

print("Q4",num, type(num), num2, type(num2), (name, type(name), (Value, type(Value))))

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Q5","Sum:", a + b)
print("Q5","Product:", a * b)
print("Q5","Difference:", a - b)

name = "Chidi"
s1, s2, s3, s4, s5 = 70, 65, 80, 55, 90
status = "Passed"
total = s1 + s2 + s3 + s4 + s5
average = total / 5
print("Q6","Name:", name)
print("Q6","Scores:", s1, s2, s3, s4, s5)
print("Q6","Status:", status)
print("Q6","Total:", total)
print("Q6","Average:", average)

fruits = ["apple", "banana", "mango", "orange", "pear", "grape", "pineapple", "guava", "lemon", "papaya"]
print("Q7","First:", fruits[0])
print("Q7","Last:", fruits[-1])
print("Q7","Total items:", len(fruits))

students = ["Ade", "Bola", "Chidi", "Dayo", "Emeka"]
students.append(input("Enter another student's name: "))
print("Q8","Updated list:", students)

Number =[1,2,3,4,5,6,7,8,9,10]
print("Q9","Even numbers:", [n for n in Number if n % 2 == 0])

nums = [15, 8, 25, 40, 12, 30, 5, 18]
largest = nums[0]
smallest = nums[0]
total = 0
for n in nums:
  if n > largest:
        largest = n
  if n < smallest:
       smallest = n
total += n
print("Q10","Largest:", largest)
print("Q10","Smallest:", smallest)
print("Q10","Sum:", total)

shopping = ["bread", "milk", "eggs", "rice", "sugar"]
for _ in range(2):
shopping.append(input("Add a product: "))
item = input("Enter a product to remove: ")
if item in shopping:
  shopping.remove(item)
else:
print("Product not found.")
print("Q11","Final shopping list:", shopping)


numbers = [5, 12, 18, 23, 7, 30, 41, 9, 15, 2]
n = int(input("Enter a number: "))
if n in numbers:
print(f"{n} exists at position (index) {numbers.index(n)}")
else:
print("Q12", f"{n} is not in the list.")

student = {"name": "Ada", "age": 20, "gender": "Female","department": "Computer Science", "matric_no": "CSC/2024/001"}
for key, value in student.items():
print("Q13", f"{key}: {value}")

products = {"Bread": 800, "Milk": 1200, "Rice": 5000, "Eggs": 2500, "Sugar": 1500}
for name, price in products.items():
print("Q14", f"{name}: {price}")

student = {"name": "Ada", "age": 20, "score": 65}
student["score"] = int(input("Enter the new score: "))
print("Q15", "Updated information:", student)

scores = {"Ade": 67, "Bola": 82, "Chidi": 75, "Dayo": 90, "Emeka": 58}
top_name, top_score = None, -1
for name, score in scores.items():
if score > top_score:
top_name, top_score = name, score
print("Q16", f"Highest score: {top_name} with {top_score}")

account = {"account_name": "Ada Obi", "account_number": "1234567890", "balance": 10000.0}
choice = input("Type 'deposit' or 'withdraw': ").strip().lower()
amount = float(input("Enter amount: "))
if choice == "deposit":
account["balance"] += amount
elif choice == "withdraw":
if amount <= account["balance"]:
account["balance"] -= amount
else:
    print("Insufficient funds.")
else:
    print("Invalid choice.")
print("Q17","Current balance:", account["balance"])

numbers = {10, 20, 30, 10, 40, 20, 50, 30}
print("Q18",numbers)

class_a = {"Ade", "Bola", "Chidi", "Dayo"}
class_b = {"Chidi", "Emeka", "Dayo", "Funke"}
print("Q19","Students in both classes:", class_a & class_b)

a = set(range(1, 11))
b = set(range(5, 16))
print("Q20","All elements:", a | b)
print("Q20","Common elements:", a & b)
print("Q20", "In first but not second:", a - b)

days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
print("Q21","First day:", days[0])
print("Q21","Last day:", days[-1])
print("Q21","Number of days:", len(days))
print("Q21","Saturday exists:", "Saturday" in days)

students = ("Ade", "Bola", "Chidi", "Dayo", "Emeka")
lst = list(students)
lst.append("Funke")
lst.append("Gozie")
lst.remove("Bola")
students = tuple(lst)
print("Q22",students)


with open("students.txt", "w") as f:
   f.write("Name: Ada\nAge: 20\nDepartment: Computer Science\n")
print("Q23","students.txt created.")


names = ["Ade", "Bola", "Chidi", "Dayo", "Emeka"]
with open("students.txt", "w") as f:  # "w" replaces previous content
for n in names:
     f.write(n + "\n")
print("Q24","students.txt overwritten with five names.")


with open("students.txt", "a") as f:  # "a" keeps previous content
for n in ["Funke", "Gozie", "Hauwa"]:
     f.write(n + "\n")
print("Q25","Three names appended.")


try:
with open("students.txt", "r") as f:
   print(f.read())
except FileNotFoundError:
print("Q26","students.txt not found. Run q23 first.")


sentences = ["Today was a good day.", "I learned about Python files.", "I wrote some code.", "I fixed a few bugs.", "Tomorrow I will practise more."]
with open("diary.txt", "w") as f:
for s in sentences:
f.write(s + "\n")
with open("diary.txt", "r") as f:
print("Q27:", f.read())

name = input("Enter your name: ")
language = input("Enter your favourite programming language: ")
with open("profile.txt", "a") as f:
f.write(f"{name} - {language}\n")
print("Q28","Saved to profile.txt.")


if not os.path.exists("numbers.txt"):  # create sample data if missing
with open("numbers.txt", "w") as f:
f.write("10\n20\n30\n40\n")
total = 0
with open("numbers.txt", "r") as f:
for line in f:
line = line.strip()
if line:
total += float(line)
print("Q29","Sum of numbers:", total)

    while True:
        print("\n1. Add student record\n2. View all records\n3. Count records\n4. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            name = input("Name: ")
            age = input("Age: ")
            score = input("Exam score: ")
            with open("records.txt", "a") as f:
                f.write(f"{name},{age},{score}\n")
            print("Record saved.")
        elif choice == "2":
            if os.path.exists("records.txt"):
                with open("records.txt", "r") as f:
                    for line in f:
                        name, age, score = line.strip().split(",")
                        print(f"Name: {name} | Age: {age} | Score: {score}")
            else:
                print("No records yet.")
        elif choice == "3":
            count = 0
            if os.path.exists("records.txt"):
                with open("records.txt", "r") as f:
                    count = sum(1 for line in f if line.strip())
            print("Total records:", count)
        elif choice == "4":
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    choice = input("Enter question number (1-30) or 'all': ").strip().lower()
    if choice == "all":
        for i in range(1, 31):
            print(f"\n--- Question {i} ---")
            globals()[f"q{i}"]()
    elif choice.isdigit() and 1 <= int(choice) <= 30:
        globals()[f"q{choice}"]()
    else:
        print("Invalid choice.")Name = "Moses"
Age = 19
Height = "6ft"
Status = "Student"

print("Q1",Name)
print("Q1",Age)
print("Q1",Height)
print("Q1",Status)

a, b = 10, 3
x, y = 4.5, 1.5
print("Q2","Addition:", a + b, x + y)
print("Q2","Subtraction:", a - b, x - y)
print("Q2","Multiplication:", a * b, x * y)
print("Q2","Division:", a / b, x / y)

Name = input("Enter your name: ")
Age = int(input("Enter your age: "))
colour = input("Enter your favourite colour: ")

print("Q3",f"My name is {Name}, I am {Age} years old and my favourite colour is {colour}.")

num = 10
num2 = 20.29
name = "Ada"
Value = True

print("Q4",num, type(num), num2, type(num2), (name, type(name), (Value, type(Value))))

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Q5","Sum:", a + b)
print("Q5","Product:", a * b)
print("Q5","Difference:", a - b)

name = "Chidi"
s1, s2, s3, s4, s5 = 70, 65, 80, 55, 90
status = "Passed"
total = s1 + s2 + s3 + s4 + s5
average = total / 5
print("Q6","Name:", name)
print("Q6","Scores:", s1, s2, s3, s4, s5)
print("Q6","Status:", status)
print("Q6","Total:", total)
print("Q6","Average:", average)

fruits = ["apple", "banana", "mango", "orange", "pear", "grape", "pineapple", "guava", "lemon", "papaya"]
print("Q7","First:", fruits[0])
print("Q7","Last:", fruits[-1])
print("Q7","Total items:", len(fruits))

students = ["Ade", "Bola", "Chidi", "Dayo", "Emeka"]
students.append(input("Enter another student's name: "))
print("Q8","Updated list:", students)

Number =[1,2,3,4,5,6,7,8,9,10]
print("Q9","Even numbers:", [n for n in Number if n % 2 == 0])

nums = [15, 8, 25, 40, 12, 30, 5, 18]
largest = nums[0]
smallest = nums[0]
total = 0
for n in nums:
  if n > largest:
        largest = n
  if n < smallest:
       smallest = n
total += n
print("Q10","Largest:", largest)
print("Q10","Smallest:", smallest)
print("Q10","Sum:", total)

shopping = ["bread", "milk", "eggs", "rice", "sugar"]
for _ in range(2):
shopping.append(input("Add a product: "))
item = input("Enter a product to remove: ")
if item in shopping:
  shopping.remove(item)
else:
print("Product not found.")
print("Q11","Final shopping list:", shopping)


numbers = [5, 12, 18, 23, 7, 30, 41, 9, 15, 2]
n = int(input("Enter a number: "))
if n in numbers:
print(f"{n} exists at position (index) {numbers.index(n)}")
else:
print("Q12", f"{n} is not in the list.")

student = {"name": "Ada", "age": 20, "gender": "Female","department": "Computer Science", "matric_no": "CSC/2024/001"}
for key, value in student.items():
print("Q13", f"{key}: {value}")

products = {"Bread": 800, "Milk": 1200, "Rice": 5000, "Eggs": 2500, "Sugar": 1500}
for name, price in products.items():
print("Q14", f"{name}: {price}")

student = {"name": "Ada", "age": 20, "score": 65}
student["score"] = int(input("Enter the new score: "))
print("Q15", "Updated information:", student)

scores = {"Ade": 67, "Bola": 82, "Chidi": 75, "Dayo": 90, "Emeka": 58}
top_name, top_score = None, -1
for name, score in scores.items():
if score > top_score:
top_name, top_score = name, score
print("Q16", f"Highest score: {top_name} with {top_score}")

account = {"account_name": "Ada Obi", "account_number": "1234567890", "balance": 10000.0}
choice = input("Type 'deposit' or 'withdraw': ").strip().lower()
amount = float(input("Enter amount: "))
if choice == "deposit":
account["balance"] += amount
elif choice == "withdraw":
if amount <= account["balance"]:
account["balance"] -= amount
else:
    print("Insufficient funds.")
else:
    print("Invalid choice.")
print("Q17","Current balance:", account["balance"])

numbers = {10, 20, 30, 10, 40, 20, 50, 30}
print("Q18",numbers)

class_a = {"Ade", "Bola", "Chidi", "Dayo"}
class_b = {"Chidi", "Emeka", "Dayo", "Funke"}
print("Q19","Students in both classes:", class_a & class_b)

a = set(range(1, 11))
b = set(range(5, 16))
print("Q20","All elements:", a | b)
print("Q20","Common elements:", a & b)
print("Q20", "In first but not second:", a - b)

days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
print("Q21","First day:", days[0])
print("Q21","Last day:", days[-1])
print("Q21","Number of days:", len(days))
print("Q21","Saturday exists:", "Saturday" in days)

students = ("Ade", "Bola", "Chidi", "Dayo", "Emeka")
lst = list(students)
lst.append("Funke")
lst.append("Gozie")
lst.remove("Bola")
students = tuple(lst)
print("Q22",students)


with open("students.txt", "w") as f:
   f.write("Name: Ada\nAge: 20\nDepartment: Computer Science\n")
print("Q23","students.txt created.")


names = ["Ade", "Bola", "Chidi", "Dayo", "Emeka"]
with open("students.txt", "w") as f:  # "w" replaces previous content
for n in names:
     f.write(n + "\n")
print("Q24","students.txt overwritten with five names.")


with open("students.txt", "a") as f:  # "a" keeps previous content
for n in ["Funke", "Gozie", "Hauwa"]:
     f.write(n + "\n")
print("Q25","Three names appended.")


try:
with open("students.txt", "r") as f:
   print(f.read())
except FileNotFoundError:
print("Q26","students.txt not found. Run q23 first.")


sentences = ["Today was a good day.", "I learned about Python files.", "I wrote some code.", "I fixed a few bugs.", "Tomorrow I will practise more."]
with open("diary.txt", "w") as f:
for s in sentences:
f.write(s + "\n")
with open("diary.txt", "r") as f:
print("Q27:", f.read())

name = input("Enter your name: ")
language = input("Enter your favourite programming language: ")
with open("profile.txt", "a") as f:
f.write(f"{name} - {language}\n")
print("Q28","Saved to profile.txt.")


if not os.path.exists("numbers.txt"):  # create sample data if missing
with open("numbers.txt", "w") as f:
f.write("10\n20\n30\n40\n")
total = 0
with open("numbers.txt", "r") as f:
for line in f:
line = line.strip()
if line:
total += float(line)
print("Q29","Sum of numbers:", total)

    while True:
        print("\n1. Add student record\n2. View all records\n3. Count records\n4. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            name = input("Name: ")
            age = input("Age: ")
            score = input("Exam score: ")
            with open("records.txt", "a") as f:
                f.write(f"{name},{age},{score}\n")
            print("Record saved.")
        elif choice == "2":
            if os.path.exists("records.txt"):
                with open("records.txt", "r") as f:
                    for line in f:
                        name, age, score = line.strip().split(",")
                        print(f"Name: {name} | Age: {age} | Score: {score}")
            else:
                print("No records yet.")
        elif choice == "3":
            count = 0
            if os.path.exists("records.txt"):
                with open("records.txt", "r") as f:
                    count = sum(1 for line in f if line.strip())
            print("Total records:", count)
        elif choice == "4":
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    choice = input("Enter question number (1-30) or 'all': ").strip().lower()
    if choice == "all":
        for i in range(1, 31):
            print(f"\n--- Question {i} ---")
            globals()[f"q{i}"]()
    elif choice.isdigit() and 1 <= int(choice) <= 30:
        globals()[f"q{choice}"]()
    else:
        print("Invalid choice.")Name = "Moses"
Age = 19
Height = "6ft"
Status = "Student"

print("Q1",Name)
print("Q1",Age)
print("Q1",Height)
print("Q1",Status)

a, b = 10, 3
x, y = 4.5, 1.5
print("Q2","Addition:", a + b, x + y)
print("Q2","Subtraction:", a - b, x - y)
print("Q2","Multiplication:", a * b, x * y)
print("Q2","Division:", a / b, x / y)

Name = input("Enter your name: ")
Age = int(input("Enter your age: "))
colour = input("Enter your favourite colour: ")

print("Q3",f"My name is {Name}, I am {Age} years old and my favourite colour is {colour}.")

num = 10
num2 = 20.29
name = "Ada"
Value = True

print("Q4",num, type(num), num2, type(num2), (name, type(name), (Value, type(Value))))

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Q5","Sum:", a + b)
print("Q5","Product:", a * b)
print("Q5","Difference:", a - b)

name = "Chidi"
s1, s2, s3, s4, s5 = 70, 65, 80, 55, 90
status = "Passed"
total = s1 + s2 + s3 + s4 + s5
average = total / 5
print("Q6","Name:", name)
print("Q6","Scores:", s1, s2, s3, s4, s5)
print("Q6","Status:", status)
print("Q6","Total:", total)
print("Q6","Average:", average)

fruits = ["apple", "banana", "mango", "orange", "pear", "grape", "pineapple", "guava", "lemon", "papaya"]
print("Q7","First:", fruits[0])
print("Q7","Last:", fruits[-1])
print("Q7","Total items:", len(fruits))

students = ["Ade", "Bola", "Chidi", "Dayo", "Emeka"]
students.append(input("Enter another student's name: "))
print("Q8","Updated list:", students)

Number =[1,2,3,4,5,6,7,8,9,10]
print("Q9","Even numbers:", [n for n in Number if n % 2 == 0])

nums = [15, 8, 25, 40, 12, 30, 5, 18]
largest = nums[0]
smallest = nums[0]
total = 0
for n in nums:
  if n > largest:
        largest = n
  if n < smallest:
       smallest = n
total += n
print("Q10","Largest:", largest)
print("Q10","Smallest:", smallest)
print("Q10","Sum:", total)

shopping = ["bread", "milk", "eggs", "rice", "sugar"]
for _ in range(2):
shopping.append(input("Add a product: "))
item = input("Enter a product to remove: ")
if item in shopping:
  shopping.remove(item)
else:
print("Product not found.")
print("Q11","Final shopping list:", shopping)


numbers = [5, 12, 18, 23, 7, 30, 41, 9, 15, 2]
n = int(input("Enter a number: "))
if n in numbers:
print(f"{n} exists at position (index) {numbers.index(n)}")
else:
print("Q12", f"{n} is not in the list.")

student = {"name": "Ada", "age": 20, "gender": "Female","department": "Computer Science", "matric_no": "CSC/2024/001"}
for key, value in student.items():
print("Q13", f"{key}: {value}")

products = {"Bread": 800, "Milk": 1200, "Rice": 5000, "Eggs": 2500, "Sugar": 1500}
for name, price in products.items():
print("Q14", f"{name}: {price}")

student = {"name": "Ada", "age": 20, "score": 65}
student["score"] = int(input("Enter the new score: "))
print("Q15", "Updated information:", student)

scores = {"Ade": 67, "Bola": 82, "Chidi": 75, "Dayo": 90, "Emeka": 58}
top_name, top_score = None, -1
for name, score in scores.items():
if score > top_score:
top_name, top_score = name, score
print("Q16", f"Highest score: {top_name} with {top_score}")

account = {"account_name": "Ada Obi", "account_number": "1234567890", "balance": 10000.0}
choice = input("Type 'deposit' or 'withdraw': ").strip().lower()
amount = float(input("Enter amount: "))
if choice == "deposit":
account["balance"] += amount
elif choice == "withdraw":
if amount <= account["balance"]:
account["balance"] -= amount
else:
    print("Insufficient funds.")
else:
    print("Invalid choice.")
print("Q17","Current balance:", account["balance"])

numbers = {10, 20, 30, 10, 40, 20, 50, 30}
print("Q18",numbers)

class_a = {"Ade", "Bola", "Chidi", "Dayo"}
class_b = {"Chidi", "Emeka", "Dayo", "Funke"}
print("Q19","Students in both classes:", class_a & class_b)

a = set(range(1, 11))
b = set(range(5, 16))
print("Q20","All elements:", a | b)
print("Q20","Common elements:", a & b)
print("Q20", "In first but not second:", a - b)

days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
print("Q21","First day:", days[0])
print("Q21","Last day:", days[-1])
print("Q21","Number of days:", len(days))
print("Q21","Saturday exists:", "Saturday" in days)

students = ("Ade", "Bola", "Chidi", "Dayo", "Emeka")
lst = list(students)
lst.append("Funke")
lst.append("Gozie")
lst.remove("Bola")
students = tuple(lst)
print("Q22",students)


with open("students.txt", "w") as f:
   f.write("Name: Ada\nAge: 20\nDepartment: Computer Science\n")
print("Q23","students.txt created.")


names = ["Ade", "Bola", "Chidi", "Dayo", "Emeka"]
with open("students.txt", "w") as f:  # "w" replaces previous content
for n in names:
     f.write(n + "\n")
print("Q24","students.txt overwritten with five names.")


with open("students.txt", "a") as f:  # "a" keeps previous content
for n in ["Funke", "Gozie", "Hauwa"]:
     f.write(n + "\n")
print("Q25","Three names appended.")


try:
with open("students.txt", "r") as f:
   print(f.read())
except FileNotFoundError:
print("Q26","students.txt not found. Run q23 first.")


sentences = ["Today was a good day.", "I learned about Python files.", "I wrote some code.", "I fixed a few bugs.", "Tomorrow I will practise more."]
with open("diary.txt", "w") as f:
for s in sentences:
f.write(s + "\n")
with open("diary.txt", "r") as f:
print("Q27:", f.read())

name = input("Enter your name: ")
language = input("Enter your favourite programming language: ")
with open("profile.txt", "a") as f:
f.write(f"{name} - {language}\n")
print("Q28","Saved to profile.txt.")


if not os.path.exists("numbers.txt"):  # create sample data if missing
with open("numbers.txt", "w") as f:
f.write("10\n20\n30\n40\n")
total = 0
with open("numbers.txt", "r") as f:
for line in f:
line = line.strip()
if line:
total += float(line)
print("Q29","Sum of numbers:", total)

    while True:
        print("\n1. Add student record\n2. View all records\n3. Count records\n4. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            name = input("Name: ")
            age = input("Age: ")
            score = input("Exam score: ")
            with open("records.txt", "a") as f:
                f.write(f"{name},{age},{score}\n")
            print("Record saved.")
        elif choice == "2":
            if os.path.exists("records.txt"):
                with open("records.txt", "r") as f:
                    for line in f:
                        name, age, score = line.strip().split(",")
                        print(f"Name: {name} | Age: {age} | Score: {score}")
            else:
                print("No records yet.")
        elif choice == "3":
            count = 0
            if os.path.exists("records.txt"):
                with open("records.txt", "r") as f:
                    count = sum(1 for line in f if line.strip())
            print("Total records:", count)
        elif choice == "4":
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    choice = input("Enter question number (1-30) or 'all': ").strip().lower()
    if choice == "all":
        for i in range(1, 31):
            print(f"\n--- Question {i} ---")
            globals()[f"q{i}"]()
    elif choice.isdigit() and 1 <= int(choice) <= 30:
        globals()[f"q{choice}"]()
    else:
        print("Invalid choice.")Name = "Moses"
Age = 19
Height = "6ft"
Status = "Student"

print("Q1",Name)
print("Q1",Age)
print("Q1",Height)
print("Q1",Status)

a, b = 10, 3
x, y = 4.5, 1.5
print("Q2","Addition:", a + b, x + y)
print("Q2","Subtraction:", a - b, x - y)
print("Q2","Multiplication:", a * b, x * y)
print("Q2","Division:", a / b, x / y)

Name = input("Enter your name: ")
Age = int(input("Enter your age: "))
colour = input("Enter your favourite colour: ")

print("Q3",f"My name is {Name}, I am {Age} years old and my favourite colour is {colour}.")

num = 10
num2 = 20.29
name = "Ada"
Value = True

print("Q4",num, type(num), num2, type(num2), (name, type(name), (Value, type(Value))))

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Q5","Sum:", a + b)
print("Q5","Product:", a * b)
print("Q5","Difference:", a - b)

name = "Chidi"
s1, s2, s3, s4, s5 = 70, 65, 80, 55, 90
status = "Passed"
total = s1 + s2 + s3 + s4 + s5
average = total / 5
print("Q6","Name:", name)
print("Q6","Scores:", s1, s2, s3, s4, s5)
print("Q6","Status:", status)
print("Q6","Total:", total)
print("Q6","Average:", average)

fruits = ["apple", "banana", "mango", "orange", "pear", "grape", "pineapple", "guava", "lemon", "papaya"]
print("Q7","First:", fruits[0])
print("Q7","Last:", fruits[-1])
print("Q7","Total items:", len(fruits))

students = ["Ade", "Bola", "Chidi", "Dayo", "Emeka"]
students.append(input("Enter another student's name: "))
print("Q8","Updated list:", students)

Number =[1,2,3,4,5,6,7,8,9,10]
print("Q9","Even numbers:", [n for n in Number if n % 2 == 0])

nums = [15, 8, 25, 40, 12, 30, 5, 18]
largest = nums[0]
smallest = nums[0]
total = 0
for n in nums:
  if n > largest:
        largest = n
  if n < smallest:
       smallest = n
total += n
print("Q10","Largest:", largest)
print("Q10","Smallest:", smallest)
print("Q10","Sum:", total)

shopping = ["bread", "milk", "eggs", "rice", "sugar"]
for _ in range(2):
shopping.append(input("Add a product: "))
item = input("Enter a product to remove: ")
if item in shopping:
  shopping.remove(item)
else:
print("Product not found.")
print("Q11","Final shopping list:", shopping)


numbers = [5, 12, 18, 23, 7, 30, 41, 9, 15, 2]
n = int(input("Enter a number: "))
if n in numbers:
print(f"{n} exists at position (index) {numbers.index(n)}")
else:
print("Q12", f"{n} is not in the list.")

student = {"name": "Ada", "age": 20, "gender": "Female","department": "Computer Science", "matric_no": "CSC/2024/001"}
for key, value in student.items():
print("Q13", f"{key}: {value}")

products = {"Bread": 800, "Milk": 1200, "Rice": 5000, "Eggs": 2500, "Sugar": 1500}
for name, price in products.items():
print("Q14", f"{name}: {price}")

student = {"name": "Ada", "age": 20, "score": 65}
student["score"] = int(input("Enter the new score: "))
print("Q15", "Updated information:", student)

scores = {"Ade": 67, "Bola": 82, "Chidi": 75, "Dayo": 90, "Emeka": 58}
top_name, top_score = None, -1
for name, score in scores.items():
if score > top_score:
top_name, top_score = name, score
print("Q16", f"Highest score: {top_name} with {top_score}")

account = {"account_name": "Ada Obi", "account_number": "1234567890", "balance": 10000.0}
choice = input("Type 'deposit' or 'withdraw': ").strip().lower()
amount = float(input("Enter amount: "))
if choice == "deposit":
account["balance"] += amount
elif choice == "withdraw":
if amount <= account["balance"]:
account["balance"] -= amount
else:
    print("Insufficient funds.")
else:
    print("Invalid choice.")
print("Q17","Current balance:", account["balance"])

numbers = {10, 20, 30, 10, 40, 20, 50, 30}
print("Q18",numbers)

class_a = {"Ade", "Bola", "Chidi", "Dayo"}
class_b = {"Chidi", "Emeka", "Dayo", "Funke"}
print("Q19","Students in both classes:", class_a & class_b)

a = set(range(1, 11))
b = set(range(5, 16))
print("Q20","All elements:", a | b)
print("Q20","Common elements:", a & b)
print("Q20", "In first but not second:", a - b)

days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
print("Q21","First day:", days[0])
print("Q21","Last day:", days[-1])
print("Q21","Number of days:", len(days))
print("Q21","Saturday exists:", "Saturday" in days)

students = ("Ade", "Bola", "Chidi", "Dayo", "Emeka")
lst = list(students)
lst.append("Funke")
lst.append("Gozie")
lst.remove("Bola")
students = tuple(lst)
print("Q22",students)


with open("students.txt", "w") as f:
   f.write("Name: Ada\nAge: 20\nDepartment: Computer Science\n")
print("Q23","students.txt created.")


names = ["Ade", "Bola", "Chidi", "Dayo", "Emeka"]
with open("students.txt", "w") as f:  # "w" replaces previous content
for n in names:
     f.write(n + "\n")
print("Q24","students.txt overwritten with five names.")


with open("students.txt", "a") as f:  # "a" keeps previous content
for n in ["Funke", "Gozie", "Hauwa"]:
     f.write(n + "\n")
print("Q25","Three names appended.")


try:
with open("students.txt", "r") as f:
   print(f.read())
except FileNotFoundError:
print("Q26","students.txt not found. Run q23 first.")


sentences = ["Today was a good day.", "I learned about Python files.", "I wrote some code.", "I fixed a few bugs.", "Tomorrow I will practise more."]
with open("diary.txt", "w") as f:
for s in sentences:
f.write(s + "\n")
with open("diary.txt", "r") as f:
print("Q27:", f.read())

name = input("Enter your name: ")
language = input("Enter your favourite programming language: ")
with open("profile.txt", "a") as f:
f.write(f"{name} - {language}\n")
print("Q28","Saved to profile.txt.")


if not os.path.exists("numbers.txt"):  # create sample data if missing
with open("numbers.txt", "w") as f:
f.write("10\n20\n30\n40\n")
total = 0
with open("numbers.txt", "r") as f:
for line in f:
line = line.strip()
if line:
total += float(line)
print("Q29","Sum of numbers:", total)

    while True:
        print("\n1. Add student record\n2. View all records\n3. Count records\n4. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            name = input("Name: ")
            age = input("Age: ")
            score = input("Exam score: ")
            with open("records.txt", "a") as f:
                f.write(f"{name},{age},{score}\n")
            print("Record saved.")
        elif choice == "2":
            if os.path.exists("records.txt"):
                with open("records.txt", "r") as f:
                    for line in f:
                        name, age, score = line.strip().split(",")
                        print(f"Name: {name} | Age: {age} | Score: {score}")
            else:
                print("No records yet.")
        elif choice == "3":
            count = 0
            if os.path.exists("records.txt"):
                with open("records.txt", "r") as f:
                    count = sum(1 for line in f if line.strip())
            print("Total records:", count)
        elif choice == "4":
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    choice = input("Enter question number (1-30) or 'all': ").strip().lower()
    if choice == "all":
        for i in range(1, 31):
            print(f"\n--- Question {i} ---")
            globals()[f"q{i}"]()
    elif choice.isdigit() and 1 <= int(choice) <= 30:
        globals()[f"q{choice}"]()
    else:
        print("Invalid choice.")Name = "Moses"
Age = 19
Height = "6ft"
Status = "Student"

print("Q1",Name)
print("Q1",Age)
print("Q1",Height)
print("Q1",Status)

a, b = 10, 3
x, y = 4.5, 1.5
print("Q2","Addition:", a + b, x + y)
print("Q2","Subtraction:", a - b, x - y)
print("Q2","Multiplication:", a * b, x * y)
print("Q2","Division:", a / b, x / y)

Name = input("Enter your name: ")
Age = int(input("Enter your age: "))
colour = input("Enter your favourite colour: ")

print("Q3",f"My name is {Name}, I am {Age} years old and my favourite colour is {colour}.")

num = 10
num2 = 20.29
name = "Ada"
Value = True

print("Q4",num, type(num), num2, type(num2), (name, type(name), (Value, type(Value))))

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Q5","Sum:", a + b)
print("Q5","Product:", a * b)
print("Q5","Difference:", a - b)

name = "Chidi"
s1, s2, s3, s4, s5 = 70, 65, 80, 55, 90
status = "Passed"
total = s1 + s2 + s3 + s4 + s5
average = total / 5
print("Q6","Name:", name)
print("Q6","Scores:", s1, s2, s3, s4, s5)
print("Q6","Status:", status)
print("Q6","Total:", total)
print("Q6","Average:", average)

fruits = ["apple", "banana", "mango", "orange", "pear", "grape", "pineapple", "guava", "lemon", "papaya"]
print("Q7","First:", fruits[0])
print("Q7","Last:", fruits[-1])
print("Q7","Total items:", len(fruits))

students = ["Ade", "Bola", "Chidi", "Dayo", "Emeka"]
students.append(input("Enter another student's name: "))
print("Q8","Updated list:", students)

Number =[1,2,3,4,5,6,7,8,9,10]
print("Q9","Even numbers:", [n for n in Number if n % 2 == 0])

nums = [15, 8, 25, 40, 12, 30, 5, 18]
largest = nums[0]
smallest = nums[0]
total = 0
for n in nums:
  if n > largest:
        largest = n
  if n < smallest:
       smallest = n
total += n
print("Q10","Largest:", largest)
print("Q10","Smallest:", smallest)
print("Q10","Sum:", total)

shopping = ["bread", "milk", "eggs", "rice", "sugar"]
for _ in range(2):
shopping.append(input("Add a product: "))
item = input("Enter a product to remove: ")
if item in shopping:
  shopping.remove(item)
else:
print("Product not found.")
print("Q11","Final shopping list:", shopping)


numbers = [5, 12, 18, 23, 7, 30, 41, 9, 15, 2]
n = int(input("Enter a number: "))
if n in numbers:
print(f"{n} exists at position (index) {numbers.index(n)}")
else:
print("Q12", f"{n} is not in the list.")

student = {"name": "Ada", "age": 20, "gender": "Female","department": "Computer Science", "matric_no": "CSC/2024/001"}
for key, value in student.items():
print("Q13", f"{key}: {value}")

products = {"Bread": 800, "Milk": 1200, "Rice": 5000, "Eggs": 2500, "Sugar": 1500}
for name, price in products.items():
print("Q14", f"{name}: {price}")

student = {"name": "Ada", "age": 20, "score": 65}
student["score"] = int(input("Enter the new score: "))
print("Q15", "Updated information:", student)

scores = {"Ade": 67, "Bola": 82, "Chidi": 75, "Dayo": 90, "Emeka": 58}
top_name, top_score = None, -1
for name, score in scores.items():
if score > top_score:
top_name, top_score = name, score
print("Q16", f"Highest score: {top_name} with {top_score}")

account = {"account_name": "Ada Obi", "account_number": "1234567890", "balance": 10000.0}
choice = input("Type 'deposit' or 'withdraw': ").strip().lower()
amount = float(input("Enter amount: "))
if choice == "deposit":
account["balance"] += amount
elif choice == "withdraw":
if amount <= account["balance"]:
account["balance"] -= amount
else:
    print("Insufficient funds.")
else:
    print("Invalid choice.")
print("Q17","Current balance:", account["balance"])

numbers = {10, 20, 30, 10, 40, 20, 50, 30}
print("Q18",numbers)

class_a = {"Ade", "Bola", "Chidi", "Dayo"}
class_b = {"Chidi", "Emeka", "Dayo", "Funke"}
print("Q19","Students in both classes:", class_a & class_b)

a = set(range(1, 11))
b = set(range(5, 16))
print("Q20","All elements:", a | b)
print("Q20","Common elements:", a & b)
print("Q20", "In first but not second:", a - b)

days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
print("Q21","First day:", days[0])
print("Q21","Last day:", days[-1])
print("Q21","Number of days:", len(days))
print("Q21","Saturday exists:", "Saturday" in days)

students = ("Ade", "Bola", "Chidi", "Dayo", "Emeka")
lst = list(students)
lst.append("Funke")
lst.append("Gozie")
lst.remove("Bola")
students = tuple(lst)
print("Q22",students)


with open("students.txt", "w") as f:
   f.write("Name: Ada\nAge: 20\nDepartment: Computer Science\n")
print("Q23","students.txt created.")


names = ["Ade", "Bola", "Chidi", "Dayo", "Emeka"]
with open("students.txt", "w") as f:  # "w" replaces previous content
for n in names:
     f.write(n + "\n")
print("Q24","students.txt overwritten with five names.")


with open("students.txt", "a") as f:  # "a" keeps previous content
for n in ["Funke", "Gozie", "Hauwa"]:
     f.write(n + "\n")
print("Q25","Three names appended.")


try:
with open("students.txt", "r") as f:
   print(f.read())
except FileNotFoundError:
print("Q26","students.txt not found. Run q23 first.")


sentences = ["Today was a good day.", "I learned about Python files.", "I wrote some code.", "I fixed a few bugs.", "Tomorrow I will practise more."]
with open("diary.txt", "w") as f:
for s in sentences:
f.write(s + "\n")
with open("diary.txt", "r") as f:
print("Q27:", f.read())

name = input("Enter your name: ")
language = input("Enter your favourite programming language: ")
with open("profile.txt", "a") as f:
f.write(f"{name} - {language}\n")
print("Q28","Saved to profile.txt.")


if not os.path.exists("numbers.txt"):  # create sample data if missing
with open("numbers.txt", "w") as f:
f.write("10\n20\n30\n40\n")
total = 0
with open("numbers.txt", "r") as f:
for line in f:
line = line.strip()
if line:
total += float(line)
print("Q29","Sum of numbers:", total)

    while True:
        print("\n1. Add student record\n2. View all records\n3. Count records\n4. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            name = input("Name: ")
            age = input("Age: ")
            score = input("Exam score: ")
            with open("records.txt", "a") as f:
                f.write(f"{name},{age},{score}\n")
            print("Record saved.")
        elif choice == "2":
            if os.path.exists("records.txt"):
                with open("records.txt", "r") as f:
                    for line in f:
                        name, age, score = line.strip().split(",")
                        print(f"Name: {name} | Age: {age} | Score: {score}")
            else:
                print("No records yet.")
        elif choice == "3":
            count = 0
            if os.path.exists("records.txt"):
                with open("records.txt", "r") as f:
                    count = sum(1 for line in f if line.strip())
            print("Total records:", count)
        elif choice == "4":
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    choice = input("Enter question number (1-30) or 'all': ").strip().lower()
    if choice == "all":
        for i in range(1, 31):
            print(f"\n--- Question {i} ---")
            globals()[f"q{i}"]()
    elif choice.isdigit() and 1 <= int(choice) <= 30:
        globals()[f"q{choice}"]()
    else:
        print("Invalid choice.")Name = "Moses"
Age = 19
Height = "6ft"
Status = "Student"

print("Q1",Name)
print("Q1",Age)
print("Q1",Height)
print("Q1",Status)

a, b = 10, 3
x, y = 4.5, 1.5
print("Q2","Addition:", a + b, x + y)
print("Q2","Subtraction:", a - b, x - y)
print("Q2","Multiplication:", a * b, x * y)
print("Q2","Division:", a / b, x / y)

Name = input("Enter your name: ")
Age = int(input("Enter your age: "))
colour = input("Enter your favourite colour: ")

print("Q3",f"My name is {Name}, I am {Age} years old and my favourite colour is {colour}.")

num = 10
num2 = 20.29
name = "Ada"
Value = True

print("Q4",num, type(num), num2, type(num2), (name, type(name), (Value, type(Value))))

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Q5","Sum:", a + b)
print("Q5","Product:", a * b)
print("Q5","Difference:", a - b)

name = "Chidi"
s1, s2, s3, s4, s5 = 70, 65, 80, 55, 90
status = "Passed"
total = s1 + s2 + s3 + s4 + s5
average = total / 5
print("Q6","Name:", name)
print("Q6","Scores:", s1, s2, s3, s4, s5)
print("Q6","Status:", status)
print("Q6","Total:", total)
print("Q6","Average:", average)

fruits = ["apple", "banana", "mango", "orange", "pear", "grape", "pineapple", "guava", "lemon", "papaya"]
print("Q7","First:", fruits[0])
print("Q7","Last:", fruits[-1])
print("Q7","Total items:", len(fruits))

students = ["Ade", "Bola", "Chidi", "Dayo", "Emeka"]
students.append(input("Enter another student's name: "))
print("Q8","Updated list:", students)

Number =[1,2,3,4,5,6,7,8,9,10]
print("Q9","Even numbers:", [n for n in Number if n % 2 == 0])

nums = [15, 8, 25, 40, 12, 30, 5, 18]
largest = nums[0]
smallest = nums[0]
total = 0
for n in nums:
  if n > largest:
        largest = n
  if n < smallest:
       smallest = n
total += n
print("Q10","Largest:", largest)
print("Q10","Smallest:", smallest)
print("Q10","Sum:", total)

shopping = ["bread", "milk", "eggs", "rice", "sugar"]
for _ in range(2):
shopping.append(input("Add a product: "))
item = input("Enter a product to remove: ")
if item in shopping:
  shopping.remove(item)
else:
print("Product not found.")
print("Q11","Final shopping list:", shopping)


numbers = [5, 12, 18, 23, 7, 30, 41, 9, 15, 2]
n = int(input("Enter a number: "))
if n in numbers:
print(f"{n} exists at position (index) {numbers.index(n)}")
else:
print("Q12", f"{n} is not in the list.")

student = {"name": "Ada", "age": 20, "gender": "Female","department": "Computer Science", "matric_no": "CSC/2024/001"}
for key, value in student.items():
print("Q13", f"{key}: {value}")

products = {"Bread": 800, "Milk": 1200, "Rice": 5000, "Eggs": 2500, "Sugar": 1500}
for name, price in products.items():
print("Q14", f"{name}: {price}")

student = {"name": "Ada", "age": 20, "score": 65}
student["score"] = int(input("Enter the new score: "))
print("Q15", "Updated information:", student)

scores = {"Ade": 67, "Bola": 82, "Chidi": 75, "Dayo": 90, "Emeka": 58}
top_name, top_score = None, -1
for name, score in scores.items():
if score > top_score:
top_name, top_score = name, score
print("Q16", f"Highest score: {top_name} with {top_score}")

account = {"account_name": "Ada Obi", "account_number": "1234567890", "balance": 10000.0}
choice = input("Type 'deposit' or 'withdraw': ").strip().lower()
amount = float(input("Enter amount: "))
if choice == "deposit":
account["balance"] += amount
elif choice == "withdraw":
if amount <= account["balance"]:
account["balance"] -= amount
else:
    print("Insufficient funds.")
else:
    print("Invalid choice.")
print("Q17","Current balance:", account["balance"])

numbers = {10, 20, 30, 10, 40, 20, 50, 30}
print("Q18",numbers)

class_a = {"Ade", "Bola", "Chidi", "Dayo"}
class_b = {"Chidi", "Emeka", "Dayo", "Funke"}
print("Q19","Students in both classes:", class_a & class_b)

a = set(range(1, 11))
b = set(range(5, 16))
print("Q20","All elements:", a | b)
print("Q20","Common elements:", a & b)
print("Q20", "In first but not second:", a - b)

days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
print("Q21","First day:", days[0])
print("Q21","Last day:", days[-1])
print("Q21","Number of days:", len(days))
print("Q21","Saturday exists:", "Saturday" in days)

students = ("Ade", "Bola", "Chidi", "Dayo", "Emeka")
lst = list(students)
lst.append("Funke")
lst.append("Gozie")
lst.remove("Bola")
students = tuple(lst)
print("Q22",students)


with open("students.txt", "w") as f:
   f.write("Name: Ada\nAge: 20\nDepartment: Computer Science\n")
print("Q23","students.txt created.")


names = ["Ade", "Bola", "Chidi", "Dayo", "Emeka"]
with open("students.txt", "w") as f:  # "w" replaces previous content
for n in names:
     f.write(n + "\n")
print("Q24","students.txt overwritten with five names.")


with open("students.txt", "a") as f:  # "a" keeps previous content
for n in ["Funke", "Gozie", "Hauwa"]:
     f.write(n + "\n")
print("Q25","Three names appended.")


try:
with open("students.txt", "r") as f:
   print(f.read())
except FileNotFoundError:
print("Q26","students.txt not found. Run q23 first.")


sentences = ["Today was a good day.", "I learned about Python files.", "I wrote some code.", "I fixed a few bugs.", "Tomorrow I will practise more."]
with open("diary.txt", "w") as f:
for s in sentences:
f.write(s + "\n")
with open("diary.txt", "r") as f:
print("Q27:", f.read())

name = input("Enter your name: ")
language = input("Enter your favourite programming language: ")
with open("profile.txt", "a") as f:
f.write(f"{name} - {language}\n")
print("Q28","Saved to profile.txt.")


if not os.path.exists("numbers.txt"):  # create sample data if missing
with open("numbers.txt", "w") as f:
f.write("10\n20\n30\n40\n")
total = 0
with open("numbers.txt", "r") as f:
for line in f:
line = line.strip()
if line:
total += float(line)
print("Q29","Sum of numbers:", total)

    while True:
        print("\n1. Add student record\n2. View all records\n3. Count records\n4. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            name = input("Name: ")
            age = input("Age: ")
            score = input("Exam score: ")
            with open("records.txt", "a") as f:
                f.write(f"{name},{age},{score}\n")
            print("Record saved.")
        elif choice == "2":
            if os.path.exists("records.txt"):
                with open("records.txt", "r") as f:
                    for line in f:
                        name, age, score = line.strip().split(",")
                        print(f"Name: {name} | Age: {age} | Score: {score}")
            else:
                print("No records yet.")
        elif choice == "3":
            count = 0
            if os.path.exists("records.txt"):
                with open("records.txt", "r") as f:
                    count = sum(1 for line in f if line.strip())
            print("Total records:", count)
        elif choice == "4":
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    choice = input("Enter question number (1-30) or 'all': ").strip().lower()
    if choice == "all":
        for i in range(1, 31):
            print(f"\n--- Question {i} ---")
            globals()[f"q{i}"]()
    elif choice.isdigit() and 1 <= int(choice) <= 30:
        globals()[f"q{choice}"]()
    else:
        print("Invalid choice.")Name = "Moses"
Age = 19
Height = "6ft"
Status = "Student"

print("Q1",Name)
print("Q1",Age)
print("Q1",Height)
print("Q1",Status)

a, b = 10, 3
x, y = 4.5, 1.5
print("Q2","Addition:", a + b, x + y)
print("Q2","Subtraction:", a - b, x - y)
print("Q2","Multiplication:", a * b, x * y)
print("Q2","Division:", a / b, x / y)

Name = input("Enter your name: ")
Age = int(input("Enter your age: "))
colour = input("Enter your favourite colour: ")

print("Q3",f"My name is {Name}, I am {Age} years old and my favourite colour is {colour}.")

num = 10
num2 = 20.29
name = "Ada"
Value = True

print("Q4",num, type(num), num2, type(num2), (name, type(name), (Value, type(Value))))

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Q5","Sum:", a + b)
print("Q5","Product:", a * b)
print("Q5","Difference:", a - b)

name = "Chidi"
s1, s2, s3, s4, s5 = 70, 65, 80, 55, 90
status = "Passed"
total = s1 + s2 + s3 + s4 + s5
average = total / 5
print("Q6","Name:", name)
print("Q6","Scores:", s1, s2, s3, s4, s5)
print("Q6","Status:", status)
print("Q6","Total:", total)
print("Q6","Average:", average)

fruits = ["apple", "banana", "mango", "orange", "pear", "grape", "pineapple", "guava", "lemon", "papaya"]
print("Q7","First:", fruits[0])
print("Q7","Last:", fruits[-1])
print("Q7","Total items:", len(fruits))

students = ["Ade", "Bola", "Chidi", "Dayo", "Emeka"]
students.append(input("Enter another student's name: "))
print("Q8","Updated list:", students)

Number =[1,2,3,4,5,6,7,8,9,10]
print("Q9","Even numbers:", [n for n in Number if n % 2 == 0])

nums = [15, 8, 25, 40, 12, 30, 5, 18]
largest = nums[0]
smallest = nums[0]
total = 0
for n in nums:
  if n > largest:
        largest = n
  if n < smallest:
       smallest = n
total += n
print("Q10","Largest:", largest)
print("Q10","Smallest:", smallest)
print("Q10","Sum:", total)

shopping = ["bread", "milk", "eggs", "rice", "sugar"]
for _ in range(2):
shopping.append(input("Add a product: "))
item = input("Enter a product to remove: ")
if item in shopping:
  shopping.remove(item)
else:
print("Product not found.")
print("Q11","Final shopping list:", shopping)


numbers = [5, 12, 18, 23, 7, 30, 41, 9, 15, 2]
n = int(input("Enter a number: "))
if n in numbers:
print(f"{n} exists at position (index) {numbers.index(n)}")
else:
print("Q12", f"{n} is not in the list.")

student = {"name": "Ada", "age": 20, "gender": "Female","department": "Computer Science", "matric_no": "CSC/2024/001"}
for key, value in student.items():
print("Q13", f"{key}: {value}")

products = {"Bread": 800, "Milk": 1200, "Rice": 5000, "Eggs": 2500, "Sugar": 1500}
for name, price in products.items():
print("Q14", f"{name}: {price}")

student = {"name": "Ada", "age": 20, "score": 65}
student["score"] = int(input("Enter the new score: "))
print("Q15", "Updated information:", student)

scores = {"Ade": 67, "Bola": 82, "Chidi": 75, "Dayo": 90, "Emeka": 58}
top_name, top_score = None, -1
for name, score in scores.items():
if score > top_score:
top_name, top_score = name, score
print("Q16", f"Highest score: {top_name} with {top_score}")

account = {"account_name": "Ada Obi", "account_number": "1234567890", "balance": 10000.0}
choice = input("Type 'deposit' or 'withdraw': ").strip().lower()
amount = float(input("Enter amount: "))
if choice == "deposit":
account["balance"] += amount
elif choice == "withdraw":
if amount <= account["balance"]:
account["balance"] -= amount
else:
    print("Insufficient funds.")
else:
    print("Invalid choice.")
print("Q17","Current balance:", account["balance"])

numbers = {10, 20, 30, 10, 40, 20, 50, 30}
print("Q18",numbers)

class_a = {"Ade", "Bola", "Chidi", "Dayo"}
class_b = {"Chidi", "Emeka", "Dayo", "Funke"}
print("Q19","Students in both classes:", class_a & class_b)

a = set(range(1, 11))
b = set(range(5, 16))
print("Q20","All elements:", a | b)
print("Q20","Common elements:", a & b)
print("Q20", "In first but not second:", a - b)

days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
print("Q21","First day:", days[0])
print("Q21","Last day:", days[-1])
print("Q21","Number of days:", len(days))
print("Q21","Saturday exists:", "Saturday" in days)

students = ("Ade", "Bola", "Chidi", "Dayo", "Emeka")
lst = list(students)
lst.append("Funke")
lst.append("Gozie")
lst.remove("Bola")
students = tuple(lst)
print("Q22",students)


with open("students.txt", "w") as f:
   f.write("Name: Ada\nAge: 20\nDepartment: Computer Science\n")
print("Q23","students.txt created.")


names = ["Ade", "Bola", "Chidi", "Dayo", "Emeka"]
with open("students.txt", "w") as f:  # "w" replaces previous content
for n in names:
     f.write(n + "\n")
print("Q24","students.txt overwritten with five names.")


with open("students.txt", "a") as f:  # "a" keeps previous content
for n in ["Funke", "Gozie", "Hauwa"]:
     f.write(n + "\n")
print("Q25","Three names appended.")


try:
with open("students.txt", "r") as f:
   print(f.read())
except FileNotFoundError:
print("Q26","students.txt not found. Run q23 first.")


sentences = ["Today was a good day.", "I learned about Python files.", "I wrote some code.", "I fixed a few bugs.", "Tomorrow I will practise more."]
with open("diary.txt", "w") as f:
for s in sentences:
f.write(s + "\n")
with open("diary.txt", "r") as f:
print("Q27:", f.read())

name = input("Enter your name: ")
language = input("Enter your favourite programming language: ")
with open("profile.txt", "a") as f:
f.write(f"{name} - {language}\n")
print("Q28","Saved to profile.txt.")


if not os.path.exists("numbers.txt"):  # create sample data if missing
with open("numbers.txt", "w") as f:
f.write("10\n20\n30\n40\n")
total = 0
with open("numbers.txt", "r") as f:
for line in f:
line = line.strip()
if line:
total += float(line)
print("Q29","Sum of numbers:", total)

    while True:
        print("\n1. Add student record\n2. View all records\n3. Count records\n4. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            name = input("Name: ")
            age = input("Age: ")
            score = input("Exam score: ")
            with open("records.txt", "a") as f:
                f.write(f"{name},{age},{score}\n")
            print("Record saved.")
        elif choice == "2":
            if os.path.exists("records.txt"):
                with open("records.txt", "r") as f:
                    for line in f:
                        name, age, score = line.strip().split(",")
                        print(f"Name: {name} | Age: {age} | Score: {score}")
            else:
                print("No records yet.")
        elif choice == "3":
            count = 0
            if os.path.exists("records.txt"):
                with open("records.txt", "r") as f:
                    count = sum(1 for line in f if line.strip())
            print("Total records:", count)
        elif choice == "4":
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    choice = input("Enter question number (1-30) or 'all': ").strip().lower()
    if choice == "all":
        for i in range(1, 31):
            print(f"\n--- Question {i} ---")
            globals()[f"q{i}"]()
    elif choice.isdigit() and 1 <= int(choice) <= 30:
        globals()[f"q{choice}"]()
    else:
        print("Invalid choice.")Name = "Moses"
Age = 19
Height = "6ft"
Status = "Student"

print("Q1",Name)
print("Q1",Age)
print("Q1",Height)
print("Q1",Status)

a, b = 10, 3
x, y = 4.5, 1.5
print("Q2","Addition:", a + b, x + y)
print("Q2","Subtraction:", a - b, x - y)
print("Q2","Multiplication:", a * b, x * y)
print("Q2","Division:", a / b, x / y)

Name = input("Enter your name: ")
Age = int(input("Enter your age: "))
colour = input("Enter your favourite colour: ")

print("Q3",f"My name is {Name}, I am {Age} years old and my favourite colour is {colour}.")

num = 10
num2 = 20.29
name = "Ada"
Value = True

print("Q4",num, type(num), num2, type(num2), (name, type(name), (Value, type(Value))))

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Q5","Sum:", a + b)
print("Q5","Product:", a * b)
print("Q5","Difference:", a - b)

name = "Chidi"
s1, s2, s3, s4, s5 = 70, 65, 80, 55, 90
status = "Passed"
total = s1 + s2 + s3 + s4 + s5
average = total / 5
print("Q6","Name:", name)
print("Q6","Scores:", s1, s2, s3, s4, s5)
print("Q6","Status:", status)
print("Q6","Total:", total)
print("Q6","Average:", average)

fruits = ["apple", "banana", "mango", "orange", "pear", "grape", "pineapple", "guava", "lemon", "papaya"]
print("Q7","First:", fruits[0])
print("Q7","Last:", fruits[-1])
print("Q7","Total items:", len(fruits))

students = ["Ade", "Bola", "Chidi", "Dayo", "Emeka"]
students.append(input("Enter another student's name: "))
print("Q8","Updated list:", students)

Number =[1,2,3,4,5,6,7,8,9,10]
print("Q9","Even numbers:", [n for n in Number if n % 2 == 0])

nums = [15, 8, 25, 40, 12, 30, 5, 18]
largest = nums[0]
smallest = nums[0]
total = 0
for n in nums:
  if n > largest:
        largest = n
  if n < smallest:
       smallest = n
total += n
print("Q10","Largest:", largest)
print("Q10","Smallest:", smallest)
print("Q10","Sum:", total)

shopping = ["bread", "milk", "eggs", "rice", "sugar"]
for _ in range(2):
shopping.append(input("Add a product: "))
item = input("Enter a product to remove: ")
if item in shopping:
  shopping.remove(item)
else:
print("Product not found.")
print("Q11","Final shopping list:", shopping)


numbers = [5, 12, 18, 23, 7, 30, 41, 9, 15, 2]
n = int(input("Enter a number: "))
if n in numbers:
print(f"{n} exists at position (index) {numbers.index(n)}")
else:
print("Q12", f"{n} is not in the list.")

student = {"name": "Ada", "age": 20, "gender": "Female","department": "Computer Science", "matric_no": "CSC/2024/001"}
for key, value in student.items():
print("Q13", f"{key}: {value}")

products = {"Bread": 800, "Milk": 1200, "Rice": 5000, "Eggs": 2500, "Sugar": 1500}
for name, price in products.items():
print("Q14", f"{name}: {price}")

student = {"name": "Ada", "age": 20, "score": 65}
student["score"] = int(input("Enter the new score: "))
print("Q15", "Updated information:", student)

scores = {"Ade": 67, "Bola": 82, "Chidi": 75, "Dayo": 90, "Emeka": 58}
top_name, top_score = None, -1
for name, score in scores.items():
if score > top_score:
top_name, top_score = name, score
print("Q16", f"Highest score: {top_name} with {top_score}")

account = {"account_name": "Ada Obi", "account_number": "1234567890", "balance": 10000.0}
choice = input("Type 'deposit' or 'withdraw': ").strip().lower()
amount = float(input("Enter amount: "))
if choice == "deposit":
account["balance"] += amount
elif choice == "withdraw":
if amount <= account["balance"]:
account["balance"] -= amount
else:
    print("Insufficient funds.")
else:
    print("Invalid choice.")
print("Q17","Current balance:", account["balance"])

numbers = {10, 20, 30, 10, 40, 20, 50, 30}
print("Q18",numbers)

class_a = {"Ade", "Bola", "Chidi", "Dayo"}
class_b = {"Chidi", "Emeka", "Dayo", "Funke"}
print("Q19","Students in both classes:", class_a & class_b)

a = set(range(1, 11))
b = set(range(5, 16))
print("Q20","All elements:", a | b)
print("Q20","Common elements:", a & b)
print("Q20", "In first but not second:", a - b)

days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
print("Q21","First day:", days[0])
print("Q21","Last day:", days[-1])
print("Q21","Number of days:", len(days))
print("Q21","Saturday exists:", "Saturday" in days)

students = ("Ade", "Bola", "Chidi", "Dayo", "Emeka")
lst = list(students)
lst.append("Funke")
lst.append("Gozie")
lst.remove("Bola")
students = tuple(lst)
print("Q22",students)


with open("students.txt", "w") as f:
   f.write("Name: Ada\nAge: 20\nDepartment: Computer Science\n")
print("Q23","students.txt created.")


names = ["Ade", "Bola", "Chidi", "Dayo", "Emeka"]
with open("students.txt", "w") as f:  # "w" replaces previous content
for n in names:
     f.write(n + "\n")
print("Q24","students.txt overwritten with five names.")


with open("students.txt", "a") as f:  # "a" keeps previous content
for n in ["Funke", "Gozie", "Hauwa"]:
     f.write(n + "\n")
print("Q25","Three names appended.")


try:
with open("students.txt", "r") as f:
   print(f.read())
except FileNotFoundError:
print("Q26","students.txt not found. Run q23 first.")


sentences = ["Today was a good day.", "I learned about Python files.", "I wrote some code.", "I fixed a few bugs.", "Tomorrow I will practise more."]
with open("diary.txt", "w") as f:
for s in sentences:
f.write(s + "\n")
with open("diary.txt", "r") as f:
print("Q27:", f.read())

name = input("Enter your name: ")
language = input("Enter your favourite programming language: ")
with open("profile.txt", "a") as f:
f.write(f"{name} - {language}\n")
print("Q28","Saved to profile.txt.")


if not os.path.exists("numbers.txt"):  # create sample data if missing
with open("numbers.txt", "w") as f:
f.write("10\n20\n30\n40\n")
total = 0
with open("numbers.txt", "r") as f:
for line in f:
line = line.strip()
if line:
total += float(line)
print("Q29","Sum of numbers:", total)

    while True:
        print("\n1. Add student record\n2. View all records\n3. Count records\n4. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            name = input("Name: ")
            age = input("Age: ")
            score = input("Exam score: ")
            with open("records.txt", "a") as f:
                f.write(f"{name},{age},{score}\n")
            print("Record saved.")
        elif choice == "2":
            if os.path.exists("records.txt"):
                with open("records.txt", "r") as f:
                    for line in f:
                        name, age, score = line.strip().split(",")
                        print(f"Name: {name} | Age: {age} | Score: {score}")
            else:
                print("No records yet.")
        elif choice == "3":
            count = 0
            if os.path.exists("records.txt"):
                with open("records.txt", "r") as f:
                    count = sum(1 for line in f if line.strip())
            print("Total records:", count)
        elif choice == "4":
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    choice = input("Enter question number (1-30) or 'all': ").strip().lower()
    if choice == "all":
        for i in range(1, 31):
            print(f"\n--- Question {i} ---")
            globals()[f"q{i}"]()
    elif choice.isdigit() and 1 <= int(choice) <= 30:
        globals()[f"q{choice}"]()
    else:
        print("Invalid choice.")Name = "Moses"
Age = 19
Height = "6ft"
Status = "Student"

print("Q1",Name)
print("Q1",Age)
print("Q1",Height)
print("Q1",Status)

a, b = 10, 3
x, y = 4.5, 1.5
print("Q2","Addition:", a + b, x + y)
print("Q2","Subtraction:", a - b, x - y)
print("Q2","Multiplication:", a * b, x * y)
print("Q2","Division:", a / b, x / y)

Name = input("Enter your name: ")
Age = int(input("Enter your age: "))
colour = input("Enter your favourite colour: ")

print("Q3",f"My name is {Name}, I am {Age} years old and my favourite colour is {colour}.")

num = 10
num2 = 20.29
name = "Ada"
Value = True

print("Q4",num, type(num), num2, type(num2), (name, type(name), (Value, type(Value))))

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Q5","Sum:", a + b)
print("Q5","Product:", a * b)
print("Q5","Difference:", a - b)

name = "Chidi"
s1, s2, s3, s4, s5 = 70, 65, 80, 55, 90
status = "Passed"
total = s1 + s2 + s3 + s4 + s5
average = total / 5
print("Q6","Name:", name)
print("Q6","Scores:", s1, s2, s3, s4, s5)
print("Q6","Status:", status)
print("Q6","Total:", total)
print("Q6","Average:", average)

fruits = ["apple", "banana", "mango", "orange", "pear", "grape", "pineapple", "guava", "lemon", "papaya"]
print("Q7","First:", fruits[0])
print("Q7","Last:", fruits[-1])
print("Q7","Total items:", len(fruits))

students = ["Ade", "Bola", "Chidi", "Dayo", "Emeka"]
students.append(input("Enter another student's name: "))
print("Q8","Updated list:", students)

Number =[1,2,3,4,5,6,7,8,9,10]
print("Q9","Even numbers:", [n for n in Number if n % 2 == 0])

nums = [15, 8, 25, 40, 12, 30, 5, 18]
largest = nums[0]
smallest = nums[0]
total = 0
for n in nums:
  if n > largest:
        largest = n
  if n < smallest:
       smallest = n
total += n
print("Q10","Largest:", largest)
print("Q10","Smallest:", smallest)
print("Q10","Sum:", total)

shopping = ["bread", "milk", "eggs", "rice", "sugar"]
for _ in range(2):
shopping.append(input("Add a product: "))
item = input("Enter a product to remove: ")
if item in shopping:
  shopping.remove(item)
else:
print("Product not found.")
print("Q11","Final shopping list:", shopping)


numbers = [5, 12, 18, 23, 7, 30, 41, 9, 15, 2]
n = int(input("Enter a number: "))
if n in numbers:
print(f"{n} exists at position (index) {numbers.index(n)}")
else:
print("Q12", f"{n} is not in the list.")

student = {"name": "Ada", "age": 20, "gender": "Female","department": "Computer Science", "matric_no": "CSC/2024/001"}
for key, value in student.items():
print("Q13", f"{key}: {value}")

products = {"Bread": 800, "Milk": 1200, "Rice": 5000, "Eggs": 2500, "Sugar": 1500}
for name, price in products.items():
print("Q14", f"{name}: {price}")

student = {"name": "Ada", "age": 20, "score": 65}
student["score"] = int(input("Enter the new score: "))
print("Q15", "Updated information:", student)

scores = {"Ade": 67, "Bola": 82, "Chidi": 75, "Dayo": 90, "Emeka": 58}
top_name, top_score = None, -1
for name, score in scores.items():
if score > top_score:
top_name, top_score = name, score
print("Q16", f"Highest score: {top_name} with {top_score}")

account = {"account_name": "Ada Obi", "account_number": "1234567890", "balance": 10000.0}
choice = input("Type 'deposit' or 'withdraw': ").strip().lower()
amount = float(input("Enter amount: "))
if choice == "deposit":
account["balance"] += amount
elif choice == "withdraw":
if amount <= account["balance"]:
account["balance"] -= amount
else:
    print("Insufficient funds.")
else:
    print("Invalid choice.")
print("Q17","Current balance:", account["balance"])

numbers = {10, 20, 30, 10, 40, 20, 50, 30}
print("Q18",numbers)

class_a = {"Ade", "Bola", "Chidi", "Dayo"}
class_b = {"Chidi", "Emeka", "Dayo", "Funke"}
print("Q19","Students in both classes:", class_a & class_b)

a = set(range(1, 11))
b = set(range(5, 16))
print("Q20","All elements:", a | b)
print("Q20","Common elements:", a & b)
print("Q20", "In first but not second:", a - b)

days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
print("Q21","First day:", days[0])
print("Q21","Last day:", days[-1])
print("Q21","Number of days:", len(days))
print("Q21","Saturday exists:", "Saturday" in days)

students = ("Ade", "Bola", "Chidi", "Dayo", "Emeka")
lst = list(students)
lst.append("Funke")
lst.append("Gozie")
lst.remove("Bola")
students = tuple(lst)
print("Q22",students)


with open("students.txt", "w") as f:
   f.write("Name: Ada\nAge: 20\nDepartment: Computer Science\n")
print("Q23","students.txt created.")


names = ["Ade", "Bola", "Chidi", "Dayo", "Emeka"]
with open("students.txt", "w") as f:  # "w" replaces previous content
for n in names:
     f.write(n + "\n")
print("Q24","students.txt overwritten with five names.")


with open("students.txt", "a") as f:  # "a" keeps previous content
for n in ["Funke", "Gozie", "Hauwa"]:
     f.write(n + "\n")
print("Q25","Three names appended.")


try:
with open("students.txt", "r") as f:
   print(f.read())
except FileNotFoundError:
print("Q26","students.txt not found. Run q23 first.")


sentences = ["Today was a good day.", "I learned about Python files.", "I wrote some code.", "I fixed a few bugs.", "Tomorrow I will practise more."]
with open("diary.txt", "w") as f:
for s in sentences:
f.write(s + "\n")
with open("diary.txt", "r") as f:
print("Q27:", f.read())

name = input("Enter your name: ")
language = input("Enter your favourite programming language: ")
with open("profile.txt", "a") as f:
f.write(f"{name} - {language}\n")
print("Q28","Saved to profile.txt.")


if not os.path.exists("numbers.txt"):  # create sample data if missing
with open("numbers.txt", "w") as f:
f.write("10\n20\n30\n40\n")
total = 0
with open("numbers.txt", "r") as f:
for line in f:
line = line.strip()
if line:
total += float(line)
print("Q29","Sum of numbers:", total)

    while True:
        print("\n1. Add student record\n2. View all records\n3. Count records\n4. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            name = input("Name: ")
            age = input("Age: ")
            score = input("Exam score: ")
            with open("records.txt", "a") as f:
                f.write(f"{name},{age},{score}\n")
            print("Record saved.")
        elif choice == "2":
            if os.path.exists("records.txt"):
                with open("records.txt", "r") as f:
                    for line in f:
                        name, age, score = line.strip().split(",")
                        print(f"Name: {name} | Age: {age} | Score: {score}")
            else:
                print("No records yet.")
        elif choice == "3":
            count = 0
            if os.path.exists("records.txt"):
                with open("records.txt", "r") as f:
                    count = sum(1 for line in f if line.strip())
            print("Total records:", count)
        elif choice == "4":
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    choice = input("Enter question number (1-30) or 'all': ").strip().lower()
    if choice == "all":
        for i in range(1, 31):
            print(f"\n--- Question {i} ---")
            globals()[f"q{i}"]()
    elif choice.isdigit() and 1 <= int(choice) <= 30:
        globals()[f"q{choice}"]()
    else:
        print("Invalid choice.")Name = "Moses"
Age = 19
Height = "6ft"
Status = "Student"

print("Q1",Name)
print("Q1",Age)
print("Q1",Height)
print("Q1",Status)

a, b = 10, 3
x, y = 4.5, 1.5
print("Q2","Addition:", a + b, x + y)
print("Q2","Subtraction:", a - b, x - y)
print("Q2","Multiplication:", a * b, x * y)
print("Q2","Division:", a / b, x / y)

Name = input("Enter your name: ")
Age = int(input("Enter your age: "))
colour = input("Enter your favourite colour: ")

print("Q3",f"My name is {Name}, I am {Age} years old and my favourite colour is {colour}.")

num = 10
num2 = 20.29
name = "Ada"
Value = True

print("Q4",num, type(num), num2, type(num2), (name, type(name), (Value, type(Value))))

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Q5","Sum:", a + b)
print("Q5","Product:", a * b)
print("Q5","Difference:", a - b)

name = "Chidi"
s1, s2, s3, s4, s5 = 70, 65, 80, 55, 90
status = "Passed"
total = s1 + s2 + s3 + s4 + s5
average = total / 5
print("Q6","Name:", name)
print("Q6","Scores:", s1, s2, s3, s4, s5)
print("Q6","Status:", status)
print("Q6","Total:", total)
print("Q6","Average:", average)

fruits = ["apple", "banana", "mango", "orange", "pear", "grape", "pineapple", "guava", "lemon", "papaya"]
print("Q7","First:", fruits[0])
print("Q7","Last:", fruits[-1])
print("Q7","Total items:", len(fruits))

students = ["Ade", "Bola", "Chidi", "Dayo", "Emeka"]
students.append(input("Enter another student's name: "))
print("Q8","Updated list:", students)

Number =[1,2,3,4,5,6,7,8,9,10]
print("Q9","Even numbers:", [n for n in Number if n % 2 == 0])

nums = [15, 8, 25, 40, 12, 30, 5, 18]
largest = nums[0]
smallest = nums[0]
total = 0
for n in nums:
  if n > largest:
        largest = n
  if n < smallest:
       smallest = n
total += n
print("Q10","Largest:", largest)
print("Q10","Smallest:", smallest)
print("Q10","Sum:", total)

shopping = ["bread", "milk", "eggs", "rice", "sugar"]
for _ in range(2):
shopping.append(input("Add a product: "))
item = input("Enter a product to remove: ")
if item in shopping:
  shopping.remove(item)
else:
print("Product not found.")
print("Q11","Final shopping list:", shopping)


numbers = [5, 12, 18, 23, 7, 30, 41, 9, 15, 2]
n = int(input("Enter a number: "))
if n in numbers:
print(f"{n} exists at position (index) {numbers.index(n)}")
else:
print("Q12", f"{n} is not in the list.")

student = {"name": "Ada", "age": 20, "gender": "Female","department": "Computer Science", "matric_no": "CSC/2024/001"}
for key, value in student.items():
print("Q13", f"{key}: {value}")

products = {"Bread": 800, "Milk": 1200, "Rice": 5000, "Eggs": 2500, "Sugar": 1500}
for name, price in products.items():
print("Q14", f"{name}: {price}")

student = {"name": "Ada", "age": 20, "score": 65}
student["score"] = int(input("Enter the new score: "))
print("Q15", "Updated information:", student)

scores = {"Ade": 67, "Bola": 82, "Chidi": 75, "Dayo": 90, "Emeka": 58}
top_name, top_score = None, -1
for name, score in scores.items():
if score > top_score:
top_name, top_score = name, score
print("Q16", f"Highest score: {top_name} with {top_score}")

account = {"account_name": "Ada Obi", "account_number": "1234567890", "balance": 10000.0}
choice = input("Type 'deposit' or 'withdraw': ").strip().lower()
amount = float(input("Enter amount: "))
if choice == "deposit":
account["balance"] += amount
elif choice == "withdraw":
if amount <= account["balance"]:
account["balance"] -= amount
else:
    print("Insufficient funds.")
else:
    print("Invalid choice.")
print("Q17","Current balance:", account["balance"])

numbers = {10, 20, 30, 10, 40, 20, 50, 30}
print("Q18",numbers)

class_a = {"Ade", "Bola", "Chidi", "Dayo"}
class_b = {"Chidi", "Emeka", "Dayo", "Funke"}
print("Q19","Students in both classes:", class_a & class_b)

a = set(range(1, 11))
b = set(range(5, 16))
print("Q20","All elements:", a | b)
print("Q20","Common elements:", a & b)
print("Q20", "In first but not second:", a - b)

days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
print("Q21","First day:", days[0])
print("Q21","Last day:", days[-1])
print("Q21","Number of days:", len(days))
print("Q21","Saturday exists:", "Saturday" in days)

students = ("Ade", "Bola", "Chidi", "Dayo", "Emeka")
lst = list(students)
lst.append("Funke")
lst.append("Gozie")
lst.remove("Bola")
students = tuple(lst)
print("Q22",students)


with open("students.txt", "w") as f:
   f.write("Name: Ada\nAge: 20\nDepartment: Computer Science\n")
print("Q23","students.txt created.")


names = ["Ade", "Bola", "Chidi", "Dayo", "Emeka"]
with open("students.txt", "w") as f:  # "w" replaces previous content
for n in names:
     f.write(n + "\n")
print("Q24","students.txt overwritten with five names.")


with open("students.txt", "a") as f:  # "a" keeps previous content
for n in ["Funke", "Gozie", "Hauwa"]:
     f.write(n + "\n")
print("Q25","Three names appended.")


try:
with open("students.txt", "r") as f:
   print(f.read())
except FileNotFoundError:
print("Q26","students.txt not found. Run q23 first.")


sentences = ["Today was a good day.", "I learned about Python files.", "I wrote some code.", "I fixed a few bugs.", "Tomorrow I will practise more."]
with open("diary.txt", "w") as f:
for s in sentences:
f.write(s + "\n")
with open("diary.txt", "r") as f:
print("Q27:", f.read())

name = input("Enter your name: ")
language = input("Enter your favourite programming language: ")
with open("profile.txt", "a") as f:
f.write(f"{name} - {language}\n")
print("Q28","Saved to profile.txt.")


if not os.path.exists("numbers.txt"):  # create sample data if missing
with open("numbers.txt", "w") as f:
f.write("10\n20\n30\n40\n")
total = 0
with open("numbers.txt", "r") as f:
for line in f:
line = line.strip()
if line:
total += float(line)
print("Q29","Sum of numbers:", total)

    while True:
        print("\n1. Add student record\n2. View all records\n3. Count records\n4. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            name = input("Name: ")
            age = input("Age: ")
            score = input("Exam score: ")
            with open("records.txt", "a") as f:
                f.write(f"{name},{age},{score}\n")
            print("Record saved.")
        elif choice == "2":
            if os.path.exists("records.txt"):
                with open("records.txt", "r") as f:
                    for line in f:
                        name, age, score = line.strip().split(",")
                        print(f"Name: {name} | Age: {age} | Score: {score}")
            else:
                print("No records yet.")
        elif choice == "3":
            count = 0
            if os.path.exists("records.txt"):
                with open("records.txt", "r") as f:
                    count = sum(1 for line in f if line.strip())
            print("Total records:", count)
        elif choice == "4":
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    choice = input("Enter question number (1-30) or 'all': ").strip().lower()
    if choice == "all":
        for i in range(1, 31):
            print(f"\n--- Question {i} ---")
            globals()[f"q{i}"]()
    elif choice.isdigit() and 1 <= int(choice) <= 30:
        globals()[f"q{choice}"]()
    else:
        print("Invalid choice.")Name = "Moses"
Age = 19
Height = "6ft"
Status = "Student"

print("Q1",Name)
print("Q1",Age)
print("Q1",Height)
print("Q1",Status)

a, b = 10, 3
x, y = 4.5, 1.5
print("Q2","Addition:", a + b, x + y)
print("Q2","Subtraction:", a - b, x - y)
print("Q2","Multiplication:", a * b, x * y)
print("Q2","Division:", a / b, x / y)

Name = input("Enter your name: ")
Age = int(input("Enter your age: "))
colour = input("Enter your favourite colour: ")

print("Q3",f"My name is {Name}, I am {Age} years old and my favourite colour is {colour}.")

num = 10
num2 = 20.29
name = "Ada"
Value = True

print("Q4",num, type(num), num2, type(num2), (name, type(name), (Value, type(Value))))

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Q5","Sum:", a + b)
print("Q5","Product:", a * b)
print("Q5","Difference:", a - b)

name = "Chidi"
s1, s2, s3, s4, s5 = 70, 65, 80, 55, 90
status = "Passed"
total = s1 + s2 + s3 + s4 + s5
average = total / 5
print("Q6","Name:", name)
print("Q6","Scores:", s1, s2, s3, s4, s5)
print("Q6","Status:", status)
print("Q6","Total:", total)
print("Q6","Average:", average)

fruits = ["apple", "banana", "mango", "orange", "pear", "grape", "pineapple", "guava", "lemon", "papaya"]
print("Q7","First:", fruits[0])
print("Q7","Last:", fruits[-1])
print("Q7","Total items:", len(fruits))

students = ["Ade", "Bola", "Chidi", "Dayo", "Emeka"]
students.append(input("Enter another student's name: "))
print("Q8","Updated list:", students)

Number =[1,2,3,4,5,6,7,8,9,10]
print("Q9","Even numbers:", [n for n in Number if n % 2 == 0])

nums = [15, 8, 25, 40, 12, 30, 5, 18]
largest = nums[0]
smallest = nums[0]
total = 0
for n in nums:
  if n > largest:
        largest = n
  if n < smallest:
       smallest = n
total += n
print("Q10","Largest:", largest)
print("Q10","Smallest:", smallest)
print("Q10","Sum:", total)

shopping = ["bread", "milk", "eggs", "rice", "sugar"]
for _ in range(2):
shopping.append(input("Add a product: "))
item = input("Enter a product to remove: ")
if item in shopping:
  shopping.remove(item)
else:
print("Product not found.")
print("Q11","Final shopping list:", shopping)


numbers = [5, 12, 18, 23, 7, 30, 41, 9, 15, 2]
n = int(input("Enter a number: "))
if n in numbers:
print(f"{n} exists at position (index) {numbers.index(n)}")
else:
print("Q12", f"{n} is not in the list.")

student = {"name": "Ada", "age": 20, "gender": "Female","department": "Computer Science", "matric_no": "CSC/2024/001"}
for key, value in student.items():
print("Q13", f"{key}: {value}")

products = {"Bread": 800, "Milk": 1200, "Rice": 5000, "Eggs": 2500, "Sugar": 1500}
for name, price in products.items():
print("Q14", f"{name}: {price}")

student = {"name": "Ada", "age": 20, "score": 65}
student["score"] = int(input("Enter the new score: "))
print("Q15", "Updated information:", student)

scores = {"Ade": 67, "Bola": 82, "Chidi": 75, "Dayo": 90, "Emeka": 58}
top_name, top_score = None, -1
for name, score in scores.items():
if score > top_score:
top_name, top_score = name, score
print("Q16", f"Highest score: {top_name} with {top_score}")

account = {"account_name": "Ada Obi", "account_number": "1234567890", "balance": 10000.0}
choice = input("Type 'deposit' or 'withdraw': ").strip().lower()
amount = float(input("Enter amount: "))
if choice == "deposit":
account["balance"] += amount
elif choice == "withdraw":
if amount <= account["balance"]:
account["balance"] -= amount
else:
    print("Insufficient funds.")
else:
    print("Invalid choice.")
print("Q17","Current balance:", account["balance"])

numbers = {10, 20, 30, 10, 40, 20, 50, 30}
print("Q18",numbers)

class_a = {"Ade", "Bola", "Chidi", "Dayo"}
class_b = {"Chidi", "Emeka", "Dayo", "Funke"}
print("Q19","Students in both classes:", class_a & class_b)

a = set(range(1, 11))
b = set(range(5, 16))
print("Q20","All elements:", a | b)
print("Q20","Common elements:", a & b)
print("Q20", "In first but not second:", a - b)

days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
print("Q21","First day:", days[0])
print("Q21","Last day:", days[-1])
print("Q21","Number of days:", len(days))
print("Q21","Saturday exists:", "Saturday" in days)

students = ("Ade", "Bola", "Chidi", "Dayo", "Emeka")
lst = list(students)
lst.append("Funke")
lst.append("Gozie")
lst.remove("Bola")
students = tuple(lst)
print("Q22",students)


with open("students.txt", "w") as f:
   f.write("Name: Ada\nAge: 20\nDepartment: Computer Science\n")
print("Q23","students.txt created.")


names = ["Ade", "Bola", "Chidi", "Dayo", "Emeka"]
with open("students.txt", "w") as f:  # "w" replaces previous content
for n in names:
     f.write(n + "\n")
print("Q24","students.txt overwritten with five names.")


with open("students.txt", "a") as f:  # "a" keeps previous content
for n in ["Funke", "Gozie", "Hauwa"]:
     f.write(n + "\n")
print("Q25","Three names appended.")


try:
with open("students.txt", "r") as f:
   print(f.read())
except FileNotFoundError:
print("Q26","students.txt not found. Run q23 first.")


sentences = ["Today was a good day.", "I learned about Python files.", "I wrote some code.", "I fixed a few bugs.", "Tomorrow I will practise more."]
with open("diary.txt", "w") as f:
for s in sentences:
f.write(s + "\n")
with open("diary.txt", "r") as f:
print("Q27:", f.read())

name = input("Enter your name: ")
language = input("Enter your favourite programming language: ")
with open("profile.txt", "a") as f:
f.write(f"{name} - {language}\n")
print("Q28","Saved to profile.txt.")


if not os.path.exists("numbers.txt"):  # create sample data if missing
with open("numbers.txt", "w") as f:
f.write("10\n20\n30\n40\n")
total = 0
with open("numbers.txt", "r") as f:
for line in f:
line = line.strip()
if line:
total += float(line)
print("Q29","Sum of numbers:", total)

    while True:
        print("\n1. Add student record\n2. View all records\n3. Count records\n4. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            name = input("Name: ")
            age = input("Age: ")
            score = input("Exam score: ")
            with open("records.txt", "a") as f:
                f.write(f"{name},{age},{score}\n")
            print("Record saved.")
        elif choice == "2":
            if os.path.exists("records.txt"):
                with open("records.txt", "r") as f:
                    for line in f:
                        name, age, score = line.strip().split(",")
                        print(f"Name: {name} | Age: {age} | Score: {score}")
            else:
                print("No records yet.")
        elif choice == "3":
            count = 0
            if os.path.exists("records.txt"):
                with open("records.txt", "r") as f:
                    count = sum(1 for line in f if line.strip())
            print("Total records:", count)
        elif choice == "4":
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    choice = input("Enter question number (1-30) or 'all': ").strip().lower()
    if choice == "all":
        for i in range(1, 31):
            print(f"\n--- Question {i} ---")
            globals()[f"q{i}"]()
    elif choice.isdigit() and 1 <= int(choice) <= 30:
        globals()[f"q{choice}"]()
    else:
        print("Invalid choice.")Name = "Moses"
Age = 19
Height = "6ft"
Status = "Student"

print("Q1",Name)
print("Q1",Age)
print("Q1",Height)
print("Q1",Status)

a, b = 10, 3
x, y = 4.5, 1.5
print("Q2","Addition:", a + b, x + y)
print("Q2","Subtraction:", a - b, x - y)
print("Q2","Multiplication:", a * b, x * y)
print("Q2","Division:", a / b, x / y)

Name = input("Enter your name: ")
Age = int(input("Enter your age: "))
colour = input("Enter your favourite colour: ")

print("Q3",f"My name is {Name}, I am {Age} years old and my favourite colour is {colour}.")

num = 10
num2 = 20.29
name = "Ada"
Value = True

print("Q4",num, type(num), num2, type(num2), (name, type(name), (Value, type(Value))))

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Q5","Sum:", a + b)
print("Q5","Product:", a * b)
print("Q5","Difference:", a - b)

name = "Chidi"
s1, s2, s3, s4, s5 = 70, 65, 80, 55, 90
status = "Passed"
total = s1 + s2 + s3 + s4 + s5
average = total / 5
print("Q6","Name:", name)
print("Q6","Scores:", s1, s2, s3, s4, s5)
print("Q6","Status:", status)
print("Q6","Total:", total)
print("Q6","Average:", average)

fruits = ["apple", "banana", "mango", "orange", "pear", "grape", "pineapple", "guava", "lemon", "papaya"]
print("Q7","First:", fruits[0])
print("Q7","Last:", fruits[-1])
print("Q7","Total items:", len(fruits))

students = ["Ade", "Bola", "Chidi", "Dayo", "Emeka"]
students.append(input("Enter another student's name: "))
print("Q8","Updated list:", students)

Number =[1,2,3,4,5,6,7,8,9,10]
print("Q9","Even numbers:", [n for n in Number if n % 2 == 0])

nums = [15, 8, 25, 40, 12, 30, 5, 18]
largest = nums[0]
smallest = nums[0]
total = 0
for n in nums:
  if n > largest:
        largest = n
  if n < smallest:
       smallest = n
total += n
print("Q10","Largest:", largest)
print("Q10","Smallest:", smallest)
print("Q10","Sum:", total)

shopping = ["bread", "milk", "eggs", "rice", "sugar"]
for _ in range(2):
shopping.append(input("Add a product: "))
item = input("Enter a product to remove: ")
if item in shopping:
  shopping.remove(item)
else:
print("Product not found.")
print("Q11","Final shopping list:", shopping)


numbers = [5, 12, 18, 23, 7, 30, 41, 9, 15, 2]
n = int(input("Enter a number: "))
if n in numbers:
print(f"{n} exists at position (index) {numbers.index(n)}")
else:
print("Q12", f"{n} is not in the list.")

student = {"name": "Ada", "age": 20, "gender": "Female","department": "Computer Science", "matric_no": "CSC/2024/001"}
for key, value in student.items():
print("Q13", f"{key}: {value}")

products = {"Bread": 800, "Milk": 1200, "Rice": 5000, "Eggs": 2500, "Sugar": 1500}
for name, price in products.items():
print("Q14", f"{name}: {price}")

student = {"name": "Ada", "age": 20, "score": 65}
student["score"] = int(input("Enter the new score: "))
print("Q15", "Updated information:", student)

scores = {"Ade": 67, "Bola": 82, "Chidi": 75, "Dayo": 90, "Emeka": 58}
top_name, top_score = None, -1
for name, score in scores.items():
if score > top_score:
top_name, top_score = name, score
print("Q16", f"Highest score: {top_name} with {top_score}")

account = {"account_name": "Ada Obi", "account_number": "1234567890", "balance": 10000.0}
choice = input("Type 'deposit' or 'withdraw': ").strip().lower()
amount = float(input("Enter amount: "))
if choice == "deposit":
account["balance"] += amount
elif choice == "withdraw":
if amount <= account["balance"]:
account["balance"] -= amount
else:
    print("Insufficient funds.")
else:
    print("Invalid choice.")
print("Q17","Current balance:", account["balance"])

numbers = {10, 20, 30, 10, 40, 20, 50, 30}
print("Q18",numbers)

class_a = {"Ade", "Bola", "Chidi", "Dayo"}
class_b = {"Chidi", "Emeka", "Dayo", "Funke"}
print("Q19","Students in both classes:", class_a & class_b)

a = set(range(1, 11))
b = set(range(5, 16))
print("Q20","All elements:", a | b)
print("Q20","Common elements:", a & b)
print("Q20", "In first but not second:", a - b)

days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
print("Q21","First day:", days[0])
print("Q21","Last day:", days[-1])
print("Q21","Number of days:", len(days))
print("Q21","Saturday exists:", "Saturday" in days)

students = ("Ade", "Bola", "Chidi", "Dayo", "Emeka")
lst = list(students)
lst.append("Funke")
lst.append("Gozie")
lst.remove("Bola")
students = tuple(lst)
print("Q22",students)


with open("students.txt", "w") as f:
   f.write("Name: Ada\nAge: 20\nDepartment: Computer Science\n")
print("Q23","students.txt created.")


names = ["Ade", "Bola", "Chidi", "Dayo", "Emeka"]
with open("students.txt", "w") as f:  # "w" replaces previous content
for n in names:
     f.write(n + "\n")
print("Q24","students.txt overwritten with five names.")


with open("students.txt", "a") as f:  # "a" keeps previous content
for n in ["Funke", "Gozie", "Hauwa"]:
     f.write(n + "\n")
print("Q25","Three names appended.")


try:
with open("students.txt", "r") as f:
   print(f.read())
except FileNotFoundError:
print("Q26","students.txt not found. Run q23 first.")


sentences = ["Today was a good day.", "I learned about Python files.", "I wrote some code.", "I fixed a few bugs.", "Tomorrow I will practise more."]
with open("diary.txt", "w") as f:
for s in sentences:
f.write(s + "\n")
with open("diary.txt", "r") as f:
print("Q27:", f.read())

name = input("Enter your name: ")
language = input("Enter your favourite programming language: ")
with open("profile.txt", "a") as f:
f.write(f"{name} - {language}\n")
print("Q28","Saved to profile.txt.")


if not os.path.exists("numbers.txt"):  # create sample data if missing
with open("numbers.txt", "w") as f:
f.write("10\n20\n30\n40\n")
total = 0
with open("numbers.txt", "r") as f:
for line in f:
line = line.strip()
if line:
total += float(line)
print("Q29","Sum of numbers:", total)

    while True:
        print("\n1. Add student record\n2. View all records\n3. Count records\n4. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            name = input("Name: ")
            age = input("Age: ")
            score = input("Exam score: ")
            with open("records.txt", "a") as f:
                f.write(f"{name},{age},{score}\n")
            print("Record saved.")
        elif choice == "2":
            if os.path.exists("records.txt"):
                with open("records.txt", "r") as f:
                    for line in f:
                        name, age, score = line.strip().split(",")
                        print(f"Name: {name} | Age: {age} | Score: {score}")
            else:
                print("No records yet.")
        elif choice == "3":
            count = 0
            if os.path.exists("records.txt"):
                with open("records.txt", "r") as f:
                    count = sum(1 for line in f if line.strip())
            print("Total records:", count)
        elif choice == "4":
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    choice = input("Enter question number (1-30) or 'all': ").strip().lower()
    if choice == "all":
        for i in range(1, 31):
            print(f"\n--- Question {i} ---")
            globals()[f"q{i}"]()
    elif choice.isdigit() and 1 <= int(choice) <= 30:
        globals()[f"q{choice}"]()
    else:
        print("Invalid choice.")Name = "Moses"
Age = 19
Height = "6ft"
Status = "Student"

print("Q1",Name)
print("Q1",Age)
print("Q1",Height)
print("Q1",Status)

a, b = 10, 3
x, y = 4.5, 1.5
print("Q2","Addition:", a + b, x + y)
print("Q2","Subtraction:", a - b, x - y)
print("Q2","Multiplication:", a * b, x * y)
print("Q2","Division:", a / b, x / y)

Name = input("Enter your name: ")
Age = int(input("Enter your age: "))
colour = input("Enter your favourite colour: ")

print("Q3",f"My name is {Name}, I am {Age} years old and my favourite colour is {colour}.")

num = 10
num2 = 20.29
name = "Ada"
Value = True

print("Q4",num, type(num), num2, type(num2), (name, type(name), (Value, type(Value))))

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Q5","Sum:", a + b)
print("Q5","Product:", a * b)
print("Q5","Difference:", a - b)

name = "Chidi"
s1, s2, s3, s4, s5 = 70, 65, 80, 55, 90
status = "Passed"
total = s1 + s2 + s3 + s4 + s5
average = total / 5
print("Q6","Name:", name)
print("Q6","Scores:", s1, s2, s3, s4, s5)
print("Q6","Status:", status)
print("Q6","Total:", total)
print("Q6","Average:", average)

fruits = ["apple", "banana", "mango", "orange", "pear", "grape", "pineapple", "guava", "lemon", "papaya"]
print("Q7","First:", fruits[0])
print("Q7","Last:", fruits[-1])
print("Q7","Total items:", len(fruits))

students = ["Ade", "Bola", "Chidi", "Dayo", "Emeka"]
students.append(input("Enter another student's name: "))
print("Q8","Updated list:", students)

Number =[1,2,3,4,5,6,7,8,9,10]
print("Q9","Even numbers:", [n for n in Number if n % 2 == 0])

nums = [15, 8, 25, 40, 12, 30, 5, 18]
largest = nums[0]
smallest = nums[0]
total = 0
for n in nums:
  if n > largest:
        largest = n
  if n < smallest:
       smallest = n
total += n
print("Q10","Largest:", largest)
print("Q10","Smallest:", smallest)
print("Q10","Sum:", total)

shopping = ["bread", "milk", "eggs", "rice", "sugar"]
for _ in range(2):
shopping.append(input("Add a product: "))
item = input("Enter a product to remove: ")
if item in shopping:
  shopping.remove(item)
else:
print("Product not found.")
print("Q11","Final shopping list:", shopping)


numbers = [5, 12, 18, 23, 7, 30, 41, 9, 15, 2]
n = int(input("Enter a number: "))
if n in numbers:
print(f"{n} exists at position (index) {numbers.index(n)}")
else:
print("Q12", f"{n} is not in the list.")

student = {"name": "Ada", "age": 20, "gender": "Female","department": "Computer Science", "matric_no": "CSC/2024/001"}
for key, value in student.items():
print("Q13", f"{key}: {value}")

products = {"Bread": 800, "Milk": 1200, "Rice": 5000, "Eggs": 2500, "Sugar": 1500}
for name, price in products.items():
print("Q14", f"{name}: {price}")

student = {"name": "Ada", "age": 20, "score": 65}
student["score"] = int(input("Enter the new score: "))
print("Q15", "Updated information:", student)

scores = {"Ade": 67, "Bola": 82, "Chidi": 75, "Dayo": 90, "Emeka": 58}
top_name, top_score = None, -1
for name, score in scores.items():
if score > top_score:
top_name, top_score = name, score
print("Q16", f"Highest score: {top_name} with {top_score}")

account = {"account_name": "Ada Obi", "account_number": "1234567890", "balance": 10000.0}
choice = input("Type 'deposit' or 'withdraw': ").strip().lower()
amount = float(input("Enter amount: "))
if choice == "deposit":
account["balance"] += amount
elif choice == "withdraw":
if amount <= account["balance"]:
account["balance"] -= amount
else:
    print("Insufficient funds.")
else:
    print("Invalid choice.")
print("Q17","Current balance:", account["balance"])

numbers = {10, 20, 30, 10, 40, 20, 50, 30}
print("Q18",numbers)

class_a = {"Ade", "Bola", "Chidi", "Dayo"}
class_b = {"Chidi", "Emeka", "Dayo", "Funke"}
print("Q19","Students in both classes:", class_a & class_b)

a = set(range(1, 11))
b = set(range(5, 16))
print("Q20","All elements:", a | b)
print("Q20","Common elements:", a & b)
print("Q20", "In first but not second:", a - b)

days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
print("Q21","First day:", days[0])
print("Q21","Last day:", days[-1])
print("Q21","Number of days:", len(days))
print("Q21","Saturday exists:", "Saturday" in days)

students = ("Ade", "Bola", "Chidi", "Dayo", "Emeka")
lst = list(students)
lst.append("Funke")
lst.append("Gozie")
lst.remove("Bola")
students = tuple(lst)
print("Q22",students)


with open("students.txt", "w") as f:
   f.write("Name: Ada\nAge: 20\nDepartment: Computer Science\n")
print("Q23","students.txt created.")


names = ["Ade", "Bola", "Chidi", "Dayo", "Emeka"]
with open("students.txt", "w") as f:  # "w" replaces previous content
for n in names:
     f.write(n + "\n")
print("Q24","students.txt overwritten with five names.")


with open("students.txt", "a") as f:  # "a" keeps previous content
for n in ["Funke", "Gozie", "Hauwa"]:
     f.write(n + "\n")
print("Q25","Three names appended.")


try:
with open("students.txt", "r") as f:
   print(f.read())
except FileNotFoundError:
print("Q26","students.txt not found. Run q23 first.")


sentences = ["Today was a good day.", "I learned about Python files.", "I wrote some code.", "I fixed a few bugs.", "Tomorrow I will practise more."]
with open("diary.txt", "w") as f:
for s in sentences:
f.write(s + "\n")
with open("diary.txt", "r") as f:
print("Q27:", f.read())

name = input("Enter your name: ")
language = input("Enter your favourite programming language: ")
with open("profile.txt", "a") as f:
f.write(f"{name} - {language}\n")
print("Q28","Saved to profile.txt.")


if not os.path.exists("numbers.txt"):  # create sample data if missing
with open("numbers.txt", "w") as f:
f.write("10\n20\n30\n40\n")
total = 0
with open("numbers.txt", "r") as f:
for line in f:
line = line.strip()
if line:
total += float(line)
print("Q29","Sum of numbers:", total)

    while True:
        print("\n1. Add student record\n2. View all records\n3. Count records\n4. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            name = input("Name: ")
            age = input("Age: ")
            score = input("Exam score: ")
            with open("records.txt", "a") as f:
                f.write(f"{name},{age},{score}\n")
            print("Record saved.")
        elif choice == "2":
            if os.path.exists("records.txt"):
                with open("records.txt", "r") as f:
                    for line in f:
                        name, age, score = line.strip().split(",")
                        print(f"Name: {name} | Age: {age} | Score: {score}")
            else:
                print("No records yet.")
        elif choice == "3":
            count = 0
            if os.path.exists("records.txt"):
                with open("records.txt", "r") as f:
                    count = sum(1 for line in f if line.strip())
            print("Total records:", count)
        elif choice == "4":
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    choice = input("Enter question number (1-30) or 'all': ").strip().lower()
    if choice == "all":
        for i in range(1, 31):
            print(f"\n--- Question {i} ---")
            globals()[f"q{i}"]()
    elif choice.isdigit() and 1 <= int(choice) <= 30:
        globals()[f"q{choice}"]()
    else:
        print("Invalid choice.")Name = "Moses"
Age = 19
Height = "6ft"
Status = "Student"

print("Q1",Name)
print("Q1",Age)
print("Q1",Height)
print("Q1",Status)

a, b = 10, 3
x, y = 4.5, 1.5
print("Q2","Addition:", a + b, x + y)
print("Q2","Subtraction:", a - b, x - y)
print("Q2","Multiplication:", a * b, x * y)
print("Q2","Division:", a / b, x / y)

Name = input("Enter your name: ")
Age = int(input("Enter your age: "))
colour = input("Enter your favourite colour: ")

print("Q3",f"My name is {Name}, I am {Age} years old and my favourite colour is {colour}.")

num = 10
num2 = 20.29
name = "Ada"
Value = True

print("Q4",num, type(num), num2, type(num2), (name, type(name), (Value, type(Value))))

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Q5","Sum:", a + b)
print("Q5","Product:", a * b)
print("Q5","Difference:", a - b)

name = "Chidi"
s1, s2, s3, s4, s5 = 70, 65, 80, 55, 90
status = "Passed"
total = s1 + s2 + s3 + s4 + s5
average = total / 5
print("Q6","Name:", name)
print("Q6","Scores:", s1, s2, s3, s4, s5)
print("Q6","Status:", status)
print("Q6","Total:", total)
print("Q6","Average:", average)

fruits = ["apple", "banana", "mango", "orange", "pear", "grape", "pineapple", "guava", "lemon", "papaya"]
print("Q7","First:", fruits[0])
print("Q7","Last:", fruits[-1])
print("Q7","Total items:", len(fruits))

students = ["Ade", "Bola", "Chidi", "Dayo", "Emeka"]
students.append(input("Enter another student's name: "))
print("Q8","Updated list:", students)

Number =[1,2,3,4,5,6,7,8,9,10]
print("Q9","Even numbers:", [n for n in Number if n % 2 == 0])

nums = [15, 8, 25, 40, 12, 30, 5, 18]
largest = nums[0]
smallest = nums[0]
total = 0
for n in nums:
  if n > largest:
        largest = n
  if n < smallest:
       smallest = n
total += n
print("Q10","Largest:", largest)
print("Q10","Smallest:", smallest)
print("Q10","Sum:", total)

shopping = ["bread", "milk", "eggs", "rice", "sugar"]
for _ in range(2):
shopping.append(input("Add a product: "))
item = input("Enter a product to remove: ")
if item in shopping:
  shopping.remove(item)
else:
print("Product not found.")
print("Q11","Final shopping list:", shopping)


numbers = [5, 12, 18, 23, 7, 30, 41, 9, 15, 2]
n = int(input("Enter a number: "))
if n in numbers:
print(f"{n} exists at position (index) {numbers.index(n)}")
else:
print("Q12", f"{n} is not in the list.")

student = {"name": "Ada", "age": 20, "gender": "Female","department": "Computer Science", "matric_no": "CSC/2024/001"}
for key, value in student.items():
print("Q13", f"{key}: {value}")

products = {"Bread": 800, "Milk": 1200, "Rice": 5000, "Eggs": 2500, "Sugar": 1500}
for name, price in products.items():
print("Q14", f"{name}: {price}")

student = {"name": "Ada", "age": 20, "score": 65}
student["score"] = int(input("Enter the new score: "))
print("Q15", "Updated information:", student)

scores = {"Ade": 67, "Bola": 82, "Chidi": 75, "Dayo": 90, "Emeka": 58}
top_name, top_score = None, -1
for name, score in scores.items():
if score > top_score:
top_name, top_score = name, score
print("Q16", f"Highest score: {top_name} with {top_score}")

account = {"account_name": "Ada Obi", "account_number": "1234567890", "balance": 10000.0}
choice = input("Type 'deposit' or 'withdraw': ").strip().lower()
amount = float(input("Enter amount: "))
if choice == "deposit":
account["balance"] += amount
elif choice == "withdraw":
if amount <= account["balance"]:
account["balance"] -= amount
else:
    print("Insufficient funds.")
else:
    print("Invalid choice.")
print("Q17","Current balance:", account["balance"])

numbers = {10, 20, 30, 10, 40, 20, 50, 30}
print("Q18",numbers)

class_a = {"Ade", "Bola", "Chidi", "Dayo"}
class_b = {"Chidi", "Emeka", "Dayo", "Funke"}
print("Q19","Students in both classes:", class_a & class_b)

a = set(range(1, 11))
b = set(range(5, 16))
print("Q20","All elements:", a | b)
print("Q20","Common elements:", a & b)
print("Q20", "In first but not second:", a - b)

days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
print("Q21","First day:", days[0])
print("Q21","Last day:", days[-1])
print("Q21","Number of days:", len(days))
print("Q21","Saturday exists:", "Saturday" in days)

students = ("Ade", "Bola", "Chidi", "Dayo", "Emeka")
lst = list(students)
lst.append("Funke")
lst.append("Gozie")
lst.remove("Bola")
students = tuple(lst)
print("Q22",students)


with open("students.txt", "w") as f:
   f.write("Name: Ada\nAge: 20\nDepartment: Computer Science\n")
print("Q23","students.txt created.")


names = ["Ade", "Bola", "Chidi", "Dayo", "Emeka"]
with open("students.txt", "w") as f:  # "w" replaces previous content
for n in names:
     f.write(n + "\n")
print("Q24","students.txt overwritten with five names.")


with open("students.txt", "a") as f:  # "a" keeps previous content
for n in ["Funke", "Gozie", "Hauwa"]:
     f.write(n + "\n")
print("Q25","Three names appended.")


try:
with open("students.txt", "r") as f:
   print(f.read())
except FileNotFoundError:
print("Q26","students.txt not found. Run q23 first.")


sentences = ["Today was a good day.", "I learned about Python files.", "I wrote some code.", "I fixed a few bugs.", "Tomorrow I will practise more."]
with open("diary.txt", "w") as f:
for s in sentences:
f.write(s + "\n")
with open("diary.txt", "r") as f:
print("Q27:", f.read())

name = input("Enter your name: ")
language = input("Enter your favourite programming language: ")
with open("profile.txt", "a") as f:
f.write(f"{name} - {language}\n")
print("Q28","Saved to profile.txt.")


if not os.path.exists("numbers.txt"):  # create sample data if missing
with open("numbers.txt", "w") as f:
f.write("10\n20\n30\n40\n")
total = 0
with open("numbers.txt", "r") as f:
for line in f:
line = line.strip()
if line:
total += float(line)
print("Q29","Sum of numbers:", total)

    while True:
        print("\n1. Add student record\n2. View all records\n3. Count records\n4. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            name = input("Name: ")
            age = input("Age: ")
            score = input("Exam score: ")
            with open("records.txt", "a") as f:
                f.write(f"{name},{age},{score}\n")
            print("Record saved.")
        elif choice == "2":
            if os.path.exists("records.txt"):
                with open("records.txt", "r") as f:
                    for line in f:
                        name, age, score = line.strip().split(",")
                        print(f"Name: {name} | Age: {age} | Score: {score}")
            else:
                print("No records yet.")
        elif choice == "3":
            count = 0
            if os.path.exists("records.txt"):
                with open("records.txt", "r") as f:
                    count = sum(1 for line in f if line.strip())
            print("Total records:", count)
        elif choice == "4":
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    choice = input("Enter question number (1-30) or 'all': ").strip().lower()
    if choice == "all":
        for i in range(1, 31):
            print(f"\n--- Question {i} ---")
            globals()[f"q{i}"]()
    elif choice.isdigit() and 1 <= int(choice) <= 30:
        globals()[f"q{choice}"]()
    else:
        print("Invalid choice.")Name = "Moses"
Age = 19
Height = "6ft"
Status = "Student"

print("Q1",Name)
print("Q1",Age)
print("Q1",Height)
print("Q1",Status)

a, b = 10, 3
x, y = 4.5, 1.5
print("Q2","Addition:", a + b, x + y)
print("Q2","Subtraction:", a - b, x - y)
print("Q2","Multiplication:", a * b, x * y)
print("Q2","Division:", a / b, x / y)

Name = input("Enter your name: ")
Age = int(input("Enter your age: "))
colour = input("Enter your favourite colour: ")

print("Q3",f"My name is {Name}, I am {Age} years old and my favourite colour is {colour}.")

num = 10
num2 = 20.29
name = "Ada"
Value = True

print("Q4",num, type(num), num2, type(num2), (name, type(name), (Value, type(Value))))

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Q5","Sum:", a + b)
print("Q5","Product:", a * b)
print("Q5","Difference:", a - b)

name = "Chidi"
s1, s2, s3, s4, s5 = 70, 65, 80, 55, 90
status = "Passed"
total = s1 + s2 + s3 + s4 + s5
average = total / 5
print("Q6","Name:", name)
print("Q6","Scores:", s1, s2, s3, s4, s5)
print("Q6","Status:", status)
print("Q6","Total:", total)
print("Q6","Average:", average)

fruits = ["apple", "banana", "mango", "orange", "pear", "grape", "pineapple", "guava", "lemon", "papaya"]
print("Q7","First:", fruits[0])
print("Q7","Last:", fruits[-1])
print("Q7","Total items:", len(fruits))

students = ["Ade", "Bola", "Chidi", "Dayo", "Emeka"]
students.append(input("Enter another student's name: "))
print("Q8","Updated list:", students)

Number =[1,2,3,4,5,6,7,8,9,10]
print("Q9","Even numbers:", [n for n in Number if n % 2 == 0])

nums = [15, 8, 25, 40, 12, 30, 5, 18]
largest = nums[0]
smallest = nums[0]
total = 0
for n in nums:
  if n > largest:
        largest = n
  if n < smallest:
       smallest = n
total += n
print("Q10","Largest:", largest)
print("Q10","Smallest:", smallest)
print("Q10","Sum:", total)

shopping = ["bread", "milk", "eggs", "rice", "sugar"]
for _ in range(2):
shopping.append(input("Add a product: "))
item = input("Enter a product to remove: ")
if item in shopping:
  shopping.remove(item)
else:
print("Product not found.")
print("Q11","Final shopping list:", shopping)


numbers = [5, 12, 18, 23, 7, 30, 41, 9, 15, 2]
n = int(input("Enter a number: "))
if n in numbers:
print(f"{n} exists at position (index) {numbers.index(n)}")
else:
print("Q12", f"{n} is not in the list.")

student = {"name": "Ada", "age": 20, "gender": "Female","department": "Computer Science", "matric_no": "CSC/2024/001"}
for key, value in student.items():
print("Q13", f"{key}: {value}")

products = {"Bread": 800, "Milk": 1200, "Rice": 5000, "Eggs": 2500, "Sugar": 1500}
for name, price in products.items():
print("Q14", f"{name}: {price}")

student = {"name": "Ada", "age": 20, "score": 65}
student["score"] = int(input("Enter the new score: "))
print("Q15", "Updated information:", student)

scores = {"Ade": 67, "Bola": 82, "Chidi": 75, "Dayo": 90, "Emeka": 58}
top_name, top_score = None, -1
for name, score in scores.items():
if score > top_score:
top_name, top_score = name, score
print("Q16", f"Highest score: {top_name} with {top_score}")

account = {"account_name": "Ada Obi", "account_number": "1234567890", "balance": 10000.0}
choice = input("Type 'deposit' or 'withdraw': ").strip().lower()
amount = float(input("Enter amount: "))
if choice == "deposit":
account["balance"] += amount
elif choice == "withdraw":
if amount <= account["balance"]:
account["balance"] -= amount
else:
    print("Insufficient funds.")
else:
    print("Invalid choice.")
print("Q17","Current balance:", account["balance"])

numbers = {10, 20, 30, 10, 40, 20, 50, 30}
print("Q18",numbers)

class_a = {"Ade", "Bola", "Chidi", "Dayo"}
class_b = {"Chidi", "Emeka", "Dayo", "Funke"}
print("Q19","Students in both classes:", class_a & class_b)

a = set(range(1, 11))
b = set(range(5, 16))
print("Q20","All elements:", a | b)
print("Q20","Common elements:", a & b)
print("Q20", "In first but not second:", a - b)

days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
print("Q21","First day:", days[0])
print("Q21","Last day:", days[-1])
print("Q21","Number of days:", len(days))
print("Q21","Saturday exists:", "Saturday" in days)

students = ("Ade", "Bola", "Chidi", "Dayo", "Emeka")
lst = list(students)
lst.append("Funke")
lst.append("Gozie")
lst.remove("Bola")
students = tuple(lst)
print("Q22",students)


with open("students.txt", "w") as f:
   f.write("Name: Ada\nAge: 20\nDepartment: Computer Science\n")
print("Q23","students.txt created.")


names = ["Ade", "Bola", "Chidi", "Dayo", "Emeka"]
with open("students.txt", "w") as f:  # "w" replaces previous content
for n in names:
     f.write(n + "\n")
print("Q24","students.txt overwritten with five names.")


with open("students.txt", "a") as f:  # "a" keeps previous content
for n in ["Funke", "Gozie", "Hauwa"]:
     f.write(n + "\n")
print("Q25","Three names appended.")


try:
with open("students.txt", "r") as f:
   print(f.read())
except FileNotFoundError:
print("Q26","students.txt not found. Run q23 first.")


sentences = ["Today was a good day.", "I learned about Python files.", "I wrote some code.", "I fixed a few bugs.", "Tomorrow I will practise more."]
with open("diary.txt", "w") as f:
for s in sentences:
f.write(s + "\n")
with open("diary.txt", "r") as f:
print("Q27:", f.read())

name = input("Enter your name: ")
language = input("Enter your favourite programming language: ")
with open("profile.txt", "a") as f:
f.write(f"{name} - {language}\n")
print("Q28","Saved to profile.txt.")


if not os.path.exists("numbers.txt"):  # create sample data if missing
with open("numbers.txt", "w") as f:
f.write("10\n20\n30\n40\n")
total = 0
with open("numbers.txt", "r") as f:
for line in f:
line = line.strip()
if line:
total += float(line)
print("Q29","Sum of numbers:", total)

    while True:
        print("\n1. Add student record\n2. View all records\n3. Count records\n4. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            name = input("Name: ")
            age = input("Age: ")
            score = input("Exam score: ")
            with open("records.txt", "a") as f:
                f.write(f"{name},{age},{score}\n")
            print("Record saved.")
        elif choice == "2":
            if os.path.exists("records.txt"):
                with open("records.txt", "r") as f:
                    for line in f:
                        name, age, score = line.strip().split(",")
                        print(f"Name: {name} | Age: {age} | Score: {score}")
            else:
                print("No records yet.")
        elif choice == "3":
            count = 0
            if os.path.exists("records.txt"):
                with open("records.txt", "r") as f:
                    count = sum(1 for line in f if line.strip())
            print("Total records:", count)
        elif choice == "4":
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    choice = input("Enter question number (1-30) or 'all': ").strip().lower()
    if choice == "all":
        for i in range(1, 31):
            print(f"\n--- Question {i} ---")
            globals()[f"q{i}"]()
    elif choice.isdigit() and 1 <= int(choice) <= 30:
        globals()[f"q{choice}"]()
    else:
        print("Invalid choice.")Name = "Moses"
Age = 19
Height = "6ft"
Status = "Student"

print("Q1",Name)
print("Q1",Age)
print("Q1",Height)
print("Q1",Status)

a, b = 10, 3
x, y = 4.5, 1.5
print("Q2","Addition:", a + b, x + y)
print("Q2","Subtraction:", a - b, x - y)
print("Q2","Multiplication:", a * b, x * y)
print("Q2","Division:", a / b, x / y)

Name = input("Enter your name: ")
Age = int(input("Enter your age: "))
colour = input("Enter your favourite colour: ")

print("Q3",f"My name is {Name}, I am {Age} years old and my favourite colour is {colour}.")

num = 10
num2 = 20.29
name = "Ada"
Value = True

print("Q4",num, type(num), num2, type(num2), (name, type(name), (Value, type(Value))))

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Q5","Sum:", a + b)
print("Q5","Product:", a * b)
print("Q5","Difference:", a - b)

name = "Chidi"
s1, s2, s3, s4, s5 = 70, 65, 80, 55, 90
status = "Passed"
total = s1 + s2 + s3 + s4 + s5
average = total / 5
print("Q6","Name:", name)
print("Q6","Scores:", s1, s2, s3, s4, s5)
print("Q6","Status:", status)
print("Q6","Total:", total)
print("Q6","Average:", average)

fruits = ["apple", "banana", "mango", "orange", "pear", "grape", "pineapple", "guava", "lemon", "papaya"]
print("Q7","First:", fruits[0])
print("Q7","Last:", fruits[-1])
print("Q7","Total items:", len(fruits))

students = ["Ade", "Bola", "Chidi", "Dayo", "Emeka"]
students.append(input("Enter another student's name: "))
print("Q8","Updated list:", students)

Number =[1,2,3,4,5,6,7,8,9,10]
print("Q9","Even numbers:", [n for n in Number if n % 2 == 0])

nums = [15, 8, 25, 40, 12, 30, 5, 18]
largest = nums[0]
smallest = nums[0]
total = 0
for n in nums:
  if n > largest:
        largest = n
  if n < smallest:
       smallest = n
total += n
print("Q10","Largest:", largest)
print("Q10","Smallest:", smallest)
print("Q10","Sum:", total)

shopping = ["bread", "milk", "eggs", "rice", "sugar"]
for _ in range(2):
shopping.append(input("Add a product: "))
item = input("Enter a product to remove: ")
if item in shopping:
  shopping.remove(item)
else:
print("Product not found.")
print("Q11","Final shopping list:", shopping)


numbers = [5, 12, 18, 23, 7, 30, 41, 9, 15, 2]
n = int(input("Enter a number: "))
if n in numbers:
print(f"{n} exists at position (index) {numbers.index(n)}")
else:
print("Q12", f"{n} is not in the list.")

student = {"name": "Ada", "age": 20, "gender": "Female","department": "Computer Science", "matric_no": "CSC/2024/001"}
for key, value in student.items():
print("Q13", f"{key}: {value}")

products = {"Bread": 800, "Milk": 1200, "Rice": 5000, "Eggs": 2500, "Sugar": 1500}
for name, price in products.items():
print("Q14", f"{name}: {price}")

student = {"name": "Ada", "age": 20, "score": 65}
student["score"] = int(input("Enter the new score: "))
print("Q15", "Updated information:", student)

scores = {"Ade": 67, "Bola": 82, "Chidi": 75, "Dayo": 90, "Emeka": 58}
top_name, top_score = None, -1
for name, score in scores.items():
if score > top_score:
top_name, top_score = name, score
print("Q16", f"Highest score: {top_name} with {top_score}")

account = {"account_name": "Ada Obi", "account_number": "1234567890", "balance": 10000.0}
choice = input("Type 'deposit' or 'withdraw': ").strip().lower()
amount = float(input("Enter amount: "))
if choice == "deposit":
account["balance"] += amount
elif choice == "withdraw":
if amount <= account["balance"]:
account["balance"] -= amount
else:
    print("Insufficient funds.")
else:
    print("Invalid choice.")
print("Q17","Current balance:", account["balance"])

numbers = {10, 20, 30, 10, 40, 20, 50, 30}
print("Q18",numbers)

class_a = {"Ade", "Bola", "Chidi", "Dayo"}
class_b = {"Chidi", "Emeka", "Dayo", "Funke"}
print("Q19","Students in both classes:", class_a & class_b)

a = set(range(1, 11))
b = set(range(5, 16))
print("Q20","All elements:", a | b)
print("Q20","Common elements:", a & b)
print("Q20", "In first but not second:", a - b)

days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
print("Q21","First day:", days[0])
print("Q21","Last day:", days[-1])
print("Q21","Number of days:", len(days))
print("Q21","Saturday exists:", "Saturday" in days)

students = ("Ade", "Bola", "Chidi", "Dayo", "Emeka")
lst = list(students)
lst.append("Funke")
lst.append("Gozie")
lst.remove("Bola")
students = tuple(lst)
print("Q22",students)


with open("students.txt", "w") as f:
   f.write("Name: Ada\nAge: 20\nDepartment: Computer Science\n")
print("Q23","students.txt created.")


names = ["Ade", "Bola", "Chidi", "Dayo", "Emeka"]
with open("students.txt", "w") as f:  # "w" replaces previous content
for n in names:
     f.write(n + "\n")
print("Q24","students.txt overwritten with five names.")


with open("students.txt", "a") as f:  # "a" keeps previous content
for n in ["Funke", "Gozie", "Hauwa"]:
     f.write(n + "\n")
print("Q25","Three names appended.")


try:
with open("students.txt", "r") as f:
   print(f.read())
except FileNotFoundError:
print("Q26","students.txt not found. Run q23 first.")


sentences = ["Today was a good day.", "I learned about Python files.", "I wrote some code.", "I fixed a few bugs.", "Tomorrow I will practise more."]
with open("diary.txt", "w") as f:
for s in sentences:
f.write(s + "\n")
with open("diary.txt", "r") as f:
print("Q27:", f.read())

name = input("Enter your name: ")
language = input("Enter your favourite programming language: ")
with open("profile.txt", "a") as f:
f.write(f"{name} - {language}\n")
print("Q28","Saved to profile.txt.")


if not os.path.exists("numbers.txt"):  # create sample data if missing
with open("numbers.txt", "w") as f:
f.write("10\n20\n30\n40\n")
total = 0
with open("numbers.txt", "r") as f:
for line in f:
line = line.strip()
if line:
total += float(line)
print("Q29","Sum of numbers:", total)

    while True:
        print("\n1. Add student record\n2. View all records\n3. Count records\n4. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            name = input("Name: ")
            age = input("Age: ")
            score = input("Exam score: ")
            with open("records.txt", "a") as f:
                f.write(f"{name},{age},{score}\n")
            print("Record saved.")
        elif choice == "2":
            if os.path.exists("records.txt"):
                with open("records.txt", "r") as f:
                    for line in f:
                        name, age, score = line.strip().split(",")
                        print(f"Name: {name} | Age: {age} | Score: {score}")
            else:
                print("No records yet.")
        elif choice == "3":
            count = 0
            if os.path.exists("records.txt"):
                with open("records.txt", "r") as f:
                    count = sum(1 for line in f if line.strip())
            print("Total records:", count)
        elif choice == "4":
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    choice = input("Enter question number (1-30) or 'all': ").strip().lower()
    if choice == "all":
        for i in range(1, 31):
            print(f"\n--- Question {i} ---")
            globals()[f"q{i}"]()
    elif choice.isdigit() and 1 <= int(choice) <= 30:
        globals()[f"q{choice}"]()
    else:
        print("Invalid choice.")Name = "Moses"
Age = 19
Height = "6ft"
Status = "Student"

print("Q1",Name)
print("Q1",Age)
print("Q1",Height)
print("Q1",Status)

a, b = 10, 3
x, y = 4.5, 1.5
print("Q2","Addition:", a + b, x + y)
print("Q2","Subtraction:", a - b, x - y)
print("Q2","Multiplication:", a * b, x * y)
print("Q2","Division:", a / b, x / y)

Name = input("Enter your name: ")
Age = int(input("Enter your age: "))
colour = input("Enter your favourite colour: ")

print("Q3",f"My name is {Name}, I am {Age} years old and my favourite colour is {colour}.")

num = 10
num2 = 20.29
name = "Ada"
Value = True

print("Q4",num, type(num), num2, type(num2), (name, type(name), (Value, type(Value))))

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Q5","Sum:", a + b)
print("Q5","Product:", a * b)
print("Q5","Difference:", a - b)

name = "Chidi"
s1, s2, s3, s4, s5 = 70, 65, 80, 55, 90
status = "Passed"
total = s1 + s2 + s3 + s4 + s5
average = total / 5
print("Q6","Name:", name)
print("Q6","Scores:", s1, s2, s3, s4, s5)
print("Q6","Status:", status)
print("Q6","Total:", total)
print("Q6","Average:", average)

fruits = ["apple", "banana", "mango", "orange", "pear", "grape", "pineapple", "guava", "lemon", "papaya"]
print("Q7","First:", fruits[0])
print("Q7","Last:", fruits[-1])
print("Q7","Total items:", len(fruits))

students = ["Ade", "Bola", "Chidi", "Dayo", "Emeka"]
students.append(input("Enter another student's name: "))
print("Q8","Updated list:", students)

Number =[1,2,3,4,5,6,7,8,9,10]
print("Q9","Even numbers:", [n for n in Number if n % 2 == 0])

nums = [15, 8, 25, 40, 12, 30, 5, 18]
largest = nums[0]
smallest = nums[0]
total = 0
for n in nums:
  if n > largest:
        largest = n
  if n < smallest:
       smallest = n
total += n
print("Q10","Largest:", largest)
print("Q10","Smallest:", smallest)
print("Q10","Sum:", total)

shopping = ["bread", "milk", "eggs", "rice", "sugar"]
for _ in range(2):
shopping.append(input("Add a product: "))
item = input("Enter a product to remove: ")
if item in shopping:
  shopping.remove(item)
else:
print("Product not found.")
print("Q11","Final shopping list:", shopping)


numbers = [5, 12, 18, 23, 7, 30, 41, 9, 15, 2]
n = int(input("Enter a number: "))
if n in numbers:
print(f"{n} exists at position (index) {numbers.index(n)}")
else:
print("Q12", f"{n} is not in the list.")

student = {"name": "Ada", "age": 20, "gender": "Female","department": "Computer Science", "matric_no": "CSC/2024/001"}
for key, value in student.items():
print("Q13", f"{key}: {value}")

products = {"Bread": 800, "Milk": 1200, "Rice": 5000, "Eggs": 2500, "Sugar": 1500}
for name, price in products.items():
print("Q14", f"{name}: {price}")

student = {"name": "Ada", "age": 20, "score": 65}
student["score"] = int(input("Enter the new score: "))
print("Q15", "Updated information:", student)

scores = {"Ade": 67, "Bola": 82, "Chidi": 75, "Dayo": 90, "Emeka": 58}
top_name, top_score = None, -1
for name, score in scores.items():
if score > top_score:
top_name, top_score = name, score
print("Q16", f"Highest score: {top_name} with {top_score}")

account = {"account_name": "Ada Obi", "account_number": "1234567890", "balance": 10000.0}
choice = input("Type 'deposit' or 'withdraw': ").strip().lower()
amount = float(input("Enter amount: "))
if choice == "deposit":
account["balance"] += amount
elif choice == "withdraw":
if amount <= account["balance"]:
account["balance"] -= amount
else:
    print("Insufficient funds.")
else:
    print("Invalid choice.")
print("Q17","Current balance:", account["balance"])

numbers = {10, 20, 30, 10, 40, 20, 50, 30}
print("Q18",numbers)

class_a = {"Ade", "Bola", "Chidi", "Dayo"}
class_b = {"Chidi", "Emeka", "Dayo", "Funke"}
print("Q19","Students in both classes:", class_a & class_b)

a = set(range(1, 11))
b = set(range(5, 16))
print("Q20","All elements:", a | b)
print("Q20","Common elements:", a & b)
print("Q20", "In first but not second:", a - b)

days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
print("Q21","First day:", days[0])
print("Q21","Last day:", days[-1])
print("Q21","Number of days:", len(days))
print("Q21","Saturday exists:", "Saturday" in days)

students = ("Ade", "Bola", "Chidi", "Dayo", "Emeka")
lst = list(students)
lst.append("Funke")
lst.append("Gozie")
lst.remove("Bola")
students = tuple(lst)
print("Q22",students)


with open("students.txt", "w") as f:
   f.write("Name: Ada\nAge: 20\nDepartment: Computer Science\n")
print("Q23","students.txt created.")


names = ["Ade", "Bola", "Chidi", "Dayo", "Emeka"]
with open("students.txt", "w") as f:  # "w" replaces previous content
for n in names:
     f.write(n + "\n")
print("Q24","students.txt overwritten with five names.")


with open("students.txt", "a") as f:  # "a" keeps previous content
for n in ["Funke", "Gozie", "Hauwa"]:
     f.write(n + "\n")
print("Q25","Three names appended.")


try:
with open("students.txt", "r") as f:
   print(f.read())
except FileNotFoundError:
print("Q26","students.txt not found. Run q23 first.")


sentences = ["Today was a good day.", "I learned about Python files.", "I wrote some code.", "I fixed a few bugs.", "Tomorrow I will practise more."]
with open("diary.txt", "w") as f:
for s in sentences:
f.write(s + "\n")
with open("diary.txt", "r") as f:
print("Q27:", f.read())

name = input("Enter your name: ")
language = input("Enter your favourite programming language: ")
with open("profile.txt", "a") as f:
f.write(f"{name} - {language}\n")
print("Q28","Saved to profile.txt.")


if not os.path.exists("numbers.txt"):  # create sample data if missing
with open("numbers.txt", "w") as f:
f.write("10\n20\n30\n40\n")
total = 0
with open("numbers.txt", "r") as f:
for line in f:
line = line.strip()
if line:
total += float(line)
print("Q29","Sum of numbers:", total)

    while True:
        print("\n1. Add student record\n2. View all records\n3. Count records\n4. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            name = input("Name: ")
            age = input("Age: ")
            score = input("Exam score: ")
            with open("records.txt", "a") as f:
                f.write(f"{name},{age},{score}\n")
            print("Record saved.")
        elif choice == "2":
            if os.path.exists("records.txt"):
                with open("records.txt", "r") as f:
                    for line in f:
                        name, age, score = line.strip().split(",")
                        print(f"Name: {name} | Age: {age} | Score: {score}")
            else:
                print("No records yet.")
        elif choice == "3":
            count = 0
            if os.path.exists("records.txt"):
                with open("records.txt", "r") as f:
                    count = sum(1 for line in f if line.strip())
            print("Total records:", count)
        elif choice == "4":
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    choice = input("Enter question number (1-30) or 'all': ").strip().lower()
    if choice == "all":
        for i in range(1, 31):
            print(f"\n--- Question {i} ---")
            globals()[f"q{i}"]()
    elif choice.isdigit() and 1 <= int(choice) <= 30:
        globals()[f"q{choice}"]()
    else:
        print("Invalid choice.")Name = "Moses"
Age = 19
Height = "6ft"
Status = "Student"

print("Q1",Name)
print("Q1",Age)
print("Q1",Height)
print("Q1",Status)

a, b = 10, 3
x, y = 4.5, 1.5
print("Q2","Addition:", a + b, x + y)
print("Q2","Subtraction:", a - b, x - y)
print("Q2","Multiplication:", a * b, x * y)
print("Q2","Division:", a / b, x / y)

Name = input("Enter your name: ")
Age = int(input("Enter your age: "))
colour = input("Enter your favourite colour: ")

print("Q3",f"My name is {Name}, I am {Age} years old and my favourite colour is {colour}.")

num = 10
num2 = 20.29
name = "Ada"
Value = True

print("Q4",num, type(num), num2, type(num2), (name, type(name), (Value, type(Value))))

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Q5","Sum:", a + b)
print("Q5","Product:", a * b)
print("Q5","Difference:", a - b)

name = "Chidi"
s1, s2, s3, s4, s5 = 70, 65, 80, 55, 90
status = "Passed"
total = s1 + s2 + s3 + s4 + s5
average = total / 5
print("Q6","Name:", name)
print("Q6","Scores:", s1, s2, s3, s4, s5)
print("Q6","Status:", status)
print("Q6","Total:", total)
print("Q6","Average:", average)

fruits = ["apple", "banana", "mango", "orange", "pear", "grape", "pineapple", "guava", "lemon", "papaya"]
print("Q7","First:", fruits[0])
print("Q7","Last:", fruits[-1])
print("Q7","Total items:", len(fruits))

students = ["Ade", "Bola", "Chidi", "Dayo", "Emeka"]
students.append(input("Enter another student's name: "))
print("Q8","Updated list:", students)

Number =[1,2,3,4,5,6,7,8,9,10]
print("Q9","Even numbers:", [n for n in Number if n % 2 == 0])

nums = [15, 8, 25, 40, 12, 30, 5, 18]
largest = nums[0]
smallest = nums[0]
total = 0
for n in nums:
  if n > largest:
        largest = n
  if n < smallest:
       smallest = n
total += n
print("Q10","Largest:", largest)
print("Q10","Smallest:", smallest)
print("Q10","Sum:", total)

shopping = ["bread", "milk", "eggs", "rice", "sugar"]
for _ in range(2):
shopping.append(input("Add a product: "))
item = input("Enter a product to remove: ")
if item in shopping:
  shopping.remove(item)
else:
print("Product not found.")
print("Q11","Final shopping list:", shopping)


numbers = [5, 12, 18, 23, 7, 30, 41, 9, 15, 2]
n = int(input("Enter a number: "))
if n in numbers:
print(f"{n} exists at position (index) {numbers.index(n)}")
else:
print("Q12", f"{n} is not in the list.")

student = {"name": "Ada", "age": 20, "gender": "Female","department": "Computer Science", "matric_no": "CSC/2024/001"}
for key, value in student.items():
print("Q13", f"{key}: {value}")

products = {"Bread": 800, "Milk": 1200, "Rice": 5000, "Eggs": 2500, "Sugar": 1500}
for name, price in products.items():
print("Q14", f"{name}: {price}")

student = {"name": "Ada", "age": 20, "score": 65}
student["score"] = int(input("Enter the new score: "))
print("Q15", "Updated information:", student)

scores = {"Ade": 67, "Bola": 82, "Chidi": 75, "Dayo": 90, "Emeka": 58}
top_name, top_score = None, -1
for name, score in scores.items():
if score > top_score:
top_name, top_score = name, score
print("Q16", f"Highest score: {top_name} with {top_score}")

account = {"account_name": "Ada Obi", "account_number": "1234567890", "balance": 10000.0}
choice = input("Type 'deposit' or 'withdraw': ").strip().lower()
amount = float(input("Enter amount: "))
if choice == "deposit":
account["balance"] += amount
elif choice == "withdraw":
if amount <= account["balance"]:
account["balance"] -= amount
else:
    print("Insufficient funds.")
else:
    print("Invalid choice.")
print("Q17","Current balance:", account["balance"])

numbers = {10, 20, 30, 10, 40, 20, 50, 30}
print("Q18",numbers)

class_a = {"Ade", "Bola", "Chidi", "Dayo"}
class_b = {"Chidi", "Emeka", "Dayo", "Funke"}
print("Q19","Students in both classes:", class_a & class_b)

a = set(range(1, 11))
b = set(range(5, 16))
print("Q20","All elements:", a | b)
print("Q20","Common elements:", a & b)
print("Q20", "In first but not second:", a - b)

days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
print("Q21","First day:", days[0])
print("Q21","Last day:", days[-1])
print("Q21","Number of days:", len(days))
print("Q21","Saturday exists:", "Saturday" in days)

students = ("Ade", "Bola", "Chidi", "Dayo", "Emeka")
lst = list(students)
lst.append("Funke")
lst.append("Gozie")
lst.remove("Bola")
students = tuple(lst)
print("Q22",students)


with open("students.txt", "w") as f:
   f.write("Name: Ada\nAge: 20\nDepartment: Computer Science\n")
print("Q23","students.txt created.")


names = ["Ade", "Bola", "Chidi", "Dayo", "Emeka"]
with open("students.txt", "w") as f:  # "w" replaces previous content
for n in names:
     f.write(n + "\n")
print("Q24","students.txt overwritten with five names.")


with open("students.txt", "a") as f:  # "a" keeps previous content
for n in ["Funke", "Gozie", "Hauwa"]:
     f.write(n + "\n")
print("Q25","Three names appended.")


try:
with open("students.txt", "r") as f:
   print(f.read())
except FileNotFoundError:
print("Q26","students.txt not found. Run q23 first.")


sentences = ["Today was a good day.", "I learned about Python files.", "I wrote some code.", "I fixed a few bugs.", "Tomorrow I will practise more."]
with open("diary.txt", "w") as f:
for s in sentences:
f.write(s + "\n")
with open("diary.txt", "r") as f:
print("Q27:", f.read())

name = input("Enter your name: ")
language = input("Enter your favourite programming language: ")
with open("profile.txt", "a") as f:
f.write(f"{name} - {language}\n")
print("Q28","Saved to profile.txt.")


if not os.path.exists("numbers.txt"):  # create sample data if missing
with open("numbers.txt", "w") as f:
f.write("10\n20\n30\n40\n")
total = 0
with open("numbers.txt", "r") as f:
for line in f:
line = line.strip()
if line:
total += float(line)
print("Q29","Sum of numbers:", total)

    while True:
        print("\n1. Add student record\n2. View all records\n3. Count records\n4. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            name = input("Name: ")
            age = input("Age: ")
            score = input("Exam score: ")
            with open("records.txt", "a") as f:
                f.write(f"{name},{age},{score}\n")
            print("Record saved.")
        elif choice == "2":
            if os.path.exists("records.txt"):
                with open("records.txt", "r") as f:
                    for line in f:
                        name, age, score = line.strip().split(",")
                        print(f"Name: {name} | Age: {age} | Score: {score}")
            else:
                print("No records yet.")
        elif choice == "3":
            count = 0
            if os.path.exists("records.txt"):
                with open("records.txt", "r") as f:
                    count = sum(1 for line in f if line.strip())
            print("Total records:", count)
        elif choice == "4":
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    choice = input("Enter question number (1-30) or 'all': ").strip().lower()
    if choice == "all":
        for i in range(1, 31):
            print(f"\n--- Question {i} ---")
            globals()[f"q{i}"]()
    elif choice.isdigit() and 1 <= int(choice) <= 30:
        globals()[f"q{choice}"]()
    else:
        print("Invalid choice.")Name = "Moses"
Age = 19
Height = "6ft"
Status = "Student"

print("Q1",Name)
print("Q1",Age)
print("Q1",Height)
print("Q1",Status)

a, b = 10, 3
x, y = 4.5, 1.5
print("Q2","Addition:", a + b, x + y)
print("Q2","Subtraction:", a - b, x - y)
print("Q2","Multiplication:", a * b, x * y)
print("Q2","Division:", a / b, x / y)

Name = input("Enter your name: ")
Age = int(input("Enter your age: "))
colour = input("Enter your favourite colour: ")

print("Q3",f"My name is {Name}, I am {Age} years old and my favourite colour is {colour}.")

num = 10
num2 = 20.29
name = "Ada"
Value = True

print("Q4",num, type(num), num2, type(num2), (name, type(name), (Value, type(Value))))

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Q5","Sum:", a + b)
print("Q5","Product:", a * b)
print("Q5","Difference:", a - b)

name = "Chidi"
s1, s2, s3, s4, s5 = 70, 65, 80, 55, 90
status = "Passed"
total = s1 + s2 + s3 + s4 + s5
average = total / 5
print("Q6","Name:", name)
print("Q6","Scores:", s1, s2, s3, s4, s5)
print("Q6","Status:", status)
print("Q6","Total:", total)
print("Q6","Average:", average)

fruits = ["apple", "banana", "mango", "orange", "pear", "grape", "pineapple", "guava", "lemon", "papaya"]
print("Q7","First:", fruits[0])
print("Q7","Last:", fruits[-1])
print("Q7","Total items:", len(fruits))

students = ["Ade", "Bola", "Chidi", "Dayo", "Emeka"]
students.append(input("Enter another student's name: "))
print("Q8","Updated list:", students)

Number =[1,2,3,4,5,6,7,8,9,10]
print("Q9","Even numbers:", [n for n in Number if n % 2 == 0])

nums = [15, 8, 25, 40, 12, 30, 5, 18]
largest = nums[0]
smallest = nums[0]
total = 0
for n in nums:
  if n > largest:
        largest = n
  if n < smallest:
       smallest = n
total += n
print("Q10","Largest:", largest)
print("Q10","Smallest:", smallest)
print("Q10","Sum:", total)

shopping = ["bread", "milk", "eggs", "rice", "sugar"]
for _ in range(2):
shopping.append(input("Add a product: "))
item = input("Enter a product to remove: ")
if item in shopping:
  shopping.remove(item)
else:
print("Product not found.")
print("Q11","Final shopping list:", shopping)


numbers = [5, 12, 18, 23, 7, 30, 41, 9, 15, 2]
n = int(input("Enter a number: "))
if n in numbers:
print(f"{n} exists at position (index) {numbers.index(n)}")
else:
print("Q12", f"{n} is not in the list.")

student = {"name": "Ada", "age": 20, "gender": "Female","department": "Computer Science", "matric_no": "CSC/2024/001"}
for key, value in student.items():
print("Q13", f"{key}: {value}")

products = {"Bread": 800, "Milk": 1200, "Rice": 5000, "Eggs": 2500, "Sugar": 1500}
for name, price in products.items():
print("Q14", f"{name}: {price}")

student = {"name": "Ada", "age": 20, "score": 65}
student["score"] = int(input("Enter the new score: "))
print("Q15", "Updated information:", student)

scores = {"Ade": 67, "Bola": 82, "Chidi": 75, "Dayo": 90, "Emeka": 58}
top_name, top_score = None, -1
for name, score in scores.items():
if score > top_score:
top_name, top_score = name, score
print("Q16", f"Highest score: {top_name} with {top_score}")

account = {"account_name": "Ada Obi", "account_number": "1234567890", "balance": 10000.0}
choice = input("Type 'deposit' or 'withdraw': ").strip().lower()
amount = float(input("Enter amount: "))
if choice == "deposit":
account["balance"] += amount
elif choice == "withdraw":
if amount <= account["balance"]:
account["balance"] -= amount
else:
    print("Insufficient funds.")
else:
    print("Invalid choice.")
print("Q17","Current balance:", account["balance"])

numbers = {10, 20, 30, 10, 40, 20, 50, 30}
print("Q18",numbers)

class_a = {"Ade", "Bola", "Chidi", "Dayo"}
class_b = {"Chidi", "Emeka", "Dayo", "Funke"}
print("Q19","Students in both classes:", class_a & class_b)

a = set(range(1, 11))
b = set(range(5, 16))
print("Q20","All elements:", a | b)
print("Q20","Common elements:", a & b)
print("Q20", "In first but not second:", a - b)

days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
print("Q21","First day:", days[0])
print("Q21","Last day:", days[-1])
print("Q21","Number of days:", len(days))
print("Q21","Saturday exists:", "Saturday" in days)

students = ("Ade", "Bola", "Chidi", "Dayo", "Emeka")
lst = list(students)
lst.append("Funke")
lst.append("Gozie")
lst.remove("Bola")
students = tuple(lst)
print("Q22",students)


with open("students.txt", "w") as f:
   f.write("Name: Ada\nAge: 20\nDepartment: Computer Science\n")
print("Q23","students.txt created.")


names = ["Ade", "Bola", "Chidi", "Dayo", "Emeka"]
with open("students.txt", "w") as f:  # "w" replaces previous content
for n in names:
     f.write(n + "\n")
print("Q24","students.txt overwritten with five names.")


with open("students.txt", "a") as f:  # "a" keeps previous content
for n in ["Funke", "Gozie", "Hauwa"]:
     f.write(n + "\n")
print("Q25","Three names appended.")


try:
with open("students.txt", "r") as f:
   print(f.read())
except FileNotFoundError:
print("Q26","students.txt not found. Run q23 first.")


sentences = ["Today was a good day.", "I learned about Python files.", "I wrote some code.", "I fixed a few bugs.", "Tomorrow I will practise more."]
with open("diary.txt", "w") as f:
for s in sentences:
f.write(s + "\n")
with open("diary.txt", "r") as f:
print("Q27:", f.read())

name = input("Enter your name: ")
language = input("Enter your favourite programming language: ")
with open("profile.txt", "a") as f:
f.write(f"{name} - {language}\n")
print("Q28","Saved to profile.txt.")


if not os.path.exists("numbers.txt"):  # create sample data if missing
with open("numbers.txt", "w") as f:
f.write("10\n20\n30\n40\n")
total = 0
with open("numbers.txt", "r") as f:
for line in f:
line = line.strip()
if line:
total += float(line)
print("Q29","Sum of numbers:", total)

    while True:
        print("\n1. Add student record\n2. View all records\n3. Count records\n4. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            name = input("Name: ")
            age = input("Age: ")
            score = input("Exam score: ")
            with open("records.txt", "a") as f:
                f.write(f"{name},{age},{score}\n")
            print("Record saved.")
        elif choice == "2":
            if os.path.exists("records.txt"):
                with open("records.txt", "r") as f:
                    for line in f:
                        name, age, score = line.strip().split(",")
                        print(f"Name: {name} | Age: {age} | Score: {score}")
            else:
                print("No records yet.")
        elif choice == "3":
            count = 0
            if os.path.exists("records.txt"):
                with open("records.txt", "r") as f:
                    count = sum(1 for line in f if line.strip())
            print("Total records:", count)
        elif choice == "4":
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    choice = input("Enter question number (1-30) or 'all': ").strip().lower()
    if choice == "all":
        for i in range(1, 31):
            print(f"\n--- Question {i} ---")
            globals()[f"q{i}"]()
    elif choice.isdigit() and 1 <= int(choice) <= 30:
        globals()[f"q{choice}"]()
    else:
        print("Invalid choice.")Name = "Moses"
Age = 19
Height = "6ft"
Status = "Student"

print("Q1",Name)
print("Q1",Age)
print("Q1",Height)
print("Q1",Status)

a, b = 10, 3
x, y = 4.5, 1.5
print("Q2","Addition:", a + b, x + y)
print("Q2","Subtraction:", a - b, x - y)
print("Q2","Multiplication:", a * b, x * y)
print("Q2","Division:", a / b, x / y)

Name = input("Enter your name: ")
Age = int(input("Enter your age: "))
colour = input("Enter your favourite colour: ")

print("Q3",f"My name is {Name}, I am {Age} years old and my favourite colour is {colour}.")

num = 10
num2 = 20.29
name = "Ada"
Value = True

print("Q4",num, type(num), num2, type(num2), (name, type(name), (Value, type(Value))))

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Q5","Sum:", a + b)
print("Q5","Product:", a * b)
print("Q5","Difference:", a - b)

name = "Chidi"
s1, s2, s3, s4, s5 = 70, 65, 80, 55, 90
status = "Passed"
total = s1 + s2 + s3 + s4 + s5
average = total / 5
print("Q6","Name:", name)
print("Q6","Scores:", s1, s2, s3, s4, s5)
print("Q6","Status:", status)
print("Q6","Total:", total)
print("Q6","Average:", average)

fruits = ["apple", "banana", "mango", "orange", "pear", "grape", "pineapple", "guava", "lemon", "papaya"]
print("Q7","First:", fruits[0])
print("Q7","Last:", fruits[-1])
print("Q7","Total items:", len(fruits))

students = ["Ade", "Bola", "Chidi", "Dayo", "Emeka"]
students.append(input("Enter another student's name: "))
print("Q8","Updated list:", students)

Number =[1,2,3,4,5,6,7,8,9,10]
print("Q9","Even numbers:", [n for n in Number if n % 2 == 0])

nums = [15, 8, 25, 40, 12, 30, 5, 18]
largest = nums[0]
smallest = nums[0]
total = 0
for n in nums:
  if n > largest:
        largest = n
  if n < smallest:
       smallest = n
total += n
print("Q10","Largest:", largest)
print("Q10","Smallest:", smallest)
print("Q10","Sum:", total)

shopping = ["bread", "milk", "eggs", "rice", "sugar"]
for _ in range(2):
shopping.append(input("Add a product: "))
item = input("Enter a product to remove: ")
if item in shopping:
  shopping.remove(item)
else:
print("Product not found.")
print("Q11","Final shopping list:", shopping)


numbers = [5, 12, 18, 23, 7, 30, 41, 9, 15, 2]
n = int(input("Enter a number: "))
if n in numbers:
print(f"{n} exists at position (index) {numbers.index(n)}")
else:
print("Q12", f"{n} is not in the list.")

student = {"name": "Ada", "age": 20, "gender": "Female","department": "Computer Science", "matric_no": "CSC/2024/001"}
for key, value in student.items():
print("Q13", f"{key}: {value}")

products = {"Bread": 800, "Milk": 1200, "Rice": 5000, "Eggs": 2500, "Sugar": 1500}
for name, price in products.items():
print("Q14", f"{name}: {price}")

student = {"name": "Ada", "age": 20, "score": 65}
student["score"] = int(input("Enter the new score: "))
print("Q15", "Updated information:", student)

scores = {"Ade": 67, "Bola": 82, "Chidi": 75, "Dayo": 90, "Emeka": 58}
top_name, top_score = None, -1
for name, score in scores.items():
if score > top_score:
top_name, top_score = name, score
print("Q16", f"Highest score: {top_name} with {top_score}")

account = {"account_name": "Ada Obi", "account_number": "1234567890", "balance": 10000.0}
choice = input("Type 'deposit' or 'withdraw': ").strip().lower()
amount = float(input("Enter amount: "))
if choice == "deposit":
account["balance"] += amount
elif choice == "withdraw":
if amount <= account["balance"]:
account["balance"] -= amount
else:
    print("Insufficient funds.")
else:
    print("Invalid choice.")
print("Q17","Current balance:", account["balance"])

numbers = {10, 20, 30, 10, 40, 20, 50, 30}
print("Q18",numbers)

class_a = {"Ade", "Bola", "Chidi", "Dayo"}
class_b = {"Chidi", "Emeka", "Dayo", "Funke"}
print("Q19","Students in both classes:", class_a & class_b)

a = set(range(1, 11))
b = set(range(5, 16))
print("Q20","All elements:", a | b)
print("Q20","Common elements:", a & b)
print("Q20", "In first but not second:", a - b)

days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
print("Q21","First day:", days[0])
print("Q21","Last day:", days[-1])
print("Q21","Number of days:", len(days))
print("Q21","Saturday exists:", "Saturday" in days)

students = ("Ade", "Bola", "Chidi", "Dayo", "Emeka")
lst = list(students)
lst.append("Funke")
lst.append("Gozie")
lst.remove("Bola")
students = tuple(lst)
print("Q22",students)


with open("students.txt", "w") as f:
   f.write("Name: Ada\nAge: 20\nDepartment: Computer Science\n")
print("Q23","students.txt created.")


names = ["Ade", "Bola", "Chidi", "Dayo", "Emeka"]
with open("students.txt", "w") as f:  # "w" replaces previous content
for n in names:
     f.write(n + "\n")
print("Q24","students.txt overwritten with five names.")


with open("students.txt", "a") as f:  # "a" keeps previous content
for n in ["Funke", "Gozie", "Hauwa"]:
     f.write(n + "\n")
print("Q25","Three names appended.")


try:
with open("students.txt", "r") as f:
   print(f.read())
except FileNotFoundError:
print("Q26","students.txt not found. Run q23 first.")


sentences = ["Today was a good day.", "I learned about Python files.", "I wrote some code.", "I fixed a few bugs.", "Tomorrow I will practise more."]
with open("diary.txt", "w") as f:
for s in sentences:
f.write(s + "\n")
with open("diary.txt", "r") as f:
print("Q27:", f.read())

name = input("Enter your name: ")
language = input("Enter your favourite programming language: ")
with open("profile.txt", "a") as f:
f.write(f"{name} - {language}\n")
print("Q28","Saved to profile.txt.")


if not os.path.exists("numbers.txt"):  # create sample data if missing
with open("numbers.txt", "w") as f:
f.write("10\n20\n30\n40\n")
total = 0
with open("numbers.txt", "r") as f:
for line in f:
line = line.strip()
if line:
total += float(line)
print("Q29","Sum of numbers:", total)

    while True:
        print("\n1. Add student record\n2. View all records\n3. Count records\n4. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            name = input("Name: ")
            age = input("Age: ")
            score = input("Exam score: ")
            with open("records.txt", "a") as f:
                f.write(f"{name},{age},{score}\n")
            print("Record saved.")
        elif choice == "2":
            if os.path.exists("records.txt"):
                with open("records.txt", "r") as f:
                    for line in f:
                        name, age, score = line.strip().split(",")
                        print(f"Name: {name} | Age: {age} | Score: {score}")
            else:
                print("No records yet.")
        elif choice == "3":
            count = 0
            if os.path.exists("records.txt"):
                with open("records.txt", "r") as f:
                    count = sum(1 for line in f if line.strip())
            print("Total records:", count)
        elif choice == "4":
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    choice = input("Enter question number (1-30) or 'all': ").strip().lower()
    if choice == "all":
        for i in range(1, 31):
            print(f"\n--- Question {i} ---")
            globals()[f"q{i}"]()
    elif choice.isdigit() and 1 <= int(choice) <= 30:
        globals()[f"q{choice}"]()
    else:
        print("Invalid choice.")Name = "Moses"
Age = 19
Height = "6ft"
Status = "Student"

print("Q1",Name)
print("Q1",Age)
print("Q1",Height)
print("Q1",Status)

a, b = 10, 3
x, y = 4.5, 1.5
print("Q2","Addition:", a + b, x + y)
print("Q2","Subtraction:", a - b, x - y)
print("Q2","Multiplication:", a * b, x * y)
print("Q2","Division:", a / b, x / y)

Name = input("Enter your name: ")
Age = int(input("Enter your age: "))
colour = input("Enter your favourite colour: ")

print("Q3",f"My name is {Name}, I am {Age} years old and my favourite colour is {colour}.")

num = 10
num2 = 20.29
name = "Ada"
Value = True

print("Q4",num, type(num), num2, type(num2), (name, type(name), (Value, type(Value))))

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Q5","Sum:", a + b)
print("Q5","Product:", a * b)
print("Q5","Difference:", a - b)

name = "Chidi"
s1, s2, s3, s4, s5 = 70, 65, 80, 55, 90
status = "Passed"
total = s1 + s2 + s3 + s4 + s5
average = total / 5
print("Q6","Name:", name)
print("Q6","Scores:", s1, s2, s3, s4, s5)
print("Q6","Status:", status)
print("Q6","Total:", total)
print("Q6","Average:", average)

fruits = ["apple", "banana", "mango", "orange", "pear", "grape", "pineapple", "guava", "lemon", "papaya"]
print("Q7","First:", fruits[0])
print("Q7","Last:", fruits[-1])
print("Q7","Total items:", len(fruits))

students = ["Ade", "Bola", "Chidi", "Dayo", "Emeka"]
students.append(input("Enter another student's name: "))
print("Q8","Updated list:", students)

Number =[1,2,3,4,5,6,7,8,9,10]
print("Q9","Even numbers:", [n for n in Number if n % 2 == 0])

nums = [15, 8, 25, 40, 12, 30, 5, 18]
largest = nums[0]
smallest = nums[0]
total = 0
for n in nums:
  if n > largest:
        largest = n
  if n < smallest:
       smallest = n
total += n
print("Q10","Largest:", largest)
print("Q10","Smallest:", smallest)
print("Q10","Sum:", total)

shopping = ["bread", "milk", "eggs", "rice", "sugar"]
for _ in range(2):
shopping.append(input("Add a product: "))
item = input("Enter a product to remove: ")
if item in shopping:
  shopping.remove(item)
else:
print("Product not found.")
print("Q11","Final shopping list:", shopping)


numbers = [5, 12, 18, 23, 7, 30, 41, 9, 15, 2]
n = int(input("Enter a number: "))
if n in numbers:
print(f"{n} exists at position (index) {numbers.index(n)}")
else:
print("Q12", f"{n} is not in the list.")

student = {"name": "Ada", "age": 20, "gender": "Female","department": "Computer Science", "matric_no": "CSC/2024/001"}
for key, value in student.items():
print("Q13", f"{key}: {value}")

products = {"Bread": 800, "Milk": 1200, "Rice": 5000, "Eggs": 2500, "Sugar": 1500}
for name, price in products.items():
print("Q14", f"{name}: {price}")

student = {"name": "Ada", "age": 20, "score": 65}
student["score"] = int(input("Enter the new score: "))
print("Q15", "Updated information:", student)

scores = {"Ade": 67, "Bola": 82, "Chidi": 75, "Dayo": 90, "Emeka": 58}
top_name, top_score = None, -1
for name, score in scores.items():
if score > top_score:
top_name, top_score = name, score
print("Q16", f"Highest score: {top_name} with {top_score}")

account = {"account_name": "Ada Obi", "account_number": "1234567890", "balance": 10000.0}
choice = input("Type 'deposit' or 'withdraw': ").strip().lower()
amount = float(input("Enter amount: "))
if choice == "deposit":
account["balance"] += amount
elif choice == "withdraw":
if amount <= account["balance"]:
account["balance"] -= amount
else:
    print("Insufficient funds.")
else:
    print("Invalid choice.")
print("Q17","Current balance:", account["balance"])

numbers = {10, 20, 30, 10, 40, 20, 50, 30}
print("Q18",numbers)

class_a = {"Ade", "Bola", "Chidi", "Dayo"}
class_b = {"Chidi", "Emeka", "Dayo", "Funke"}
print("Q19","Students in both classes:", class_a & class_b)

a = set(range(1, 11))
b = set(range(5, 16))
print("Q20","All elements:", a | b)
print("Q20","Common elements:", a & b)
print("Q20", "In first but not second:", a - b)

days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
print("Q21","First day:", days[0])
print("Q21","Last day:", days[-1])
print("Q21","Number of days:", len(days))
print("Q21","Saturday exists:", "Saturday" in days)

students = ("Ade", "Bola", "Chidi", "Dayo", "Emeka")
lst = list(students)
lst.append("Funke")
lst.append("Gozie")
lst.remove("Bola")
students = tuple(lst)
print("Q22",students)


with open("students.txt", "w") as f:
   f.write("Name: Ada\nAge: 20\nDepartment: Computer Science\n")
print("Q23","students.txt created.")


names = ["Ade", "Bola", "Chidi", "Dayo", "Emeka"]
with open("students.txt", "w") as f:  # "w" replaces previous content
for n in names:
     f.write(n + "\n")
print("Q24","students.txt overwritten with five names.")


with open("students.txt", "a") as f:  # "a" keeps previous content
for n in ["Funke", "Gozie", "Hauwa"]:
     f.write(n + "\n")
print("Q25","Three names appended.")


try:
with open("students.txt", "r") as f:
   print(f.read())
except FileNotFoundError:
print("Q26","students.txt not found. Run q23 first.")


sentences = ["Today was a good day.", "I learned about Python files.", "I wrote some code.", "I fixed a few bugs.", "Tomorrow I will practise more."]
with open("diary.txt", "w") as f:
for s in sentences:
f.write(s + "\n")
with open("diary.txt", "r") as f:
print("Q27:", f.read())

name = input("Enter your name: ")
language = input("Enter your favourite programming language: ")
with open("profile.txt", "a") as f:
f.write(f"{name} - {language}\n")
print("Q28","Saved to profile.txt.")


if not os.path.exists("numbers.txt"):  # create sample data if missing
with open("numbers.txt", "w") as f:
f.write("10\n20\n30\n40\n")
total = 0
with open("numbers.txt", "r") as f:
for line in f:
line = line.strip()
if line:
total += float(line)
print("Q29","Sum of numbers:", total)

    while True:
        print("\n1. Add student record\n2. View all records\n3. Count records\n4. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            name = input("Name: ")
            age = input("Age: ")
            score = input("Exam score: ")
            with open("records.txt", "a") as f:
                f.write(f"{name},{age},{score}\n")
            print("Record saved.")
        elif choice == "2":
            if os.path.exists("records.txt"):
                with open("records.txt", "r") as f:
                    for line in f:
                        name, age, score = line.strip().split(",")
                        print(f"Name: {name} | Age: {age} | Score: {score}")
            else:
                print("No records yet.")
        elif choice == "3":
            count = 0
            if os.path.exists("records.txt"):
                with open("records.txt", "r") as f:
                    count = sum(1 for line in f if line.strip())
            print("Total records:", count)
        elif choice == "4":
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    choice = input("Enter question number (1-30) or 'all': ").strip().lower()
    if choice == "all":
        for i in range(1, 31):
            print(f"\n--- Question {i} ---")
            globals()[f"q{i}"]()
    elif choice.isdigit() and 1 <= int(choice) <= 30:
        globals()[f"q{choice}"]()
    else:
        print("Invalid choice.")Name = "Moses"
Age = 19
Height = "6ft"
Status = "Student"

print("Q1",Name)
print("Q1",Age)
print("Q1",Height)
print("Q1",Status)

a, b = 10, 3
x, y = 4.5, 1.5
print("Q2","Addition:", a + b, x + y)
print("Q2","Subtraction:", a - b, x - y)
print("Q2","Multiplication:", a * b, x * y)
print("Q2","Division:", a / b, x / y)

Name = input("Enter your name: ")
Age = int(input("Enter your age: "))
colour = input("Enter your favourite colour: ")

print("Q3",f"My name is {Name}, I am {Age} years old and my favourite colour is {colour}.")

num = 10
num2 = 20.29
name = "Ada"
Value = True

print("Q4",num, type(num), num2, type(num2), (name, type(name), (Value, type(Value))))

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Q5","Sum:", a + b)
print("Q5","Product:", a * b)
print("Q5","Difference:", a - b)

name = "Chidi"
s1, s2, s3, s4, s5 = 70, 65, 80, 55, 90
status = "Passed"
total = s1 + s2 + s3 + s4 + s5
average = total / 5
print("Q6","Name:", name)
print("Q6","Scores:", s1, s2, s3, s4, s5)
print("Q6","Status:", status)
print("Q6","Total:", total)
print("Q6","Average:", average)

fruits = ["apple", "banana", "mango", "orange", "pear", "grape", "pineapple", "guava", "lemon", "papaya"]
print("Q7","First:", fruits[0])
print("Q7","Last:", fruits[-1])
print("Q7","Total items:", len(fruits))

students = ["Ade", "Bola", "Chidi", "Dayo", "Emeka"]
students.append(input("Enter another student's name: "))
print("Q8","Updated list:", students)

Number =[1,2,3,4,5,6,7,8,9,10]
print("Q9","Even numbers:", [n for n in Number if n % 2 == 0])

nums = [15, 8, 25, 40, 12, 30, 5, 18]
largest = nums[0]
smallest = nums[0]
total = 0
for n in nums:
  if n > largest:
        largest = n
  if n < smallest:
       smallest = n
total += n
print("Q10","Largest:", largest)
print("Q10","Smallest:", smallest)
print("Q10","Sum:", total)

shopping = ["bread", "milk", "eggs", "rice", "sugar"]
for _ in range(2):
shopping.append(input("Add a product: "))
item = input("Enter a product to remove: ")
if item in shopping:
  shopping.remove(item)
else:
print("Product not found.")
print("Q11","Final shopping list:", shopping)


numbers = [5, 12, 18, 23, 7, 30, 41, 9, 15, 2]
n = int(input("Enter a number: "))
if n in numbers:
print(f"{n} exists at position (index) {numbers.index(n)}")
else:
print("Q12", f"{n} is not in the list.")

student = {"name": "Ada", "age": 20, "gender": "Female","department": "Computer Science", "matric_no": "CSC/2024/001"}
for key, value in student.items():
print("Q13", f"{key}: {value}")

products = {"Bread": 800, "Milk": 1200, "Rice": 5000, "Eggs": 2500, "Sugar": 1500}
for name, price in products.items():
print("Q14", f"{name}: {price}")

student = {"name": "Ada", "age": 20, "score": 65}
student["score"] = int(input("Enter the new score: "))
print("Q15", "Updated information:", student)

scores = {"Ade": 67, "Bola": 82, "Chidi": 75, "Dayo": 90, "Emeka": 58}
top_name, top_score = None, -1
for name, score in scores.items():
if score > top_score:
top_name, top_score = name, score
print("Q16", f"Highest score: {top_name} with {top_score}")

account = {"account_name": "Ada Obi", "account_number": "1234567890", "balance": 10000.0}
choice = input("Type 'deposit' or 'withdraw': ").strip().lower()
amount = float(input("Enter amount: "))
if choice == "deposit":
account["balance"] += amount
elif choice == "withdraw":
if amount <= account["balance"]:
account["balance"] -= amount
else:
    print("Insufficient funds.")
else:
    print("Invalid choice.")
print("Q17","Current balance:", account["balance"])

numbers = {10, 20, 30, 10, 40, 20, 50, 30}
print("Q18",numbers)

class_a = {"Ade", "Bola", "Chidi", "Dayo"}
class_b = {"Chidi", "Emeka", "Dayo", "Funke"}
print("Q19","Students in both classes:", class_a & class_b)

a = set(range(1, 11))
b = set(range(5, 16))
print("Q20","All elements:", a | b)
print("Q20","Common elements:", a & b)
print("Q20", "In first but not second:", a - b)

days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
print("Q21","First day:", days[0])
print("Q21","Last day:", days[-1])
print("Q21","Number of days:", len(days))
print("Q21","Saturday exists:", "Saturday" in days)

students = ("Ade", "Bola", "Chidi", "Dayo", "Emeka")
lst = list(students)
lst.append("Funke")
lst.append("Gozie")
lst.remove("Bola")
students = tuple(lst)
print("Q22",students)


with open("students.txt", "w") as f:
   f.write("Name: Ada\nAge: 20\nDepartment: Computer Science\n")
print("Q23","students.txt created.")


names = ["Ade", "Bola", "Chidi", "Dayo", "Emeka"]
with open("students.txt", "w") as f:  # "w" replaces previous content
for n in names:
     f.write(n + "\n")
print("Q24","students.txt overwritten with five names.")


with open("students.txt", "a") as f:  # "a" keeps previous content
for n in ["Funke", "Gozie", "Hauwa"]:
     f.write(n + "\n")
print("Q25","Three names appended.")


try:
with open("students.txt", "r") as f:
   print(f.read())
except FileNotFoundError:
print("Q26","students.txt not found. Run q23 first.")


sentences = ["Today was a good day.", "I learned about Python files.", "I wrote some code.", "I fixed a few bugs.", "Tomorrow I will practise more."]
with open("diary.txt", "w") as f:
for s in sentences:
f.write(s + "\n")
with open("diary.txt", "r") as f:
print("Q27:", f.read())

name = input("Enter your name: ")
language = input("Enter your favourite programming language: ")
with open("profile.txt", "a") as f:
f.write(f"{name} - {language}\n")
print("Q28","Saved to profile.txt.")


if not os.path.exists("numbers.txt"):  # create sample data if missing
with open("numbers.txt", "w") as f:
f.write("10\n20\n30\n40\n")
total = 0
with open("numbers.txt", "r") as f:
for line in f:
line = line.strip()
if line:
total += float(line)
print("Q29","Sum of numbers:", total)

    while True:
        print("\n1. Add student record\n2. View all records\n3. Count records\n4. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            name = input("Name: ")
            age = input("Age: ")
            score = input("Exam score: ")
            with open("records.txt", "a") as f:
                f.write(f"{name},{age},{score}\n")
            print("Record saved.")
        elif choice == "2":
            if os.path.exists("records.txt"):
                with open("records.txt", "r") as f:
                    for line in f:
                        name, age, score = line.strip().split(",")
                        print(f"Name: {name} | Age: {age} | Score: {score}")
            else:
                print("No records yet.")
        elif choice == "3":
            count = 0
            if os.path.exists("records.txt"):
                with open("records.txt", "r") as f:
                    count = sum(1 for line in f if line.strip())
            print("Total records:", count)
        elif choice == "4":
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    choice = input("Enter question number (1-30) or 'all': ").strip().lower()
    if choice == "all":
        for i in range(1, 31):
            print(f"\n--- Question {i} ---")
            globals()[f"q{i}"]()
    elif choice.isdigit() and 1 <= int(choice) <= 30:
        globals()[f"q{choice}"]()
    else:
        print("Invalid choice.")Name = "Moses"
Age = 19
Height = "6ft"
Status = "Student"

print("Q1",Name)
print("Q1",Age)
print("Q1",Height)
print("Q1",Status)

a, b = 10, 3
x, y = 4.5, 1.5
print("Q2","Addition:", a + b, x + y)
print("Q2","Subtraction:", a - b, x - y)
print("Q2","Multiplication:", a * b, x * y)
print("Q2","Division:", a / b, x / y)

Name = input("Enter your name: ")
Age = int(input("Enter your age: "))
colour = input("Enter your favourite colour: ")

print("Q3",f"My name is {Name}, I am {Age} years old and my favourite colour is {colour}.")

num = 10
num2 = 20.29
name = "Ada"
Value = True

print("Q4",num, type(num), num2, type(num2), (name, type(name), (Value, type(Value))))

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Q5","Sum:", a + b)
print("Q5","Product:", a * b)
print("Q5","Difference:", a - b)

name = "Chidi"
s1, s2, s3, s4, s5 = 70, 65, 80, 55, 90
status = "Passed"
total = s1 + s2 + s3 + s4 + s5
average = total / 5
print("Q6","Name:", name)
print("Q6","Scores:", s1, s2, s3, s4, s5)
print("Q6","Status:", status)
print("Q6","Total:", total)
print("Q6","Average:", average)

fruits = ["apple", "banana", "mango", "orange", "pear", "grape", "pineapple", "guava", "lemon", "papaya"]
print("Q7","First:", fruits[0])
print("Q7","Last:", fruits[-1])
print("Q7","Total items:", len(fruits))

students = ["Ade", "Bola", "Chidi", "Dayo", "Emeka"]
students.append(input("Enter another student's name: "))
print("Q8","Updated list:", students)

Number =[1,2,3,4,5,6,7,8,9,10]
print("Q9","Even numbers:", [n for n in Number if n % 2 == 0])

nums = [15, 8, 25, 40, 12, 30, 5, 18]
largest = nums[0]
smallest = nums[0]
total = 0
for n in nums:
  if n > largest:
        largest = n
  if n < smallest:
       smallest = n
total += n
print("Q10","Largest:", largest)
print("Q10","Smallest:", smallest)
print("Q10","Sum:", total)

shopping = ["bread", "milk", "eggs", "rice", "sugar"]
for _ in range(2):
shopping.append(input("Add a product: "))
item = input("Enter a product to remove: ")
if item in shopping:
  shopping.remove(item)
else:
print("Product not found.")
print("Q11","Final shopping list:", shopping)


numbers = [5, 12, 18, 23, 7, 30, 41, 9, 15, 2]
n = int(input("Enter a number: "))
if n in numbers:
print(f"{n} exists at position (index) {numbers.index(n)}")
else:
print("Q12", f"{n} is not in the list.")

student = {"name": "Ada", "age": 20, "gender": "Female","department": "Computer Science", "matric_no": "CSC/2024/001"}
for key, value in student.items():
print("Q13", f"{key}: {value}")

products = {"Bread": 800, "Milk": 1200, "Rice": 5000, "Eggs": 2500, "Sugar": 1500}
for name, price in products.items():
print("Q14", f"{name}: {price}")

student = {"name": "Ada", "age": 20, "score": 65}
student["score"] = int(input("Enter the new score: "))
print("Q15", "Updated information:", student)

scores = {"Ade": 67, "Bola": 82, "Chidi": 75, "Dayo": 90, "Emeka": 58}
top_name, top_score = None, -1
for name, score in scores.items():
if score > top_score:
top_name, top_score = name, score
print("Q16", f"Highest score: {top_name} with {top_score}")

account = {"account_name": "Ada Obi", "account_number": "1234567890", "balance": 10000.0}
choice = input("Type 'deposit' or 'withdraw': ").strip().lower()
amount = float(input("Enter amount: "))
if choice == "deposit":
account["balance"] += amount
elif choice == "withdraw":
if amount <= account["balance"]:
account["balance"] -= amount
else:
    print("Insufficient funds.")
else:
    print("Invalid choice.")
print("Q17","Current balance:", account["balance"])

numbers = {10, 20, 30, 10, 40, 20, 50, 30}
print("Q18",numbers)

class_a = {"Ade", "Bola", "Chidi", "Dayo"}
class_b = {"Chidi", "Emeka", "Dayo", "Funke"}
print("Q19","Students in both classes:", class_a & class_b)

a = set(range(1, 11))
b = set(range(5, 16))
print("Q20","All elements:", a | b)
print("Q20","Common elements:", a & b)
print("Q20", "In first but not second:", a - b)

days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
print("Q21","First day:", days[0])
print("Q21","Last day:", days[-1])
print("Q21","Number of days:", len(days))
print("Q21","Saturday exists:", "Saturday" in days)

students = ("Ade", "Bola", "Chidi", "Dayo", "Emeka")
lst = list(students)
lst.append("Funke")
lst.append("Gozie")
lst.remove("Bola")
students = tuple(lst)
print("Q22",students)


with open("students.txt", "w") as f:
   f.write("Name: Ada\nAge: 20\nDepartment: Computer Science\n")
print("Q23","students.txt created.")


names = ["Ade", "Bola", "Chidi", "Dayo", "Emeka"]
with open("students.txt", "w") as f:  # "w" replaces previous content
for n in names:
     f.write(n + "\n")
print("Q24","students.txt overwritten with five names.")


with open("students.txt", "a") as f:  # "a" keeps previous content
for n in ["Funke", "Gozie", "Hauwa"]:
     f.write(n + "\n")
print("Q25","Three names appended.")


try:
with open("students.txt", "r") as f:
   print(f.read())
except FileNotFoundError:
print("Q26","students.txt not found. Run q23 first.")


sentences = ["Today was a good day.", "I learned about Python files.", "I wrote some code.", "I fixed a few bugs.", "Tomorrow I will practise more."]
with open("diary.txt", "w") as f:
for s in sentences:
f.write(s + "\n")
with open("diary.txt", "r") as f:
print("Q27:", f.read())

name = input("Enter your name: ")
language = input("Enter your favourite programming language: ")
with open("profile.txt", "a") as f:
f.write(f"{name} - {language}\n")
print("Q28","Saved to profile.txt.")


if not os.path.exists("numbers.txt"):  # create sample data if missing
with open("numbers.txt", "w") as f:
f.write("10\n20\n30\n40\n")
total = 0
with open("numbers.txt", "r") as f:
for line in f:
line = line.strip()
if line:
total += float(line)
print("Q29","Sum of numbers:", total)

    while True:
        print("\n1. Add student record\n2. View all records\n3. Count records\n4. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            name = input("Name: ")
            age = input("Age: ")
            score = input("Exam score: ")
            with open("records.txt", "a") as f:
                f.write(f"{name},{age},{score}\n")
            print("Record saved.")
        elif choice == "2":
            if os.path.exists("records.txt"):
                with open("records.txt", "r") as f:
                    for line in f:
                        name, age, score = line.strip().split(",")
                        print(f"Name: {name} | Age: {age} | Score: {score}")
            else:
                print("No records yet.")
        elif choice == "3":
            count = 0
            if os.path.exists("records.txt"):
                with open("records.txt", "r") as f:
                    count = sum(1 for line in f if line.strip())
            print("Total records:", count)
        elif choice == "4":
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    choice = input("Enter question number (1-30) or 'all': ").strip().lower()
    if choice == "all":
        for i in range(1, 31):
            print(f"\n--- Question {i} ---")
            globals()[f"q{i}"]()
    elif choice.isdigit() and 1 <= int(choice) <= 30:
        globals()[f"q{choice}"]()
    else:
        print("Invalid choice.")Name = "Moses"
Age = 19
Height = "6ft"
Status = "Student"

print("Q1",Name)
print("Q1",Age)
print("Q1",Height)
print("Q1",Status)

a, b = 10, 3
x, y = 4.5, 1.5
print("Q2","Addition:", a + b, x + y)
print("Q2","Subtraction:", a - b, x - y)
print("Q2","Multiplication:", a * b, x * y)
print("Q2","Division:", a / b, x / y)

Name = input("Enter your name: ")
Age = int(input("Enter your age: "))
colour = input("Enter your favourite colour: ")

print("Q3",f"My name is {Name}, I am {Age} years old and my favourite colour is {colour}.")

num = 10
num2 = 20.29
name = "Ada"
Value = True

print("Q4",num, type(num), num2, type(num2), (name, type(name), (Value, type(Value))))

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Q5","Sum:", a + b)
print("Q5","Product:", a * b)
print("Q5","Difference:", a - b)

name = "Chidi"
s1, s2, s3, s4, s5 = 70, 65, 80, 55, 90
status = "Passed"
total = s1 + s2 + s3 + s4 + s5
average = total / 5
print("Q6","Name:", name)
print("Q6","Scores:", s1, s2, s3, s4, s5)
print("Q6","Status:", status)
print("Q6","Total:", total)
print("Q6","Average:", average)

fruits = ["apple", "banana", "mango", "orange", "pear", "grape", "pineapple", "guava", "lemon", "papaya"]
print("Q7","First:", fruits[0])
print("Q7","Last:", fruits[-1])
print("Q7","Total items:", len(fruits))

students = ["Ade", "Bola", "Chidi", "Dayo", "Emeka"]
students.append(input("Enter another student's name: "))
print("Q8","Updated list:", students)

Number =[1,2,3,4,5,6,7,8,9,10]
print("Q9","Even numbers:", [n for n in Number if n % 2 == 0])

nums = [15, 8, 25, 40, 12, 30, 5, 18]
largest = nums[0]
smallest = nums[0]
total = 0
for n in nums:
  if n > largest:
        largest = n
  if n < smallest:
       smallest = n
total += n
print("Q10","Largest:", largest)
print("Q10","Smallest:", smallest)
print("Q10","Sum:", total)

shopping = ["bread", "milk", "eggs", "rice", "sugar"]
for _ in range(2):
shopping.append(input("Add a product: "))
item = input("Enter a product to remove: ")
if item in shopping:
  shopping.remove(item)
else:
print("Product not found.")
print("Q11","Final shopping list:", shopping)


numbers = [5, 12, 18, 23, 7, 30, 41, 9, 15, 2]
n = int(input("Enter a number: "))
if n in numbers:
print(f"{n} exists at position (index) {numbers.index(n)}")
else:
print("Q12", f"{n} is not in the list.")

student = {"name": "Ada", "age": 20, "gender": "Female","department": "Computer Science", "matric_no": "CSC/2024/001"}
for key, value in student.items():
print("Q13", f"{key}: {value}")

products = {"Bread": 800, "Milk": 1200, "Rice": 5000, "Eggs": 2500, "Sugar": 1500}
for name, price in products.items():
print("Q14", f"{name}: {price}")

student = {"name": "Ada", "age": 20, "score": 65}
student["score"] = int(input("Enter the new score: "))
print("Q15", "Updated information:", student)

scores = {"Ade": 67, "Bola": 82, "Chidi": 75, "Dayo": 90, "Emeka": 58}
top_name, top_score = None, -1
for name, score in scores.items():
if score > top_score:
top_name, top_score = name, score
print("Q16", f"Highest score: {top_name} with {top_score}")

account = {"account_name": "Ada Obi", "account_number": "1234567890", "balance": 10000.0}
choice = input("Type 'deposit' or 'withdraw': ").strip().lower()
amount = float(input("Enter amount: "))
if choice == "deposit":
account["balance"] += amount
elif choice == "withdraw":
if amount <= account["balance"]:
account["balance"] -= amount
else:
    print("Insufficient funds.")
else:
    print("Invalid choice.")
print("Q17","Current balance:", account["balance"])

numbers = {10, 20, 30, 10, 40, 20, 50, 30}
print("Q18",numbers)

class_a = {"Ade", "Bola", "Chidi", "Dayo"}
class_b = {"Chidi", "Emeka", "Dayo", "Funke"}
print("Q19","Students in both classes:", class_a & class_b)

a = set(range(1, 11))
b = set(range(5, 16))
print("Q20","All elements:", a | b)
print("Q20","Common elements:", a & b)
print("Q20", "In first but not second:", a - b)

days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
print("Q21","First day:", days[0])
print("Q21","Last day:", days[-1])
print("Q21","Number of days:", len(days))
print("Q21","Saturday exists:", "Saturday" in days)

students = ("Ade", "Bola", "Chidi", "Dayo", "Emeka")
lst = list(students)
lst.append("Funke")
lst.append("Gozie")
lst.remove("Bola")
students = tuple(lst)
print("Q22",students)


with open("students.txt", "w") as f:
   f.write("Name: Ada\nAge: 20\nDepartment: Computer Science\n")
print("Q23","students.txt created.")


names = ["Ade", "Bola", "Chidi", "Dayo", "Emeka"]
with open("students.txt", "w") as f:  # "w" replaces previous content
for n in names:
     f.write(n + "\n")
print("Q24","students.txt overwritten with five names.")


with open("students.txt", "a") as f:  # "a" keeps previous content
for n in ["Funke", "Gozie", "Hauwa"]:
     f.write(n + "\n")
print("Q25","Three names appended.")


try:
with open("students.txt", "r") as f:
   print(f.read())
except FileNotFoundError:
print("Q26","students.txt not found. Run q23 first.")


sentences = ["Today was a good day.", "I learned about Python files.", "I wrote some code.", "I fixed a few bugs.", "Tomorrow I will practise more."]
with open("diary.txt", "w") as f:
for s in sentences:
f.write(s + "\n")
with open("diary.txt", "r") as f:
print("Q27:", f.read())

name = input("Enter your name: ")
language = input("Enter your favourite programming language: ")
with open("profile.txt", "a") as f:
f.write(f"{name} - {language}\n")
print("Q28","Saved to profile.txt.")


if not os.path.exists("numbers.txt"):  # create sample data if missing
with open("numbers.txt", "w") as f:
f.write("10\n20\n30\n40\n")
total = 0
with open("numbers.txt", "r") as f:
for line in f:
line = line.strip()
if line:
total += float(line)
print("Q29","Sum of numbers:", total)

    while True:
        print("\n1. Add student record\n2. View all records\n3. Count records\n4. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            name = input("Name: ")
            age = input("Age: ")
            score = input("Exam score: ")
            with open("records.txt", "a") as f:
                f.write(f"{name},{age},{score}\n")
            print("Record saved.")
        elif choice == "2":
            if os.path.exists("records.txt"):
                with open("records.txt", "r") as f:
                    for line in f:
                        name, age, score = line.strip().split(",")
                        print(f"Name: {name} | Age: {age} | Score: {score}")
            else:
                print("No records yet.")
        elif choice == "3":
            count = 0
            if os.path.exists("records.txt"):
                with open("records.txt", "r") as f:
                    count = sum(1 for line in f if line.strip())
            print("Total records:", count)
        elif choice == "4":
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    choice = input("Enter question number (1-30) or 'all': ").strip().lower()
    if choice == "all":
        for i in range(1, 31):
            print(f"\n--- Question {i} ---")
            globals()[f"q{i}"]()
    elif choice.isdigit() and 1 <= int(choice) <= 30:
        globals()[f"q{choice}"]()
    else:
        print("Invalid choice.")Name = "Moses"
Age = 19
Height = "6ft"
Status = "Student"

print("Q1",Name)
print("Q1",Age)
print("Q1",Height)
print("Q1",Status)

a, b = 10, 3
x, y = 4.5, 1.5
print("Q2","Addition:", a + b, x + y)
print("Q2","Subtraction:", a - b, x - y)
print("Q2","Multiplication:", a * b, x * y)
print("Q2","Division:", a / b, x / y)

Name = input("Enter your name: ")
Age = int(input("Enter your age: "))
colour = input("Enter your favourite colour: ")

print("Q3",f"My name is {Name}, I am {Age} years old and my favourite colour is {colour}.")

num = 10
num2 = 20.29
name = "Ada"
Value = True

print("Q4",num, type(num), num2, type(num2), (name, type(name), (Value, type(Value))))

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Q5","Sum:", a + b)
print("Q5","Product:", a * b)
print("Q5","Difference:", a - b)

name = "Chidi"
s1, s2, s3, s4, s5 = 70, 65, 80, 55, 90
status = "Passed"
total = s1 + s2 + s3 + s4 + s5
average = total / 5
print("Q6","Name:", name)
print("Q6","Scores:", s1, s2, s3, s4, s5)
print("Q6","Status:", status)
print("Q6","Total:", total)
print("Q6","Average:", average)

fruits = ["apple", "banana", "mango", "orange", "pear", "grape", "pineapple", "guava", "lemon", "papaya"]
print("Q7","First:", fruits[0])
print("Q7","Last:", fruits[-1])
print("Q7","Total items:", len(fruits))

students = ["Ade", "Bola", "Chidi", "Dayo", "Emeka"]
students.append(input("Enter another student's name: "))
print("Q8","Updated list:", students)

Number =[1,2,3,4,5,6,7,8,9,10]
print("Q9","Even numbers:", [n for n in Number if n % 2 == 0])

nums = [15, 8, 25, 40, 12, 30, 5, 18]
largest = nums[0]
smallest = nums[0]
total = 0
for n in nums:
  if n > largest:
        largest = n
  if n < smallest:
       smallest = n
total += n
print("Q10","Largest:", largest)
print("Q10","Smallest:", smallest)
print("Q10","Sum:", total)

shopping = ["bread", "milk", "eggs", "rice", "sugar"]
for _ in range(2):
shopping.append(input("Add a product: "))
item = input("Enter a product to remove: ")
if item in shopping:
  shopping.remove(item)
else:
print("Product not found.")
print("Q11","Final shopping list:", shopping)


numbers = [5, 12, 18, 23, 7, 30, 41, 9, 15, 2]
n = int(input("Enter a number: "))
if n in numbers:
print(f"{n} exists at position (index) {numbers.index(n)}")
else:
print("Q12", f"{n} is not in the list.")

student = {"name": "Ada", "age": 20, "gender": "Female","department": "Computer Science", "matric_no": "CSC/2024/001"}
for key, value in student.items():
print("Q13", f"{key}: {value}")

products = {"Bread": 800, "Milk": 1200, "Rice": 5000, "Eggs": 2500, "Sugar": 1500}
for name, price in products.items():
print("Q14", f"{name}: {price}")

student = {"name": "Ada", "age": 20, "score": 65}
student["score"] = int(input("Enter the new score: "))
print("Q15", "Updated information:", student)

scores = {"Ade": 67, "Bola": 82, "Chidi": 75, "Dayo": 90, "Emeka": 58}
top_name, top_score = None, -1
for name, score in scores.items():
if score > top_score:
top_name, top_score = name, score
print("Q16", f"Highest score: {top_name} with {top_score}")

account = {"account_name": "Ada Obi", "account_number": "1234567890", "balance": 10000.0}
choice = input("Type 'deposit' or 'withdraw': ").strip().lower()
amount = float(input("Enter amount: "))
if choice == "deposit":
account["balance"] += amount
elif choice == "withdraw":
if amount <= account["balance"]:
account["balance"] -= amount
else:
    print("Insufficient funds.")
else:
    print("Invalid choice.")
print("Q17","Current balance:", account["balance"])

numbers = {10, 20, 30, 10, 40, 20, 50, 30}
print("Q18",numbers)

class_a = {"Ade", "Bola", "Chidi", "Dayo"}
class_b = {"Chidi", "Emeka", "Dayo", "Funke"}
print("Q19","Students in both classes:", class_a & class_b)

a = set(range(1, 11))
b = set(range(5, 16))
print("Q20","All elements:", a | b)
print("Q20","Common elements:", a & b)
print("Q20", "In first but not second:", a - b)

days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
print("Q21","First day:", days[0])
print("Q21","Last day:", days[-1])
print("Q21","Number of days:", len(days))
print("Q21","Saturday exists:", "Saturday" in days)

students = ("Ade", "Bola", "Chidi", "Dayo", "Emeka")
lst = list(students)
lst.append("Funke")
lst.append("Gozie")
lst.remove("Bola")
students = tuple(lst)
print("Q22",students)


with open("students.txt", "w") as f:
   f.write("Name: Ada\nAge: 20\nDepartment: Computer Science\n")
print("Q23","students.txt created.")


names = ["Ade", "Bola", "Chidi", "Dayo", "Emeka"]
with open("students.txt", "w") as f:  # "w" replaces previous content
for n in names:
     f.write(n + "\n")
print("Q24","students.txt overwritten with five names.")


with open("students.txt", "a") as f:  # "a" keeps previous content
for n in ["Funke", "Gozie", "Hauwa"]:
     f.write(n + "\n")
print("Q25","Three names appended.")


try:
with open("students.txt", "r") as f:
   print(f.read())
except FileNotFoundError:
print("Q26","students.txt not found. Run q23 first.")


sentences = ["Today was a good day.", "I learned about Python files.", "I wrote some code.", "I fixed a few bugs.", "Tomorrow I will practise more."]
with open("diary.txt", "w") as f:
for s in sentences:
f.write(s + "\n")
with open("diary.txt", "r") as f:
print("Q27:", f.read())

name = input("Enter your name: ")
language = input("Enter your favourite programming language: ")
with open("profile.txt", "a") as f:
f.write(f"{name} - {language}\n")
print("Q28","Saved to profile.txt.")


if not os.path.exists("numbers.txt"):  # create sample data if missing
with open("numbers.txt", "w") as f:
f.write("10\n20\n30\n40\n")
total = 0
with open("numbers.txt", "r") as f:
for line in f:
line = line.strip()
if line:
total += float(line)
print("Q29","Sum of numbers:", total)

    while True:
        print("\n1. Add student record\n2. View all records\n3. Count records\n4. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            name = input("Name: ")
            age = input("Age: ")
            score = input("Exam score: ")
            with open("records.txt", "a") as f:
                f.write(f"{name},{age},{score}\n")
            print("Record saved.")
        elif choice == "2":
            if os.path.exists("records.txt"):
                with open("records.txt", "r") as f:
                    for line in f:
                        name, age, score = line.strip().split(",")
                        print(f"Name: {name} | Age: {age} | Score: {score}")
            else:
                print("No records yet.")
        elif choice == "3":
            count = 0
            if os.path.exists("records.txt"):
                with open("records.txt", "r") as f:
                    count = sum(1 for line in f if line.strip())
            print("Total records:", count)
        elif choice == "4":
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    choice = input("Enter question number (1-30) or 'all': ").strip().lower()
    if choice == "all":
        for i in range(1, 31):
            print(f"\n--- Question {i} ---")
            globals()[f"q{i}"]()
    elif choice.isdigit() and 1 <= int(choice) <= 30:
        globals()[f"q{choice}"]()
    else:
        print("Invalid choice.")Name = "Moses"
Age = 19
Height = "6ft"
Status = "Student"

print("Q1",Name)
print("Q1",Age)
print("Q1",Height)
print("Q1",Status)

a, b = 10, 3
x, y = 4.5, 1.5
print("Q2","Addition:", a + b, x + y)
print("Q2","Subtraction:", a - b, x - y)
print("Q2","Multiplication:", a * b, x * y)
print("Q2","Division:", a / b, x / y)

Name = input("Enter your name: ")
Age = int(input("Enter your age: "))
colour = input("Enter your favourite colour: ")

print("Q3",f"My name is {Name}, I am {Age} years old and my favourite colour is {colour}.")

num = 10
num2 = 20.29
name = "Ada"
Value = True

print("Q4",num, type(num), num2, type(num2), (name, type(name), (Value, type(Value))))

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Q5","Sum:", a + b)
print("Q5","Product:", a * b)
print("Q5","Difference:", a - b)

name = "Chidi"
s1, s2, s3, s4, s5 = 70, 65, 80, 55, 90
status = "Passed"
total = s1 + s2 + s3 + s4 + s5
average = total / 5
print("Q6","Name:", name)
print("Q6","Scores:", s1, s2, s3, s4, s5)
print("Q6","Status:", status)
print("Q6","Total:", total)
print("Q6","Average:", average)

fruits = ["apple", "banana", "mango", "orange", "pear", "grape", "pineapple", "guava", "lemon", "papaya"]
print("Q7","First:", fruits[0])
print("Q7","Last:", fruits[-1])
print("Q7","Total items:", len(fruits))

students = ["Ade", "Bola", "Chidi", "Dayo", "Emeka"]
students.append(input("Enter another student's name: "))
print("Q8","Updated list:", students)

Number =[1,2,3,4,5,6,7,8,9,10]
print("Q9","Even numbers:", [n for n in Number if n % 2 == 0])

nums = [15, 8, 25, 40, 12, 30, 5, 18]
largest = nums[0]
smallest = nums[0]
total = 0
for n in nums:
  if n > largest:
        largest = n
  if n < smallest:
       smallest = n
total += n
print("Q10","Largest:", largest)
print("Q10","Smallest:", smallest)
print("Q10","Sum:", total)

shopping = ["bread", "milk", "eggs", "rice", "sugar"]
for _ in range(2):
shopping.append(input("Add a product: "))
item = input("Enter a product to remove: ")
if item in shopping:
  shopping.remove(item)
else:
print("Product not found.")
print("Q11","Final shopping list:", shopping)


numbers = [5, 12, 18, 23, 7, 30, 41, 9, 15, 2]
n = int(input("Enter a number: "))
if n in numbers:
print(f"{n} exists at position (index) {numbers.index(n)}")
else:
print("Q12", f"{n} is not in the list.")

student = {"name": "Ada", "age": 20, "gender": "Female","department": "Computer Science", "matric_no": "CSC/2024/001"}
for key, value in student.items():
print("Q13", f"{key}: {value}")

products = {"Bread": 800, "Milk": 1200, "Rice": 5000, "Eggs": 2500, "Sugar": 1500}
for name, price in products.items():
print("Q14", f"{name}: {price}")

student = {"name": "Ada", "age": 20, "score": 65}
student["score"] = int(input("Enter the new score: "))
print("Q15", "Updated information:", student)

scores = {"Ade": 67, "Bola": 82, "Chidi": 75, "Dayo": 90, "Emeka": 58}
top_name, top_score = None, -1
for name, score in scores.items():
if score > top_score:
top_name, top_score = name, score
print("Q16", f"Highest score: {top_name} with {top_score}")

account = {"account_name": "Ada Obi", "account_number": "1234567890", "balance": 10000.0}
choice = input("Type 'deposit' or 'withdraw': ").strip().lower()
amount = float(input("Enter amount: "))
if choice == "deposit":
account["balance"] += amount
elif choice == "withdraw":
if amount <= account["balance"]:
account["balance"] -= amount
else:
    print("Insufficient funds.")
else:
    print("Invalid choice.")
print("Q17","Current balance:", account["balance"])

numbers = {10, 20, 30, 10, 40, 20, 50, 30}
print("Q18",numbers)

class_a = {"Ade", "Bola", "Chidi", "Dayo"}
class_b = {"Chidi", "Emeka", "Dayo", "Funke"}
print("Q19","Students in both classes:", class_a & class_b)

a = set(range(1, 11))
b = set(range(5, 16))
print("Q20","All elements:", a | b)
print("Q20","Common elements:", a & b)
print("Q20", "In first but not second:", a - b)

days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
print("Q21","First day:", days[0])
print("Q21","Last day:", days[-1])
print("Q21","Number of days:", len(days))
print("Q21","Saturday exists:", "Saturday" in days)

students = ("Ade", "Bola", "Chidi", "Dayo", "Emeka")
lst = list(students)
lst.append("Funke")
lst.append("Gozie")
lst.remove("Bola")
students = tuple(lst)
print("Q22",students)


with open("students.txt", "w") as f:
   f.write("Name: Ada\nAge: 20\nDepartment: Computer Science\n")
print("Q23","students.txt created.")


names = ["Ade", "Bola", "Chidi", "Dayo", "Emeka"]
with open("students.txt", "w") as f:  # "w" replaces previous content
for n in names:
     f.write(n + "\n")
print("Q24","students.txt overwritten with five names.")


with open("students.txt", "a") as f:  # "a" keeps previous content
for n in ["Funke", "Gozie", "Hauwa"]:
     f.write(n + "\n")
print("Q25","Three names appended.")


try:
with open("students.txt", "r") as f:
   print(f.read())
except FileNotFoundError:
print("Q26","students.txt not found. Run q23 first.")


sentences = ["Today was a good day.", "I learned about Python files.", "I wrote some code.", "I fixed a few bugs.", "Tomorrow I will practise more."]
with open("diary.txt", "w") as f:
for s in sentences:
f.write(s + "\n")
with open("diary.txt", "r") as f:
print("Q27:", f.read())

name = input("Enter your name: ")
language = input("Enter your favourite programming language: ")
with open("profile.txt", "a") as f:
f.write(f"{name} - {language}\n")
print("Q28","Saved to profile.txt.")


if not os.path.exists("numbers.txt"):  # create sample data if missing
with open("numbers.txt", "w") as f:
f.write("10\n20\n30\n40\n")
total = 0
with open("numbers.txt", "r") as f:
for line in f:
line = line.strip()
if line:
total += float(line)
print("Q29","Sum of numbers:", total)

    while True:
        print("\n1. Add student record\n2. View all records\n3. Count records\n4. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            name = input("Name: ")
            age = input("Age: ")
            score = input("Exam score: ")
            with open("records.txt", "a") as f:
                f.write(f"{name},{age},{score}\n")
            print("Record saved.")
        elif choice == "2":
            if os.path.exists("records.txt"):
                with open("records.txt", "r") as f:
                    for line in f:
                        name, age, score = line.strip().split(",")
                        print(f"Name: {name} | Age: {age} | Score: {score}")
            else:
                print("No records yet.")
        elif choice == "3":
            count = 0
            if os.path.exists("records.txt"):
                with open("records.txt", "r") as f:
                    count = sum(1 for line in f if line.strip())
            print("Total records:", count)
        elif choice == "4":
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    choice = input("Enter question number (1-30) or 'all': ").strip().lower()
    if choice == "all":
        for i in range(1, 31):
            print(f"\n--- Question {i} ---")
            globals()[f"q{i}"]()
    elif choice.isdigit() and 1 <= int(choice) <= 30:
        globals()[f"q{choice}"]()
    else:
        print("Invalid choice.")Name = "Moses"
Age = 19
Height = "6ft"
Status = "Student"

print("Q1",Name)
print("Q1",Age)
print("Q1",Height)
print("Q1",Status)

a, b = 10, 3
x, y = 4.5, 1.5
print("Q2","Addition:", a + b, x + y)
print("Q2","Subtraction:", a - b, x - y)
print("Q2","Multiplication:", a * b, x * y)
print("Q2","Division:", a / b, x / y)

Name = input("Enter your name: ")
Age = int(input("Enter your age: "))
colour = input("Enter your favourite colour: ")

print("Q3",f"My name is {Name}, I am {Age} years old and my favourite colour is {colour}.")

num = 10
num2 = 20.29
name = "Ada"
Value = True

print("Q4",num, type(num), num2, type(num2), (name, type(name), (Value, type(Value))))

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Q5","Sum:", a + b)
print("Q5","Product:", a * b)
print("Q5","Difference:", a - b)

name = "Chidi"
s1, s2, s3, s4, s5 = 70, 65, 80, 55, 90
status = "Passed"
total = s1 + s2 + s3 + s4 + s5
average = total / 5
print("Q6","Name:", name)
print("Q6","Scores:", s1, s2, s3, s4, s5)
print("Q6","Status:", status)
print("Q6","Total:", total)
print("Q6","Average:", average)

fruits = ["apple", "banana", "mango", "orange", "pear", "grape", "pineapple", "guava", "lemon", "papaya"]
print("Q7","First:", fruits[0])
print("Q7","Last:", fruits[-1])
print("Q7","Total items:", len(fruits))

students = ["Ade", "Bola", "Chidi", "Dayo", "Emeka"]
students.append(input("Enter another student's name: "))
print("Q8","Updated list:", students)

Number =[1,2,3,4,5,6,7,8,9,10]
print("Q9","Even numbers:", [n for n in Number if n % 2 == 0])

nums = [15, 8, 25, 40, 12, 30, 5, 18]
largest = nums[0]
smallest = nums[0]
total = 0
for n in nums:
  if n > largest:
        largest = n
  if n < smallest:
       smallest = n
total += n
print("Q10","Largest:", largest)
print("Q10","Smallest:", smallest)
print("Q10","Sum:", total)

shopping = ["bread", "milk", "eggs", "rice", "sugar"]
for _ in range(2):
shopping.append(input("Add a product: "))
item = input("Enter a product to remove: ")
if item in shopping:
  shopping.remove(item)
else:
print("Product not found.")
print("Q11","Final shopping list:", shopping)


numbers = [5, 12, 18, 23, 7, 30, 41, 9, 15, 2]
n = int(input("Enter a number: "))
if n in numbers:
print(f"{n} exists at position (index) {numbers.index(n)}")
else:
print("Q12", f"{n} is not in the list.")

student = {"name": "Ada", "age": 20, "gender": "Female","department": "Computer Science", "matric_no": "CSC/2024/001"}
for key, value in student.items():
print("Q13", f"{key}: {value}")

products = {"Bread": 800, "Milk": 1200, "Rice": 5000, "Eggs": 2500, "Sugar": 1500}
for name, price in products.items():
print("Q14", f"{name}: {price}")

student = {"name": "Ada", "age": 20, "score": 65}
student["score"] = int(input("Enter the new score: "))
print("Q15", "Updated information:", student)

scores = {"Ade": 67, "Bola": 82, "Chidi": 75, "Dayo": 90, "Emeka": 58}
top_name, top_score = None, -1
for name, score in scores.items():
if score > top_score:
top_name, top_score = name, score
print("Q16", f"Highest score: {top_name} with {top_score}")

account = {"account_name": "Ada Obi", "account_number": "1234567890", "balance": 10000.0}
choice = input("Type 'deposit' or 'withdraw': ").strip().lower()
amount = float(input("Enter amount: "))
if choice == "deposit":
account["balance"] += amount
elif choice == "withdraw":
if amount <= account["balance"]:
account["balance"] -= amount
else:
    print("Insufficient funds.")
else:
    print("Invalid choice.")
print("Q17","Current balance:", account["balance"])

numbers = {10, 20, 30, 10, 40, 20, 50, 30}
print("Q18",numbers)

class_a = {"Ade", "Bola", "Chidi", "Dayo"}
class_b = {"Chidi", "Emeka", "Dayo", "Funke"}
print("Q19","Students in both classes:", class_a & class_b)

a = set(range(1, 11))
b = set(range(5, 16))
print("Q20","All elements:", a | b)
print("Q20","Common elements:", a & b)
print("Q20", "In first but not second:", a - b)

days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
print("Q21","First day:", days[0])
print("Q21","Last day:", days[-1])
print("Q21","Number of days:", len(days))
print("Q21","Saturday exists:", "Saturday" in days)

students = ("Ade", "Bola", "Chidi", "Dayo", "Emeka")
lst = list(students)
lst.append("Funke")
lst.append("Gozie")
lst.remove("Bola")
students = tuple(lst)
print("Q22",students)


with open("students.txt", "w") as f:
   f.write("Name: Ada\nAge: 20\nDepartment: Computer Science\n")
print("Q23","students.txt created.")


names = ["Ade", "Bola", "Chidi", "Dayo", "Emeka"]
with open("students.txt", "w") as f:  # "w" replaces previous content
for n in names:
     f.write(n + "\n")
print("Q24","students.txt overwritten with five names.")


with open("students.txt", "a") as f:  # "a" keeps previous content
for n in ["Funke", "Gozie", "Hauwa"]:
     f.write(n + "\n")
print("Q25","Three names appended.")


try:
with open("students.txt", "r") as f:
   print(f.read())
except FileNotFoundError:
print("Q26","students.txt not found. Run q23 first.")


sentences = ["Today was a good day.", "I learned about Python files.", "I wrote some code.", "I fixed a few bugs.", "Tomorrow I will practise more."]
with open("diary.txt", "w") as f:
for s in sentences:
f.write(s + "\n")
with open("diary.txt", "r") as f:
print("Q27:", f.read())

name = input("Enter your name: ")
language = input("Enter your favourite programming language: ")
with open("profile.txt", "a") as f:
f.write(f"{name} - {language}\n")
print("Q28","Saved to profile.txt.")


if not os.path.exists("numbers.txt"):  # create sample data if missing
with open("numbers.txt", "w") as f:
f.write("10\n20\n30\n40\n")
total = 0
with open("numbers.txt", "r") as f:
for line in f:
line = line.strip()
if line:
total += float(line)
print("Q29","Sum of numbers:", total)

    while True:
        print("\n1. Add student record\n2. View all records\n3. Count records\n4. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            name = input("Name: ")
            age = input("Age: ")
            score = input("Exam score: ")
            with open("records.txt", "a") as f:
                f.write(f"{name},{age},{score}\n")
            print("Record saved.")
        elif choice == "2":
            if os.path.exists("records.txt"):
                with open("records.txt", "r") as f:
                    for line in f:
                        name, age, score = line.strip().split(",")
                        print(f"Name: {name} | Age: {age} | Score: {score}")
            else:
                print("No records yet.")
        elif choice == "3":
            count = 0
            if os.path.exists("records.txt"):
                with open("records.txt", "r") as f:
                    count = sum(1 for line in f if line.strip())
            print("Total records:", count)
        elif choice == "4":
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    choice = input("Enter question number (1-30) or 'all': ").strip().lower()
    if choice == "all":
        for i in range(1, 31):
            print(f"\n--- Question {i} ---")
            globals()[f"q{i}"]()
    elif choice.isdigit() and 1 <= int(choice) <= 30:
        globals()[f"q{choice}"]()
    else:
        print("Invalid choice.")Name = "Moses"
Age = 19
Height = "6ft"
Status = "Student"

print("Q1",Name)
print("Q1",Age)
print("Q1",Height)
print("Q1",Status)

a, b = 10, 3
x, y = 4.5, 1.5
print("Q2","Addition:", a + b, x + y)
print("Q2","Subtraction:", a - b, x - y)
print("Q2","Multiplication:", a * b, x * y)
print("Q2","Division:", a / b, x / y)

Name = input("Enter your name: ")
Age = int(input("Enter your age: "))
colour = input("Enter your favourite colour: ")

print("Q3",f"My name is {Name}, I am {Age} years old and my favourite colour is {colour}.")

num = 10
num2 = 20.29
name = "Ada"
Value = True

print("Q4",num, type(num), num2, type(num2), (name, type(name), (Value, type(Value))))

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Q5","Sum:", a + b)
print("Q5","Product:", a * b)
print("Q5","Difference:", a - b)

name = "Chidi"
s1, s2, s3, s4, s5 = 70, 65, 80, 55, 90
status = "Passed"
total = s1 + s2 + s3 + s4 + s5
average = total / 5
print("Q6","Name:", name)
print("Q6","Scores:", s1, s2, s3, s4, s5)
print("Q6","Status:", status)
print("Q6","Total:", total)
print("Q6","Average:", average)

fruits = ["apple", "banana", "mango", "orange", "pear", "grape", "pineapple", "guava", "lemon", "papaya"]
print("Q7","First:", fruits[0])
print("Q7","Last:", fruits[-1])
print("Q7","Total items:", len(fruits))

students = ["Ade", "Bola", "Chidi", "Dayo", "Emeka"]
students.append(input("Enter another student's name: "))
print("Q8","Updated list:", students)

Number =[1,2,3,4,5,6,7,8,9,10]
print("Q9","Even numbers:", [n for n in Number if n % 2 == 0])

nums = [15, 8, 25, 40, 12, 30, 5, 18]
largest = nums[0]
smallest = nums[0]
total = 0
for n in nums:
  if n > largest:
        largest = n
  if n < smallest:
       smallest = n
total += n
print("Q10","Largest:", largest)
print("Q10","Smallest:", smallest)
print("Q10","Sum:", total)

shopping = ["bread", "milk", "eggs", "rice", "sugar"]
for _ in range(2):
shopping.append(input("Add a product: "))
item = input("Enter a product to remove: ")
if item in shopping:
  shopping.remove(item)
else:
print("Product not found.")
print("Q11","Final shopping list:", shopping)


numbers = [5, 12, 18, 23, 7, 30, 41, 9, 15, 2]
n = int(input("Enter a number: "))
if n in numbers:
print(f"{n} exists at position (index) {numbers.index(n)}")
else:
print("Q12", f"{n} is not in the list.")

student = {"name": "Ada", "age": 20, "gender": "Female","department": "Computer Science", "matric_no": "CSC/2024/001"}
for key, value in student.items():
print("Q13", f"{key}: {value}")

products = {"Bread": 800, "Milk": 1200, "Rice": 5000, "Eggs": 2500, "Sugar": 1500}
for name, price in products.items():
print("Q14", f"{name}: {price}")

student = {"name": "Ada", "age": 20, "score": 65}
student["score"] = int(input("Enter the new score: "))
print("Q15", "Updated information:", student)

scores = {"Ade": 67, "Bola": 82, "Chidi": 75, "Dayo": 90, "Emeka": 58}
top_name, top_score = None, -1
for name, score in scores.items():
if score > top_score:
top_name, top_score = name, score
print("Q16", f"Highest score: {top_name} with {top_score}")

account = {"account_name": "Ada Obi", "account_number": "1234567890", "balance": 10000.0}
choice = input("Type 'deposit' or 'withdraw': ").strip().lower()
amount = float(input("Enter amount: "))
if choice == "deposit":
account["balance"] += amount
elif choice == "withdraw":
if amount <= account["balance"]:
account["balance"] -= amount
else:
    print("Insufficient funds.")
else:
    print("Invalid choice.")
print("Q17","Current balance:", account["balance"])

numbers = {10, 20, 30, 10, 40, 20, 50, 30}
print("Q18",numbers)

class_a = {"Ade", "Bola", "Chidi", "Dayo"}
class_b = {"Chidi", "Emeka", "Dayo", "Funke"}
print("Q19","Students in both classes:", class_a & class_b)

a = set(range(1, 11))
b = set(range(5, 16))
print("Q20","All elements:", a | b)
print("Q20","Common elements:", a & b)
print("Q20", "In first but not second:", a - b)

days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
print("Q21","First day:", days[0])
print("Q21","Last day:", days[-1])
print("Q21","Number of days:", len(days))
print("Q21","Saturday exists:", "Saturday" in days)

students = ("Ade", "Bola", "Chidi", "Dayo", "Emeka")
lst = list(students)
lst.append("Funke")
lst.append("Gozie")
lst.remove("Bola")
students = tuple(lst)
print("Q22",students)


with open("students.txt", "w") as f:
   f.write("Name: Ada\nAge: 20\nDepartment: Computer Science\n")
print("Q23","students.txt created.")


names = ["Ade", "Bola", "Chidi", "Dayo", "Emeka"]
with open("students.txt", "w") as f:  # "w" replaces previous content
for n in names:
     f.write(n + "\n")
print("Q24","students.txt overwritten with five names.")


with open("students.txt", "a") as f:  # "a" keeps previous content
for n in ["Funke", "Gozie", "Hauwa"]:
     f.write(n + "\n")
print("Q25","Three names appended.")


try:
with open("students.txt", "r") as f:
   print(f.read())
except FileNotFoundError:
print("Q26","students.txt not found. Run q23 first.")


sentences = ["Today was a good day.", "I learned about Python files.", "I wrote some code.", "I fixed a few bugs.", "Tomorrow I will practise more."]
with open("diary.txt", "w") as f:
for s in sentences:
f.write(s + "\n")
with open("diary.txt", "r") as f:
print("Q27:", f.read())

name = input("Enter your name: ")
language = input("Enter your favourite programming language: ")
with open("profile.txt", "a") as f:
f.write(f"{name} - {language}\n")
print("Q28","Saved to profile.txt.")


if not os.path.exists("numbers.txt"):  # create sample data if missing
with open("numbers.txt", "w") as f:
f.write("10\n20\n30\n40\n")
total = 0
with open("numbers.txt", "r") as f:
for line in f:
line = line.strip()
if line:
total += float(line)
print("Q29","Sum of numbers:", total)

    while True:
        print("\n1. Add student record\n2. View all records\n3. Count records\n4. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            name = input("Name: ")
            age = input("Age: ")
            score = input("Exam score: ")
            with open("records.txt", "a") as f:
                f.write(f"{name},{age},{score}\n")
            print("Record saved.")
        elif choice == "2":
            if os.path.exists("records.txt"):
                with open("records.txt", "r") as f:
                    for line in f:
                        name, age, score = line.strip().split(",")
                        print(f"Name: {name} | Age: {age} | Score: {score}")
            else:
                print("No records yet.")
        elif choice == "3":
            count = 0
            if os.path.exists("records.txt"):
                with open("records.txt", "r") as f:
                    count = sum(1 for line in f if line.strip())
            print("Total records:", count)
        elif choice == "4":
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    choice = input("Enter question number (1-30) or 'all': ").strip().lower()
    if choice == "all":
        for i in range(1, 31):
            print(f"\n--- Question {i} ---")
            globals()[f"q{i}"]()
    elif choice.isdigit() and 1 <= int(choice) <= 30:
        globals()[f"q{choice}"]()
    else:
        print("Invalid choice.")Name = "Moses"
Age = 19
Height = "6ft"
Status = "Student"

print("Q1",Name)
print("Q1",Age)
print("Q1",Height)
print("Q1",Status)

a, b = 10, 3
x, y = 4.5, 1.5
print("Q2","Addition:", a + b, x + y)
print("Q2","Subtraction:", a - b, x - y)
print("Q2","Multiplication:", a * b, x * y)
print("Q2","Division:", a / b, x / y)

Name = input("Enter your name: ")
Age = int(input("Enter your age: "))
colour = input("Enter your favourite colour: ")

print("Q3",f"My name is {Name}, I am {Age} years old and my favourite colour is {colour}.")

num = 10
num2 = 20.29
name = "Ada"
Value = True

print("Q4",num, type(num), num2, type(num2), (name, type(name), (Value, type(Value))))

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Q5","Sum:", a + b)
print("Q5","Product:", a * b)
print("Q5","Difference:", a - b)

name = "Chidi"
s1, s2, s3, s4, s5 = 70, 65, 80, 55, 90
status = "Passed"
total = s1 + s2 + s3 + s4 + s5
average = total / 5
print("Q6","Name:", name)
print("Q6","Scores:", s1, s2, s3, s4, s5)
print("Q6","Status:", status)
print("Q6","Total:", total)
print("Q6","Average:", average)

fruits = ["apple", "banana", "mango", "orange", "pear", "grape", "pineapple", "guava", "lemon", "papaya"]
print("Q7","First:", fruits[0])
print("Q7","Last:", fruits[-1])
print("Q7","Total items:", len(fruits))

students = ["Ade", "Bola", "Chidi", "Dayo", "Emeka"]
students.append(input("Enter another student's name: "))
print("Q8","Updated list:", students)

Number =[1,2,3,4,5,6,7,8,9,10]
print("Q9","Even numbers:", [n for n in Number if n % 2 == 0])

nums = [15, 8, 25, 40, 12, 30, 5, 18]
largest = nums[0]
smallest = nums[0]
total = 0
for n in nums:
  if n > largest:
        largest = n
  if n < smallest:
       smallest = n
total += n
print("Q10","Largest:", largest)
print("Q10","Smallest:", smallest)
print("Q10","Sum:", total)

shopping = ["bread", "milk", "eggs", "rice", "sugar"]
for _ in range(2):
shopping.append(input("Add a product: "))
item = input("Enter a product to remove: ")
if item in shopping:
  shopping.remove(item)
else:
print("Product not found.")
print("Q11","Final shopping list:", shopping)


numbers = [5, 12, 18, 23, 7, 30, 41, 9, 15, 2]
n = int(input("Enter a number: "))
if n in numbers:
print(f"{n} exists at position (index) {numbers.index(n)}")
else:
print("Q12", f"{n} is not in the list.")

student = {"name": "Ada", "age": 20, "gender": "Female","department": "Computer Science", "matric_no": "CSC/2024/001"}
for key, value in student.items():
print("Q13", f"{key}: {value}")

products = {"Bread": 800, "Milk": 1200, "Rice": 5000, "Eggs": 2500, "Sugar": 1500}
for name, price in products.items():
print("Q14", f"{name}: {price}")

student = {"name": "Ada", "age": 20, "score": 65}
student["score"] = int(input("Enter the new score: "))
print("Q15", "Updated information:", student)

scores = {"Ade": 67, "Bola": 82, "Chidi": 75, "Dayo": 90, "Emeka": 58}
top_name, top_score = None, -1
for name, score in scores.items():
if score > top_score:
top_name, top_score = name, score
print("Q16", f"Highest score: {top_name} with {top_score}")

account = {"account_name": "Ada Obi", "account_number": "1234567890", "balance": 10000.0}
choice = input("Type 'deposit' or 'withdraw': ").strip().lower()
amount = float(input("Enter amount: "))
if choice == "deposit":
account["balance"] += amount
elif choice == "withdraw":
if amount <= account["balance"]:
account["balance"] -= amount
else:
    print("Insufficient funds.")
else:
    print("Invalid choice.")
print("Q17","Current balance:", account["balance"])

numbers = {10, 20, 30, 10, 40, 20, 50, 30}
print("Q18",numbers)

class_a = {"Ade", "Bola", "Chidi", "Dayo"}
class_b = {"Chidi", "Emeka", "Dayo", "Funke"}
print("Q19","Students in both classes:", class_a & class_b)

a = set(range(1, 11))
b = set(range(5, 16))
print("Q20","All elements:", a | b)
print("Q20","Common elements:", a & b)
print("Q20", "In first but not second:", a - b)

days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
print("Q21","First day:", days[0])
print("Q21","Last day:", days[-1])
print("Q21","Number of days:", len(days))
print("Q21","Saturday exists:", "Saturday" in days)

students = ("Ade", "Bola", "Chidi", "Dayo", "Emeka")
lst = list(students)
lst.append("Funke")
lst.append("Gozie")
lst.remove("Bola")
students = tuple(lst)
print("Q22",students)


with open("students.txt", "w") as f:
   f.write("Name: Ada\nAge: 20\nDepartment: Computer Science\n")
print("Q23","students.txt created.")


names = ["Ade", "Bola", "Chidi", "Dayo", "Emeka"]
with open("students.txt", "w") as f:  # "w" replaces previous content
for n in names:
     f.write(n + "\n")
print("Q24","students.txt overwritten with five names.")


with open("students.txt", "a") as f:  # "a" keeps previous content
for n in ["Funke", "Gozie", "Hauwa"]:
     f.write(n + "\n")
print("Q25","Three names appended.")


try:
with open("students.txt", "r") as f:
   print(f.read())
except FileNotFoundError:
print("Q26","students.txt not found. Run q23 first.")


sentences = ["Today was a good day.", "I learned about Python files.", "I wrote some code.", "I fixed a few bugs.", "Tomorrow I will practise more."]
with open("diary.txt", "w") as f:
for s in sentences:
f.write(s + "\n")
with open("diary.txt", "r") as f:
print("Q27:", f.read())

name = input("Enter your name: ")
language = input("Enter your favourite programming language: ")
with open("profile.txt", "a") as f:
f.write(f"{name} - {language}\n")
print("Q28","Saved to profile.txt.")


if not os.path.exists("numbers.txt"):  # create sample data if missing
with open("numbers.txt", "w") as f:
f.write("10\n20\n30\n40\n")
total = 0
with open("numbers.txt", "r") as f:
for line in f:
line = line.strip()
if line:
total += float(line)
print("Q29","Sum of numbers:", total)

    while True:
        print("\n1. Add student record\n2. View all records\n3. Count records\n4. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            name = input("Name: ")
            age = input("Age: ")
            score = input("Exam score: ")
            with open("records.txt", "a") as f:
                f.write(f"{name},{age},{score}\n")
            print("Record saved.")
        elif choice == "2":
            if os.path.exists("records.txt"):
                with open("records.txt", "r") as f:
                    for line in f:
                        name, age, score = line.strip().split(",")
                        print(f"Name: {name} | Age: {age} | Score: {score}")
            else:
                print("No records yet.")
        elif choice == "3":
            count = 0
            if os.path.exists("records.txt"):
                with open("records.txt", "r") as f:
                    count = sum(1 for line in f if line.strip())
            print("Total records:", count)
        elif choice == "4":
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    choice = input("Enter question number (1-30) or 'all': ").strip().lower()
    if choice == "all":
        for i in range(1, 31):
            print(f"\n--- Question {i} ---")
            globals()[f"q{i}"]()
    elif choice.isdigit() and 1 <= int(choice) <= 30:
        globals()[f"q{choice}"]()
    else:
        print("Invalid choice.")Name = "Moses"
Age = 19
Height = "6ft"
Status = "Student"

print("Q1",Name)
print("Q1",Age)
print("Q1",Height)
print("Q1",Status)

a, b = 10, 3
x, y = 4.5, 1.5
print("Q2","Addition:", a + b, x + y)
print("Q2","Subtraction:", a - b, x - y)
print("Q2","Multiplication:", a * b, x * y)
print("Q2","Division:", a / b, x / y)

Name = input("Enter your name: ")
Age = int(input("Enter your age: "))
colour = input("Enter your favourite colour: ")

print("Q3",f"My name is {Name}, I am {Age} years old and my favourite colour is {colour}.")

num = 10
num2 = 20.29
name = "Ada"
Value = True

print("Q4",num, type(num), num2, type(num2), (name, type(name), (Value, type(Value))))

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Q5","Sum:", a + b)
print("Q5","Product:", a * b)
print("Q5","Difference:", a - b)

name = "Chidi"
s1, s2, s3, s4, s5 = 70, 65, 80, 55, 90
status = "Passed"
total = s1 + s2 + s3 + s4 + s5
average = total / 5
print("Q6","Name:", name)
print("Q6","Scores:", s1, s2, s3, s4, s5)
print("Q6","Status:", status)
print("Q6","Total:", total)
print("Q6","Average:", average)

fruits = ["apple", "banana", "mango", "orange", "pear", "grape", "pineapple", "guava", "lemon", "papaya"]
print("Q7","First:", fruits[0])
print("Q7","Last:", fruits[-1])
print("Q7","Total items:", len(fruits))

students = ["Ade", "Bola", "Chidi", "Dayo", "Emeka"]
students.append(input("Enter another student's name: "))
print("Q8","Updated list:", students)

Number =[1,2,3,4,5,6,7,8,9,10]
print("Q9","Even numbers:", [n for n in Number if n % 2 == 0])

nums = [15, 8, 25, 40, 12, 30, 5, 18]
largest = nums[0]
smallest = nums[0]
total = 0
for n in nums:
  if n > largest:
        largest = n
  if n < smallest:
       smallest = n
total += n
print("Q10","Largest:", largest)
print("Q10","Smallest:", smallest)
print("Q10","Sum:", total)

shopping = ["bread", "milk", "eggs", "rice", "sugar"]
for _ in range(2):
shopping.append(input("Add a product: "))
item = input("Enter a product to remove: ")
if item in shopping:
  shopping.remove(item)
else:
print("Product not found.")
print("Q11","Final shopping list:", shopping)


numbers = [5, 12, 18, 23, 7, 30, 41, 9, 15, 2]
n = int(input("Enter a number: "))
if n in numbers:
print(f"{n} exists at position (index) {numbers.index(n)}")
else:
print("Q12", f"{n} is not in the list.")

student = {"name": "Ada", "age": 20, "gender": "Female","department": "Computer Science", "matric_no": "CSC/2024/001"}
for key, value in student.items():
print("Q13", f"{key}: {value}")

products = {"Bread": 800, "Milk": 1200, "Rice": 5000, "Eggs": 2500, "Sugar": 1500}
for name, price in products.items():
print("Q14", f"{name}: {price}")

student = {"name": "Ada", "age": 20, "score": 65}
student["score"] = int(input("Enter the new score: "))
print("Q15", "Updated information:", student)

scores = {"Ade": 67, "Bola": 82, "Chidi": 75, "Dayo": 90, "Emeka": 58}
top_name, top_score = None, -1
for name, score in scores.items():
if score > top_score:
top_name, top_score = name, score
print("Q16", f"Highest score: {top_name} with {top_score}")

account = {"account_name": "Ada Obi", "account_number": "1234567890", "balance": 10000.0}
choice = input("Type 'deposit' or 'withdraw': ").strip().lower()
amount = float(input("Enter amount: "))
if choice == "deposit":
account["balance"] += amount
elif choice == "withdraw":
if amount <= account["balance"]:
account["balance"] -= amount
else:
    print("Insufficient funds.")
else:
    print("Invalid choice.")
print("Q17","Current balance:", account["balance"])

numbers = {10, 20, 30, 10, 40, 20, 50, 30}
print("Q18",numbers)

class_a = {"Ade", "Bola", "Chidi", "Dayo"}
class_b = {"Chidi", "Emeka", "Dayo", "Funke"}
print("Q19","Students in both classes:", class_a & class_b)

a = set(range(1, 11))
b = set(range(5, 16))
print("Q20","All elements:", a | b)
print("Q20","Common elements:", a & b)
print("Q20", "In first but not second:", a - b)

days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
print("Q21","First day:", days[0])
print("Q21","Last day:", days[-1])
print("Q21","Number of days:", len(days))
print("Q21","Saturday exists:", "Saturday" in days)

students = ("Ade", "Bola", "Chidi", "Dayo", "Emeka")
lst = list(students)
lst.append("Funke")
lst.append("Gozie")
lst.remove("Bola")
students = tuple(lst)
print("Q22",students)


with open("students.txt", "w") as f:
   f.write("Name: Ada\nAge: 20\nDepartment: Computer Science\n")
print("Q23","students.txt created.")


names = ["Ade", "Bola", "Chidi", "Dayo", "Emeka"]
with open("students.txt", "w") as f:  # "w" replaces previous content
for n in names:
     f.write(n + "\n")
print("Q24","students.txt overwritten with five names.")


with open("students.txt", "a") as f:  # "a" keeps previous content
for n in ["Funke", "Gozie", "Hauwa"]:
     f.write(n + "\n")
print("Q25","Three names appended.")


try:
with open("students.txt", "r") as f:
   print(f.read())
except FileNotFoundError:
print("Q26","students.txt not found. Run q23 first.")


sentences = ["Today was a good day.", "I learned about Python files.", "I wrote some code.", "I fixed a few bugs.", "Tomorrow I will practise more."]
with open("diary.txt", "w") as f:
for s in sentences:
f.write(s + "\n")
with open("diary.txt", "r") as f:
print("Q27:", f.read())

name = input("Enter your name: ")
language = input("Enter your favourite programming language: ")
with open("profile.txt", "a") as f:
f.write(f"{name} - {language}\n")
print("Q28","Saved to profile.txt.")


if not os.path.exists("numbers.txt"):  # create sample data if missing
with open("numbers.txt", "w") as f:
f.write("10\n20\n30\n40\n")
total = 0
with open("numbers.txt", "r") as f:
for line in f:
line = line.strip()
if line:
total += float(line)
print("Q29","Sum of numbers:", total)

    while True:
        print("\n1. Add student record\n2. View all records\n3. Count records\n4. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            name = input("Name: ")
            age = input("Age: ")
            score = input("Exam score: ")
            with open("records.txt", "a") as f:
                f.write(f"{name},{age},{score}\n")
            print("Record saved.")
        elif choice == "2":
            if os.path.exists("records.txt"):
                with open("records.txt", "r") as f:
                    for line in f:
                        name, age, score = line.strip().split(",")
                        print(f"Name: {name} | Age: {age} | Score: {score}")
            else:
                print("No records yet.")
        elif choice == "3":
            count = 0
            if os.path.exists("records.txt"):
                with open("records.txt", "r") as f:
                    count = sum(1 for line in f if line.strip())
            print("Total records:", count)
        elif choice == "4":
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    choice = input("Enter question number (1-30) or 'all': ").strip().lower()
    if choice == "all":
        for i in range(1, 31):
            print(f"\n--- Question {i} ---")
            globals()[f"q{i}"]()
    elif choice.isdigit() and 1 <= int(choice) <= 30:
        globals()[f"q{choice}"]()
    else:
        print("Invalid choice.")Name = "Moses"
Age = 19
Height = "6ft"
Status = "Student"

print("Q1",Name)
print("Q1",Age)
print("Q1",Height)
print("Q1",Status)

a, b = 10, 3
x, y = 4.5, 1.5
print("Q2","Addition:", a + b, x + y)
print("Q2","Subtraction:", a - b, x - y)
print("Q2","Multiplication:", a * b, x * y)
print("Q2","Division:", a / b, x / y)

Name = input("Enter your name: ")
Age = int(input("Enter your age: "))
colour = input("Enter your favourite colour: ")

print("Q3",f"My name is {Name}, I am {Age} years old and my favourite colour is {colour}.")

num = 10
num2 = 20.29
name = "Ada"
Value = True

print("Q4",num, type(num), num2, type(num2), (name, type(name), (Value, type(Value))))

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Q5","Sum:", a + b)
print("Q5","Product:", a * b)
print("Q5","Difference:", a - b)

name = "Chidi"
s1, s2, s3, s4, s5 = 70, 65, 80, 55, 90
status = "Passed"
total = s1 + s2 + s3 + s4 + s5
average = total / 5
print("Q6","Name:", name)
print("Q6","Scores:", s1, s2, s3, s4, s5)
print("Q6","Status:", status)
print("Q6","Total:", total)
print("Q6","Average:", average)

fruits = ["apple", "banana", "mango", "orange", "pear", "grape", "pineapple", "guava", "lemon", "papaya"]
print("Q7","First:", fruits[0])
print("Q7","Last:", fruits[-1])
print("Q7","Total items:", len(fruits))

students = ["Ade", "Bola", "Chidi", "Dayo", "Emeka"]
students.append(input("Enter another student's name: "))
print("Q8","Updated list:", students)

Number =[1,2,3,4,5,6,7,8,9,10]
print("Q9","Even numbers:", [n for n in Number if n % 2 == 0])

nums = [15, 8, 25, 40, 12, 30, 5, 18]
largest = nums[0]
smallest = nums[0]
total = 0
for n in nums:
  if n > largest:
        largest = n
  if n < smallest:
       smallest = n
total += n
print("Q10","Largest:", largest)
print("Q10","Smallest:", smallest)
print("Q10","Sum:", total)

shopping = ["bread", "milk", "eggs", "rice", "sugar"]
for _ in range(2):
shopping.append(input("Add a product: "))
item = input("Enter a product to remove: ")
if item in shopping:
  shopping.remove(item)
else:
print("Product not found.")
print("Q11","Final shopping list:", shopping)


numbers = [5, 12, 18, 23, 7, 30, 41, 9, 15, 2]
n = int(input("Enter a number: "))
if n in numbers:
print(f"{n} exists at position (index) {numbers.index(n)}")
else:
print("Q12", f"{n} is not in the list.")

student = {"name": "Ada", "age": 20, "gender": "Female","department": "Computer Science", "matric_no": "CSC/2024/001"}
for key, value in student.items():
print("Q13", f"{key}: {value}")

products = {"Bread": 800, "Milk": 1200, "Rice": 5000, "Eggs": 2500, "Sugar": 1500}
for name, price in products.items():
print("Q14", f"{name}: {price}")

student = {"name": "Ada", "age": 20, "score": 65}
student["score"] = int(input("Enter the new score: "))
print("Q15", "Updated information:", student)

scores = {"Ade": 67, "Bola": 82, "Chidi": 75, "Dayo": 90, "Emeka": 58}
top_name, top_score = None, -1
for name, score in scores.items():
if score > top_score:
top_name, top_score = name, score
print("Q16", f"Highest score: {top_name} with {top_score}")

account = {"account_name": "Ada Obi", "account_number": "1234567890", "balance": 10000.0}
choice = input("Type 'deposit' or 'withdraw': ").strip().lower()
amount = float(input("Enter amount: "))
if choice == "deposit":
account["balance"] += amount
elif choice == "withdraw":
if amount <= account["balance"]:
account["balance"] -= amount
else:
    print("Insufficient funds.")
else:
    print("Invalid choice.")
print("Q17","Current balance:", account["balance"])

numbers = {10, 20, 30, 10, 40, 20, 50, 30}
print("Q18",numbers)

class_a = {"Ade", "Bola", "Chidi", "Dayo"}
class_b = {"Chidi", "Emeka", "Dayo", "Funke"}
print("Q19","Students in both classes:", class_a & class_b)

a = set(range(1, 11))
b = set(range(5, 16))
print("Q20","All elements:", a | b)
print("Q20","Common elements:", a & b)
print("Q20", "In first but not second:", a - b)

days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
print("Q21","First day:", days[0])
print("Q21","Last day:", days[-1])
print("Q21","Number of days:", len(days))
print("Q21","Saturday exists:", "Saturday" in days)

students = ("Ade", "Bola", "Chidi", "Dayo", "Emeka")
lst = list(students)
lst.append("Funke")
lst.append("Gozie")
lst.remove("Bola")
students = tuple(lst)
print("Q22",students)


with open("students.txt", "w") as f:
   f.write("Name: Ada\nAge: 20\nDepartment: Computer Science\n")
print("Q23","students.txt created.")


names = ["Ade", "Bola", "Chidi", "Dayo", "Emeka"]
with open("students.txt", "w") as f:  # "w" replaces previous content
for n in names:
     f.write(n + "\n")
print("Q24","students.txt overwritten with five names.")


with open("students.txt", "a") as f:  # "a" keeps previous content
for n in ["Funke", "Gozie", "Hauwa"]:
     f.write(n + "\n")
print("Q25","Three names appended.")


try:
with open("students.txt", "r") as f:
   print(f.read())
except FileNotFoundError:
print("Q26","students.txt not found. Run q23 first.")


sentences = ["Today was a good day.", "I learned about Python files.", "I wrote some code.", "I fixed a few bugs.", "Tomorrow I will practise more."]
with open("diary.txt", "w") as f:
for s in sentences:
f.write(s + "\n")
with open("diary.txt", "r") as f:
print("Q27:", f.read())

name = input("Enter your name: ")
language = input("Enter your favourite programming language: ")
with open("profile.txt", "a") as f:
f.write(f"{name} - {language}\n")
print("Q28","Saved to profile.txt.")


if not os.path.exists("numbers.txt"):  # create sample data if missing
with open("numbers.txt", "w") as f:
f.write("10\n20\n30\n40\n")
total = 0
with open("numbers.txt", "r") as f:
for line in f:
line = line.strip()
if line:
total += float(line)
print("Q29","Sum of numbers:", total)

    while True:
        print("\n1. Add student record\n2. View all records\n3. Count records\n4. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            name = input("Name: ")
            age = input("Age: ")
            score = input("Exam score: ")
            with open("records.txt", "a") as f:
                f.write(f"{name},{age},{score}\n")
            print("Record saved.")
        elif choice == "2":
            if os.path.exists("records.txt"):
                with open("records.txt", "r") as f:
                    for line in f:
                        name, age, score = line.strip().split(",")
                        print(f"Name: {name} | Age: {age} | Score: {score}")
            else:
                print("No records yet.")
        elif choice == "3":
            count = 0
            if os.path.exists("records.txt"):
                with open("records.txt", "r") as f:
                    count = sum(1 for line in f if line.strip())
            print("Total records:", count)
        elif choice == "4":
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    choice = input("Enter question number (1-30) or 'all': ").strip().lower()
    if choice == "all":
        for i in range(1, 31):
            print(f"\n--- Question {i} ---")
            globals()[f"q{i}"]()
    elif choice.isdigit() and 1 <= int(choice) <= 30:
        globals()[f"q{choice}"]()
    else:
        print("Invalid choice.")Name = "Moses"
Age = 19
Height = "6ft"
Status = "Student"

print("Q1",Name)
print("Q1",Age)
print("Q1",Height)
print("Q1",Status)

a, b = 10, 3
x, y = 4.5, 1.5
print("Q2","Addition:", a + b, x + y)
print("Q2","Subtraction:", a - b, x - y)
print("Q2","Multiplication:", a * b, x * y)
print("Q2","Division:", a / b, x / y)

Name = input("Enter your name: ")
Age = int(input("Enter your age: "))
colour = input("Enter your favourite colour: ")

print("Q3",f"My name is {Name}, I am {Age} years old and my favourite colour is {colour}.")

num = 10
num2 = 20.29
name = "Ada"
Value = True

print("Q4",num, type(num), num2, type(num2), (name, type(name), (Value, type(Value))))

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Q5","Sum:", a + b)
print("Q5","Product:", a * b)
print("Q5","Difference:", a - b)

name = "Chidi"
s1, s2, s3, s4, s5 = 70, 65, 80, 55, 90
status = "Passed"
total = s1 + s2 + s3 + s4 + s5
average = total / 5
print("Q6","Name:", name)
print("Q6","Scores:", s1, s2, s3, s4, s5)
print("Q6","Status:", status)
print("Q6","Total:", total)
print("Q6","Average:", average)

fruits = ["apple", "banana", "mango", "orange", "pear", "grape", "pineapple", "guava", "lemon", "papaya"]
print("Q7","First:", fruits[0])
print("Q7","Last:", fruits[-1])
print("Q7","Total items:", len(fruits))

students = ["Ade", "Bola", "Chidi", "Dayo", "Emeka"]
students.append(input("Enter another student's name: "))
print("Q8","Updated list:", students)

Number =[1,2,3,4,5,6,7,8,9,10]
print("Q9","Even numbers:", [n for n in Number if n % 2 == 0])

nums = [15, 8, 25, 40, 12, 30, 5, 18]
largest = nums[0]
smallest = nums[0]
total = 0
for n in nums:
  if n > largest:
        largest = n
  if n < smallest:
       smallest = n
total += n
print("Q10","Largest:", largest)
print("Q10","Smallest:", smallest)
print("Q10","Sum:", total)

shopping = ["bread", "milk", "eggs", "rice", "sugar"]
for _ in range(2):
shopping.append(input("Add a product: "))
item = input("Enter a product to remove: ")
if item in shopping:
  shopping.remove(item)
else:
print("Product not found.")
print("Q11","Final shopping list:", shopping)


numbers = [5, 12, 18, 23, 7, 30, 41, 9, 15, 2]
n = int(input("Enter a number: "))
if n in numbers:
print(f"{n} exists at position (index) {numbers.index(n)}")
else:
print("Q12", f"{n} is not in the list.")

student = {"name": "Ada", "age": 20, "gender": "Female","department": "Computer Science", "matric_no": "CSC/2024/001"}
for key, value in student.items():
print("Q13", f"{key}: {value}")

products = {"Bread": 800, "Milk": 1200, "Rice": 5000, "Eggs": 2500, "Sugar": 1500}
for name, price in products.items():
print("Q14", f"{name}: {price}")

student = {"name": "Ada", "age": 20, "score": 65}
student["score"] = int(input("Enter the new score: "))
print("Q15", "Updated information:", student)

scores = {"Ade": 67, "Bola": 82, "Chidi": 75, "Dayo": 90, "Emeka": 58}
top_name, top_score = None, -1
for name, score in scores.items():
if score > top_score:
top_name, top_score = name, score
print("Q16", f"Highest score: {top_name} with {top_score}")

account = {"account_name": "Ada Obi", "account_number": "1234567890", "balance": 10000.0}
choice = input("Type 'deposit' or 'withdraw': ").strip().lower()
amount = float(input("Enter amount: "))
if choice == "deposit":
account["balance"] += amount
elif choice == "withdraw":
if amount <= account["balance"]:
account["balance"] -= amount
else:
    print("Insufficient funds.")
else:
    print("Invalid choice.")
print("Q17","Current balance:", account["balance"])

numbers = {10, 20, 30, 10, 40, 20, 50, 30}
print("Q18",numbers)

class_a = {"Ade", "Bola", "Chidi", "Dayo"}
class_b = {"Chidi", "Emeka", "Dayo", "Funke"}
print("Q19","Students in both classes:", class_a & class_b)

a = set(range(1, 11))
b = set(range(5, 16))
print("Q20","All elements:", a | b)
print("Q20","Common elements:", a & b)
print("Q20", "In first but not second:", a - b)

days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
print("Q21","First day:", days[0])
print("Q21","Last day:", days[-1])
print("Q21","Number of days:", len(days))
print("Q21","Saturday exists:", "Saturday" in days)

students = ("Ade", "Bola", "Chidi", "Dayo", "Emeka")
lst = list(students)
lst.append("Funke")
lst.append("Gozie")
lst.remove("Bola")
students = tuple(lst)
print("Q22",students)


with open("students.txt", "w") as f:
   f.write("Name: Ada\nAge: 20\nDepartment: Computer Science\n")
print("Q23","students.txt created.")


names = ["Ade", "Bola", "Chidi", "Dayo", "Emeka"]
with open("students.txt", "w") as f:  # "w" replaces previous content
for n in names:
     f.write(n + "\n")
print("Q24","students.txt overwritten with five names.")


with open("students.txt", "a") as f:  # "a" keeps previous content
for n in ["Funke", "Gozie", "Hauwa"]:
     f.write(n + "\n")
print("Q25","Three names appended.")


try:
with open("students.txt", "r") as f:
   print(f.read())
except FileNotFoundError:
print("Q26","students.txt not found. Run q23 first.")


sentences = ["Today was a good day.", "I learned about Python files.", "I wrote some code.", "I fixed a few bugs.", "Tomorrow I will practise more."]
with open("diary.txt", "w") as f:
for s in sentences:
f.write(s + "\n")
with open("diary.txt", "r") as f:
print("Q27:", f.read())

name = input("Enter your name: ")
language = input("Enter your favourite programming language: ")
with open("profile.txt", "a") as f:
f.write(f"{name} - {language}\n")
print("Q28","Saved to profile.txt.")


if not os.path.exists("numbers.txt"):  # create sample data if missing
with open("numbers.txt", "w") as f:
f.write("10\n20\n30\n40\n")
total = 0
with open("numbers.txt", "r") as f:
for line in f:
line = line.strip()
if line:
total += float(line)
print("Q29","Sum of numbers:", total)

    while True:
        print("\n1. Add student record\n2. View all records\n3. Count records\n4. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            name = input("Name: ")
            age = input("Age: ")
            score = input("Exam score: ")
            with open("records.txt", "a") as f:
                f.write(f"{name},{age},{score}\n")
            print("Record saved.")
        elif choice == "2":
            if os.path.exists("records.txt"):
                with open("records.txt", "r") as f:
                    for line in f:
                        name, age, score = line.strip().split(",")
                        print(f"Name: {name} | Age: {age} | Score: {score}")
            else:
                print("No records yet.")
        elif choice == "3":
            count = 0
            if os.path.exists("records.txt"):
                with open("records.txt", "r") as f:
                    count = sum(1 for line in f if line.strip())
            print("Total records:", count)
        elif choice == "4":
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    choice = input("Enter question number (1-30) or 'all': ").strip().lower()
    if choice == "all":
        for i in range(1, 31):
            print(f"\n--- Question {i} ---")
            globals()[f"q{i}"]()
    elif choice.isdigit() and 1 <= int(choice) <= 30:
        globals()[f"q{choice}"]()
    else:
        print("Invalid choice.")Name = "Moses"
Age = 19
Height = "6ft"
Status = "Student"

print("Q1",Name)
print("Q1",Age)
print("Q1",Height)
print("Q1",Status)

a, b = 10, 3
x, y = 4.5, 1.5
print("Q2","Addition:", a + b, x + y)
print("Q2","Subtraction:", a - b, x - y)
print("Q2","Multiplication:", a * b, x * y)
print("Q2","Division:", a / b, x / y)

Name = input("Enter your name: ")
Age = int(input("Enter your age: "))
colour = input("Enter your favourite colour: ")

print("Q3",f"My name is {Name}, I am {Age} years old and my favourite colour is {colour}.")

num = 10
num2 = 20.29
name = "Ada"
Value = True

print("Q4",num, type(num), num2, type(num2), (name, type(name), (Value, type(Value))))

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Q5","Sum:", a + b)
print("Q5","Product:", a * b)
print("Q5","Difference:", a - b)

name = "Chidi"
s1, s2, s3, s4, s5 = 70, 65, 80, 55, 90
status = "Passed"
total = s1 + s2 + s3 + s4 + s5
average = total / 5
print("Q6","Name:", name)
print("Q6","Scores:", s1, s2, s3, s4, s5)
print("Q6","Status:", status)
print("Q6","Total:", total)
print("Q6","Average:", average)

fruits = ["apple", "banana", "mango", "orange", "pear", "grape", "pineapple", "guava", "lemon", "papaya"]
print("Q7","First:", fruits[0])
print("Q7","Last:", fruits[-1])
print("Q7","Total items:", len(fruits))

students = ["Ade", "Bola", "Chidi", "Dayo", "Emeka"]
students.append(input("Enter another student's name: "))
print("Q8","Updated list:", students)

Number =[1,2,3,4,5,6,7,8,9,10]
print("Q9","Even numbers:", [n for n in Number if n % 2 == 0])

nums = [15, 8, 25, 40, 12, 30, 5, 18]
largest = nums[0]
smallest = nums[0]
total = 0
for n in nums:
  if n > largest:
        largest = n
  if n < smallest:
       smallest = n
total += n
print("Q10","Largest:", largest)
print("Q10","Smallest:", smallest)
print("Q10","Sum:", total)

shopping = ["bread", "milk", "eggs", "rice", "sugar"]
for _ in range(2):
shopping.append(input("Add a product: "))
item = input("Enter a product to remove: ")
if item in shopping:
  shopping.remove(item)
else:
print("Product not found.")
print("Q11","Final shopping list:", shopping)


numbers = [5, 12, 18, 23, 7, 30, 41, 9, 15, 2]
n = int(input("Enter a number: "))
if n in numbers:
print(f"{n} exists at position (index) {numbers.index(n)}")
else:
print("Q12", f"{n} is not in the list.")

student = {"name": "Ada", "age": 20, "gender": "Female","department": "Computer Science", "matric_no": "CSC/2024/001"}
for key, value in student.items():
print("Q13", f"{key}: {value}")

products = {"Bread": 800, "Milk": 1200, "Rice": 5000, "Eggs": 2500, "Sugar": 1500}
for name, price in products.items():
print("Q14", f"{name}: {price}")

student = {"name": "Ada", "age": 20, "score": 65}
student["score"] = int(input("Enter the new score: "))
print("Q15", "Updated information:", student)

scores = {"Ade": 67, "Bola": 82, "Chidi": 75, "Dayo": 90, "Emeka": 58}
top_name, top_score = None, -1
for name, score in scores.items():
if score > top_score:
top_name, top_score = name, score
print("Q16", f"Highest score: {top_name} with {top_score}")

account = {"account_name": "Ada Obi", "account_number": "1234567890", "balance": 10000.0}
choice = input("Type 'deposit' or 'withdraw': ").strip().lower()
amount = float(input("Enter amount: "))
if choice == "deposit":
account["balance"] += amount
elif choice == "withdraw":
if amount <= account["balance"]:
account["balance"] -= amount
else:
    print("Insufficient funds.")
else:
    print("Invalid choice.")
print("Q17","Current balance:", account["balance"])

numbers = {10, 20, 30, 10, 40, 20, 50, 30}
print("Q18",numbers)

class_a = {"Ade", "Bola", "Chidi", "Dayo"}
class_b = {"Chidi", "Emeka", "Dayo", "Funke"}
print("Q19","Students in both classes:", class_a & class_b)

a = set(range(1, 11))
b = set(range(5, 16))
print("Q20","All elements:", a | b)
print("Q20","Common elements:", a & b)
print("Q20", "In first but not second:", a - b)

days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
print("Q21","First day:", days[0])
print("Q21","Last day:", days[-1])
print("Q21","Number of days:", len(days))
print("Q21","Saturday exists:", "Saturday" in days)

students = ("Ade", "Bola", "Chidi", "Dayo", "Emeka")
lst = list(students)
lst.append("Funke")
lst.append("Gozie")
lst.remove("Bola")
students = tuple(lst)
print("Q22",students)


with open("students.txt", "w") as f:
   f.write("Name: Ada\nAge: 20\nDepartment: Computer Science\n")
print("Q23","students.txt created.")


names = ["Ade", "Bola", "Chidi", "Dayo", "Emeka"]
with open("students.txt", "w") as f:  # "w" replaces previous content
for n in names:
     f.write(n + "\n")
print("Q24","students.txt overwritten with five names.")


with open("students.txt", "a") as f:  # "a" keeps previous content
for n in ["Funke", "Gozie", "Hauwa"]:
     f.write(n + "\n")
print("Q25","Three names appended.")


try:
with open("students.txt", "r") as f:
   print(f.read())
except FileNotFoundError:
print("Q26","students.txt not found. Run q23 first.")


sentences = ["Today was a good day.", "I learned about Python files.", "I wrote some code.", "I fixed a few bugs.", "Tomorrow I will practise more."]
with open("diary.txt", "w") as f:
for s in sentences:
f.write(s + "\n")
with open("diary.txt", "r") as f:
print("Q27:", f.read())

name = input("Enter your name: ")
language = input("Enter your favourite programming language: ")
with open("profile.txt", "a") as f:
f.write(f"{name} - {language}\n")
print("Q28","Saved to profile.txt.")


if not os.path.exists("numbers.txt"):  # create sample data if missing
with open("numbers.txt", "w") as f:
f.write("10\n20\n30\n40\n")
total = 0
with open("numbers.txt", "r") as f:
for line in f:
line = line.strip()
if line:
total += float(line)
print("Q29","Sum of numbers:", total)

    while True:
        print("\n1. Add student record\n2. View all records\n3. Count records\n4. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            name = input("Name: ")
            age = input("Age: ")
            score = input("Exam score: ")
            with open("records.txt", "a") as f:
                f.write(f"{name},{age},{score}\n")
            print("Record saved.")
        elif choice == "2":
            if os.path.exists("records.txt"):
                with open("records.txt", "r") as f:
                    for line in f:
                        name, age, score = line.strip().split(",")
                        print(f"Name: {name} | Age: {age} | Score: {score}")
            else:
                print("No records yet.")
        elif choice == "3":
            count = 0
            if os.path.exists("records.txt"):
                with open("records.txt", "r") as f:
                    count = sum(1 for line in f if line.strip())
            print("Total records:", count)
        elif choice == "4":
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    choice = input("Enter question number (1-30) or 'all': ").strip().lower()
    if choice == "all":
        for i in range(1, 31):
            print(f"\n--- Question {i} ---")
            globals()[f"q{i}"]()
    elif choice.isdigit() and 1 <= int(choice) <= 30:
        globals()[f"q{choice}"]()
    else:
        print("Invalid choice.")Name = "Moses"
Age = 19
Height = "6ft"
Status = "Student"

print("Q1",Name)
print("Q1",Age)
print("Q1",Height)
print("Q1",Status)

a, b = 10, 3
x, y = 4.5, 1.5
print("Q2","Addition:", a + b, x + y)
print("Q2","Subtraction:", a - b, x - y)
print("Q2","Multiplication:", a * b, x * y)
print("Q2","Division:", a / b, x / y)

Name = input("Enter your name: ")
Age = int(input("Enter your age: "))
colour = input("Enter your favourite colour: ")

print("Q3",f"My name is {Name}, I am {Age} years old and my favourite colour is {colour}.")

num = 10
num2 = 20.29
name = "Ada"
Value = True

print("Q4",num, type(num), num2, type(num2), (name, type(name), (Value, type(Value))))

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Q5","Sum:", a + b)
print("Q5","Product:", a * b)
print("Q5","Difference:", a - b)

name = "Chidi"
s1, s2, s3, s4, s5 = 70, 65, 80, 55, 90
status = "Passed"
total = s1 + s2 + s3 + s4 + s5
average = total / 5
print("Q6","Name:", name)
print("Q6","Scores:", s1, s2, s3, s4, s5)
print("Q6","Status:", status)
print("Q6","Total:", total)
print("Q6","Average:", average)

fruits = ["apple", "banana", "mango", "orange", "pear", "grape", "pineapple", "guava", "lemon", "papaya"]
print("Q7","First:", fruits[0])
print("Q7","Last:", fruits[-1])
print("Q7","Total items:", len(fruits))

students = ["Ade", "Bola", "Chidi", "Dayo", "Emeka"]
students.append(input("Enter another student's name: "))
print("Q8","Updated list:", students)

Number =[1,2,3,4,5,6,7,8,9,10]
print("Q9","Even numbers:", [n for n in Number if n % 2 == 0])

nums = [15, 8, 25, 40, 12, 30, 5, 18]
largest = nums[0]
smallest = nums[0]
total = 0
for n in nums:
  if n > largest:
        largest = n
  if n < smallest:
       smallest = n
total += n
print("Q10","Largest:", largest)
print("Q10","Smallest:", smallest)
print("Q10","Sum:", total)

shopping = ["bread", "milk", "eggs", "rice", "sugar"]
for _ in range(2):
shopping.append(input("Add a product: "))
item = input("Enter a product to remove: ")
if item in shopping:
  shopping.remove(item)
else:
print("Product not found.")
print("Q11","Final shopping list:", shopping)


numbers = [5, 12, 18, 23, 7, 30, 41, 9, 15, 2]
n = int(input("Enter a number: "))
if n in numbers:
print(f"{n} exists at position (index) {numbers.index(n)}")
else:
print("Q12", f"{n} is not in the list.")

student = {"name": "Ada", "age": 20, "gender": "Female","department": "Computer Science", "matric_no": "CSC/2024/001"}
for key, value in student.items():
print("Q13", f"{key}: {value}")

products = {"Bread": 800, "Milk": 1200, "Rice": 5000, "Eggs": 2500, "Sugar": 1500}
for name, price in products.items():
print("Q14", f"{name}: {price}")

student = {"name": "Ada", "age": 20, "score": 65}
student["score"] = int(input("Enter the new score: "))
print("Q15", "Updated information:", student)

scores = {"Ade": 67, "Bola": 82, "Chidi": 75, "Dayo": 90, "Emeka": 58}
top_name, top_score = None, -1
for name, score in scores.items():
if score > top_score:
top_name, top_score = name, score
print("Q16", f"Highest score: {top_name} with {top_score}")

account = {"account_name": "Ada Obi", "account_number": "1234567890", "balance": 10000.0}
choice = input("Type 'deposit' or 'withdraw': ").strip().lower()
amount = float(input("Enter amount: "))
if choice == "deposit":
account["balance"] += amount
elif choice == "withdraw":
if amount <= account["balance"]:
account["balance"] -= amount
else:
    print("Insufficient funds.")
else:
    print("Invalid choice.")
print("Q17","Current balance:", account["balance"])

numbers = {10, 20, 30, 10, 40, 20, 50, 30}
print("Q18",numbers)

class_a = {"Ade", "Bola", "Chidi", "Dayo"}
class_b = {"Chidi", "Emeka", "Dayo", "Funke"}
print("Q19","Students in both classes:", class_a & class_b)

a = set(range(1, 11))
b = set(range(5, 16))
print("Q20","All elements:", a | b)
print("Q20","Common elements:", a & b)
print("Q20", "In first but not second:", a - b)

days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
print("Q21","First day:", days[0])
print("Q21","Last day:", days[-1])
print("Q21","Number of days:", len(days))
print("Q21","Saturday exists:", "Saturday" in days)

students = ("Ade", "Bola", "Chidi", "Dayo", "Emeka")
lst = list(students)
lst.append("Funke")
lst.append("Gozie")
lst.remove("Bola")
students = tuple(lst)
print("Q22",students)


with open("students.txt", "w") as f:
   f.write("Name: Ada\nAge: 20\nDepartment: Computer Science\n")
print("Q23","students.txt created.")


names = ["Ade", "Bola", "Chidi", "Dayo", "Emeka"]
with open("students.txt", "w") as f:  # "w" replaces previous content
for n in names:
     f.write(n + "\n")
print("Q24","students.txt overwritten with five names.")


with open("students.txt", "a") as f:  # "a" keeps previous content
for n in ["Funke", "Gozie", "Hauwa"]:
     f.write(n + "\n")
print("Q25","Three names appended.")


try:
with open("students.txt", "r") as f:
   print(f.read())
except FileNotFoundError:
print("Q26","students.txt not found. Run q23 first.")


sentences = ["Today was a good day.", "I learned about Python files.", "I wrote some code.", "I fixed a few bugs.", "Tomorrow I will practise more."]
with open("diary.txt", "w") as f:
for s in sentences:
f.write(s + "\n")
with open("diary.txt", "r") as f:
print("Q27:", f.read())

name = input("Enter your name: ")
language = input("Enter your favourite programming language: ")
with open("profile.txt", "a") as f:
f.write(f"{name} - {language}\n")
print("Q28","Saved to profile.txt.")


if not os.path.exists("numbers.txt"):  # create sample data if missing
with open("numbers.txt", "w") as f:
f.write("10\n20\n30\n40\n")
total = 0
with open("numbers.txt", "r") as f:
for line in f:
line = line.strip()
if line:
total += float(line)
print("Q29","Sum of numbers:", total)

    while True:
        print("\n1. Add student record\n2. View all records\n3. Count records\n4. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            name = input("Name: ")
            age = input("Age: ")
            score = input("Exam score: ")
            with open("records.txt", "a") as f:
                f.write(f"{name},{age},{score}\n")
            print("Record saved.")
        elif choice == "2":
            if os.path.exists("records.txt"):
                with open("records.txt", "r") as f:
                    for line in f:
                        name, age, score = line.strip().split(",")
                        print(f"Name: {name} | Age: {age} | Score: {score}")
            else:
                print("No records yet.")
        elif choice == "3":
            count = 0
            if os.path.exists("records.txt"):
                with open("records.txt", "r") as f:
                    count = sum(1 for line in f if line.strip())
            print("Total records:", count)
        elif choice == "4":
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    choice = input("Enter question number (1-30) or 'all': ").strip().lower()
    if choice == "all":
        for i in range(1, 31):
            print(f"\n--- Question {i} ---")
            globals()[f"q{i}"]()
    elif choice.isdigit() and 1 <= int(choice) <= 30:
        globals()[f"q{choice}"]()
    else:
        print("Invalid choice.")Name = "Moses"
Age = 19
Height = "6ft"
Status = "Student"

print("Q1",Name)
print("Q1",Age)
print("Q1",Height)
print("Q1",Status)

a, b = 10, 3
x, y = 4.5, 1.5
print("Q2","Addition:", a + b, x + y)
print("Q2","Subtraction:", a - b, x - y)
print("Q2","Multiplication:", a * b, x * y)
print("Q2","Division:", a / b, x / y)

Name = input("Enter your name: ")
Age = int(input("Enter your age: "))
colour = input("Enter your favourite colour: ")

print("Q3",f"My name is {Name}, I am {Age} years old and my favourite colour is {colour}.")

num = 10
num2 = 20.29
name = "Ada"
Value = True

print("Q4",num, type(num), num2, type(num2), (name, type(name), (Value, type(Value))))

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Q5","Sum:", a + b)
print("Q5","Product:", a * b)
print("Q5","Difference:", a - b)

name = "Chidi"
s1, s2, s3, s4, s5 = 70, 65, 80, 55, 90
status = "Passed"
total = s1 + s2 + s3 + s4 + s5
average = total / 5
print("Q6","Name:", name)
print("Q6","Scores:", s1, s2, s3, s4, s5)
print("Q6","Status:", status)
print("Q6","Total:", total)
print("Q6","Average:", average)

fruits = ["apple", "banana", "mango", "orange", "pear", "grape", "pineapple", "guava", "lemon", "papaya"]
print("Q7","First:", fruits[0])
print("Q7","Last:", fruits[-1])
print("Q7","Total items:", len(fruits))

students = ["Ade", "Bola", "Chidi", "Dayo", "Emeka"]
students.append(input("Enter another student's name: "))
print("Q8","Updated list:", students)

Number =[1,2,3,4,5,6,7,8,9,10]
print("Q9","Even numbers:", [n for n in Number if n % 2 == 0])

nums = [15, 8, 25, 40, 12, 30, 5, 18]
largest = nums[0]
smallest = nums[0]
total = 0
for n in nums:
  if n > largest:
        largest = n
  if n < smallest:
       smallest = n
total += n
print("Q10","Largest:", largest)
print("Q10","Smallest:", smallest)
print("Q10","Sum:", total)

shopping = ["bread", "milk", "eggs", "rice", "sugar"]
for _ in range(2):
shopping.append(input("Add a product: "))
item = input("Enter a product to remove: ")
if item in shopping:
  shopping.remove(item)
else:
print("Product not found.")
print("Q11","Final shopping list:", shopping)


numbers = [5, 12, 18, 23, 7, 30, 41, 9, 15, 2]
n = int(input("Enter a number: "))
if n in numbers:
print(f"{n} exists at position (index) {numbers.index(n)}")
else:
print("Q12", f"{n} is not in the list.")

student = {"name": "Ada", "age": 20, "gender": "Female","department": "Computer Science", "matric_no": "CSC/2024/001"}
for key, value in student.items():
print("Q13", f"{key}: {value}")

products = {"Bread": 800, "Milk": 1200, "Rice": 5000, "Eggs": 2500, "Sugar": 1500}
for name, price in products.items():
print("Q14", f"{name}: {price}")

student = {"name": "Ada", "age": 20, "score": 65}
student["score"] = int(input("Enter the new score: "))
print("Q15", "Updated information:", student)

scores = {"Ade": 67, "Bola": 82, "Chidi": 75, "Dayo": 90, "Emeka": 58}
top_name, top_score = None, -1
for name, score in scores.items():
if score > top_score:
top_name, top_score = name, score
print("Q16", f"Highest score: {top_name} with {top_score}")

account = {"account_name": "Ada Obi", "account_number": "1234567890", "balance": 10000.0}
choice = input("Type 'deposit' or 'withdraw': ").strip().lower()
amount = float(input("Enter amount: "))
if choice == "deposit":
account["balance"] += amount
elif choice == "withdraw":
if amount <= account["balance"]:
account["balance"] -= amount
else:
    print("Insufficient funds.")
else:
    print("Invalid choice.")
print("Q17","Current balance:", account["balance"])

numbers = {10, 20, 30, 10, 40, 20, 50, 30}
print("Q18",numbers)

class_a = {"Ade", "Bola", "Chidi", "Dayo"}
class_b = {"Chidi", "Emeka", "Dayo", "Funke"}
print("Q19","Students in both classes:", class_a & class_b)

a = set(range(1, 11))
b = set(range(5, 16))
print("Q20","All elements:", a | b)
print("Q20","Common elements:", a & b)
print("Q20", "In first but not second:", a - b)

days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
print("Q21","First day:", days[0])
print("Q21","Last day:", days[-1])
print("Q21","Number of days:", len(days))
print("Q21","Saturday exists:", "Saturday" in days)

students = ("Ade", "Bola", "Chidi", "Dayo", "Emeka")
lst = list(students)
lst.append("Funke")
lst.append("Gozie")
lst.remove("Bola")
students = tuple(lst)
print("Q22",students)


with open("students.txt", "w") as f:
   f.write("Name: Ada\nAge: 20\nDepartment: Computer Science\n")
print("Q23","students.txt created.")


names = ["Ade", "Bola", "Chidi", "Dayo", "Emeka"]
with open("students.txt", "w") as f:  # "w" replaces previous content
for n in names:
     f.write(n + "\n")
print("Q24","students.txt overwritten with five names.")


with open("students.txt", "a") as f:  # "a" keeps previous content
for n in ["Funke", "Gozie", "Hauwa"]:
     f.write(n + "\n")
print("Q25","Three names appended.")


try:
with open("students.txt", "r") as f:
   print(f.read())
except FileNotFoundError:
print("Q26","students.txt not found. Run q23 first.")


sentences = ["Today was a good day.", "I learned about Python files.", "I wrote some code.", "I fixed a few bugs.", "Tomorrow I will practise more."]
with open("diary.txt", "w") as f:
for s in sentences:
f.write(s + "\n")
with open("diary.txt", "r") as f:
print("Q27:", f.read())

name = input("Enter your name: ")
language = input("Enter your favourite programming language: ")
with open("profile.txt", "a") as f:
f.write(f"{name} - {language}\n")
print("Q28","Saved to profile.txt.")


if not os.path.exists("numbers.txt"):  # create sample data if missing
with open("numbers.txt", "w") as f:
f.write("10\n20\n30\n40\n")
total = 0
with open("numbers.txt", "r") as f:
for line in f:
line = line.strip()
if line:
total += float(line)
print("Q29","Sum of numbers:", total)

    while True:
        print("\n1. Add student record\n2. View all records\n3. Count records\n4. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            name = input("Name: ")
            age = input("Age: ")
            score = input("Exam score: ")
            with open("records.txt", "a") as f:
                f.write(f"{name},{age},{score}\n")
            print("Record saved.")
        elif choice == "2":
            if os.path.exists("records.txt"):
                with open("records.txt", "r") as f:
                    for line in f:
                        name, age, score = line.strip().split(",")
                        print(f"Name: {name} | Age: {age} | Score: {score}")
            else:
                print("No records yet.")
        elif choice == "3":
            count = 0
            if os.path.exists("records.txt"):
                with open("records.txt", "r") as f:
                    count = sum(1 for line in f if line.strip())
            print("Total records:", count)
        elif choice == "4":
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    choice = input("Enter question number (1-30) or 'all': ").strip().lower()
    if choice == "all":
        for i in range(1, 31):
            print(f"\n--- Question {i} ---")
            globals()[f"q{i}"]()
    elif choice.isdigit() and 1 <= int(choice) <= 30:
        globals()[f"q{choice}"]()
    else:
        print("Invalid choice.")Name = "Moses"
Age = 19
Height = "6ft"
Status = "Student"

print("Q1",Name)
print("Q1",Age)
print("Q1",Height)
print("Q1",Status)

a, b = 10, 3
x, y = 4.5, 1.5
print("Q2","Addition:", a + b, x + y)
print("Q2","Subtraction:", a - b, x - y)
print("Q2","Multiplication:", a * b, x * y)
print("Q2","Division:", a / b, x / y)

Name = input("Enter your name: ")
Age = int(input("Enter your age: "))
colour = input("Enter your favourite colour: ")

print("Q3",f"My name is {Name}, I am {Age} years old and my favourite colour is {colour}.")

num = 10
num2 = 20.29
name = "Ada"
Value = True

print("Q4",num, type(num), num2, type(num2), (name, type(name), (Value, type(Value))))

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Q5","Sum:", a + b)
print("Q5","Product:", a * b)
print("Q5","Difference:", a - b)

name = "Chidi"
s1, s2, s3, s4, s5 = 70, 65, 80, 55, 90
status = "Passed"
total = s1 + s2 + s3 + s4 + s5
average = total / 5
print("Q6","Name:", name)
print("Q6","Scores:", s1, s2, s3, s4, s5)
print("Q6","Status:", status)
print("Q6","Total:", total)
print("Q6","Average:", average)

fruits = ["apple", "banana", "mango", "orange", "pear", "grape", "pineapple", "guava", "lemon", "papaya"]
print("Q7","First:", fruits[0])
print("Q7","Last:", fruits[-1])
print("Q7","Total items:", len(fruits))

students = ["Ade", "Bola", "Chidi", "Dayo", "Emeka"]
students.append(input("Enter another student's name: "))
print("Q8","Updated list:", students)

Number =[1,2,3,4,5,6,7,8,9,10]
print("Q9","Even numbers:", [n for n in Number if n % 2 == 0])

nums = [15, 8, 25, 40, 12, 30, 5, 18]
largest = nums[0]
smallest = nums[0]
total = 0
for n in nums:
  if n > largest:
        largest = n
  if n < smallest:
       smallest = n
total += n
print("Q10","Largest:", largest)
print("Q10","Smallest:", smallest)
print("Q10","Sum:", total)

shopping = ["bread", "milk", "eggs", "rice", "sugar"]
for _ in range(2):
shopping.append(input("Add a product: "))
item = input("Enter a product to remove: ")
if item in shopping:
  shopping.remove(item)
else:
print("Product not found.")
print("Q11","Final shopping list:", shopping)


numbers = [5, 12, 18, 23, 7, 30, 41, 9, 15, 2]
n = int(input("Enter a number: "))
if n in numbers:
print(f"{n} exists at position (index) {numbers.index(n)}")
else:
print("Q12", f"{n} is not in the list.")

student = {"name": "Ada", "age": 20, "gender": "Female","department": "Computer Science", "matric_no": "CSC/2024/001"}
for key, value in student.items():
print("Q13", f"{key}: {value}")

products = {"Bread": 800, "Milk": 1200, "Rice": 5000, "Eggs": 2500, "Sugar": 1500}
for name, price in products.items():
print("Q14", f"{name}: {price}")

student = {"name": "Ada", "age": 20, "score": 65}
student["score"] = int(input("Enter the new score: "))
print("Q15", "Updated information:", student)

scores = {"Ade": 67, "Bola": 82, "Chidi": 75, "Dayo": 90, "Emeka": 58}
top_name, top_score = None, -1
for name, score in scores.items():
if score > top_score:
top_name, top_score = name, score
print("Q16", f"Highest score: {top_name} with {top_score}")

account = {"account_name": "Ada Obi", "account_number": "1234567890", "balance": 10000.0}
choice = input("Type 'deposit' or 'withdraw': ").strip().lower()
amount = float(input("Enter amount: "))
if choice == "deposit":
account["balance"] += amount
elif choice == "withdraw":
if amount <= account["balance"]:
account["balance"] -= amount
else:
    print("Insufficient funds.")
else:
    print("Invalid choice.")
print("Q17","Current balance:", account["balance"])

numbers = {10, 20, 30, 10, 40, 20, 50, 30}
print("Q18",numbers)

class_a = {"Ade", "Bola", "Chidi", "Dayo"}
class_b = {"Chidi", "Emeka", "Dayo", "Funke"}
print("Q19","Students in both classes:", class_a & class_b)

a = set(range(1, 11))
b = set(range(5, 16))
print("Q20","All elements:", a | b)
print("Q20","Common elements:", a & b)
print("Q20", "In first but not second:", a - b)

days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
print("Q21","First day:", days[0])
print("Q21","Last day:", days[-1])
print("Q21","Number of days:", len(days))
print("Q21","Saturday exists:", "Saturday" in days)

students = ("Ade", "Bola", "Chidi", "Dayo", "Emeka")
lst = list(students)
lst.append("Funke")
lst.append("Gozie")
lst.remove("Bola")
students = tuple(lst)
print("Q22",students)


with open("students.txt", "w") as f:
   f.write("Name: Ada\nAge: 20\nDepartment: Computer Science\n")
print("Q23","students.txt created.")


names = ["Ade", "Bola", "Chidi", "Dayo", "Emeka"]
with open("students.txt", "w") as f:  # "w" replaces previous content
for n in names:
     f.write(n + "\n")
print("Q24","students.txt overwritten with five names.")


with open("students.txt", "a") as f:  # "a" keeps previous content
for n in ["Funke", "Gozie", "Hauwa"]:
     f.write(n + "\n")
print("Q25","Three names appended.")


try:
with open("students.txt", "r") as f:
   print(f.read())
except FileNotFoundError:
print("Q26","students.txt not found. Run q23 first.")


sentences = ["Today was a good day.", "I learned about Python files.", "I wrote some code.", "I fixed a few bugs.", "Tomorrow I will practise more."]
with open("diary.txt", "w") as f:
for s in sentences:
f.write(s + "\n")
with open("diary.txt", "r") as f:
print("Q27:", f.read())

name = input("Enter your name: ")
language = input("Enter your favourite programming language: ")
with open("profile.txt", "a") as f:
f.write(f"{name} - {language}\n")
print("Q28","Saved to profile.txt.")


if not os.path.exists("numbers.txt"):  # create sample data if missing
with open("numbers.txt", "w") as f:
f.write("10\n20\n30\n40\n")
total = 0
with open("numbers.txt", "r") as f:
for line in f:
line = line.strip()
if line:
total += float(line)
print("Q29","Sum of numbers:", total)

    while True:
        print("\n1. Add student record\n2. View all records\n3. Count records\n4. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            name = input("Name: ")
            age = input("Age: ")
            score = input("Exam score: ")
            with open("records.txt", "a") as f:
                f.write(f"{name},{age},{score}\n")
            print("Record saved.")
        elif choice == "2":
            if os.path.exists("records.txt"):
                with open("records.txt", "r") as f:
                    for line in f:
                        name, age, score = line.strip().split(",")
                        print(f"Name: {name} | Age: {age} | Score: {score}")
            else:
                print("No records yet.")
        elif choice == "3":
            count = 0
            if os.path.exists("records.txt"):
                with open("records.txt", "r") as f:
                    count = sum(1 for line in f if line.strip())
            print("Total records:", count)
        elif choice == "4":
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    choice = input("Enter question number (1-30) or 'all': ").strip().lower()
    if choice == "all":
        for i in range(1, 31):
            print(f"\n--- Question {i} ---")
            globals()[f"q{i}"]()
    elif choice.isdigit() and 1 <= int(choice) <= 30:
        globals()[f"q{choice}"]()
    else:
        print("Invalid choice.")Name = "Moses"
Age = 19
Height = "6ft"
Status = "Student"

print("Q1",Name)
print("Q1",Age)
print("Q1",Height)
print("Q1",Status)

a, b = 10, 3
x, y = 4.5, 1.5
print("Q2","Addition:", a + b, x + y)
print("Q2","Subtraction:", a - b, x - y)
print("Q2","Multiplication:", a * b, x * y)
print("Q2","Division:", a / b, x / y)

Name = input("Enter your name: ")
Age = int(input("Enter your age: "))
colour = input("Enter your favourite colour: ")

print("Q3",f"My name is {Name}, I am {Age} years old and my favourite colour is {colour}.")

num = 10
num2 = 20.29
name = "Ada"
Value = True

print("Q4",num, type(num), num2, type(num2), (name, type(name), (Value, type(Value))))

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Q5","Sum:", a + b)
print("Q5","Product:", a * b)
print("Q5","Difference:", a - b)

name = "Chidi"
s1, s2, s3, s4, s5 = 70, 65, 80, 55, 90
status = "Passed"
total = s1 + s2 + s3 + s4 + s5
average = total / 5
print("Q6","Name:", name)
print("Q6","Scores:", s1, s2, s3, s4, s5)
print("Q6","Status:", status)
print("Q6","Total:", total)
print("Q6","Average:", average)

fruits = ["apple", "banana", "mango", "orange", "pear", "grape", "pineapple", "guava", "lemon", "papaya"]
print("Q7","First:", fruits[0])
print("Q7","Last:", fruits[-1])
print("Q7","Total items:", len(fruits))

students = ["Ade", "Bola", "Chidi", "Dayo", "Emeka"]
students.append(input("Enter another student's name: "))
print("Q8","Updated list:", students)

Number =[1,2,3,4,5,6,7,8,9,10]
print("Q9","Even numbers:", [n for n in Number if n % 2 == 0])

nums = [15, 8, 25, 40, 12, 30, 5, 18]
largest = nums[0]
smallest = nums[0]
total = 0
for n in nums:
  if n > largest:
        largest = n
  if n < smallest:
       smallest = n
total += n
print("Q10","Largest:", largest)
print("Q10","Smallest:", smallest)
print("Q10","Sum:", total)

shopping = ["bread", "milk", "eggs", "rice", "sugar"]
for _ in range(2):
shopping.append(input("Add a product: "))
item = input("Enter a product to remove: ")
if item in shopping:
  shopping.remove(item)
else:
print("Product not found.")
print("Q11","Final shopping list:", shopping)


numbers = [5, 12, 18, 23, 7, 30, 41, 9, 15, 2]
n = int(input("Enter a number: "))
if n in numbers:
print(f"{n} exists at position (index) {numbers.index(n)}")
else:
print("Q12", f"{n} is not in the list.")

student = {"name": "Ada", "age": 20, "gender": "Female","department": "Computer Science", "matric_no": "CSC/2024/001"}
for key, value in student.items():
print("Q13", f"{key}: {value}")

products = {"Bread": 800, "Milk": 1200, "Rice": 5000, "Eggs": 2500, "Sugar": 1500}
for name, price in products.items():
print("Q14", f"{name}: {price}")

student = {"name": "Ada", "age": 20, "score": 65}
student["score"] = int(input("Enter the new score: "))
print("Q15", "Updated information:", student)

scores = {"Ade": 67, "Bola": 82, "Chidi": 75, "Dayo": 90, "Emeka": 58}
top_name, top_score = None, -1
for name, score in scores.items():
if score > top_score:
top_name, top_score = name, score
print("Q16", f"Highest score: {top_name} with {top_score}")

account = {"account_name": "Ada Obi", "account_number": "1234567890", "balance": 10000.0}
choice = input("Type 'deposit' or 'withdraw': ").strip().lower()
amount = float(input("Enter amount: "))
if choice == "deposit":
account["balance"] += amount
elif choice == "withdraw":
if amount <= account["balance"]:
account["balance"] -= amount
else:
    print("Insufficient funds.")
else:
    print("Invalid choice.")
print("Q17","Current balance:", account["balance"])

numbers = {10, 20, 30, 10, 40, 20, 50, 30}
print("Q18",numbers)

class_a = {"Ade", "Bola", "Chidi", "Dayo"}
class_b = {"Chidi", "Emeka", "Dayo", "Funke"}
print("Q19","Students in both classes:", class_a & class_b)

a = set(range(1, 11))
b = set(range(5, 16))
print("Q20","All elements:", a | b)
print("Q20","Common elements:", a & b)
print("Q20", "In first but not second:", a - b)

days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
print("Q21","First day:", days[0])
print("Q21","Last day:", days[-1])
print("Q21","Number of days:", len(days))
print("Q21","Saturday exists:", "Saturday" in days)

students = ("Ade", "Bola", "Chidi", "Dayo", "Emeka")
lst = list(students)
lst.append("Funke")
lst.append("Gozie")
lst.remove("Bola")
students = tuple(lst)
print("Q22",students)


with open("students.txt", "w") as f:
   f.write("Name: Ada\nAge: 20\nDepartment: Computer Science\n")
print("Q23","students.txt created.")


names = ["Ade", "Bola", "Chidi", "Dayo", "Emeka"]
with open("students.txt", "w") as f:  # "w" replaces previous content
for n in names:
     f.write(n + "\n")
print("Q24","students.txt overwritten with five names.")


with open("students.txt", "a") as f:  # "a" keeps previous content
for n in ["Funke", "Gozie", "Hauwa"]:
     f.write(n + "\n")
print("Q25","Three names appended.")


try:
with open("students.txt", "r") as f:
   print(f.read())
except FileNotFoundError:
print("Q26","students.txt not found. Run q23 first.")


sentences = ["Today was a good day.", "I learned about Python files.", "I wrote some code.", "I fixed a few bugs.", "Tomorrow I will practise more."]
with open("diary.txt", "w") as f:
for s in sentences:
f.write(s + "\n")
with open("diary.txt", "r") as f:
print("Q27:", f.read())

name = input("Enter your name: ")
language = input("Enter your favourite programming language: ")
with open("profile.txt", "a") as f:
f.write(f"{name} - {language}\n")
print("Q28","Saved to profile.txt.")


if not os.path.exists("numbers.txt"):  # create sample data if missing
with open("numbers.txt", "w") as f:
f.write("10\n20\n30\n40\n")
total = 0
with open("numbers.txt", "r") as f:
for line in f:
line = line.strip()
if line:
total += float(line)
print("Q29","Sum of numbers:", total)

    while True:
        print("\n1. Add student record\n2. View all records\n3. Count records\n4. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            name = input("Name: ")
            age = input("Age: ")
            score = input("Exam score: ")
            with open("records.txt", "a") as f:
                f.write(f"{name},{age},{score}\n")
            print("Record saved.")
        elif choice == "2":
            if os.path.exists("records.txt"):
                with open("records.txt", "r") as f:
                    for line in f:
                        name, age, score = line.strip().split(",")
                        print(f"Name: {name} | Age: {age} | Score: {score}")
            else:
                print("No records yet.")
        elif choice == "3":
            count = 0
            if os.path.exists("records.txt"):
                with open("records.txt", "r") as f:
                    count = sum(1 for line in f if line.strip())
            print("Total records:", count)
        elif choice == "4":
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    choice = input("Enter question number (1-30) or 'all': ").strip().lower()
    if choice == "all":
        for i in range(1, 31):
            print(f"\n--- Question {i} ---")
            globals()[f"q{i}"]()
    elif choice.isdigit() and 1 <= int(choice) <= 30:
        globals()[f"q{choice}"]()
    else:
        print("Invalid choice.")Name = "Moses"
Age = 19
Height = "6ft"
Status = "Student"

print("Q1",Name)
print("Q1",Age)
print("Q1",Height)
print("Q1",Status)

a, b = 10, 3
x, y = 4.5, 1.5
print("Q2","Addition:", a + b, x + y)
print("Q2","Subtraction:", a - b, x - y)
print("Q2","Multiplication:", a * b, x * y)
print("Q2","Division:", a / b, x / y)

Name = input("Enter your name: ")
Age = int(input("Enter your age: "))
colour = input("Enter your favourite colour: ")

print("Q3",f"My name is {Name}, I am {Age} years old and my favourite colour is {colour}.")

num = 10
num2 = 20.29
name = "Ada"
Value = True

print("Q4",num, type(num), num2, type(num2), (name, type(name), (Value, type(Value))))

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Q5","Sum:", a + b)
print("Q5","Product:", a * b)
print("Q5","Difference:", a - b)

name = "Chidi"
s1, s2, s3, s4, s5 = 70, 65, 80, 55, 90
status = "Passed"
total = s1 + s2 + s3 + s4 + s5
average = total / 5
print("Q6","Name:", name)
print("Q6","Scores:", s1, s2, s3, s4, s5)
print("Q6","Status:", status)
print("Q6","Total:", total)
print("Q6","Average:", average)

fruits = ["apple", "banana", "mango", "orange", "pear", "grape", "pineapple", "guava", "lemon", "papaya"]
print("Q7","First:", fruits[0])
print("Q7","Last:", fruits[-1])
print("Q7","Total items:", len(fruits))

students = ["Ade", "Bola", "Chidi", "Dayo", "Emeka"]
students.append(input("Enter another student's name: "))
print("Q8","Updated list:", students)

Number =[1,2,3,4,5,6,7,8,9,10]
print("Q9","Even numbers:", [n for n in Number if n % 2 == 0])

nums = [15, 8, 25, 40, 12, 30, 5, 18]
largest = nums[0]
smallest = nums[0]
total = 0
for n in nums:
  if n > largest:
        largest = n
  if n < smallest:
       smallest = n
total += n
print("Q10","Largest:", largest)
print("Q10","Smallest:", smallest)
print("Q10","Sum:", total)

shopping = ["bread", "milk", "eggs", "rice", "sugar"]
for _ in range(2):
shopping.append(input("Add a product: "))
item = input("Enter a product to remove: ")
if item in shopping:
  shopping.remove(item)
else:
print("Product not found.")
print("Q11","Final shopping list:", shopping)


numbers = [5, 12, 18, 23, 7, 30, 41, 9, 15, 2]
n = int(input("Enter a number: "))
if n in numbers:
print(f"{n} exists at position (index) {numbers.index(n)}")
else:
print("Q12", f"{n} is not in the list.")

student = {"name": "Ada", "age": 20, "gender": "Female","department": "Computer Science", "matric_no": "CSC/2024/001"}
for key, value in student.items():
print("Q13", f"{key}: {value}")

products = {"Bread": 800, "Milk": 1200, "Rice": 5000, "Eggs": 2500, "Sugar": 1500}
for name, price in products.items():
print("Q14", f"{name}: {price}")

student = {"name": "Ada", "age": 20, "score": 65}
student["score"] = int(input("Enter the new score: "))
print("Q15", "Updated information:", student)

scores = {"Ade": 67, "Bola": 82, "Chidi": 75, "Dayo": 90, "Emeka": 58}
top_name, top_score = None, -1
for name, score in scores.items():
if score > top_score:
top_name, top_score = name, score
print("Q16", f"Highest score: {top_name} with {top_score}")

account = {"account_name": "Ada Obi", "account_number": "1234567890", "balance": 10000.0}
choice = input("Type 'deposit' or 'withdraw': ").strip().lower()
amount = float(input("Enter amount: "))
if choice == "deposit":
account["balance"] += amount
elif choice == "withdraw":
if amount <= account["balance"]:
account["balance"] -= amount
else:
    print("Insufficient funds.")
else:
    print("Invalid choice.")
print("Q17","Current balance:", account["balance"])

numbers = {10, 20, 30, 10, 40, 20, 50, 30}
print("Q18",numbers)

class_a = {"Ade", "Bola", "Chidi", "Dayo"}
class_b = {"Chidi", "Emeka", "Dayo", "Funke"}
print("Q19","Students in both classes:", class_a & class_b)

a = set(range(1, 11))
b = set(range(5, 16))
print("Q20","All elements:", a | b)
print("Q20","Common elements:", a & b)
print("Q20", "In first but not second:", a - b)

days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
print("Q21","First day:", days[0])
print("Q21","Last day:", days[-1])
print("Q21","Number of days:", len(days))
print("Q21","Saturday exists:", "Saturday" in days)

students = ("Ade", "Bola", "Chidi", "Dayo", "Emeka")
lst = list(students)
lst.append("Funke")
lst.append("Gozie")
lst.remove("Bola")
students = tuple(lst)
print("Q22",students)


with open("students.txt", "w") as f:
   f.write("Name: Ada\nAge: 20\nDepartment: Computer Science\n")
print("Q23","students.txt created.")


names = ["Ade", "Bola", "Chidi", "Dayo", "Emeka"]
with open("students.txt", "w") as f:  # "w" replaces previous content
for n in names:
     f.write(n + "\n")
print("Q24","students.txt overwritten with five names.")


with open("students.txt", "a") as f:  # "a" keeps previous content
for n in ["Funke", "Gozie", "Hauwa"]:
     f.write(n + "\n")
print("Q25","Three names appended.")


try:
with open("students.txt", "r") as f:
   print(f.read())
except FileNotFoundError:
print("Q26","students.txt not found. Run q23 first.")


sentences = ["Today was a good day.", "I learned about Python files.", "I wrote some code.", "I fixed a few bugs.", "Tomorrow I will practise more."]
with open("diary.txt", "w") as f:
for s in sentences:
f.write(s + "\n")
with open("diary.txt", "r") as f:
print("Q27:", f.read())

name = input("Enter your name: ")
language = input("Enter your favourite programming language: ")
with open("profile.txt", "a") as f:
f.write(f"{name} - {language}\n")
print("Q28","Saved to profile.txt.")


if not os.path.exists("numbers.txt"):  # create sample data if missing
with open("numbers.txt", "w") as f:
f.write("10\n20\n30\n40\n")
total = 0
with open("numbers.txt", "r") as f:
for line in f:
line = line.strip()
if line:
total += float(line)
print("Q29","Sum of numbers:", total)

    while True:
        print("\n1. Add student record\n2. View all records\n3. Count records\n4. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            name = input("Name: ")
            age = input("Age: ")
            score = input("Exam score: ")
            with open("records.txt", "a") as f:
                f.write(f"{name},{age},{score}\n")
            print("Record saved.")
        elif choice == "2":
            if os.path.exists("records.txt"):
                with open("records.txt", "r") as f:
                    for line in f:
                        name, age, score = line.strip().split(",")
                        print(f"Name: {name} | Age: {age} | Score: {score}")
            else:
                print("No records yet.")
        elif choice == "3":
            count = 0
            if os.path.exists("records.txt"):
                with open("records.txt", "r") as f:
                    count = sum(1 for line in f if line.strip())
            print("Total records:", count)
        elif choice == "4":
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    choice = input("Enter question number (1-30) or 'all': ").strip().lower()
    if choice == "all":
        for i in range(1, 31):
            print(f"\n--- Question {i} ---")
            globals()[f"q{i}"]()
    elif choice.isdigit() and 1 <= int(choice) <= 30:
        globals()[f"q{choice}"]()
    else:
        print("Invalid choice.")Name = "Moses"
Age = 19
Height = "6ft"
Status = "Student"

print("Q1",Name)
print("Q1",Age)
print("Q1",Height)
print("Q1",Status)

a, b = 10, 3
x, y = 4.5, 1.5
print("Q2","Addition:", a + b, x + y)
print("Q2","Subtraction:", a - b, x - y)
print("Q2","Multiplication:", a * b, x * y)
print("Q2","Division:", a / b, x / y)

Name = input("Enter your name: ")
Age = int(input("Enter your age: "))
colour = input("Enter your favourite colour: ")

print("Q3",f"My name is {Name}, I am {Age} years old and my favourite colour is {colour}.")

num = 10
num2 = 20.29
name = "Ada"
Value = True

print("Q4",num, type(num), num2, type(num2), (name, type(name), (Value, type(Value))))

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Q5","Sum:", a + b)
print("Q5","Product:", a * b)
print("Q5","Difference:", a - b)

name = "Chidi"
s1, s2, s3, s4, s5 = 70, 65, 80, 55, 90
status = "Passed"
total = s1 + s2 + s3 + s4 + s5
average = total / 5
print("Q6","Name:", name)
print("Q6","Scores:", s1, s2, s3, s4, s5)
print("Q6","Status:", status)
print("Q6","Total:", total)
print("Q6","Average:", average)

fruits = ["apple", "banana", "mango", "orange", "pear", "grape", "pineapple", "guava", "lemon", "papaya"]
print("Q7","First:", fruits[0])
print("Q7","Last:", fruits[-1])
print("Q7","Total items:", len(fruits))

students = ["Ade", "Bola", "Chidi", "Dayo", "Emeka"]
students.append(input("Enter another student's name: "))
print("Q8","Updated list:", students)

Number =[1,2,3,4,5,6,7,8,9,10]
print("Q9","Even numbers:", [n for n in Number if n % 2 == 0])

nums = [15, 8, 25, 40, 12, 30, 5, 18]
largest = nums[0]
smallest = nums[0]
total = 0
for n in nums:
  if n > largest:
        largest = n
  if n < smallest:
       smallest = n
total += n
print("Q10","Largest:", largest)
print("Q10","Smallest:", smallest)
print("Q10","Sum:", total)

shopping = ["bread", "milk", "eggs", "rice", "sugar"]
for _ in range(2):
shopping.append(input("Add a product: "))
item = input("Enter a product to remove: ")
if item in shopping:
  shopping.remove(item)
else:
print("Product not found.")
print("Q11","Final shopping list:", shopping)


numbers = [5, 12, 18, 23, 7, 30, 41, 9, 15, 2]
n = int(input("Enter a number: "))
if n in numbers:
print(f"{n} exists at position (index) {numbers.index(n)}")
else:
print("Q12", f"{n} is not in the list.")

student = {"name": "Ada", "age": 20, "gender": "Female","department": "Computer Science", "matric_no": "CSC/2024/001"}
for key, value in student.items():
print("Q13", f"{key}: {value}")

products = {"Bread": 800, "Milk": 1200, "Rice": 5000, "Eggs": 2500, "Sugar": 1500}
for name, price in products.items():
print("Q14", f"{name}: {price}")

student = {"name": "Ada", "age": 20, "score": 65}
student["score"] = int(input("Enter the new score: "))
print("Q15", "Updated information:", student)

scores = {"Ade": 67, "Bola": 82, "Chidi": 75, "Dayo": 90, "Emeka": 58}
top_name, top_score = None, -1
for name, score in scores.items():
if score > top_score:
top_name, top_score = name, score
print("Q16", f"Highest score: {top_name} with {top_score}")

account = {"account_name": "Ada Obi", "account_number": "1234567890", "balance": 10000.0}
choice = input("Type 'deposit' or 'withdraw': ").strip().lower()
amount = float(input("Enter amount: "))
if choice == "deposit":
account["balance"] += amount
elif choice == "withdraw":
if amount <= account["balance"]:
account["balance"] -= amount
else:
    print("Insufficient funds.")
else:
    print("Invalid choice.")
print("Q17","Current balance:", account["balance"])

numbers = {10, 20, 30, 10, 40, 20, 50, 30}
print("Q18",numbers)

class_a = {"Ade", "Bola", "Chidi", "Dayo"}
class_b = {"Chidi", "Emeka", "Dayo", "Funke"}
print("Q19","Students in both classes:", class_a & class_b)

a = set(range(1, 11))
b = set(range(5, 16))
print("Q20","All elements:", a | b)
print("Q20","Common elements:", a & b)
print("Q20", "In first but not second:", a - b)

days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
print("Q21","First day:", days[0])
print("Q21","Last day:", days[-1])
print("Q21","Number of days:", len(days))
print("Q21","Saturday exists:", "Saturday" in days)

students = ("Ade", "Bola", "Chidi", "Dayo", "Emeka")
lst = list(students)
lst.append("Funke")
lst.append("Gozie")
lst.remove("Bola")
students = tuple(lst)
print("Q22",students)


with open("students.txt", "w") as f:
   f.write("Name: Ada\nAge: 20\nDepartment: Computer Science\n")
print("Q23","students.txt created.")


names = ["Ade", "Bola", "Chidi", "Dayo", "Emeka"]
with open("students.txt", "w") as f:  # "w" replaces previous content
for n in names:
     f.write(n + "\n")
print("Q24","students.txt overwritten with five names.")


with open("students.txt", "a") as f:  # "a" keeps previous content
for n in ["Funke", "Gozie", "Hauwa"]:
     f.write(n + "\n")
print("Q25","Three names appended.")


try:
with open("students.txt", "r") as f:
   print(f.read())
except FileNotFoundError:
print("Q26","students.txt not found. Run q23 first.")


sentences = ["Today was a good day.", "I learned about Python files.", "I wrote some code.", "I fixed a few bugs.", "Tomorrow I will practise more."]
with open("diary.txt", "w") as f:
for s in sentences:
f.write(s + "\n")
with open("diary.txt", "r") as f:
print("Q27:", f.read())

name = input("Enter your name: ")
language = input("Enter your favourite programming language: ")
with open("profile.txt", "a") as f:
f.write(f"{name} - {language}\n")
print("Q28","Saved to profile.txt.")


if not os.path.exists("numbers.txt"):  # create sample data if missing
with open("numbers.txt", "w") as f:
f.write("10\n20\n30\n40\n")
total = 0
with open("numbers.txt", "r") as f:
for line in f:
line = line.strip()
if line:
total += float(line)
print("Q29","Sum of numbers:", total)

    while True:
        print("\n1. Add student record\n2. View all records\n3. Count records\n4. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            name = input("Name: ")
            age = input("Age: ")
            score = input("Exam score: ")
            with open("records.txt", "a") as f:
                f.write(f"{name},{age},{score}\n")
            print("Record saved.")
        elif choice == "2":
            if os.path.exists("records.txt"):
                with open("records.txt", "r") as f:
                    for line in f:
                        name, age, score = line.strip().split(",")
                        print(f"Name: {name} | Age: {age} | Score: {score}")
            else:
                print("No records yet.")
        elif choice == "3":
            count = 0
            if os.path.exists("records.txt"):
                with open("records.txt", "r") as f:
                    count = sum(1 for line in f if line.strip())
            print("Total records:", count)
        elif choice == "4":
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    choice = input("Enter question number (1-30) or 'all': ").strip().lower()
    if choice == "all":
        for i in range(1, 31):
            print(f"\n--- Question {i} ---")
            globals()[f"q{i}"]()
    elif choice.isdigit() and 1 <= int(choice) <= 30:
        globals()[f"q{choice}"]()
    else:
        print("Invalid choice.")Name = "Moses"
Age = 19
Height = "6ft"
Status = "Student"

print("Q1",Name)
print("Q1",Age)
print("Q1",Height)
print("Q1",Status)

a, b = 10, 3
x, y = 4.5, 1.5
print("Q2","Addition:", a + b, x + y)
print("Q2","Subtraction:", a - b, x - y)
print("Q2","Multiplication:", a * b, x * y)
print("Q2","Division:", a / b, x / y)

Name = input("Enter your name: ")
Age = int(input("Enter your age: "))
colour = input("Enter your favourite colour: ")

print("Q3",f"My name is {Name}, I am {Age} years old and my favourite colour is {colour}.")

num = 10
num2 = 20.29
name = "Ada"
Value = True

print("Q4",num, type(num), num2, type(num2), (name, type(name), (Value, type(Value))))

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Q5","Sum:", a + b)
print("Q5","Product:", a * b)
print("Q5","Difference:", a - b)

name = "Chidi"
s1, s2, s3, s4, s5 = 70, 65, 80, 55, 90
status = "Passed"
total = s1 + s2 + s3 + s4 + s5
average = total / 5
print("Q6","Name:", name)
print("Q6","Scores:", s1, s2, s3, s4, s5)
print("Q6","Status:", status)
print("Q6","Total:", total)
print("Q6","Average:", average)

fruits = ["apple", "banana", "mango", "orange", "pear", "grape", "pineapple", "guava", "lemon", "papaya"]
print("Q7","First:", fruits[0])
print("Q7","Last:", fruits[-1])
print("Q7","Total items:", len(fruits))

students = ["Ade", "Bola", "Chidi", "Dayo", "Emeka"]
students.append(input("Enter another student's name: "))
print("Q8","Updated list:", students)

Number =[1,2,3,4,5,6,7,8,9,10]
print("Q9","Even numbers:", [n for n in Number if n % 2 == 0])

nums = [15, 8, 25, 40, 12, 30, 5, 18]
largest = nums[0]
smallest = nums[0]
total = 0
for n in nums:
  if n > largest:
        largest = n
  if n < smallest:
       smallest = n
total += n
print("Q10","Largest:", largest)
print("Q10","Smallest:", smallest)
print("Q10","Sum:", total)

shopping = ["bread", "milk", "eggs", "rice", "sugar"]
for _ in range(2):
shopping.append(input("Add a product: "))
item = input("Enter a product to remove: ")
if item in shopping:
  shopping.remove(item)
else:
print("Product not found.")
print("Q11","Final shopping list:", shopping)


numbers = [5, 12, 18, 23, 7, 30, 41, 9, 15, 2]
n = int(input("Enter a number: "))
if n in numbers:
print(f"{n} exists at position (index) {numbers.index(n)}")
else:
print("Q12", f"{n} is not in the list.")

student = {"name": "Ada", "age": 20, "gender": "Female","department": "Computer Science", "matric_no": "CSC/2024/001"}
for key, value in student.items():
print("Q13", f"{key}: {value}")

products = {"Bread": 800, "Milk": 1200, "Rice": 5000, "Eggs": 2500, "Sugar": 1500}
for name, price in products.items():
print("Q14", f"{name}: {price}")

student = {"name": "Ada", "age": 20, "score": 65}
student["score"] = int(input("Enter the new score: "))
print("Q15", "Updated information:", student)

scores = {"Ade": 67, "Bola": 82, "Chidi": 75, "Dayo": 90, "Emeka": 58}
top_name, top_score = None, -1
for name, score in scores.items():
if score > top_score:
top_name, top_score = name, score
print("Q16", f"Highest score: {top_name} with {top_score}")

account = {"account_name": "Ada Obi", "account_number": "1234567890", "balance": 10000.0}
choice = input("Type 'deposit' or 'withdraw': ").strip().lower()
amount = float(input("Enter amount: "))
if choice == "deposit":
account["balance"] += amount
elif choice == "withdraw":
if amount <= account["balance"]:
account["balance"] -= amount
else:
    print("Insufficient funds.")
else:
    print("Invalid choice.")
print("Q17","Current balance:", account["balance"])

numbers = {10, 20, 30, 10, 40, 20, 50, 30}
print("Q18",numbers)

class_a = {"Ade", "Bola", "Chidi", "Dayo"}
class_b = {"Chidi", "Emeka", "Dayo", "Funke"}
print("Q19","Students in both classes:", class_a & class_b)

a = set(range(1, 11))
b = set(range(5, 16))
print("Q20","All elements:", a | b)
print("Q20","Common elements:", a & b)
print("Q20", "In first but not second:", a - b)

days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
print("Q21","First day:", days[0])
print("Q21","Last day:", days[-1])
print("Q21","Number of days:", len(days))
print("Q21","Saturday exists:", "Saturday" in days)

students = ("Ade", "Bola", "Chidi", "Dayo", "Emeka")
lst = list(students)
lst.append("Funke")
lst.append("Gozie")
lst.remove("Bola")
students = tuple(lst)
print("Q22",students)


with open("students.txt", "w") as f:
   f.write("Name: Ada\nAge: 20\nDepartment: Computer Science\n")
print("Q23","students.txt created.")


names = ["Ade", "Bola", "Chidi", "Dayo", "Emeka"]
with open("students.txt", "w") as f:  # "w" replaces previous content
for n in names:
     f.write(n + "\n")
print("Q24","students.txt overwritten with five names.")


with open("students.txt", "a") as f:  # "a" keeps previous content
for n in ["Funke", "Gozie", "Hauwa"]:
     f.write(n + "\n")
print("Q25","Three names appended.")


try:
with open("students.txt", "r") as f:
   print(f.read())
except FileNotFoundError:
print("Q26","students.txt not found. Run q23 first.")


sentences = ["Today was a good day.", "I learned about Python files.", "I wrote some code.", "I fixed a few bugs.", "Tomorrow I will practise more."]
with open("diary.txt", "w") as f:
for s in sentences:
f.write(s + "\n")
with open("diary.txt", "r") as f:
print("Q27:", f.read())

name = input("Enter your name: ")
language = input("Enter your favourite programming language: ")
with open("profile.txt", "a") as f:
f.write(f"{name} - {language}\n")
print("Q28","Saved to profile.txt.")


if not os.path.exists("numbers.txt"):  # create sample data if missing
with open("numbers.txt", "w") as f:
f.write("10\n20\n30\n40\n")
total = 0
with open("numbers.txt", "r") as f:
for line in f:
line = line.strip()
if line:
total += float(line)
print("Q29","Sum of numbers:", total)

    while True:
        print("\n1. Add student record\n2. View all records\n3. Count records\n4. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            name = input("Name: ")
            age = input("Age: ")
            score = input("Exam score: ")
            with open("records.txt", "a") as f:
                f.write(f"{name},{age},{score}\n")
            print("Record saved.")
        elif choice == "2":
            if os.path.exists("records.txt"):
                with open("records.txt", "r") as f:
                    for line in f:
                        name, age, score = line.strip().split(",")
                        print(f"Name: {name} | Age: {age} | Score: {score}")
            else:
                print("No records yet.")
        elif choice == "3":
            count = 0
            if os.path.exists("records.txt"):
                with open("records.txt", "r") as f:
                    count = sum(1 for line in f if line.strip())
            print("Total records:", count)
        elif choice == "4":
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    choice = input("Enter question number (1-30) or 'all': ").strip().lower()
    if choice == "all":
        for i in range(1, 31):
            print(f"\n--- Question {i} ---")
            globals()[f"q{i}"]()
    elif choice.isdigit() and 1 <= int(choice) <= 30:
        globals()[f"q{choice}"]()
    else:
        print("Invalid choice.")
Age = 19
Height = "6ft"
Status = "Student"

print("Q1",Name)
print("Q1",Age)
print("Q1",Height)
print("Q1",Status)

a, b = 10, 3
x, y = 4.5, 1.5
print("Q2","Addition:", a + b, x + y)
print("Q2","Subtraction:", a - b, x - y)
print("Q2","Multiplication:", a * b, x * y)
print("Q2","Division:", a / b, x / y)

Name = input("Enter your name: ")
Age = int(input("Enter your age: "))
colour = input("Enter your favourite colour: ")

print("Q3",f"My name is {Name}, I am {Age} years old and my favourite colour is {colour}.")

num = 10
num2 = 20.29
name = "Ada"
Value = True

print("Q4",num, type(num), num2, type(num2), (name, type(name), (Value, type(Value))))

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Q5","Sum:", a + b)
print("Q5","Product:", a * b)
print("Q5","Difference:", a - b)

name = "Chidi"
s1, s2, s3, s4, s5 = 70, 65, 80, 55, 90
status = "Passed"
total = s1 + s2 + s3 + s4 + s5
average = total / 5
print("Q6","Name:", name)
print("Q6","Scores:", s1, s2, s3, s4, s5)
print("Q6","Status:", status)
print("Q6","Total:", total)
print("Q6","Average:", average)

fruits = ["apple", "banana", "mango", "orange", "pear", "grape", "pineapple", "guava", "lemon", "papaya"]
print("Q7","First:", fruits[0])
print("Q7","Last:", fruits[-1])
print("Q7","Total items:", len(fruits))

students = ["Ade", "Bola", "Chidi", "Dayo", "Emeka"]
students.append(input("Enter another student's name: "))
print("Q8","Updated list:", students)

Number =[1,2,3,4,5,6,7,8,9,10]
print("Q9","Even numbers:", [n for n in Number if n % 2 == 0])

nums = [15, 8, 25, 40, 12, 30, 5, 18]
largest = nums[0]
smallest = nums[0]
total = 0
for n in nums:
  if n > largest:
        largest = n
  if n < smallest:
       smallest = n
total += n
print("Q10","Largest:", largest)
print("Q10","Smallest:", smallest)
print("Q10","Sum:", total)

shopping = ["bread", "milk", "eggs", "rice", "sugar"]
for _ in range(2):
shopping.append(input("Add a product: "))
item = input("Enter a product to remove: ")
if item in shopping:
  shopping.remove(item)
else:
print("Product not found.")
print("Q11","Final shopping list:", shopping)


numbers = [5, 12, 18, 23, 7, 30, 41, 9, 15, 2]
n = int(input("Enter a number: "))
if n in numbers:
print(f"{n} exists at position (index) {numbers.index(n)}")
else:
print("Q12", f"{n} is not in the list.")

student = {"name": "Ada", "age": 20, "gender": "Female","department": "Computer Science", "matric_no": "CSC/2024/001"}
for key, value in student.items():
print("Q13", f"{key}: {value}")

products = {"Bread": 800, "Milk": 1200, "Rice": 5000, "Eggs": 2500, "Sugar": 1500}
for name, price in products.items():
print("Q14", f"{name}: {price}")

student = {"name": "Ada", "age": 20, "score": 65}
student["score"] = int(input("Enter the new score: "))
print("Q15", "Updated information:", student)

scores = {"Ade": 67, "Bola": 82, "Chidi": 75, "Dayo": 90, "Emeka": 58}
top_name, top_score = None, -1
for name, score in scores.items():
if score > top_score:
top_name, top_score = name, score
print("Q16", f"Highest score: {top_name} with {top_score}")

account = {"account_name": "Ada Obi", "account_number": "1234567890", "balance": 10000.0}
choice = input("Type 'deposit' or 'withdraw': ").strip().lower()
amount = float(input("Enter amount: "))
if choice == "deposit":
account["balance"] += amount
elif choice == "withdraw":
if amount <= account["balance"]:
account["balance"] -= amount
else:
    print("Insufficient funds.")
else:
    print("Invalid choice.")
print("Q17","Current balance:", account["balance"])

numbers = {10, 20, 30, 10, 40, 20, 50, 30}
print("Q18",numbers)

class_a = {"Ade", "Bola", "Chidi", "Dayo"}
class_b = {"Chidi", "Emeka", "Dayo", "Funke"}
print("Q19","Students in both classes:", class_a & class_b)

a = set(range(1, 11))
b = set(range(5, 16))
print("Q20","All elements:", a | b)
print("Q20","Common elements:", a & b)
print("Q20", "In first but not second:", a - b)

days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
print("Q21","First day:", days[0])
print("Q21","Last day:", days[-1])
print("Q21","Number of days:", len(days))
print("Q21","Saturday exists:", "Saturday" in days)

students = ("Ade", "Bola", "Chidi", "Dayo", "Emeka")
lst = list(students)
lst.append("Funke")
lst.append("Gozie")
lst.remove("Bola")
students = tuple(lst)
print("Q22",students)


with open("students.txt", "w") as f:
   f.write("Name: Ada\nAge: 20\nDepartment: Computer Science\n")
print("Q23","students.txt created.")


names = ["Ade", "Bola", "Chidi", "Dayo", "Emeka"]
with open("students.txt", "w") as f:  # "w" replaces previous content
for n in names:
     f.write(n + "\n")
print("Q24","students.txt overwritten with five names.")


with open("students.txt", "a") as f:  # "a" keeps previous content
for n in ["Funke", "Gozie", "Hauwa"]:
     f.write(n + "\n")
print("Q25","Three names appended.")


try:
with open("students.txt", "r") as f:
   print(f.read())
except FileNotFoundError:
print("Q26","students.txt not found. Run q23 first.")


sentences = ["Today was a good day.", "I learned about Python files.", "I wrote some code.", "I fixed a few bugs.", "Tomorrow I will practise more."]
with open("diary.txt", "w") as f:
for s in sentences:
f.write(s + "\n")
with open("diary.txt", "r") as f:
print("Q27:", f.read())

name = input("Enter your name: ")
language = input("Enter your favourite programming language: ")
with open("profile.txt", "a") as f:
f.write(f"{name} - {language}\n")
print("Q28","Saved to profile.txt.")


if not os.path.exists("numbers.txt"):  # create sample data if missing
with open("numbers.txt", "w") as f:
f.write("10\n20\n30\n40\n")
total = 0
with open("numbers.txt", "r") as f:
for line in f:
line = line.strip()
if line:
total += float(line)
print("Q29","Sum of numbers:", total)

    while True:
        print("\n1. Add student record\n2. View all records\n3. Count records\n4. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            name = input("Name: ")
            age = input("Age: ")
            score = input("Exam score: ")
            with open("records.txt", "a") as f:
                f.write(f"{name},{age},{score}\n")
            print("Record saved.")
        elif choice == "2":
            if os.path.exists("records.txt"):
                with open("records.txt", "r") as f:
                    for line in f:
                        name, age, score = line.strip().split(",")
                        print(f"Name: {name} | Age: {age} | Score: {score}")
            else:
                print("No records yet.")
        elif choice == "3":
            count = 0
            if os.path.exists("records.txt"):
                with open("records.txt", "r") as f:
                    count = sum(1 for line in f if line.strip())
            print("Total records:", count)
        elif choice == "4":
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    choice = input("Enter question number (1-30) or 'all': ").strip().lower()
    if choice == "all":
        for i in range(1, 31):
            print(f"\n--- Question {i} ---")
            globals()[f"q{i}"]()
    elif choice.isdigit() and 1 <= int(choice) <= 30:
        globals()[f"q{choice}"]()
    else:
        print("Invalid choice.")