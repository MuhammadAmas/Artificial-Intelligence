# a = int(input("Enter a number and I'll get its square root: "))

# if (a > 0):
#     print ("The number you entered is greater than 0, so I can calculate it!") 
#     root = a ** (1/2) 
#     print ("The square root of sd is 8f", (a, root)) 
# if (a <= 0): 
#     print("I can't calculate the square root of a negative number!") 
# print ("Thanks for the input!")


# a = int (input()) #the variable is initialized with a value of 0

# if (a == 1): # if the value is 1, we change its value to 0 
#     a = 0
# if (a == 0): # if the value is 0, we change its value to 1
#     a = 1
# if (a>2 or a < 0 ):
#     print ("You have entered number between")
# print (a)

# a=int (input ("Enter a number between 10-20: "))
# if a >= 10 and a <= 20: \
#     print ("The condition has been met.") 
# else:
#     print ("You did it wrong.")

# a=int (input("Enter a number between 10-20 or 30-40: "))

# if (a>=10 and a<=20) or (a>=30 and a<=40):
#     print ("The condition has been met.")
# else:
#     print ("You did it wrong.")

# #counting positive and negative numbers
# pcount=0
# ncount=0
# count=int(input("how many numbers you want? "))
# i=1 #initialization
# while(i<=count): #condition
#     num=int(input("enter number ")) 
#     if (num>=0):
#         pcount+=1
#     else:
#         ncount+=1
#     i+=1 
# print("positive: ",pcount) 
# print("negative: ",ncount)

value='c'
userValue=input("guess a number from a to e ")
while(userValue!=value):
    print("Incorrect")
    userValue-input("guess a number from a to e")
print("welcome user")


# # Lab Exercises
# # Lab 02


# # Exercise 01 (i)
# def calculate_volume(height, width, depth):
#     volume = height * width * depth
#     return volume

# def classify_volume(volume):
#     if volume > 0 and volume <= 10:
#         return "Extra Small"
#     elif volume <= 25:
#         return "Small"
#     elif volume <= 75:
#         return "Medium"
#     elif volume <= 100:
#         return "Large"
#     elif volume <= 250:
#         return "Extra Large"
#     else:
#         return "Extra-Extra Large"

# height = float(input("Enter height in cm: "))
# width = float(input("Enter width in cm: "))
# depth = float(input("Enter depth in cm: "))

# volume = calculate_volume(height, width, depth)
# volume_classification = classify_volume(volume)

# print("The volume is", volume, "cm^3.")
# print("The object is classified as", volume_classification + ".")


# # Exercise 01 (ii)
# def evaluate_worker_efficiency(time_taken):
#     if time_taken >= 2:
#         return "Highly Efficient"
#     elif time_taken >= 3:
#         return "Ordered to Improve Speed"
#     elif time_taken >= 4:
#         return "Given Training to Improve Speed"
#     elif time_taken >= 5:
#         return "Has to Leave the Company"
    

# time_taken = float(input("Enter the time taken by the worker in hours: "))

# worker_efficiency = evaluate_worker_efficiency(time_taken)

# print("The worker's efficiency is", worker_efficiency + ".")


# # Exercise 01 (iii)
# def check_password(password):
#     known_password = 'abc$123'
#     if password.lower() == known_password:
#         return "Welcome!"
#     else: 
#         return "I don't know you."

# username = input("Enter username: ")
# password = input("Enter password: ")
# result = check_password(password)

# print(result)


# # Exercise 02
# # (i)
# n = 3
# while n >= 0:
#     n -= 1
#     print(n)

# # (ii)
# n = 4
# while n > 0:
#     n += 1
#     print(n)


# # 1. Create a loop that counts from 0 to 100
# i=0
# while i<=100:
#     print(i)
#     i+=1

# # 2. Make a multiplication table using a loop
# def print_multiplication_table(table_number):
#     i=1
#     while i<=10:
#         print(table_number, "x", i, "=", table_number*i)
#         i+=1

# table_number = int(input("Enter the table number: "))
# print_multiplication_table(table_number)

# # 3. Output the numbers 1 to 10 backwards using a loop
# i=10
# while i>=1:
#     print(i)
#     i-=1

# # 4. Create a loop that counts all even numbers to 10
# i=0
# while i<=10:
#     if i%2==0:
#         print(i)
#     i+=1

# # 5. Create a loop that sums the numbers from 100 to 200
# i=100
# sum=0
# while i<=200:
#     sum+=i
#     i+=1
# print(sum)


# # (iii)
# clist = ["Canada", "USA", "Mexico"]

# i = 0
# while i < len(clist):
#     print(clist[i])
#     i += 1
