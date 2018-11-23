#Need to pass name while running script, because we importing argv

from sys import argv

script, user_name = argv
prompt= '>'

print("Hi %s, I'am the %s script" % (user_name, script))
print("I'd like to ask few questions.")
print("Do you like me %s ?" % (user_name))
likes = input(prompt)

print("Where do you leave %s ?" % (user_name))
lives = input(prompt)

print("What kind of computer do you have")
computer = input(prompt)

print("""
Alright, so you have said %r about like me.
You live in %r. Not sure where that is.
And you have %r computer. Nice.
""" % (likes, lives, computer))
