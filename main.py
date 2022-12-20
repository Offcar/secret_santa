from random import shuffle

langSelected = 'en'
lang = {
    'en': 'Hello %s, you must give a gift to %s',
    'es': 'Hola %s, debes dar un regalo a %s',
}

# Read filename to gather names of participants
with open('nameList.txt', 'r') as file:
    names = [line.strip() for line in file]

# Shuffle list
shuffle(names)

# Create circle by adding first person as last target
names.append(names[0])

for i in range(0, len(names)-1):
    f = open(names[i]+'.txt', 'w')
    f.write(lang[langSelected] % (names[i], names[i+1]))
    f.close()
