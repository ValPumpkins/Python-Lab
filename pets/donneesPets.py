# base_de_donnees.py
import sqlite3

conn = sqlite3.connect('pets.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS animaux
                  (id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name TEXT,
                   race TEXT,
                   parent TEXT)''')

class PetDB:
    def __init__(self, name, race, parent):
        self.name = name
        self.race = race
        self.parent = parent

    def sauvegarder(self):
        cursor.execute("INSERT INTO animaux (name, race, parent) VALUES (?, ?, ?)", (self.name, self.race, self.parent))
        conn.commit()

    @staticmethod
    def lister_animaux():
        cursor.execute("SELECT * FROM animaux")
        result = cursor.fetchall()
        for row in result:
            print(f"{row[1]} ({row[2]}) - Propriétaire : {row[3]}")

if __name__ == "__main__":
    # Exemple d'utilisation de la classe PetDB pour sauvegarder et lister les animaux depuis la base de données
    my_pet = PetDB("Lucky", "chat", "Bob")
    my_pet.sauvegarder()

    PetDB.lister_animaux()

    conn.close()
