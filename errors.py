# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

print ("Welcome to the error program") # SyntaxError - missing parentheses in the call to 'print'.
print ("\n")# SyntaxError - incorrect indentation of the call to 'print'and missing parentheses.
            
    # Variables declaring the user's age, casting the str to an int, and printing the result
age_Str = 24 # SyntaxError - incorrect indentation.# 9.SyntaxError -I deleted "years old" :there should only be a numberical value in the 'age_str' variable.
age = age_Str # SyntaxError - incorrect indentation.

print("I'm " + str(age) + " years old.") # SyntaxError - incorrect indentation. Logical Error - lack of spacing after "I'm.." and before "..years old". Runtime Error - python couldn't concatenate until 'age' variable had been cast to a string.
 # Variables declaring additional years and printing the total years of age
years_from_now = 3.5 # SyntaxErrors - incorrect indentation and no quotations required. Logical Error - "3" should be "3.5" to represent 3 years and six months.
total_years = age + years_from_now # SyntaxError - incorrect indentation.

print("The total number of years: " + str(total_years))# RuntimeError - concatenation requires casting of the "age" and "years_from_now" variables to strings. # SyntaxError - missing parentheses in the call to 'print'. # Logical Error "answer_years" ought to be "total_years".

# Variable to calculate the total amount of months from the total amount of years and printing the result
total_months = float(age + years_from_now) * 12 # SyntaxError '==' should be '='. Logical Error - total_months = "((age + years_from_now) * 12)", and not "age * 12".
print ("In 3 years and 6 months, I'll be " + str(total_months) + " months old") # SyntaxError - missing parentheses in the call to 'print'.  Runtime Error - the 'total_months' variable required casting to a string for concatenation to be possible.

#HINT, 330 months is the correct answer

