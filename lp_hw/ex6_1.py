#Variable
types_of_people = 10
#variable with a variable inside
x = "There are {} types of peopel.".format(types_of_people)

#text variables
binary = "binary"
do_not = "don't"

#Variable with variables inside
y = "Those who know {} and those who {}.".format(binary, do_not)

#print 2 variables
print(x)
print(y)

#print 2 variables with a text (string inside string)
print("I said: {}".format(x))
print("I also said: {}".format(y))

#Variable
hilarious = False
#Variable with a text and one variable inside
joke_evalution = "Isn't this joke so funny?! {}"

#print 2 variables (string inside string)
print(joke_evalution.format(hilarious))

#text variables
w = "This is the left side of ..."
e = "a string with a right side."

#print 2 variables (string inside string)
print(w + e)
