#Import argv library
from sys import argv

#transfer some variables
script, filename = argv

#Open txt file
txt = open(filename)

#Print file imorted via argv
print("Here is your file %r" % (filename))
print(txt.read())

#Print some text
print("Print the file name again:")
#Request to imput file name stored in argv
file_again = input(">")
#Open and print file again
txt_again = open(file_again)
print(txt_again.read())
