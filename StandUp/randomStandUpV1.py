#!/usr/bin/python3

import random

C20 = ["Matheo", "Kevin", "Sébastien", "Arthur", "Paul-Henri", "Samira", "Jérôme"]
C21 = ["Cassandra", "Olive", "Christophe", "Lucie", "Mickael", "Valentine"]
C22 = ["Omar", "Yohan", "Sarah", "Ali", "Nathan", "François", "Cassandre", "Omer", "Amandine",
       "Dimitri", "Sayann", "M'Hamed", "Carmen-Leila", "Thomas", "Laurent", "Anne-Charlotte",
       "Laeticia", "Philippe", "Ritch", "Adnan", "Fabio", "Alexis", "Khadija"]

all_students = C20 + C21 + C22

random.shuffle(all_students)

groupe1 = all_students[:len(all_students)//3]
groupe2 = all_students[len(all_students)//3:2*len(all_students)//3]
groupe3 = all_students[2*len(all_students)//3:]

print("Groupe 1 :", groupe1)
print("Groupe 2 :", groupe2)
print("Groupe 3 :", groupe3)
