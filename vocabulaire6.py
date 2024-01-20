import random
from time import time
vb_irr = {}
dic = {}
dicf = {}
voc_all = {}

test = {'1+1':'2',
        '1*3':'3'}
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
          'enseignesr': 'teach,taught,taught',
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
                              nb_correct += 1
                    else:
                              print('faux!')
                              print('c\'était : '+ dic[entree])
                              print()
          fin = time()
          temps = (fin - debut)/60
          print('nb de réponses correctes : ' + str(nb_correct) + '/' + str(nb_questions)+ 'temps total :'+ str(temps)+ 'min')
          if (nb_correct <= nb_questions/2):
                    print('Pas terrible!!!! révise!!!')

while True :
          a = input(str('1 = vb_irr, 2=vocabulaire,3 = voc2, 4 = test'))
          dicf = {}
          if a == str(1):
                    dicf.update(vb_irr)
          if a == str(2):
                    dicf.update(dic)
          if a == str(3):
                    dicf.update(voc2)
          if a == str(4):
                    dicf.update(test)
          if a == str(0):
                    break
          if a == str():
                    break
                    
          if input(str('1 = fra=>autre langue, 2 = autre langue => fra'))== str(1):
                    debut = time()
                    exercice(dicf)

          else:
                    debut = time()
                    renv(dicf)
                    exercice(dicf)
          

