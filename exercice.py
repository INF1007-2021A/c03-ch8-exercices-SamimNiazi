#!/usr/bin/env python
# -*- coding: utf-8 -*-

PERCENTAGE_TO_LETTER = {"A*": [95, 101], "A": [90, 95], "B+": [85, 90], "B": [80, 85], "C+": [75, 80], "C": [70, 75], "F": [0, 70]}


def lecture_fichier (fichier1, fichier2):
    with open(fichier1, "r", encoding = "utf-8") as file1, open(fichier2, "r", encoding = "utf-8") as file2:
        caractere_file1 = file1.read(1)
        caractere_file2 = file2.read(1)
        
        while caractere_file1 == caractere_file2:
            caractere_file1 = file1.read(1)
            caractere_file2 = file2.read(1)

    return f'La première diffèrence est {caractere_file1} et {caractere_file2}'    

def triple_espace (fichier1, fichier2):
    with open(fichier1, "r", encoding = "utf-8") as file1, open(fichier2, "w", encoding = "utf-8") as file2:
        caractere_file1 = file1.read()
        for lettre in caractere_file1:
            if lettre != " ":
                file2.write(lettre)
            else:
                file2.write ("   ")

def pourcentage_en_lettre(fichier_de_note, fichier_avec_mentions ):
    with open(fichier_de_note, "r", encoding = "utf-8") as file1, open(fichier_avec_mentions, "w", encoding = "utf-8") as file2:





if __name__ == '__main__':
    print(lecture_fichier ("fichier1","fichier2"))
    print(triple_espace("fichier1", "fichier2"))
    pass
