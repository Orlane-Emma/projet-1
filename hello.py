nombre = int(input("Entrez un nombre : "))
print(nombre)

def afficher_multiples() :
    for i in range(1,11) :
        result = i*nombre 
        print(f"{i} * {nombre} = {result}")
        
afficher_multiples()

choix=input("Fin de l'affichage. appuyez sur R pour recommencer ou T pour terminer le programme")
if choix.upper()== "R":
    print ("Recommencer")
else :
    print("Fin de programme.")


        

