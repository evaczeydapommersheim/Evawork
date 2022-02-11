# This program reads in a student's percentage achieved 
# and prints out the corresponding grade

# Author: Eva czeyda-Pommersheim

percentage = float(input("Enter the percentage: "))

if percentage < 0 or percentage > 100: 
    print("Please enter a number between 0 and 100")
elif percentage < 40:
    print("Fail")
elif percentage < 50:
    print("Pass")
elif percentage < 60:
    print("Merit 2")
elif percentage < 70:
    print("Merit 1")
else: # the only option left is to enter values between 70 and 100
    print("Distinction")