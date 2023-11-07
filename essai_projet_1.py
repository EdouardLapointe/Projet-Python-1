def essai_console():
    nombre = int(input("Donner un nombre :"))
    liste_nombre = int(input("Un autre nombre :"))
    valeur = []
    for i in range(1, liste_nombre):
        valeur.append(i*nombre)
    print(valeur)

def deuxième_test(nom, genre, age):
    print(f"Je m'appelle {nom}, je suis un {genre} et j'ai {age} ans.")


essai_console()
deuxième_test("Édouard", "homme", 20)