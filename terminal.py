import subprocess
import os


while True:
    commande = input(os.getcwd() + " > ")
    if commande == "exit":
        break
    
    repertoire = commande.split(" ")
    if len(repertoire) == 2 and repertoire[0] == "cd":
        try:
            os.chdir(repertoire[1])
        except:
            print("Ce répertoire n'existe pas")    
    else:     
        exe = subprocess.run(commande, shell=True, capture_output=True, universal_newlines=True)
        print(exe.stdout)
        print(exe.stderr)

