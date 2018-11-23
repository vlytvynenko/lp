from sys import argv
from os.path import exists

script, from_file, to_file = argv

print("Copying from %s to %s" % (from_file, to_file))

#We could do these two on one line too, how?
in_file = open(from_file)
indata = in_file.read()

print("The input file %d bytes long" % len(indata))

print("Does the out put file exist? %r" % exists(to_file))
print("Ready, hit return to continue or CTRL-C to abort.")
input()

out_file = open(to_file, 'w')
out_file.write(indata)

print("All done")

out_file.close()
in_file.close()
