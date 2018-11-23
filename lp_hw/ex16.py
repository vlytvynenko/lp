#importing sys function
from sys import argv

#Importing arguments to our script
script, filename = argv

#print few simple line with a text
print("We are going to erase %r." % (filename))
print("If you do not want that, hit CTRL-C.")
print("If you do want that, hit return.")

#Adding imput to script with a text
input("?")
#Print a text
print("Opening the file...")
#Using method open, opening file with premissions to "w" - write
target = open(filename, 'w')
#Printing simple line with a text
print("Trancating the fila, Goodbye")
#Removing all from file using method truncate
target.truncate()
#simple print
print("Now i'm going to ask you for 3 lines.")

#Creating 3 variables and using input requesting to add text
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

#print a text
print("I'm going to write this to the file.")

#Using method write adding previously captured by input text to our file
target.write(line1)
target.write("/n")
target.write(line2)
target.write("/n")
target.write(line3)
target.write("/n")

#print a text
print("And finaly we closing it.")

#Cliosing file
target.close()
