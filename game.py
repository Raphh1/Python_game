name = input("Entre ton nom mec : ")
print(f"Bienvenue {name} dans cette grande aventure !")

start = input("veux tu commencer a jouer ou preferes tu ne rien faire ? ")
if start == 'jouer':
    print("tres bon choix, maintenant tu dois choisir ta classe")

else:
    print("dommage, bon courage pour la suite peut-etre a la prochaine")

classe = input("tu dois donc  choisir entre trois classes :\n"
               "Berserker\n"
               "Mage\n"
               "Archer\n"    )

if classe == 'Berserker':
    pv = 300
    superattack = 50
    Buff = 50
    Speed = 50
    print("Tu as choisis la classe des combattants, tu vas donc aller t'attaquer a tes adversaires au corps a corps tel un vrai guerrier")

if classe == 'Mage':
    pv = 175
    superattack = 100
    Heal = 25
    Speed = 25
    print("Tu as la fibre de la magie, tu vas te battre a distance et aider pouvoir lancer des attaques puissantes, tres bon choix")

if classe == 'Archer':
    pv = 225
    superattack = 70
    attackBuff = 30
    Speed = 80
    print("Tu as choisis l'archer, un bon compromis entre le guerrier et le mage, une agilité hors du commun et un combat a distance constant")

else:
    print("cette classe n'existe pas")


Direction = input("Tu as choisi ta classe alors ! Maintenant tu dois commencer ton aventure, tu apparais dans une taverne dans le village principal prénommé Sasososisasosasaucisse\n"
                  "Tu souhaites aller ou ? Dans le centre ville ou au port ? ")

if Direction == 'centre ville':
    print("Tu es dans le centre ville, les gens vous regardent de travers, comme si vous aviez quelque chose sur la tronche\n")
    combat = input("vous vous rendez juste compte qu'ils ont besoins d'aide, vous croisez le chemin d'un voleur armé d'une dague, combattre ou fuir ? ")  

    if combat == 'combattre':
        print("Le voleur a l'air menaçant, il a une dague tranchante, vous lancez une attaque")
    voleur = 70
    if classe == 'Berserker':
         while voleur > 0:
            damage = superattack
            voleur -= damage
            if voleur < 0:
                 voleur = 0
            if voleur == 0:
                print("Tu as reussi a le detruire avec ta mega épée de la mort qui tue, bien joué !")
            print(f"Le voleur a maintenant {voleur} points de vie.")
            if voleur > 0:
                print("Le voleur contre-attaque !")
                berserker_hp = pv
                berserker_hp -= 20
                print(f"Le voleur t'inflige 20 points de dégâts. Il te reste {berserker_hp} points de vie.")
        
    
    if classe == 'Mage':
        damage = superattack
        voleur -= damage
        if voleur < 0:
            voleur = 0
        print(f"Le voleur a maintenant {voleur} points de vie. Vous l'avez absolument atomisé avec votre magie.")

    if classe == 'Archer':
        damage = superattack
        voleur -= damage
        if voleur < 0:
            voleur = 0
        print(f"Le voleur a {voleur} points de vies, une flèche bien placé, c'etait terminé d'avance")
    
    Direction = input("Le voleur a été tué, tu sors donc de la ville après avoir traversé un peu la ville, tu peux aller vers la foret ou le desert")

    if Direction == 'foret':
        print("tu te retrouves dans la foret proche de la ville, tu croises un renard qui peut parler")
        Direction = input("il te propose de le suivre dans sa grotte, y aller ou continuer ? ")

    if Direction == 'y aller':
        print("le renard veut t'offrir un cadeau, il te donne un item et cet item est une rune de combat")

if Direction == 'port':
    print("le port est en pleine activité, un marin vous propose de prendre la mer direction le desert")
    Direction = input("Vers le desert ou rester ? ")
else: 
    print("cette direction est impossible")

