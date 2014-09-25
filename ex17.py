from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "copying from %s to %s" % (from_file, to_file)

in_file = open(from_file)
indata = in_file.read()

print "your file is %d bytes long" % len(indata)

print "does the output really exists? %r" % exists(to_file)
print "Ready, hit ENTER, else CTRL+C"
raw_input()

out_file = open(to_file, 'w')
out_file.write(indata)

print "all done"

in_file.close()
