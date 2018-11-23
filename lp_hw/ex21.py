#Taking 2 argument and printing them out, then performin a math operation and retuning them back.
def add(a, b):
    print("ADDING %d + %d" % (a, b))
    return a + b
#Taking 2 argument and printing them out, then performin a math operation and retuning them back.
def subtract(a, b):
    print("SUBTRACTING %d - %d" % (a, b))
    return a - b
#Taking 2 argument and printing them out, then performin a math operation and retuning them back.
def multiply(a, b):
    print("MULTIPLYING %d * %d" % (a, b))
    return a * b
#Taking 2 argument and printing them out, then performin a math operation and retuning them back.
def divide(a, b):
    print("DIVIDING %d * %d" % (a, b))
    return a / b

print("Let's do some math with just function")

#Making the result of function as a variable.
age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

#Printing results
print("Age: %d, Height: %d, Weight: %d, IQ: %d ." % (age, height, weight, iq))

#A puzzel for the extra credit, type it any wayself.
print("Here is a puzzle.")

#Calling function inside function inside function.
what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print("That becomest:", what,"Can you do it by hand?")
