import os.path, random, shutil, smtplib, datetime
partiesJouees, gagnantes, perdantes = 0, 0, 0

def isResultat():
    tableauFichiers = ([name for name in os.listdir('.') if os.path.isfile(name)])
    for file in tableauFichiers:
        if "resultat" in file and os.path.isfile("./partie2.log"):
            return True
    return False

while True:
    nombreFichiers = (len([name for name in os.listdir('.') if os.path.isfile(name)]))
    tableauFichiers = ([name for name in os.listdir('.') if os.path.isfile(name)])
    if isResultat():
        tableauFichiers = ([name for name in os.listdir('.') if os.path.isfile(name)])
        partiesJouees+=1
        print("\n" + str(partiesJouees) + " parties jouees.")
        for file in tableauFichiers:
            if "resultat" in file:
                while os.stat(file).st_size == 0:
                    continue
                with open(file,'r') as fich:
                    while True:
                        ligne = fich.readline()
                        if "louis.vallat@etu.u-bordeaux.fr" in ligne:
                            resultat = fich.readline()
                            print("Résultat : " + resultat)
                            if "Perdant" in resultat:
                                perdantes+=1
                            else:
                                gagnantes+=1
                            print("Ratio de parties gagnées :" + str((gagnantes*100)/partiesJouees) + "%.")
                            break
                shutil.move(file, "./resultats/")
        os.remove("./partie2.log")                
