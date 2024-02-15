def addition(a, b):
    return a + b

def soustraction(a, b):
    return a - b
1
def multiplication(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        raise ValueError("Erreur : Division par zéro.")

def calculatrice():
    print("Bienvenue dans la calculatrice !")
    while True:
        print("Sélectionnez une opération :")
        print("1. Addition")
        print("2. Soustraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Quitter")

        choix = input("Votre choix (1-5) : ")

        if choix == "5":
            print("Au revoir !")
            break

        try:
            a = float(input("Entrez le premier nombre : "))
            b = float(input("Entrez le deuxième nombre : "))

            if choix == "1":
                resultat = addition(a, b)
                print(f"Résultat : {resultat}")
            elif choix == "2":
                resultat = soustraction(a, b)
                print(f"Résultat : {resultat}")
            elif choix == "3":
                resultat = multiplication(a, b)
                print(f"Résultat : {resultat}")
            elif choix == "4":
                resultat = division(a, b)
                print(f"Résultat : {resultat}")
            else:
                print("Choix invalide. Veuillez sélectionner une option valide.")

        except ValueError as e:
            print(f"Erreur : {str(e)}")
        except Exception as e:
            print(f"Une erreur s'est produite : {str(e)}")

calculatrice()