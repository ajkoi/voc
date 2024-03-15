from tkinter import ttk
from tkinter import messagebox
import tkinter as tk
import os
import database as db
# from database import *

def quit_application() -> None:
    fenetre.destroy()

def tout_detruire() -> None:  # pour detruire tout ce quil y a dans la fenetre (hormis le menu)
    fenetre.unbind('<Return>')

    for widget in fenetre.winfo_children():

        if widget not in [barre_menu]:
            widget.destroy()


def select_table() -> None:
    tout_detruire()
    confirm_btn = tk.Button(fenetre, text="Confirm selection", command=confirm_selection)
    confirm_btn.pack(side=tk.BOTTOM, pady=10)
    scrollbar = ttk.Scrollbar(fenetre, orient="vertical")


    global list_files
    list_files = tk.Listbox(fenetre, yscrollcommand=scrollbar.set)
    scrollbar.config(command=list_files.yview)
    list_files.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")
    list_files.pack(side = tk.LEFT, fill = tk.BOTH)
    for path, subdirs, files in os.walk('./vocabulary'):
        for name in files:
            # print(os.path.join(path, name))
            list_files.insert(tk.END, os.path.join(path, name)[13:])

def return_to_homepage() -> None:
    tout_detruire()

    button_select_table = tk.Button(fenetre, command=select_table, text="select table")
    button_exercice = tk.Button(fenetre, command=exercice, text="start the exercise")
    label_selected_file = tk.Label(fenetre, text=f"The selected table is {selected_file}", font=('calibre',10))
    button_select_table.grid(row=1, column=0)
    label_selected_file.grid(row=0, column=0)
    button_exercice.grid(row=2, column=0)

def confirm_selection() -> None:
    selection = list_files.curselection()
    if selection:
        global selected_file
        selected_file = fr"{list_files.get(selection[0])}"
        return_to_homepage()
    else:
        tk.messagebox.showwarning("warning", "please select a database")
    

def on_enter(event, entry_list, index):
    """Gère l'appui sur la touche Entrée dans un champ de saisie."""
    if index + 1 < len(entry_list):
        # Déplace le focus au champ suivant
        entry_list[index + 1].focus_set()
    else:
        # Enregistre les données et réinitialise tous les champs
        save_data_and_reset_fields(entry_list)

def save_data_and_reset_fields(entry_list) -> None:
    """Enregistre les données et réinitialise tous les champs."""
    data = [entry.get() for entry in entry_list]
    print("Données enregistrées :", data)
    for entry in entry_list:
        entry.delete(0, tk.END)
    entry_list[0].focus_set()

def create_form(root, fields) -> list:
    """Crée le formulaire avec les champs de saisie."""
    tout_detruire()
    entry_list = []
    for index, field in enumerate(fields):
        label = tk.Label(root, text=field)
        label.pack()
        entry = tk.Entry(root)
        entry.pack()
        # Bind la touche Entrée à l'action on_enter pour chaque champ
        entry.bind("<Return>", lambda event, entry_list=entry_list, index=index: on_enter(event, entry_list, index))
        entry_list.append(entry)
    return entry_list
def add_vocab() -> None:
    
    table_exercice = db.Table(fr".\vocabulary\{selected_file}") # * to have the whole path
    fields_of_exercice = create_form(fenetre, [i[1] for i in table_exercice.select_columns()[1:-1]])
def exercice() -> None:
    # print(selected_file)
    table_exercice = db.Table(fr".\vocabulary\{selected_file}") # * to have the whole path
    fields_of_exercice = create_form(fenetre, [i[1] for i in table_exercice.select_columns()[1:-1]])

    

if __name__ == "__main__":
    
    fenetre = tk.Tk()
    fenetre.title("vocabulary")
    fenetre.geometry("600x400")
    global selected_file
    selected_file = '[no selected file]'
    barre_menu = tk.Menu(fenetre)
    menu_fichier = tk.Menu(barre_menu, tearoff=0)
    barre_menu.add_cascade(label="options", menu=menu_fichier)
    menu_fichier.add_command(label="select table", command=select_table)
    menu_fichier.add_command(label='exercice', command=exercice)
    # menu_fichier.add_command(label="afficher voc", command=afficher_table)
    # menu_fichier.add_command(label="ajouter voc", command=ajouter_voc)
    menu_fichier.add_separator() 
    menu_fichier.add_command(label="Exit", command=quit_application)
    return_to_homepage()

    fenetre.config(menu=barre_menu)



    fenetre.mainloop()