import sqlite3
from time import time
from random import shuffle, randint
from tkinter import ttk
import tkinter as tk
class gui:

    def afficher_message():
        print("manger")

    def quitter_application(self):
        self.fenetre.destroy()

    # Créer la fenêtre principale
    fenetre = tk.Tk()
    fenetre.title("Barre de menu")

    # Créer une barre de menu
    barre_menu = tk.Menu(fenetre)

    # Créer un menu "File" dans la barre de menu
    menu_fichier = tk.Menu(barre_menu, tearoff=0)
    barre_menu.add_cascade(label="File", menu=menu_fichier)

    # Ajouter une option "Manger" dans le menu "File"
    menu_fichier.add_command(label="Manger", command=afficher_message)

    # Ajouter une option "Exit" dans le menu "File"
    menu_fichier.add_command(label="Exit", command=quitter_application)

    # Configurer la fenêtre pour utiliser la barre de menu
    fenetre.config(menu=barre_menu)

    # Lancer la boucle principale de l'application
    fenetre.mainloop()

class table():

    def __init__(self, nom_db):

        self.name_db = nom_db
        self.con = sqlite3.connect(str(self.name_db))
        self.cur = self.con.cursor()
        self.cur.execute(
            """CREATE TABLE IF NOT EXISTS vbirreguliers(id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
                          trad VARCHAR(100), present VARCHAR(100), preterit VARCHAR(100), participe_passe VARCHAR(100),
                          is_found INTEGER DEFAULT(0))"""
        )  # création d'une table de donnée
        self.con.commit()
        # if input("ajoutervoc? \n") == "oui":  # propose d'ajouter des mots dans la table
        #     nb_de_voc = int(input("nombre de mots à saisir"))
        #     table.ajouter_voc(nb_de_voc, self)
        print('manger')


    def couper(self):  # coupe la connexion avec la table
        self.con.close()

    def ajouter_voc(
        nbdefois, self
    ):  # crée une ligne dans la table verbe irregulier contenant la traduction,
        for i in range(nbdefois):  # le présent, le prétérit, le participe passé
            trad = input("traduction du verbe \n")
            present = input("present \n")
            preterit = input("preterit \n")
            participe_passe = input("participe passé \n")  # demande les informations
            data = (trad, present, preterit, participe_passe)
            self.cur.execute(
                "INSERT INTO vbirreguliers (trad, present, preterit, participe_passe) VALUES( ?, ?, ?, ?)",  # insert la ligne
                data,
            )
            self.con.commit()

    def selectionner_non_faits(self):  # séléctionne et renvoie tout les mots qui n'ont pas étés trouvés
        self.cur.execute(
            "SELECT id, trad, present, preterit, participe_passe FROM vbirreguliers WHERE is_found == 0"
        )
        return self.cur.fetchall()

    def reset(self):  # remet tout les is_found a 0
        self.cur.execute(
            "SELECT id, trad, present, preterit, participe_passe FROM vbirreguliers WHERE is_found == 1"
        )

        for (row) in self.cur.fetchall():  # pour chaque ligne séléctionnée, met le isfound a 0
            self.cur.execute(
                "UPDATE vbirreguliers SET is_found = 0 WHERE id = ?", (row[0],)
            )
            self.con.commit()

    def afficher_table(self):  # permet d'afficher toute les lignes de la table
        listbox = tk.Listbox(self.FENETRE) 
        listbox.pack(side = tk.LEFT, fill = tk.BOTH) 
        for row in self.cur.execute(
            "SELECT id, trad, present, preterit, participe_passe, is_found FROM vbirreguliers"
        ):
            print(row)


    def exercice_fr(self):
        self.reset()  # reset de la table
        # table.afficher_table(self)       (anectotique, pour le debogage)
        start = time()  # on prend la valaure du temps pour avoir le temps total
        nb_correct = 0
        nb_questions = 0
        while (
            len(self.selectionner_non_faits(self)) != 0
        ):  # tant que l'on a pas trouvé, on continue a questionner
            table_mots = table.selectionner_non_faits(self)  # on definit une table
            shuffle(table_mots)  # on melange la table
            for entree in table_mots:  # demande pour chaque entrée de la table
                nb_questions += 1
                trad = input(
                    f"{nb_questions}) Quelle est la traduction de {entree[2]},{entree[3]}, {entree[4]}  ? \n"
                )  # on pose la question
                if trad == entree[1]:  # si le mot donné correspond a l'entrée:
                    print("correct! \n ")
                    self.cur.execute(
                        "UPDATE vbirreguliers SET is_found = 1 WHERE id = ?",
                        (entree[0],),
                    )  # on l'enlève de la liste des mots trouvés
                    self.con.commit()
                    nb_correct += 1
                else:  # sinon on dit la bonne reponse
                    print("faux!")
                    print(f"c'était : {entree[1]} \n")
        end = time()  # on prend la temps de quand on l'a fini
        temps = (
            end - start
        ) / 60  # on calcul le temps total et on le convertis en minutes
        print(
            f"nb de réponses correctes :  {nb_correct} / {nb_questions} temps total : {temps} min"
        )
        if nb_correct <= nb_questions / 2:
            print("Pas terrible!!!! révise!!!")
    def exercice_trad(self):

        table.reset(self)  # reset de la table
        # table.afficher_table(self)       (anectotique, pour le debogage)
        start = time()  # on prend la valaure du temps pour avoir le temps total
        nb_correct = 0
        nb_questions = 0
        while (
            len(table.selectionner_non_faits(self)) != 0
        ):  # tant que l'on a pas trouvé, on continue a questionner
            table_mots = table.selectionner_non_faits(self)  # on definit une table
            shuffle(table_mots)  # on melange la table
            for entree in table_mots:  # demande pour chaque entrée de la table
                nb_questions += 1
                trad = input(
                    f"{nb_questions}) Quelle est la traduction de {entree[1]}? \n"
                )  # on pose la question
                if trad == f"{entree[2]} {entree[3]} {entree[4]}":  # si le mot donné correspond a l'entrée:
                    print("correct! \n ")
                    self.cur.execute(
                        "UPDATE vbirreguliers SET is_found = 1 WHERE id = ?",
                        (entree[0],),
                    )  # on l'enlève de la liste des mots trouvés
                    self.con.commit()
                    nb_correct += 1
                else:  # sinon on dit la bonne reponse
                    print("faux!")
                    print(f"c'était :{entree[2]} {entree[3]} {entree[4]}\n")
        end = time()  # on prend la temps de quand on l'a fini
        temps = (
            end - start
        ) / 60  # on calcul le temps total et on le convertis en minutes
        print(
            f"nb de réponses correctes :  {nb_correct} / {nb_questions} temps total : {temps} min"
        )
        if nb_correct <= nb_questions / 2:
            print("Pas terrible!!!! révise!!!")
    def exercice(nom):
        if randint(1, 2)==1:
            table.exercice_trad(nom)
        else:
            table.exercice_fr(nom)


vb_irreguliers = table("verbesirr.db")
table.afficher_table(vb_irreguliers)

vb_irreguliers.FENETRE.mainloop()
table.couper(vb_irreguliers)
test = gui()