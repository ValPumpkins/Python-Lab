#!/usr/bin/python3

# ----- Print 3 groupes random  pr StandUp Lille avec les 3 cohortes ----- #
import random

C20 = ["Matheo", "Kevin", "Sébastien",
       "Arthur", "Paul-Henri", "Samira", "Jérôme"]
C21 = ["Cassandra", "Olive", "Christophe", "Lucie", "Mickael", "Valentine"]
C22 = ["Omar", "Yohan", "Sarah", "Ali", "Nathan", "François",
       "Cassandre", "Omer", "Amandine", "Dimitri", "Sayann",
       "M'Hamed", "Carmen-Leila", "Thomas", "Laurent",
       "Anne-Charlotte", "Laeticia", "Philippe", "Ritch",
       "Adnan", "Fabio", "Alexis", "Khadija"]



# ----- Fonction pour afficher les groupes ----- #


def printGroupe(group, number):
    print(f"Groupe {number}")
    for i, (student, cohorte) in enumerate(group, 1):
        print(f"{i}. {student} - {cohorte}")
    print()

# ----- Mise en page ----- #


print()
print("STAND UP LILLE")
print()
printGroupe(groupe1, 1)
printGroupe(groupe2, 2)
printGroupe(groupe3, 3)
