from sys import argv

script, filename = argv

print "kasujemy pliczek? (ENTER/CTRL+C)"

raw_input("?")

print "no wiec bedzie kasowanko"

cel = open(filename, 'a')


print "zbudujemy nowy plik, podaj 3 linie"

linia1 = raw_input(">")
linia2 = raw_input(">")
linia3 = raw_input(">")

print "zapisywanko .................."

cel.write(linia1)
cel.write("\n")
cel.write(linia2)
cel.write("\n")
cel.write(linia3)
cel.write("\n")

print "mozesz sprawdzic pliczek o nazwie %r" % filename
