print("Bienvenue dans le premier projet de code")

print("")

def demander_nom():

    reponse_nom = ""

    while reponse_nom == "":
        reponse_nom = input("Quel est ton nom ?")

    return reponse_nom


def demander_age(nom_personne):

    age_int = 0

    while age_int == 0:
        age_str = input(nom_personne + " quel est ton age ?")
        try:
            age_int = int(age_str)
        except:
            print("ERREUR: Vous devez utiliser un nombre pour l'age")
    return age_int


def afficher_informations_personne(nom, age):

    print("Vous vous appelez " + nom + ", vous avez " + str(age) + " ans.")
    print("L'an prochain vous aurez " + str(age + 1) + "ans.")

    #print(f"Vous vous appelez {nom}, vous avez {age }ans. ")
    #print(f"L'an prochain vous aurez {age + 1} ans. ")

    if age == 17:
        print("Vous êtes presque majeur.")
    elif 12 <= age < 18:
        print("Vous êtes adolescent.")
    elif age == 1 or age == 2:
        print("Vous êtes un bébé.")
    elif age == 18:
        print("Tout juste majeur, FELICITATION.")
    elif age > 60:
        print("Vous êtes un senior.")
    elif age < 10:
        print("Vous êtes enfant.")
    elif age > 18:
        print("Vous êtes majeur.")
    elif age == 18:
        print("Tout juste majeur, FELICITATION.")
    else:
        print("Vous êtes mineur.")


#DEMANDER LE NOM

nom1 = demander_nom()
nom2 = demander_nom()

# DEMANDER L'AGE

age1 = demander_age(nom1)
age2 = demander_age(nom2)

# Afficher les resultats

information1 = afficher_informations_personne(nom1, age1)
information2 = afficher_informations_personne(nom2, age2)






