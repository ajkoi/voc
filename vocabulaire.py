#@title
import random
from time import time
vb_irr = {}
dic = {}
dicf = {}
voc_all = {}

test = {'1+1':'2',
        '1*3':'3'}


#HG
dicHG = {'1967': 'loi autorisant la contraception sous conditions', 
         '1974': 'loi Veil : légalisation de la contraception', 
         '1970': "loi sur l'autorité parentale partagé", 
         '1975': "Loi Veil : autoriation de l'IVG", 
         '1983': 'loi Roudy : égalité professionnelle'}
#voc_anglais
voc2 = {'break up': 'séparer',
        'realease a record': 'sortir un disque',
        'slum': 'bidonville', 'since': 'puisque',
        'raise(a child)': 'élever (un enfant)',
        'in the early 60s': 'au début des années 60',
        'be of a mixed race': 'être métis(se)',
        'still': 'toujours/encore',
        'teach sb sth/how to do sth': 'soigner',
        'shoot sb': 'tuer qqn par balles'}

vb_irr = {'blesser': 'hurt,hurt,hurt',
       'frapper': 'hit,hit,hit',
       'mettre': 'put,put,put',
       'permettre/louer': 'let,let,let',
       'couper': 'cut,cut,cut',
       'fermer': 'shut,shut,shut',
       'coûter': 'cost,cost,cost',
       'apporter': 'bring,brought,brought',
       'construire': 'build,built,built',
       'acheter': 'buy,bought,bought',
       'brûler': 'burn,burnt,burnt',
       'trouver': 'find,found,found',
       'se sentir/ressentir': 'feel,felt,felt',
       'se battre': 'fight,fought,fought',
       'rêver': 'dream,dreamt,dreamt',
       'attraper': 'catch,caught,caught',
       'tenir': 'hold,held,held',
          'garder': 'keep,kept,kept',
          'entendre': 'hear,heard,heard',
          'obtenir': 'get,got,got',
          'avoir': 'have,had,had',
          'perdre': 'lose,lost,lost',
          'vouloir dire': 'mean,meant,meant', 'prêter':
          'lend,lent,lent', 'partir': 'leave,left,left',
          'poser': 'lay,laid,laid', 'mener': 'lead,led,led',
          'faire,fabriquer': 'make,made,made',
          'apprendre': 'learn,learnt,learnt',
          'envoyer': 'send,sent,sent',
          'vendre': 'sell,sold,sold',
          'dire': 'say,said,said',
          'tirer': 'shoot,shot,shot',
          "s'asseoir": 'sit,sat,sat',
          'payer': 'pay,paid,paid',
          'lire': 'read,read,read',
          'rencontrer': 'meet,met,met',
          'gagner': 'win,won,won',
          'penser': 'think,thought,thought',
          'comprendre': 'understand,understood,understood',
          'épeler': 'spell,spelt,spelt',
          'raconter/dire': 'tell,told,told',
          'enseigner': 'teach,taught,taught',
          'dormir': 'sleep,slept,slept',
          'sentir': 'smell,smelt,smelt',
          'dépenser': 'spend,spent,spent',
          'se lever/être debout': 'stand,stood,stood',
          'venir': 'come,came,come',
          'devenir': 'become,became,become',
          'courir' : 'run,ran,run',
          'conduire': 'drive,drove,driven',
          'être': 'be,was,been',
          'battre': 'beat,beat,beatten',
          'faire (pas make)': 'do,did,done',
          'dessiner': 'draw,drew,drawn',
          'mordre': 'bite,bit,bitten',
          'casser': 'break,broke,broken',
          'choisir': 'choose,chose,chosen'}
dic['take/adopt a stance(on/toward/against)']='adopter une position(sur/contre)'
dic['consider oneself as']= 'se considérer comme'
dic['estabish/regard oneself as']= 'se présenter/s\'affirmer comme'
dic['to/in order to/so as to']= 'pour/afin de'
dic['address somebody']='parler à quelqu\'un'
dic['make a difference between']='faire une différence entre'
dic['make sb understand sth']='faire comprendre qqch à qqn'
dic['raise awarness about']='sensibiliser'
dic['undereducated']='peu instruit'
dic['unskilled']='non qualifié'
dic['improve']='améliorer'
dic['living conditions']='conditions de vie'
dic['get across/send out a message']='faire passer un message'
dic['be prone to sth/to do/doing sth']='être enclin/sujet à'
#voc_allemand
voc_all = {'le correspondant':'der Austauschpartner',
           "la famille d'accueil": 'die Gastfamilie(n)',
           'faire des progrès': 'Fortschritte machen',
           'participer à un échange': 'an einem Austausch teilnehmen',
           "l'ami": 'der Freund(e)', "l'amie": 'die Freundin(nen)',
           'le pays': 'das Land(¨er)',
           "l'échange": 'der Austausch(e)',
           'le pays étranger': 'das Ausland'}
