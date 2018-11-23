#Need to pass arguments while running this script

from sys import argv

dn, first, second, third, something = argv

print("This is script:", dn)
dn = input("Ok? Answer:")

print("I'am:", second)
second = input("And you? Answer:")

print("We are:", third)
third = input("Don't you? Answer:")

print("This is:", something)
something = input("Your idea:")


print(dn, second, third, something)
