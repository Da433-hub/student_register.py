# user inputs for time taken, in minutes, to complete each triathlon event
swimming = int(input("Please enter your finish time in minutes for SWIMMING: ")) 
print (swimming)
cycling = int(input("Please enter your finish time in minutes for CYCLING: "))
print (cycling)
running = int(input("Please enter your finish time in minutes for RUNNING: "))
print (running)

# Use the arithmetic operator to calculate the user's total minutes.
total_minutes = ((swimming) + (cycling) + (running))


""" Use 'and' as well as the comparison operators (>=, <=).  Print award statements that correspond to the 'if' statements. """

if (total_minutes <= 100):
    print ("Congratulations - You have been awarded the Provincial Colours !!!")
elif (total_minutes  >= 101) and (total_minutes <= 105):
    print ("Congratulations - You have been awarded the Provincial Half Colours !!")
elif (total_minutes >= 106) and (total_minutes <= 110):
    print ("Congratulations - You have been awarded the Provincial Scroll !")

    # all the elif conditions are false...execute the 'else' statement for >= 111 minutes
else: 
    print("No award")




