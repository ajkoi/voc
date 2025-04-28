import random
import os


def mot_propre(mot:str):
    list_ban = []
    for ind_lettre in range(len(mot)):
        if not mot[ind_lettre].isalpha():
            list_ban += [ind_lettre]
    j = 0
    for ind in list_ban:
        n = ind-j
        mot = mot[:n]+mot[n+1:]
        j += 1
    return mot

def list_fichier_csv():
    tab_csv = []
    tab_nom = []
    tab_fichiers = os.listdir()
    for fichier in tab_fichiers:
        if fichier.endswith('.csv'):
            tab_csv += [fichier]
            tab_nom += [fichier.split(sep='_')[-1][:-4]]
    return tab_nom, tab_csv

def dico_langues_vb(tab_fichier):
    dico_langues = {}
    for ind_tuple_fichier in range(len(tab_fichier)):
        dico_langues[tab_fichier[0][ind_tuple_fichier]] = tab_fichier[1][ind_tuple_fichier]
    return dico_langues

def list_verbes_correspondances(langue, tab_fichier):
    dico_langues = dico_langues_vb(tab_fichier)
    fichier_source = dico_langues[langue]
    with open(fichier_source, 'r', encoding='utf-8') as fichier:
        tab_verbe = []
        txt = fichier.read().split(sep='\n')
        for ligne in txt:
            tab_vb = ligne.split(sep=',')
            tab_verbe += [tab_vb]
        return tab_verbe


def flashcard(tab_verbe):
    ind_ligne_vb = random.choice(range(1,len(tab_verbe)))
    verbe = tab_verbe[ind_ligne_vb]
    ind_temps_vb = random.choice(range(len(verbe)))
    return verbe, ind_temps_vb, ind_ligne_vb, tab_verbe

def voc_card(tab_verbe):
    verbes = flashcard(tab_verbe)

    verbe = verbes[0]
    ind_temps_vb = verbes[1]
    ind_ligne_vb = verbes[2]
    tab_verbe = verbes[3]
    for vb in range(len(verbe)):
        if vb == ind_temps_vb:
            print('----,', end='')
        else:
            print(f'{verbe[vb]},', end='')
    vb_manquant = str(input('--vb_manquant--'))
    if mot_propre(vb_manquant) == mot_propre(verbe[ind_temps_vb]):
        print(f'Bravo\n{verbe}')
        tab_verbe = tab_verbe[:ind_ligne_vb] + tab_verbe[ind_ligne_vb+1:]
        return True, tab_verbe
    else:
        print(verbe)
        return False, tab_verbe


def voc():
    tab_fichier = list_fichier_csv()
    langue = str(input(f'random.choice({tab_fichier[0]}) == '))
    if langue in tab_fichier[0]:
        tab_verbe = list_verbes_correspondances(langue, tab_fichier)

        while len(tab_verbe) > 1:
            res, tab_verbe = voc_card(tab_verbe)

        remake = str(input('return ?'))
        if remake:
            voc()
        else:
            print("^C")
    else:
        voc()

