import sqlite3
from time import time
from random import shuffle, randint
from tkinter import ttk
import tkinter as tk
class table():



    def __init__(self, nom_fenetre, nom_db, nom_tableau):


        self.fenetre = tk.Tk()
        self.fenetre.title(nom_fenetre)
        self.fenetre.geometry("600x400")
        # création d'un menu déroulant avec les différentes fonctions
        self.barre_menu = tk.Menu(self.fenetre)

        self.menu_fichier = tk.Menu(self.barre_menu, tearoff=0)
        self.barre_menu.add_cascade(label="options", menu=self.menu_fichier)
        self.menu_fichier.add_command(label="test", command=self.afficher_message)
        self.menu_fichier.add_command(label="afficher voc", command=self.afficher_table)
        self.menu_fichier.add_command(label="ajouter voc", command=self.ajouter_voc)
        self.menu_fichier.add_separator() 
        self.menu_fichier.add_command(label="Exit", command=self.quitter_application)

        # Configurer la fenêtre pour utiliser la barre de menu
        self.fenetre.config(menu=self.barre_menu)


        # Lancer la boucle principale de l'application
        self.name_db = nom_db
        self.nom_tableau = nom_tableau
        self.con = sqlite3.connect(str(self.name_db))
        self.cur = self.con.cursor()
        self.cur.execute(
            f"""CREATE TABLE IF NOT EXISTS {self.nom_tableau}(id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
                        trad VARCHAR(100),
                        present VARCHAR(100),
                        preterit VARCHAR(100), 
                        participe_passe VARCHAR(100),
                        is_found INTEGER DEFAULT(0))"""
        )  # création d'une table de donnée
        self.con.commit()
        self.fenetre.mainloop()


    def couper(self):  # coupe la connexion avec la table
        self.con.close()

    # fonctions menu déroulant
    def afficher_message(self): # deboggage et tests
        print(f"manger ")
    def quitter_application(self):
        self.fenetre.destroy()
    
    # relatif a l'ajout de choses dans la table
    def recuperer_input(self, event=None): # recupere l'input dans le champ
        self.info=self.info_demande.get() 
        self.data.append(self.info)
        self.info_demande.set("")
        print(self.data)
        # toutes les 4 entrées, il entre les données dans la table
        if len(self.data)==0:
            self.name_label.config(text="trad")
        elif len(self.data)==1:
            self.name_label.config(text="present")
        elif len(self.data)==2:
            self.name_label.config(text="preterit")
        elif len(self.data)==3:
            self.name_label.config(text='participe passe')
        if len(self.data)==4:
            self.cur.execute(
            f"INSERT INTO {self.nom_tableau} (trad, present, preterit, participe_passe) VALUES( ?, ?, ?, ?)",  self.data)
            self.data = []
            self.name_label.config(text="trad")
    def fin_du_voc(self): # fonction appelée pour finir d'entrer du voc
        self.fenetre.unbind('<Return>')
        self.name_label.destroy()
        self.name_entry.destroy()
        self.button_fin.destroy()



    
    def ajouter_voc(
        self
    ):  # crée une ligne dans la table verbe irregulier contenant la traduction,
      # le présent, le prétérit, le participe passé
        self.tout_detruire() # enleve tout ce qu'il y a ds la fenetre
        self.fenetre.bind('<Return>', self.recuperer_input)  
        self.data = []
        self.info_demande = tk.StringVar()
        self.phase = 'trad'
        self.name_label = tk.Label(self.fenetre, text = self.phase, font=('calibre',10, 'bold'))  # creation du label, du champ d'entré et du 
        self.name_entry = tk.Entry(self.fenetre, textvariable = self.info_demande, font=('calibre',10,'normal')) # button ainsi que leur package
        self.button_fin = tk.Button(self.fenetre, text = 'fin',command=self.fin_du_voc) # en grille
        self.name_label.grid(row=0,column=0)
        self.name_entry.grid(row=1,column=0)
        self.button_fin.grid(row=2,column=1)




    def afficher_table(self):  # permet d'afficher toute les lignes de la table
        self.tout_detruire()
        list_voc = tk.Listbox(self.fenetre)
        list_voc.pack(side = tk.LEFT, fill = tk.BOTH) 
        for row in self.cur.execute(
            f"SELECT id, trad, present, preterit, participe_passe, is_found FROM {self.nom_tableau}"
        ):
            print(row)




# fonctions exercice
    def selectionner_non_faits(self):  # séléctionne et renvoie tout les mots qui n'ont pas étés trouvés
        self.cur.execute(
            f"SELECT id, trad, present, preterit, participe_passe FROM {self.nom_tableau} WHERE is_found == 0"
        )
        return self.cur.fetchall()

    def reset(self):  # remet tout les is_found a 0
        self.cur.execute(
            f"SELECT id, trad, present, preterit, participe_passe FROM {self.nom_tableau} WHERE is_found == 1"
        )

        for (row) in self.cur.fetchall():  # pour chaque ligne séléctionnée, met le isfound a 0
            self.cur.execute(
                f"UPDATE {self.nom_tableau} SET is_found = 0 WHERE id = ?", (row[0],)
            )
            self.con.commit()
    


    # fonctions générales    
    def tout_detruire(self):  # pour detruire tout ce quil y a dans la fenetre (hormis le menu)
        for widget in self.fenetre.winfo_children():
            if widget not in [self.menu_fichier]:
                widget.destroy()



test = table('voc', 'test1', 'test2')