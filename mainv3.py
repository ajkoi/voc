import tkinter as tk
import csv_database
import random
import time
import os


class fenetre:
    def __init__(self):
        self.main = tk.Tk()
        self.main.title("voc")
        self.selected_file = "[no selected file]"
        self.barre_menu = tk.Menu(self.main)
        self.menu_fichier = tk.Menu(self.barre_menu, tearoff=0)
        self.barre_menu.add_cascade(label="options", menu=self.menu_fichier)
        self.menu_fichier.add_command(label="select table", command=self.select_table)
        self.menu_fichier.add_command(label="exercice", command=self.exercice)
        # menu_fichier.add_command(label="afficher voc", command=afficher_table)
        # menu_fichier.add_command(label="ajouter voc", command=ajouter_voc)
        self.menu_fichier.add_separator()
        self.menu_fichier.add_command(label="Exit", command=self.quit_application)
        self.return_to_homepage()
        self.fenetre.config(menu=self.barre_menu)
        self.fenetre.mainloop()

    def quit_application(self):
        self.main.destroy()

    def goto_menu(self):
        pass


if __name__ == "__main__":
    a = fenetre()
