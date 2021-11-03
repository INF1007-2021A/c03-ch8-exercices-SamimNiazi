#!/usr/bin/env python
# -*- coding: utf-8 -*-

PERCENTAGE_TO_LETTER = {"A*": [95, 101], "A": [90, 95], "B+": [85, 90], "B": [80, 85], "C+": [75, 80], "C": [70, 75], "F": [0, 70]}

# TODO: Importez vos modules ici

# TODO: Définissez vos fonction ici
def lecture_fichier (fichier1, fichier2):
    
    with open ("fichier1", 'r') as f:
        with open ("fichier2",'r') as g:
            string_du_premier_fichier = f.readlines()
            string_du_deuxieme_fichier = g.readlines()




if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    print(lecture_fichier ("fichier1","fichier2"))
    pass
