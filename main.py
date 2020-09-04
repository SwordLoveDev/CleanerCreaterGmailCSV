#+------------------------------------------+
#+       IMPORTATION DES MODULES            +
#+------------------------------------------+

import csv  
import random

#+------------------------------------------+
#+         FONCTION MOT DE PASSE            +
#+------------------------------------------+

def mdp():
  liste1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  liste2 = "abcdefghijklmnopqrstuvwxyz"
  liste3 = "0123456789"
  liste4 = "$€£&@"
  passwd = ""
  
  for i in range(5): 
    passwd = passwd + liste2[random.randint(0, len(liste2) - 1)]

  for i in range(1): 
    passwd = passwd + liste4[random.randint(0, len(liste4) - 1)]
    
  for i in range(1): 
    passwd = passwd + liste1[random.randint(0, len(liste1) - 1)]
  
  for i in range(1): 
    passwd = passwd + liste3[random.randint(0, len(liste3) - 1)]
   
    return passwd

passwd = mdp()
pas = passwd[1]+passwd[7]+passwd[2]+passwd[0]+passwd[6]+passwd[3]+passwd[5]+passwd[4]

#+------------------------------------------+
#+          FONCTION NETTOYAGE              +
#+------------------------------------------+

def espace(x):
  compteur = 0
  for i in x:
      if i==' ':
          compteur += 1
      else :
          pass
  if compteur != 0:
    x = '.'.join(x.split())
  else :
    pass
  accent = ['é', 'è', 'ê', 'à', 'ù', 'û', 'ç', 'ô', 'î', 'ï', 'â', 'É']                  
  sans_accent = ['e', 'e', 'e', 'a', 'u', 'u', 'c', 'o', 'i', 'i', 'a', 'e']
  i = 0   
  while i < len(accent):
    x = x.replace(accent[i], sans_accent[i])
    i += 1
  x = x.lower()
  return x

#+------------------------------------------+
#+          FONCTION PRINCIPALE             +
#+------------------------------------------+

def main():
  with open("base.csv") as fichier: 
    reader = csv.reader(fichier) 
    for colonne in reader:
      prenom = (colonne[0])
      print(espace(prenom) + "@gmail.com"+":"+mdp())
  return 

main()

#+------------------------------------------+
#+              NOUVEAU CSV                 +
#+------------------------------------------+

with open("base.csv") as fichier: 
  reader = csv.reader(fichier) 
  for colonne in reader:
    prenom = (colonne[0])
    TEST = [espace(prenom) + "@gmail.com"+":"+mdp()]
    with open('nouveau.csv','w') as f:
      f_csv = csv.writer(f)
      f_csv.writerow(TEST)