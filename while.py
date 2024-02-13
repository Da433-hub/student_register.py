# Start with three variables set to zero.
total = 0
count = 0
average = 0
# Add the 'while' loop to repeat the 'enter a number' request from the user.
while True:
    num = input("Please enter a number (-1 to exit) : ")
# Make the 'if' condition to allow the user to get the 'total' and the 'average'.
    if num == ("-1"):
        break
    total += float (num)

    count += 1

average = total / count
# Print the total and the average.
print("Total: " ,  total)
print("The average: " , average)