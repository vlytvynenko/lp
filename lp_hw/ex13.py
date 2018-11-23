#Need to pass arguments while running script
#python3 ex13.py arg1 arg2 arg3


from sys import argv

script, first, second, third = argv

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)
