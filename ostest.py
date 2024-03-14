import tkinter as tk
from tkinter import messagebox
import os

def list_files():
    start_dir = os.path.dirname(os.path.abspath(__file__))  # Démarrer le parcours à partir du répertoire du script
    for dirpath, dirnames, filenames in os.walk(start_dir):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            file_listbox.insert(tk.END, file_path)

def confirm_selection():
    selection = file_listbox.curselection()
    if selection:
        selected_file = file_listbox.get(selection[0])
        messagebox.showinfo("Sélection", f"Vous avez sélectionné : {selected_file}")
    else:
        messagebox.showwarning("Attention", "Veuillez sélectionner un fichier.")

# Initialisation de la fenêtre Tkinter
root = tk.Tk()
root.title("Liste des fichiers")
root.geometry("600x400")

# Création d'une scrollbar
scrollbar = tk.Scrollbar(root)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Création de la listbox pour afficher la liste des fichiers
file_listbox = tk.Listbox(root, yscrollcommand=scrollbar.set, width=80, height=20)
file_listbox.pack(side=tk.LEFT, fill=tk.BOTH)

# Configuration de la scrollbar
scrollbar.config(command=file_listbox.yview)

# Bouton pour confirmer la sélection
confirm_btn = tk.Button(root, text="Confirmer la sélection", command=confirm_selection)
confirm_btn.pack(side=tk.BOTTOM, pady=10)

# Remplir la liste des fichiers au lancement de l'application
list_files()

# Lancement de la boucle Tkinter
root.mainloop()
