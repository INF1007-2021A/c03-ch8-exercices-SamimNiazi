#!/usr/bin/env python
# -*- coding: utf-8 -*-

PERCENTAGE_TO_LETTER = {"A*": [95, 101], "A": [90, 95], "B+": [85, 90], "B": [80, 85], "C+": [75, 80], "C": [70, 75], "F": [0, 70]}


# def lecture_fichier (fichier1, fichier2):
#     with open(fichier1, "r", encoding = "utf-8") as file1, open(fichier2, "r", encoding = "utf-8") as file2:
#         caractere_file1 = file1.read(1)
#         caractere_file2 = file2.read(1)
        
#         while caractere_file1 == caractere_file2:
#             caractere_file1 = file1.read(1)
#             caractere_file2 = file2.read(1)

#     return f'La première diffèrence est {caractere_file1} et {caractere_file2}'    

# def triple_espace (fichier1, fichier2):
#     with open(fichier1, "r", encoding = "utf-8") as file1, open(fichier2, "w", encoding = "utf-8") as file2:
#         caractere_file1 = file1.read()
#         for lettre in caractere_file1:
#             if lettre != " ":
#                 file2.write(lettre)
#             else:
#                 file2.write ("   ")

# def pourcentage_en_lettre(fichier_de_note, fichier_avec_mentions ):
#     with open(fichier_de_note, "r", encoding = "utf-8") as file1, open(fichier_avec_mentions, "w", encoding = "utf-8") as file2:
        
#         liste_de_note = file1.read().splitlines()
#         for note in liste_de_note:
#             if int(note) >= 95 and int(note) < 101:
#                 file2.write(note + " A*\n")
#             elif int(note) >= 90 and int(note) <95:
#                 file2.write(note + " A \n")
#             elif int(note) >= 85 and int(note) <90:
#                 file2.write(note + " B+ \n")
#             elif int(note) >= 80 and int(note) <85:
#                 file2.write(note + " B \n")
#             elif int(note) >= 75 and int(note) <80:
#                 file2.write(note + " C+ \n")
#             elif int(note) >= 70 and int(note) <75:
#                 file2.write(note + " C \n")
#             else:
#                 file2.write(note +  " F \n")

# def nombre_croissant():
#     with open("exemple.txt", "r", encoding = "utf-8") as exemple:
#         ligne_exemple = exemple.read()
#         print(ligne_exemple)

        
    
        

    
    




# if __name__ == '__main__':
#     # print(lecture_fichier ("fichier1","fichier2"))
#     # print(triple_espace("fichier1", "fichier2"))
#     print(pourcentage_en_lettre("./notes.txt", "fichier1"))
#     print(nombre_croissant())
#     pass
