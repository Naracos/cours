print("Enzo")



def main1():
    def main2():
        y = int(input("Donner une valeur entière comprise entre 3 et 9: "))

        if 2<y<10:
            print("La valeur {} à bien était enregistrer".format(y))
            print("La valeur première valeur({0}) multiplié par la deuxième({1}) donne = {2}".format(x, y, x*y))
            print("La valeur première valeur({0}) à la puissance de la deuxième({1}) donne = {2}".format(x, y, x**y))
            
            
        if y<3:
            print("La valeur est inférieur à 3")
            main2()
        if y>9:
            print("La valeur est supérieur à 9")
            main2()
        else:
            print("-----------Valeur réinitialisé-----------")
            main1()
        
    x = int(input("Donner une valeur entière comprise entre 10 et 20 : "))

    if 9<x<21:
        print("La valeur {} à bien était enregistrer".format(x))
        return x, main2()

    if x<10:
        print("La valeur est inférieur à 10")
        main1()

    if 20<x:
        print("La valeur est supérieur à 20")
        main1()
    else:
        print("Vous n'avez rentrée aucune valeurs")
        main1()
        
if __name__ =='__main__':
    main1()
