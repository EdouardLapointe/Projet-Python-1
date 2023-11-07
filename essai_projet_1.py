def essai_console():
    nombre = int(input("Donner un nombre :"))
    liste_nombre = int(input("Un autre nombre :"))
    valeur = []
    for i in range(1, liste_nombre):
        valeur.append(i*nombre)
    print(valeur)

essai_console()