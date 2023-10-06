import datetime
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

# Fonction qui sera appelée lorsque le bouton sera cliqué ------------------------

def afficher_message():
	date_actuelle = datetime.datetime.now()
	date_formatee = date_actuelle.strftime("%Y-%m-%d %H:%M:%S")
	text_format = "Valentine - 35\n{}".format(date_formatee)
	label.config(text=text_format, foreground="darkgreen")
	label.update_idletasks()
	fenetre.after(5000, fenetre.quit())


# Création de la fenêtre principale ----------------------------------------------

fenetre = tk.Tk()
fenetre.title("Ma première application Tkinter")


# Calculer la position x et y pour centrer la fenêtre ----------------------------

largeur_fenetre = 400
hauteur_fenetre = 300
largeur_ecran = fenetre.winfo_screenwidth()
hauteur_ecran = fenetre.winfo_screenheight()
x = (largeur_ecran - largeur_fenetre) // 2
y = (hauteur_ecran - hauteur_fenetre) // 2


# Spécifier la taille et la position de la fenêtre -------------------------------

fenetre.geometry(f"{largeur_fenetre}x{hauteur_fenetre}+{x}+{y}")
fenetre.minsize(largeur_fenetre, hauteur_fenetre)
fenetre.maxsize(largeur_fenetre + 200, hauteur_fenetre + 200)


# Création d'un label ------------------------------------------------------------

label = tk.Label(fenetre, text="Cliquez sur le bouton pour afficher un message\n")
label.config(
	font=("Courrier", 10, "bold"),
	foreground="darkred"
)
label.pack(pady=10)


# creation de style pour les boutons ---------------------------------------------

style = ttk.Style()
style.configure(
	'Rounded.TButton',
	borderwidth=0,
	relief="flat",
	background="lightblue",
	padding=0
)


# Charge une image et redimensionne-la -------------------------------------------

image = Image.open("/Users/valentineq/Desktop/Formation/Python/TKinter/istockphoto-1165294761-612x612.jpg")
image = image.resize((200, 200))
photo = ImageTk.PhotoImage(image)


# Crée un bouton avec une image sans texte ---------------------------------------

bouton1 = ttk.Button(
	fenetre,
	text="",
	cursor="hand2",
	style="Rounded.TButton",
	command=afficher_message,
	image=photo,
	compound="center"  # Utilisez "center" pour centrer l'image dans le bouton
)
bouton1.pack(pady=15)


# Lancement de la boucle principale ----------------------------------------------

fenetre.mainloop()
