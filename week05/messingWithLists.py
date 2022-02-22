# messing with lists from lecture
# Author: Eva Czeyda-Pommersheim

# thi will print the list
list = [2, 4, 5, 6,]
print(list)

# this is the way to iterate through the list 
list = [2, 4, 5, 6,]

for x in list:
    print(x) 

# or accumulate the values in a list

list = [2, 4, 5, 6,]
sum = 0
for x in list:
    sum += x    # if want to add the values of the list
    print(sum)


# not advised way of doing it
# for i in range(0,len(list)):
#    print(i)