voc_all2 = {'rêver de qqch':'von etwas(D) träumen','souhaiter qqch':'sich etwas wünschen','etwas ausüben':'exercer',
            'travailler':'arbeiten','s\'intéresser à':'sich interessieren für',
            'gagner de l\'argent':'Geld verdinen','choisir':'etwas wählen','s\'intéresser à qqch':'sich für etwas interessieren',
            'réussir':'etwas schaffen','réaliser qqch':'etwas verwirklichen',
            'aller/convenir à qqn':'zu jn passen','planifier de faire qqch':'planen, etwas zu','prévoir de faire qqch':'vor/haben,etwas zu',
            'le baccalauréat':'das Abitur','le choix du métier':'die Berufswahl','la formation':'das Ausbildung','la valeur':'der Wert'}
voc_all_vb_fort = {'rester':'geblieben',
                   'manger':'gegessen',
                   'aller(en véhicule)':'gefahren',
                   'venir':'gekommen',
                   'nager':'geschwommen',
                   'voir':'gesehen',
                   'voler(avion)':'geflogen',
                   'aller(à pieds)':'gegangen'}
voc_Physique ={"l'énergie": 'die Kraft', 'passé': 'vergangen',
                'circuler (rumeur)': 'die Runde machen',
                  'dans le monde entier': 'weltweit',
                    'être à la base de': 'zugrunde liegen(a,e)+D',
                      "l'étude": 'die Studie(n)',
                        "l'autorité (administrative)": 'die Behörde(n)'
                    , 'à moyen terme': 'mittelfristig', 'au moins': 'mindestens',
                      "l'installation": 'die Anlage(n)', 'la population': 'die Bevölkerung',
                     'la serre': 'das Treibhaus(¨er)', "l'hypothèse": 'die Annahme',
                       'les faits': 'die Fakten', 'la majorité': 'die Mehrzahl',
                         'le pays': 'das Land(¨er)', "jusqu'à présent": 'bislang',
                           'la Pologne': 'Polen', "la sortie, l'abandon": 'der Ausstieg',
                             'le gouvernement': 'die Regierung(en)',
                               'le cas [particulier]': 'der [Sonder]fall(¨e)',
                                 'envisager': 'planen', 'construire': 'bauen',
                        "à l'heure actuelle": 'derzeit', 'la construction': 'der [Neu]bau',
                        'le groupe insustriel': 'der Konzern(e)', 'le prix fixe': 'der Festpreis',
                          'toutefois': 'allerdings', 'le constructeur': 'der Erbauer(-)',
                            'le coût': 'die Kosten', 'être valable': 'gelten(i,a,o)',
                              'le membre': 'das Mitglied(er)'
                        , "l'adversaire": 'die Gegnerin(nen)'}
#{'spüren':'ressentir','wirken':'agir','vor/kommen':'se produire','merken':'voir',
#               'etw zur Verfügung haben':'avoir qqch à sa disposition'

def renv(dic):
  list_dep = list()
  list_trad = list()
  for keys,val in dic.items():
    list_dep.append(val)
    list_trad.append(keys)
    dic.clear()
    for z in range (len(list_dep)-1):
      dic[list_dep[z]]= list_trad[z]


def exercice(dic):
    
    nb_correct = 0
    nb_questions = 0
    liste_entrees = list(dic.keys())
    random.shuffle(liste_entrees)
    for entree in liste_entrees:
        nb_questions +=1
        trad = input(str(nb_questions) +'. Quelle est la traduction de '+ entree +'? \n')

        if trad == dic[entree]:
      
            print('correct!')
            print()
            nb_correct += 1
        else:
            print('faux!')
            print('c\'était : '+ dic[entree])
            print()
        fin = time()
        temps = (fin - debut)/60
        print('nb de réponses correctes : ' + str(nb_correct) + '/' + str(nb_questions)+ ' temps total :'+ str(temps)+ 'min')
        if (nb_correct <= nb_questions/2):
            print('Pas terrible!!!! révise!!!')



while True :
    a = 0
    a = input(str('1 = vb_irr, 2=vocabulaire,3 = voc2, 4 = test, 5 = HG, 6 = verbes forts,7 = allemand seconde "les métiers",8 = vocabulaire PCALL'))          
    if a == str(1):
        dicf.update(vb_irr)
    elif a == str(2):
        dicf.update(dic)
    elif a == str(3):
        dicf.update(voc2)
    elif a == str(4):
        dicf.update(test)
    elif a == str(5):
        dicf.update(dicHG)
    elif a == str(6):
        dicf.update(voc_all_vb_fort)
    elif a == str(7):
        dicf.update(voc_all2)
    elif a == str(8):
        dicf.update(voc_Physique)
    else:
        break
                    
    if input(str('1 = fra=>autre langue, 2 = autre langue => fra'))== str(1):
        debut = time()
        exercice(dicf)

    else:
        debut = time()
        renv(dicf)
        exercice(dicf)
