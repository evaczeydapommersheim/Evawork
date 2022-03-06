# Automate the Boring stuff Cahpter 3 pg72
# Author: Eva Czeyda-Pommersheim

def spam(divideBy):
    try: 
        return 42 / divideBy
    except ZeroDivisionError:
        print('Error: Invalid argument.')

print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))