# This program creates a tuple that stores the months of the year, 
# using this tuple it creates another tuple with just the summer months (May, June, July), 
# it prints out the summer months one at a time.

# Author: Eva Czeyda-Pommersheim

months = ("January",        # variable name is multiple to indicate it is a data structure marked with parentheses for tuple
            "February", 
            "March", 
            "April", 
            "May", 
            "June", 
            "July", 
            "August", 
            "September", 
            "October", 
            "November", 
            "December")     # tuple of months
summerMonths = (months[4:7])    #slicing the tuple to only include the required elements "May" being element 4, "June" being element 5 and "July" being element 6, element 7 is not included

for month in summerMonths:      # for is used in order to iterate through the tuple, returning the month one at a time
    print(month)