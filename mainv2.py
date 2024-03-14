import sqlite3
from time import time
from random import shuffle, randint
from tkinter import ttk
import tkinter as tk
from database import *

# USELESS FILE



# fonctions menu déroulant
def afficher_message(): # deboggage et tests
    print(f"manger ")
def quitter_application():
    fenetre.destroy()

# relatif a l'ajout de choses dans la table
def recuperer_input(event=None): # recupere l'input dans le champ
    info = info_demande.get() 
    data.append(info)
    info_demande.set("")
    print(data)
    # toutes les 4 entrées, il entre les données dans la table
    if len(data)==0:
        name_label.config(text="trad")
    elif len(data)==1:
        name_label.config(text="present")
    elif len(data)==2:
        name_label.config(text="preterit")
    elif len(data)==3:
        name_label.config(text='participe passe')
    if len(data)==4:
        
        data = []
        name_label.config(text="trad")

def fin_du_voc(): # fonction appelée pour finir d'entrer du voc
    fenetre.unbind('<Return>')
    name_label.destroy()
    name_entry.destroy()
    button_fin.destroy()




def ajouter_voc():  # crée une ligne dans la table verbe irregulier contenant la traduction,
    # le présent, le prétérit, le participe passé
    tout_detruire() # enleve tout ce qu'il y a ds la fenetre
    fenetre.bind('<Return>', recuperer_input)  
    data = []
    global info_demande 
    info_demande = tk.StringVar()
    phase = 'trad'
    name_label = tk.Label(fenetre, text = phase, font=('calibre',10, 'bold'))  # creation du label, du champ d'entré et du 
    name_entry = tk.Entry(fenetre, textvariable = info_demande, font=('calibre',10,'normal')) # button ainsi que leur package
    button_fin = tk.Button(fenetre, text = 'fin',command=fin_du_voc) # en grille
    name_label.grid(row=0,column=0)
    name_entry.grid(row=1,column=0)
    button_fin.grid(row=2,column=0)




def afficher_table():  # permet d'afficher toute les lignes de la table
    tout_detruire()

    scrollbar = ttk.Scrollbar(fenetre, orient="vertical")
    list_voc = tk.Listbox(fenetre, yscrollcommand=scrollbar.set)
    scrollbar.config(command=list_voc.yview)
    list_voc.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")
    list_voc.pack(side = tk.LEFT, fill = tk.BOTH) 
    for row in cur.execute(
        f"SELECT id, trad, present, preterit, participe_passe, is_found FROM {nom_tableau}"
    ):
        subrow = [row[1], row[2], row[3], row[4]]
        print(row)
        list_voc.insert(tk.END, subrow) 






    



# fonctions générales    
def tout_detruire():  # pour detruire tout ce quil y a dans la fenetre (hormis le menu)
    fenetre.unbind('<Return>')

    for widget in fenetre.winfo_children():

        if widget not in [barre_menu]:
            widget.destroy()


if __name__ == "__name__":
    fenetre = tk.Tk()
    fenetre.title("vocabulary")
    fenetre.geometry("600x400")
    # création d'un menu déroulant avec les différentes fonctions
    barre_menu = tk.Menu(fenetre)

    menu_fichier = tk.Menu(barre_menu, tearoff=0)
    barre_menu.add_cascade(label="options", menu=menu_fichier)
    menu_fichier.add_command(label="test", command=afficher_message)
    menu_fichier.add_command(label="afficher voc", command=afficher_table)
    menu_fichier.add_command(label="ajouter voc", command=ajouter_voc)
    menu_fichier.add_separator() 
    menu_fichier.add_command(label="Exit", command=quitter_application)

    # Configurer la fenêtre pour utiliser la barre de menu
    fenetre.config(menu=barre_menu)



    fenetre.mainloop()