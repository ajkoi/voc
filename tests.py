# # # import sqlite3
# # # # from random import shuffle
# # # con = sqlite3.connect("test1.db")
# # # cur = con.cursor()

# # # # # # # # cur.execute("""UPDATE vbirreguliers SET preterit = 'was/were', participe_passe = 'been' WHERE id = 4""")
# # # # # # # # cur.execute("""INSERT INTO vbirreguliers (trad, present, preterit, participe_passe) VALUES( 'gronder', 'chide','chid' ,'chid' )""")
# # # # # # # con.commit()
# # # # # # # print("t")
# # # for row in cur.execute("SELECT id, trad, present, preterit, participe_passe, is_found FROM test2"):
# # #     print(row, '\n')
# # # con.close()

# # from tkinter import *
# # def x():
# #     global t
# #     t = a.get()
# #     b.update()

# # f = Tk()
# # t = StringVar()
# # a = StringVar()
# # b = Label(f, text=t)
# # entry = Entry(f, textvariable=a)
# # b.pack()
# # entry.pack()
# # b.after(1000, x)
# # f.mainloop()
# import tkinter as tk

# def on_enter(event, entry_list, index):
#     """Gère l'appui sur la touche Entrée dans un champ de saisie."""
#     if index + 1 < len(entry_list):
#         # Déplace le focus au champ suivant
#         entry_list[index + 1].focus_set()
#     else:
#         # Enregistre les données et réinitialise tous les champs
#         save_data_and_reset_fields(entry_list)

# def save_data_and_reset_fields(entry_list):
#     """Enregistre les données et réinitialise tous les champs."""
#     # Exemple d'enregistrement des données (ici, affichage dans la console)
#     data = [entry.get() for entry in entry_list]
#     print("Données enregistrées :", data)
#     # Efface les champs
#     for entry in entry_list:
#         entry.delete(0, tk.END)
#     # Remet le focus au premier champ
#     entry_list[0].focus_set()

# def create_form(root, fields):
#     """Crée le formulaire avec les champs de saisie."""
#     entry_list = []
#     for index, field in enumerate(fields):
#         label = tk.Label(root, text=field)
#         label.pack()
#         entry = tk.Entry(root)
#         entry.pack()
#         # Bind la touche Entrée à l'action on_enter pour chaque champ
#         entry.bind("<Return>", lambda event, entry_list=entry_list, index=index: on_enter(event, entry_list, index))
#         entry_list.append(entry)
#     return entry_list

# root = tk.Tk()
# root.title("Formulaire d'enregistrement avec réinitialisation complète")

# fields = ['Nom', 'Prénom', 'Email', 'Âge']

# # Création du formulaire
# entry_list = create_form(root, fields)

# # Sélectionne le premier champ au démarrage
# if entry_list:
#     entry_list[0].focus_set()

# root.mainloop()


def a():
    ta = 'ttot'
    def b():
        print(ta)
        bqds = 'tre'
    def c():
        print('test')
    b()
a()