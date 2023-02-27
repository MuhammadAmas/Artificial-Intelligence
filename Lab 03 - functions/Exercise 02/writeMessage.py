# (ii). Write a python program to create a data file student.txt and append the message “Now we are AI students”s

# opening a file
with open("student.txt", "a") as f:
    
    # Writing the message to the file
    f.write("Now we are AI students")
