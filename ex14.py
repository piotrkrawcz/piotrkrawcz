from sys import argv

script, user_name, wiek = argv
prompt = '\n>>?>> '

print "Hi %s. I'm the %s script" % (user_name, script)
print "My questions are:"

print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "where do you live %s" % user_name
lives = raw_input(prompt)

print "what kind of computer do you have?"
computer = raw_input(prompt)

print """
Alrigght you said %r about liking me. As you have %r so lick yourself
You live in %r. Not siur where it is.
And you have a %r computer. Nice.
""" % (likes, wiek, lives, computer)
