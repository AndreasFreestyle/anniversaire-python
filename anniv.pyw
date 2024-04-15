import tkinter as tk
from tkcalendar import Calendar
from look import look

def ecrire_texte_dans_fichier():
    texte = champ_texte.get()
    date_selectionnee = cal.selection_get()
    with open("texte_saisi.txt", "a") as fichier:
        fichier.write(texte + ' ' + str(date_selectionnee) + "\n" )
    print("Texte ajouté au fichier : ", texte)
    champ_texte.delete(0, tk.END)  # Effacer le contenu du champ texte après l'écriture

# Créer la fenêtre principale
fenetre = tk.Tk()
fenetre.title("date d'anniversaire")

# Créer un widget Label pour le nom de la personne 
label = tk.Label(fenetre, text="nom de la personne")
label.pack()

# Créer un champ de texte pour la saisie
champ_texte = tk.Entry(fenetre)
champ_texte.pack()

# Créer un widget Label pour la date d'anniversaire
label = tk.Label(fenetre, text="date de d'aniversaire")
label.pack()

# Créer le widget de calendrier
cal = Calendar(fenetre, selectmode='day', year=2024, month=4, day=14, yearvisible=False)
cal.pack()

# Créer un bouton pour ajouter le texte au fichier
bouton_ecrire_texte = tk.Button(fenetre, text="Ajouter l'anniversaire", command=ecrire_texte_dans_fichier)
bouton_ecrire_texte.pack()

# Créer un bouton pour voir si il y a un anniversaire
bouton_ecrire_texte = tk.Button(fenetre, text="anniversaire", command=look)
bouton_ecrire_texte.pack()

# Lancer la boucle principale
fenetre.mainloop()
