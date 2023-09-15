import animaux
import donneesPets

if __name__ == "__main__":
    # Vous pouvez maintenant utiliser les classes et fonctions des modules importés
    # Exemple d'utilisation de la classe Pet
    my_pet = animaux.Pet("Lucky", "chat", "Bob")
    my_pet.manger()

    # Exemple d'utilisation de la classe PetDB pour sauvegarder un animal dans la base de données
    pet_db = donneesPets.PetDB("Tetris", "chien", "Valentine")
    pet_db.sauvegarder()

    # Exemple d'utilisation de la classe PetDB pour lister les animaux depuis la base de données
    donneesPets.PetDB.lister_animaux()
