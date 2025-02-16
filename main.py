# This is printing some sentences.
from warnings import catch_warnings

print("I like orange!")
print("It's really good!")

# Variable = A
# Strings
first_name = "Bro"
fruit = "orange"
email = "2cevening@gmail.com"

# Integers
age = 25
quantity = 3
num_of_students = 30

# Float
price = 10.99
gpa = 3.2
distance = 5.5

# Boolean
is_student = True
is_adult = False
for_sale = True
is_online = True

print(first_name)
print("first_name2")
print(f"Hello {first_name}")
print(f"I like {fruit}")
print(f"My email is {email}")

print(f"My age is {age}")
print(f"There is {quantity} students studying in classroom")
print(f"Actually we have {num_of_students} in our classroom")

print(f"The price is ${price}")
print(f"Your gpa is :{gpa}")
print(f"You ran {distance} kilometres")

print(f"Are you a student?:{is_student}")
print(f"Are you a adult?:{is_adult}")

if is_student:
    print("You are a student")
else:
    print("You are NOT a student")

if for_sale:
    print("That item is for sale")
else:
    print("That item is NOT available")

if is_online:
    print("You are online")
else:
    print("You are offline")

# Typecasting = the process of converting a variable from one data type to another
# str(), int(), float(), bool()
name = "Churchill0z"
name1 = ""
age = 25
gpa = 59.89
is_student = False
age1 = "25"

print(type(name))
print(type(age))
print(type(gpa))
print(type(is_student))

gpa = int(gpa)
print(gpa)
age = float(age)
print(age)
age = str(age)
print(age)
print(type(age))

#age1 += 1 It can't work
age1 += "1"
print(age1)

name = bool(name)
name1 = bool(name1)
print(name)
print(name1)

# input() = A function that prompts the user to enter data
# Returns the entered data as a string

input_name = input("What's your name?: ")
input_age = input("How old are you:? ")
is_not_number = True
while is_not_number:
    try:
        input_age = int(input_age)
        is_not_number = False
    except:
        print("You only can input number for your age!")
        input_age = input("Please input your age again:? ")
        is_not_number = True

input_age = input_age + 1

print(f"hello {input_name}")
print("Happy birthday!")
print(f"You are {input_age} years old")

# num locks on and hold alt + 0178
print(f"I'm gonna type superscript²²")

## 32.48 minutes  https://www.youtube.com/watch?v=ix9cRaBkVe0&ab_channel=BroCode