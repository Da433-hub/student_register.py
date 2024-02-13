""" Exam Register program """
student_num = input("Please enter the number of students registering:") # Request the number of students, for the iteration in the for loop in line 4.

with open("reg_form.txt","a+") as f: # Python's built-in open() function makes a text file. # Append mode 'a+' enables editing and reading. # Use with/as for auto-closure of the file.
    for i in range(int(student_num)): # Make a for loop that requests all student's ID numbers. Cast the loop to integers: 'int'.
        iD_num = input("Please enter the next student ID number:")
        f.write(iD_num + "....................\n") # Use the write() method to write the iD_num variable's data to the 'reg_form.txt' file.
