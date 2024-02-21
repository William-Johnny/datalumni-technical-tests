import csv
import json

if __name__ == "__main__":

    filename = '/Users/william-johnguenon/Documents/datalumni-technical-tests/python/students.csv'

    # Ecrivez une fonction permettant de récupérer toutes les lignes
    # du fichier CSV dans une list() `rows`
    rows=[]
    with open(filename) as csvfile:
        csvReader = csv.reader(csvfile, delimiter=',')
        for row in csvReader:
            rows.append(row)
    
    print(f'\nLe fichier brut contient {len(rows)} lignes')

    # Les étudiants ont chacun un diplôme qui leur est attribué
    # La variable `degrees` contient la liste des diplômes
    listeDegrees=[]
    for i in range (len(rows)):
        if rows[i][4] not in listeDegrees:
            listeDegrees.append(rows[i][4])
    degrees = listeDegrees
    print(f'\nLe fichier contient {len(degrees)} diplômes uniques')

    # Donnez, dans un dict, pour chaque diplôme le nombre d'étudiant
    # par catégorie d'utilisateur (student, alumni, ...)
    #
    #   - Master Un -> Student : 123
    #               -> Alumni : 456
    #               -> ...
    #   - Master Deux -> ...
    #

    users_per_degree = {}
    def usersPerDegree (degree):
        Student = 0
        Alumni = 0 
        schoolAdmin = 0
        Teacher = 0
        for i in range (len(rows)):
            if rows[i][4]==degree:
                if rows[i][5]=="Student":
                    Student+=1
                elif rows[i][5]=="Alumni":
                    Alumni+=1
                elif rows[i][5]=="School admin":
                    schoolAdmin+=1
                elif rows[i][5]=="Teacher":
                    Teacher+=1
        users_per_degree[degree]={"Student":Student,"Alumni":Alumni,"School admin":schoolAdmin,"Teacher":Teacher}
        return users_per_degree
    
    for el in degrees:
        usersPerDegree(el)
    
    # Enregistrez le dictionnaire dans un nouveau fichier `degree_count.json`
    tf = open("degree_count.json", "w")
    json.dump(users_per_degree, tf)
    tf.close()

    print(f'\nFichier `degree_count.json` enregistré !')