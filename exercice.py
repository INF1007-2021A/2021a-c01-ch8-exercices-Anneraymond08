#!/usr/bin/env python
# -*- coding: utf-8 -*-

PERCENTAGE_TO_LETTER = {"A*": [95, 101], "A": [90, 95], "B+": [85, 90], "B": [80, 85], "C+": [75, 80], "C": [70, 75], "F": [0, 70]}

# TODO: Importez vos modules ici


# TODO: Définissez vos fonction ici

def exercice1(file_path1, file_path2):
    with open(file_path1, encoding='utf-8') as f1, open(file_path2, encoding='utf-8') as f2:
        for count, line_f1 in enumerate(f1):
            line_f2 = f2.readline()
            if line_f1 != line_f2:
                print(f"the files are not identical. line {count +1} is different.")
                print(line_f1)
                print('is not the same as')
                print(line_f2)
                return
        print("the files are identical.")

def exercice2(file_path1, file_path2):
    with open(file_path1) as f1:
        db = f1.readlines()
    with open(file_path2, 'w') as f2:
        for line in db:
            f2.write('   '.join(line.split(' ')))


def exercice3(file_path1, file_path2):
    with open(file_path1) as f1:
        db = f1.readlines()
    with open(file_path2, 'w') as f2:
        for note in db:
            for key, value in PERCENTAGE_TO_LETTER.items():
                if value[0] < int(note) < value[1]:
                    f2.write(note.strip() + ' ' + key + '\n')
                    break


def exercice5(file_path):
    with open(file_path) as f:
        db = f.readlines()
        liste_num = []
        for line in db:
            for elem in line.split(' '):
                if elem.isdigit():
                    liste_num.append(float(elem))
        return sorted(liste_num)


def exercice6(file_path1, file_path2):
    with open(file_path1) as f1:
        db = f1.readlines()
    with open(file_path2, 'w') as f2:
        for index, line in enumerate(db):
            if index % 2 == 0:
                f2.write(line)


if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    exercice1('exemple.txt', 'exemple.txt')
    exercice2('exemple2_f1.txt', 'exemple2_f2.txt')
    exercice3('notes.txt', 'result.txt')
    print(exercice5('exemple.txt'))
    exercice6('exemple.txt', 'exercice6.txt')

