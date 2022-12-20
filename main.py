from random import shuffle

# Read filename to gather names of participants
with open('nameList.txt', 'r') as file:
    names = [line.strip() for line in file]

# Shuffle list
shuffle(names)

# Create circle by adding first person as last target
names.append(names[0])

for i in range(0, len(names)-1):
    f = open(names[i]+'.txt', 'w')
    f.write('Hola '+names[i]+', tu amigo secreto es '+names[i+1])
    f.close()
