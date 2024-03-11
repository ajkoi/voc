import sqlite3
from time import time
from random import shuffle


class table:
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
        if input("ajoutervoc? \n") == "oui":  # propose d'ajouter des mots dans la table
            nb_de_voc = int(input("nombre de mots à saisir"))
            table.ajouter_voc(nb_de_voc, self.con, self.cur)

    def couper(self):  # coupe la connexion avec la table
        self.con.close()

    def ajouter_voc(nbdefois, con, cur):  # crée une ligne dans la table verbe irregulier contenant la traduction,
        for i in range( nbdefois):  # le présent, le prétérit, le participe passé 
            trad = input("traduction du verbe \n")
            present = input("present \n")
            preterit = input("preterit \n")
            participe_passe = input("participe passé \n")  # demande les informations
            data = (trad, present, preterit, participe_passe)
            cur.execute(
                "INSERT INTO vbirreguliers (trad, present, preterit, participe_passe) VALUES( ?, ?, ?, ?)", # insert la ligne
                data,
            )
            con.commit()

    def selectionner_non_faits(cur): # séléctionne et renvoie tout les mots qui n'ont pas étés trouvés
        cur.execute(
            "SELECT id, trad, present, preterit, participe_passe FROM vbirreguliers WHERE is_found == 0"
        )
        return cur.fetchall()

    def reset(cur, con): #remet tout les is_found a 0
        cur.execute(
            "SELECT id, trad, present, preterit, participe_passe FROM vbirreguliers WHERE is_found == 1" 
        )

        for row in cur.fetchall(): # pour chaque ligne séléctionnée, met le isfound a 0
            cur.execute("UPDATE vbirreguliers SET is_found = 0 WHERE id = ?", (row[0],))
            con.commit()

    def afficher_table(self): #permet d'afficher toute les lignes de la table
        for row in self.cur.execute(
            "SELECT id, trad, present, preterit, participe_passe, is_found FROM vbirreguliers"
        ):
            print(row)

    def exercice(self):
        table.reset(self.cur, self.con) # reset de la table
        table.afficher_table(self)       # (anectotique, pour le debogage)
        start = time()    #on prend la valaure du temps pour avoir le temps total
        nb_correct = 0
        nb_questions = 0
        while len(table.selectionner_non_faits(self.cur)) != 0:   # tant que l'on a pas trouvé, on continue a questionner
            table_mots = table.selectionner_non_faits(self.cur) # on definit une table
            shuffle(table_mots) # on melange la table 
            for entree in table_mots: # demande pour chaque entrée de la table
                nb_questions += 1
                trad = input(
                    f"{nb_questions}) Quelle est la traduction de {entree[2]},{entree[3]}, {entree[4]}  ? \n"
                ) # on pose la question
                if trad == entree[1]: # si le mot donné correspond a l'entrée:
                    print("correct! \n ") 
                    self.cur.execute(
                        "UPDATE vbirreguliers SET is_found = 1 WHERE id = ?", 
                        (entree[0],),
                    ) # on l'enlève de la liste des mots trouvés
                    self.con.commit()
                    nb_correct += 1
                else: # sinon on dit la bonne reponse
                    print("faux!")
                    print(f"c'était : {entree[1]} \n")
        end = time() # on prend la temps de quand on l'a fini
        temps = (end - start) / 60 # on calcul le temps total et on le convertis en minutes
        print(
            f"nb de réponses correctes :  {nb_correct} / {nb_questions} temps total : {temps} min"
        )
        if nb_correct <= nb_questions / 2:
            print("Pas terrible!!!! révise!!!")

if __name__  == "__main__":
    vb_irreguliers = table("verbesirr.db")

    table.exercice(vb_irreguliers)

    table.couper(vb_irreguliers)