# TASK: LAB # 01
# Name: Muhammad Amas 
# Seat No: B20102077

# Dir and Help

# Try out some of the string functions listed in dir (ignore those with underscores '_' around the method name). 

print(dir(str))
str = "Muhammad Amas Waseem"
str1=str.capitalize()
str2 =str.upper()
str3 =str. lower()
str4= str.count("m")
print(str1)
print(str2)
print(str3)
print(str4)
print (help(str))



# Exercise Python input /output Basic operations

# (i) Write a Python program to swap 4 variables values (input four values)

a = 10
b = 67
c = 38
d = 55
print('before swapping', 'a =', a, ' b =', b, ' c =', c, ' d =', d)
a, b, c, d = d, c, b, a
print('after swapping', 'a =', a, ' b =', b, ' c =', c, ' d =', d)

# (ii) Write a Python program to convert temperatures to and from celsius, Fahrenheit.

print("Temperature Conversion")
print("1. Celsius to Fahrenheit     2. Fahrenheit to Celsius")
choice = int(input("Enter your choice: "))
if choice == 1:
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print("Temperature in Fahrenheit: ", fahrenheit)

elif choice == 2:
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5/9
    print("Temperature in Celsius: ", celsius)

else:
    print("Wrong Input")

# LISTS

# (i)

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list.pop())
print(list.pop(0))
list.append(14)
print(list)
list.reverse()
print(list)



# (ii)Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings.

list = ['abc', 'xyz', 'aba', '1221']
count = 0
for x in list:
    if len(x) >= 2 and x[0] == x[-1]:
        count+=1
print(count)


# Dictionaries

# (i)Use dir and help to learn about the functions you can call on dictionaries and implement it.

dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
dic4 ={}

for d in (dic1, dic2, dic3): dic4.update(d)
print(dic4)



# (ii)Write a Python script to concatenate following dictionaries to create a new one.

dic1={1:10, 2:20}
print(dic1.keys())
print(dic1.values())
print(dic1.items())
dic1.update({3:30, 4:40})
print(dic1)



# List Comprehensions

# (i)Write a list comprehension which, from a list, generates a lowercased version of each string that has length greater than five.

str = ["My", "name", "is", "Muhammad", "Amas", "Waseem"]
print("Lower case string :", [x.lower() for x in str if len(x) > 5])


# (ii)Write a Python program to print a specified list after removing the 0th, 4th and 5th elements

list =  ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow','Teapink']
colors = [x for (i,x) in enumerate(list) if i not in (0, 4, 5)]
print(colors)



# Exercise Create a Python Program that perform following tasks for any problem of your choice:

# Initialize a list to store tasks
tasks = []

# Function to add a task
def add_task(task):
    tasks.append(task)
    print("Task added successfully: " + task)

# Function to view all tasks
def view_tasks():
    print("Tasks:")
    for i, task in enumerate(tasks):
        print(str(i + 1) + ". " + task)

# Function to delete a task
def delete_task(index):
    task = tasks.pop(index - 1)
    print("Task deleted successfully: " + task)

# Main loop to interact with user
while True:
    print("1. Add task")
    print("2. View tasks")
    print("3. Delete task")
    print("4. Exit")
    choice = int(input("Enter your choice: "))

    # Conditional statements to perform actions based on user input
    if choice == 1:
        task = input("Enter the task: ")
        add_task(task)
    elif choice == 2:
        view_tasks()
    elif choice == 3:
        view_tasks()
        index = int(input("Enter the task number to delete: "))
        delete_task(index)
    elif choice == 4:
        break
    else:
        print("Invalid choice")



# Bit wise operator
a = 60
b = 30

# c = a&b
# c = a|b
# c = a^b
# c = ~a
# c = a<<2
# c = a>>2

print("Line #",bin(c))
