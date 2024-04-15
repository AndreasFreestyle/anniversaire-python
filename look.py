import datetime
import tkinter as tk
from PIL import Image, ImageTk


aujourdhui = datetime.date.today()

chemin_fichier = "texte_saisi.txt"

def look():
    with open(chemin_fichier, 'r') as fichier:
        for ligne in fichier:
            ligne = ligne.strip()
            date_str = ligne.split()[-1]  
        
            try:
                date_ligne = datetime.datetime.strptime(date_str, '%Y-%m-%d').date()
            
                if date_ligne == aujourdhui:
                    mail = ligne
                    print(mail)

                    anniversaire = tk.Tk()
                    anniversaire.title("date d'anniversaire")

                    print("c'est anniersaire de" + ' ' + mail)

                    label = tk.Label(anniversaire, text="c'est anniersaire de" + ' ' + mail)
                    label.pack()

                    anniversaire.mainloop()
                
            except ValueError:
                continue


