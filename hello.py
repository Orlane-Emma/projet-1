nombre = int(input("Entrez un nombre : "))
print(nombre)

def afficher_multiples() :
    for i in range(1,11) :
        result = i*nombre 
        print(f"{i} * {nombre} = {result}")
        
afficher_multiples()

        

