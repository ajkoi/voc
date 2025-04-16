import tkinter as tk
from tkinter import ttk, messagebox
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
        # self.menu_fichier.add_command(label="exercice", command=self.exercice)
        # menu_fichier.add_command(label="afficher voc", command=afficher_table)
        # menu_fichier.add_command(label="ajouter voc", command=ajouter_voc)
        self.menu_fichier.add_separator()
        # self.menu_fichier.add_command(label="Exit", command=self.quit_application)
        self.return_to_homepage()
        # self.self.main.config(menu=self.barre_menu)
        self.test = tk.LabelFrame(self.main, text="manfge")
        self.test.pack()
        self.main.mainloop()

    def quit_application(self) -> None:
        self.main.destroy()

    def destroy_everything(self) -> None:
        """Destroy everything except the menu"""
        self.main.unbind("<Return>")

        for widget in self.main.winfo_children():
            if widget not in [self.barre_menu]:
                widget.destroy()

    def return_to_homepage(self):
        self.destroy_everything()

        self.button_select_table = tk.Button(
            self.main, command=self.select_table, text="select table"
        )
        self.button_exercice = tk.Button(
            self.main, command=self.exercice, text="start the exercise"
        )
        self.label_selected_file = tk.Label(
            self.main,
            text=rf"The selected table is {self.selected_file}",
            font=("calibre", 10),
        )
        self.button_select_table.grid(row=1, column=0)
        self.label_selected_file.grid(row=0, column=0)
        self.button_exercice.grid(row=2, column=0)

    def select_table(self) -> None:
        self.destroy_everything()
        self.confirm_btn = tk.Button(
            self.main, text="Confirm selection", command=self.confirm_selection
        )
        self.confirm_btn.pack(side=tk.BOTTOM, pady=10)
        scrollbar = ttk.Scrollbar(self.main, orient="vertical")

        self.list_files = tk.Listbox(self.main, yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.list_files.yview)
        self.list_files.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        self.list_files.pack(side=tk.LEFT, fill=tk.BOTH)
        for path, subdirs, files in os.walk("./vocabulary"):
            for name in files:
                # print(os.path.join(path, name))
                self.list_files.insert(tk.END, os.path.join(path, name)[13:])

    def confirm_selection(self) -> None:
        selection = self.list_files.curselection()
        if selection:
            self.selected_file = rf"{self.list_files.get(selection[0])}"
            self.return_to_homepage()
        else:
            messagebox.showwarning("warning", "please select a database")


if __name__ == "__main__":
    a = fenetre()
