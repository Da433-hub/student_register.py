# age variable user input created
age = int(input("Please enter your age:  "))

# if-elif-else age data established with messages added
if age < 13:
	message = "You qualify for the kiddie discount."
elif age > 100:
	message = "Sorry, you're dead."	
elif age >= 65:
	message = "Enjoy your retirement!"		
elif age > 40:
	message = "You're over the hill."
elif age == 21:
	message = "Congrats on your 21st!"
else:
	message = "Age is but a number."

# instruction to print corresponding message following user input
print(message)
