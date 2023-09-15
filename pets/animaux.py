class Pet:
	def __init__(self, name, race, parent):
		self.name = name
		self.race = race
		self.parent = parent
		self.hunger = 0

	def manger(self):
		self.hunger -= 1
		print(f"{self.name} a mangé et n'a plus faim.")

def afficher_menu():
	print("1. Ajouter un animal")
	print("2. Afficher les animaux")
	print("3. Donner à manger")
	print("4. Quitter")

animaux = []

while True:
	afficher_menu()
	choix = input("Choississez une option: ")

	if choix == "1":
		name = input("Nom: ")
		race = input("Race: ")
		parent = input("Parent: ")
		animal =  Pet(name, race, parent)
		animaux.append(animal)
		print(f"{animal.name} a été ajouté à la liste d'animaux")
	elif choix == "2":
		print("Liste d'animaux")
		for animal in animaux:
			print(f"{animal.name} est un {animal.race} adopté par {animal.parent}")
	elif choix == "3":
		print("Donner à manger à tous les animaux")
		for animal in animaux:
			animal.manger()
	elif choix == "4":
		print("Au revoir")
		break
	else:
		print("Choix invalide, veuillez réessayer")

