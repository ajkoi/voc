import main_CSV as main
import tkinter as tk
from tkinter import ttk


def confirm_langue(root, tab_fichier, str_langue, frame):
    if str_langue.get() in tab_fichier[0]:
        tab_verbe = main.list_verbes_correspondances(str_langue.get(), tab_fichier)
        tab_verbe = voc_card_GUI_tkinter(root,tab_verbe)
        frame.destroy()

def verif_vb_res(root, frame_vb_pp, str_var_vb, tab_verbe, verbe, ind_temps_vb, ind_ligne_vb):
    tab_verbe = verif_vb_res_part(root, frame_vb_pp, str_var_vb, tab_verbe, verbe, ind_temps_vb, ind_ligne_vb)

def verif_vb_res_part(root, frame_vb_pp, str_var_vb, tab_verbe, verbe, ind_temps_vb, ind_ligne_vb):
    frame_vb_res = ttk.Frame(master=root)
    frame_vb_res.grid(row=3)

    if main.mot_propre(str_var_vb.get()) == main.mot_propre(verbe[ind_temps_vb]):
        ttk.Label(master=frame_vb_res, text=f'Well Done  ->  {verbe}').pack()
        tab_verbe = tab_verbe[:ind_ligne_vb] + tab_verbe[ind_ligne_vb+1:]
    else:
        ttk.Label(master=frame_vb_res, text=f'SyntaxError  ->  {verbe}').pack()
    
    if len(tab_verbe) > 1:
        root.after(50, voc_card_GUI_tkinter(root,tab_verbe))
        frame_vb_pp.destroy()
        return tab_verbe


def voc_card_GUI_tkinter(root,tab_verbe):

    frame_vb_pp = ttk.Frame(master=root)
    frame_vb_pp.grid()

    frame_vb_label = ttk.Frame(master=frame_vb_pp)
    frame_vb_label.grid(row=0)

    verbes = main.flashcard(tab_verbe)
    verbe = verbes[0]
    ind_temps_vb = verbes[1]
    ind_ligne_vb = verbes[2]
    tab_verbe = verbes[3]

    str_var_vb = tk.StringVar(value='....')

    ttk.Entry(master=frame_vb_pp, textvariable=str_var_vb).grid(row=1)

    for vb in range(len(verbe)):
        if vb == ind_temps_vb:
            ttk.Label(master=frame_vb_label, textvariable=str_var_vb).grid(column=vb, row=0)
        elif vb < ind_temps_vb:
            ttk.Label(master=frame_vb_label, text=f'{verbe[vb]}, ').grid(column=vb, row=0)
        elif vb > ind_temps_vb:
            ttk.Label(master=frame_vb_label, text=f', {verbe[vb]}').grid(column=vb, row=0)

    ttk.Button(master=frame_vb_pp, text='Confirm...', command= lambda: verif_vb_res(root, frame_vb_pp, str_var_vb, tab_verbe, verbe, ind_temps_vb, ind_ligne_vb)).grid(row=2)

    return tab_verbe


def voc_GUI_tkinter():
    root = tk.Tk()

    tab_fichier = main.list_fichier_csv()
    
    str_langue = tk.StringVar()

    frame_langue = ttk.Frame(master = root)
    label_langue_choice = ttk.Label(master=frame_langue, text=f'random.choice({tab_fichier[0]}) ==')
    label_langue_res = ttk.Label(master=frame_langue, textvariable=str_langue)
    entry_langue = ttk.Entry(master=frame_langue, textvariable=str_langue)

    frame_langue.grid(column=0, row=0)
    label_langue_choice.grid(column=0, row=0)
    label_langue_res.grid(column=1, row=0)
    entry_langue.grid(row=1)

    button_langue_confirm = ttk.Button(master=frame_langue, text='Confirm...' ,command=lambda: confirm_langue(root, tab_fichier, str_langue, frame_langue))
    button_langue_confirm.grid(column=0, row=2)

    frame_import = ttk.Frame(master=root)
    frame_import.

    button_quit_confirm = ttk.Button(master=frame_langue, text='^C' ,command=lambda: root.detroy())
    button_quit_confirm.grid(column=0, row=3)

    button_continue_confirm = ttk.Button(master=frame_langue, text='Retry:' ,command=lambda: voc_GUI_tkinter())
    button_continue_confirm.grid(column=1, row=3)

    root.mainloop()



voc_GUI_tkinter()






