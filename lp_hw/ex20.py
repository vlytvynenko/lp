from sys import argv

#With arg taking file from command line
script, input_file = argv

#Function which take 1 argument and opening and printing
def print_all(f):
    print(f.read())

#take argument and making absolut position to file
def rewind(f):
    f.seek(0)

#taking 2 arguments and printing one argument and the second reading each line of file
def print_a_line(line_count, f):
    print(line_count, f.readline())

#Opening file
current_file = open(input_file)

#print text
print("First let's print the whole file:\n")

#run function above
print_all(current_file)

#print line
print("Now let's rewind, kind a like of tape")

#run function
rewind(current_file)

#print text
print("Let's print those lines")

#set first argument and
current_line = 1
print_a_line(current_line, current_file)
#Let's check value of variable
print(current_line)

current_line = current_line + 1
print_a_line(current_line, current_file)
#Let's check value of variable
print(current_line)

current_line = current_line + 1
print_a_line(current_line, current_file)
#Let's check value of variable
print(current_line)
