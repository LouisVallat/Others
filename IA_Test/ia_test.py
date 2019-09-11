import os.path
import random
import shutil
import smtplib
import datetime

PLAYED_GAMES, WIN, LOOSE = 0, 0, 0

STUDENT_EMAIL = "louis.vallat@etu.u-bordeaux.fr"


def isResultat():
    """
        Is there a file that contains "resultat" in its name?
    """
    for file in getFileList():
        if "resultat" in file and os.path.isfile("./partie2.log"):
            return True
    return False


def getFileList():
    """
    Get the file list in the cwd.
    """
    return [name for name in os.listdir('.') if os.path.isfile(name)]


# We want to test our AI forever.
while True:
    # If there's the "resultat" file
    if isResultat():
        PLAYED_GAMES += 1
        print("\n" + str(PLAYED_GAMES) + " parties jouees.")

        for file in getFileList():
            # Find the "resultat" file
            if "resultat" in file:

                # While this file is empty, we're waiting quietly
                while os.stat(file).st_size == 0:
                    continue

                # When the file isn't empty anymore, we read it
                with open(file, 'r') as fich:
                    while True:
                        ligne = fich.readline()

                        # We found our e-mail adress,
                        # the result should be in the next line
                        if STUDENT_EMAIL in ligne:
                            resultat = fich.readline()
                            print("Résultat : " + resultat)
                            if "Perdant" in resultat:
                                LOOSE += 1
                            else:
                                WIN += 1
                            print("Ratio de parties gagnées :"
                                  + str((WIN*100)/PLAYED_GAMES) + "%.")
                            break
                # We keep the result file
                shutil.move(file, "./resultats/")
        # And delete the partie2.log file to trigger another game
        os.remove("./partie2.log")
