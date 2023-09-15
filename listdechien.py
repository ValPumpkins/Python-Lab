class Pet:
	def __init__(self, name, race, parent):
		self.name = name
		self.race = race
		self.parent = parent

pets = [
	Pet("Lucky", "chat", "Bob"),
	Pet("Tetris", "chien", "Valentine"),
	Pet("Mimi", "chat", "Valentine"),
	Pet("Bowie", "chat", "Mary"),
	Pet("Medor", "chien", "Marcel"),
	Pet("Bella", "chien", "Peter"),
]
for Pet in pets:
	print(f"Le {Pet.race} {Pet.name} fait partie de la famille de {Pet.parent}")

