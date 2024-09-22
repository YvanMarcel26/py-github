#coding:utf-8

"""
module pour le joueur
"""

def parler(personnage, message):
    print("{}: {}".format(personnage, message))

def au_revoir():
    print("Au-revoir les amis")

if __name__ == "__script__":
    print("phase de test de player")
    parler("jason", "bonjour tout le monde")
    au_revoir()