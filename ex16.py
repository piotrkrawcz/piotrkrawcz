from sys import argv

script, filename = argv

print "we are going to erase %r." % filename
print "if you don't want that hit CTRL+C (^C)."
print "if you do want that hit RETURN"

raw_input("?")

print "opening the file..."
target = open(filename, 'w')

print "Truncating the file. Goodbye!"
target.truncate()

print "now i'm going to ask you for three lines"

line1 = raw_input("line1: ")
line2 = raw_input("line2: ")
line3 = raw_input("line3: ")

print "i'm going to write this into a file"

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "finally , we close it"
target.close()
