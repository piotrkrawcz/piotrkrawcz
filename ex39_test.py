import hashmap

states = hashmap.new()
hashmap.set(states, 'oregon', 'or')
hashmap.set(states, 'florida', 'fl')
hashmap.set(states, 'california', 'ca')
hashmap.set(states, 'new york', 'ny')
hashmap.set(states, 'michigan', 'mi')

cities = hashmap.new()
hashmap.set(cities, 'ca', 'san francisco')
hashmap.set(cities, 'mi', 'detroit')
hashmap.set(cities, 'fl', 'jacksonville')

hashmap.set(cities, 'ny', 'new york')
hashmap.set(cities, 'or', 'portland')

print '-' * 10
print "ny state has: %s" % hashmap.get(cities, 'ny')
print "or state has: %s" % hashmap.get(cities, 'or')

