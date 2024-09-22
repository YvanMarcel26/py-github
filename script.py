#coding:UTF-8

"""test d'affichage 
avec print"""
print('bonjour tout le monde')
print("ceci est une autre phrase")

agePersonne = 15
agePersonne2 = "25"
tva = 19.25
reponse = True

print(type(agePersonne))
print(type(agePersonne2))
print(type(tva))
print(type(reponse))
print(tva)

print("l'age de la deuxieme personne est {} et sa tva est de {}".format(agePersonne2, tva))

nomJoueur = input("entrer un nom: ")
print("Bienvenue a vous", nomJoueur)

# conversion

prixHt = input("entrer un montant: ")
prixHt = float(prixHt)
prixTTC = prixHt + (prixHt*tva/100)
print("prixTTC: ",prixTTC )

print("\tformulaire de conexion")

identifiant = "admin"
mot_de_passe = "admin123"

userId = input("entrer votre identifiant: ")
password = input("entrer le votre mot de passe: ")
if password == mot_de_passe:
    print("connexion reussi, bienvenue ",userId)
print("je ne suis plus dans le if")

compt = 0
while compt < 5:
    print("je suis dans la boucle")
    compt+=1

def dire_bonjour():
    print("bonjour a toute l'équipe")

dire_bonjour()

def dialogue(Nom, message):
    print("{}: {}".format(Nom, message))

dialogue("jean", "bienvenu a Orditron")
dialogue("chloe", "merci monsieur")

def show_inventory(*list_items):
    for element in list_items:
        print(element)
show_inventory("epee")
show_inventory("epee", "arme", "dragon", "voiture BMW")

from math import sqrt
value = sqrt(100)
print(value)

import includes.player as player 
player.au_revoir()
player.parler("john", "salut les abonnés")