if Direction == 'desert':
    if classe == 'Berserker':
        Slow = 15
        Speed -= Slow
        print(f"Vous arrivez dans le desert, il fait chaud, c'est fatiguant, vous avez donc {Speed} de vitesse")

    if classe == 'Mage':
        Slow = 15
        Speed -= Slow
        print(f"Vous arrivez dans le desert, il fait chaud, c'est fatiguant, vous avez donc {Speed} de vitesse")

    if classe == 'Archer':
        Slow = 15
        Speed -= Slow
        print(f"Vous arrivez dans le desert, il fait chaud, c'est fatiguant, vous avez donc {Speed} de vitesse")

    combat = input("Tu tombes sur un mega lezard du desert enflammé de la mort qui tue bien dangereux, combattre ou fuir ? ")

    if combat == 'fuir':
        print("Tu as choisi de fuir le combat. L'aventure continue.")

    if combat == 'combattre':
        print("La salamandre a l'air menaçante, elle a 1000 points de vie, vous lancez une attaque")
        salamandre = 1000
        berserker_hp = pv  
        while salamandre > 0 and berserker_hp > 0:
            damage = superattack
            salamandre -= damage
            print(f"La salamandre a maintenant {salamandre} points de vie.")
            if salamandre > 0:
                print("La salamandre contre-attaque et ça va piquer")
                berserker_hp -= 250
                if berserker_hp <= 0:
                    print("Vous êtes mort, c'est terminé")
                    exit  
                else:
                    print(f"La salamandre t'inflige 250 points de dégâts. Il te reste {berserker_hp} points de vie.")
                    combat = input("Que souhaites-tu faire maintenant ? Fuir ou continuer? ")
                    if combat == 'continuer':
                        continue
                    elif combat == 'Fuir':
                        print(f"Tu prends la fuite, la salamandre ne te suit pas, tu t'en sors avec {berserker_hp} points de vie.")
                        break
        if salamandre <= 0:
            print("Félicitations ! Tu as vaincu la salamandre. L'aventure continue.")



    print("après avoir fuis la salamandre tu avances dans le desert et tombes sur un village, tu y vas")
    Direction = input("tu n'as pas l'air le bienvenu dans ce village, certains habitants se cachent de toi, un garde brandit sa lance et provoque en combat")
    combat = input("combattre ou discuter ? ")

    if combat == 'combattre':
        garde = 150
        berserker_hp = pv
        while garde > 0:
            damage = superattack
            garde -= superattack
            print(f"le garde a maintenant {garde} points de vies")
            if garde > 0:
                print("le garde va contre attaquer")
                berserker_hp -= 80
                if berserker_hp <= 0:
                    print("vous etes dead")
                if garde <= 0:
                    print("tu as gagné le combat comme un chef")
                else:
                    print(f"le garde t'inflige 80 points de degats, il te reste {berserker_hp} points de vies")
               
        
    print("tu as battu le garde, tu vas donc partir du village en quete d'un nouvel endroit et tu tombes sur un voleur des sables")
    combat = input("Te battre ou fuir ")

    if combat == 'battre':
        Buff = 50
        voleursable = 250
        berserker_hp = pv 
        combat = input("ce voleur est fort mais il peut etre battu si tu utilise ton buff, utiliser ou pas utiliser ? ")
        if combat == 'utiliser':
            if classe == 'Berserker':
                berserker_hp = pv + Buff 
                damage = superattack
            if classe == 'Archer':
                damage = superattack + attackBuff
            while voleursable > 0:
                voleursable -= damage
                print(f"le garde a maintenant {voleursable} points de vies")
                if voleursable > 0:
                    print("le voleur des sables contre attaque")
                    berserker_hp -= 95
                    if berserker_hp <= 0:
                        print("vous etes mort")
                    else:
                        print(f"le voleur des sables t'inflige 57 points de degats, il te reste {berserker_hp} points de vies")
        if combat == 'pas utiliser':
            while voleursable > 0:
                damage = superattack
                voleursable -= damage
                print(f"le garde a maintenant {voleursable} points de vies")
                if voleursable > 0:
                    print("le voleur des sables contre attaque")
                    berserker_hp -= 95
                    if berserker_hp <= 0:
                        print("vous etes mort")
                    else:
                        print(f"le voleur des sables t'inflige 57 points de degats, il te reste {berserker_hp} points de vies")
    


    else:
        if combat == 'fuir':
            print("Tu prend la fuite, le voleur des sables se cachent dans les dunes attendant une nouvelle proie")








