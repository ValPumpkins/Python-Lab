class Player:
	def __init__(self, age, name, dog, colors):
		self.age = age
		self.name = name
		self.dog = dog
		self.colors = colors

players = [
	Player(23, "John", "Pug", "Black"),
	Player(24, "Jane", "Pug", "Brown"),
	Player(30, "Bob", "Pug", "Brown"),
	Player(31, "Sally", "Pug", "Black"),
	Player(31, "Sally", "Pug", "Brown"),
	Player(32, "Jim", "Pug", "Black"),
	Player(32, "Jim", "Pug", "Brown"),
	Player(33, "Sue", "Pug", "Black")
]

for player in players:
	print(f"Le joueur {player.name} a {player.age} ans, un chien de race {player.dog} et ses couleurs sont {player.colors}")
