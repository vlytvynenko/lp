#This on is like your script with argv
def print_two(*args):
    arg1, arg2 = args
    print("arg1: %r, arg2: %r" %(arg1, arg2))

#Ok, tat *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print("arg1: %r, arg2: %r" %(arg1, arg2))

#This just take one argument
def print_one(arg1):
    print("arg1 %r" %(arg1))

#This one take no arguments
def print_non():
    print("I got nothing...")

print_two("Zed", "Shaw")
print_two_again("Zed", "Shaw")
print_one("Victory!")
print_non()
