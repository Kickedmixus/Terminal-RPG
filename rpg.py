from random import randint
from time import sleep
from colored import Fore, Back, Style

'''

-Enemy encounter

-Pick area

-Xp system

'''

class Entity:
    def __init__(self, lvl, name):
        self.lvl = lvl
        self.hp = randint(3,5)*lvl
        self.name = name

        self.attack = self.lvl * 2

    def stats(self):
        print (f"{Fore.red}HEALTH{Style.reset}", self.hp)
        print (f"{Fore.red}LEVEL{Style.reset}", self.lvl)
   

class Player(Entity):
    def __init___(self, lvl, name):
        Entity.__init__(self, lvl, name)
    
    def get_stats(self):
        print(f"{Fore.green}")
        print (f"NAME{Style.reset}", self.name)
        self.stats()
        print(f"{Style.reset}")

class Enemy(Entity):

    def __init__(self, lvl, name):
        Entity.__init__(self, lvl, name)
        self.enemy_class = None

    def get_stats(self):
        print(f"{Fore.red}")
        print (f"NAME{Style.reset}", self.name)
        self.stats()
        print(f"{Style.reset}")
        
    def set_enemy(self,lvl):
        classes = ["fire", "water", "wind", "earth", "arcane"]
        self.enemy_class = classes[randint(0, len(classes) -1 )]
        #index*5
        names = {
            "fire":["Ashes","Hot coals","Living Fire","Lava Slime"],

            "water":["Tadpole","Seaweed","Fish","Jellyfish","Shark"],

            "wind":["Fly","Breeze","Bird","Eagle","Cloud"],

            "earth":["Ant","Worm","Snake","Monkey","Tree"],

            "arcane":["Crystal","Magic Book","Strange artifact","Rune Tablet","Wizard"]
            }
        self.name = names[self.enemy_class][lvl-1]
        return self

        

def createEnemy(lvl):
    return Enemy(lvl,"").set_enemy(lvl)
   
        
def Mathcombat():
    if randint(0,1) == 1:
        a = randint(1,12)
        b = randint(1,12)
        answer = a * b

        print (f"{Fore.aquamarine_3}What is {Fore.rgb(245, 132, 255)}",a,"x",b,f"{Fore.aquamarine_3} ? {Style.reset}")
        print ("")
        user_answer = input(">?> ")
        print ("")
        if str(answer) == user_answer:
            print (f"\t{Fore.green}-=(Correct)=-{Style.reset}")
            print ("")
            return True
        else:
            print (f"\t{Fore.red}-=(Wrong)=-{Style.reset}")
            print ("")
            return False
    else:
        a = randint(1,100)
        b = randint(1,100)
        answer = a + b

        print (f"{Fore.aquamarine_3}What is {Fore.rgb(245, 132, 255)}",a,"+",b,f"{Fore.aquamarine_3} ? {Style.reset}")
        print ("")
        user_answer = input(">?> ")
        print ("")
        if str(answer) == user_answer:
            print (f"\t{Fore.green}-=(Correct)=-{Style.reset}")
            print ("")
            return True
        else:
            print (f"\t{Fore.red}-=(Wrong)=-{Style.reset}")
            print ("")
            return False
    

def enemyencounter(player):
    enemy = createEnemy(player.lvl)
    print ("")
    print (f"{Fore.yellow} (-=(ENEMY=ENCOUNTER)=-) {Style.reset}")
    enemy.get_stats()

    while enemy.hp > 0 and player.hp > 0:
        correct = Mathcombat()
        sleep(0.5)
        if correct:
            pass

user = Player(1,"player")


print (f'''
{Fore.rgb(243, 187, 243)}  ::::::::::: :::::::::: :::::::::     :::   :::   ::::::::::: ::::    :::     :::     :::           :::::::::  :::::::::   :::::::: 
{Fore.rgb(245, 132, 255)}     :+:     :+:        :+:    :+:   :+:+: :+:+:      :+:     :+:+:   :+:   :+: :+:   :+:           :+:    :+: :+:    :+: :+:    :+: 
{Fore.rgb(245, 132, 255)}    +:+     +:+        +:+    +:+  +:+ +:+:+ +:+     +:+     :+:+:+  +:+  +:+   +:+  +:+           +:+    +:+ +:+    +:+ +:+         
{Fore.medium_purple_3b}   +#+     +#++:++#   +#++:++#:   +#+  +:+  +#+     +#+     +#+ +:+ +#+ +#++:++#++: +#+           +#++:++#:  +#++:++#+  :#:          
{Fore.medium_purple_3b}  +#+     +#+        +#+    +#+  +#+       +#+     +#+     +#+  +#+#+# +#+     +#+ +#+           +#+    +#+ +#+        +#+   +#+#    
{Fore.purple_1a} #+#     #+#        #+#    #+#  #+#       #+#     #+#     #+#   #+#+# #+#     #+# #+#           #+#    #+# #+#        #+#    #+#     
{Fore.purple_1a}###     ########## ###    ###  ###       ### ########### ###    #### ###     ### ##########    ###    ### ###         ########

{Fore.rgb(245, 132, 255)}Made by MIXUS{Style.reset}

''')

while user.hp > 0:
    into = input(">>> ")
    if into == "stop":
        break
    elif into == "":
        chance = randint(1,100)
        if chance <= 33:
            enemyencounter(user)
    elif into == "stats":
        user.get_stats()
    elif into == "attack":
        Mathcombat()

print (f"""{Fore.dark_red_2}

 ██████╗  █████╗ ███╗   ███╗███████╗     ██████╗ ██╗   ██╗███████╗██████╗ 
██╔════╝ ██╔══██╗████╗ ████║██╔════╝    ██╔═══██╗██║   ██║██╔════╝██╔══██╗
██║  ███╗███████║██╔████╔██║█████╗      ██║   ██║██║   ██║█████╗  ██████╔╝
██║   ██║██╔══██║██║╚██╔╝██║██╔══╝      ██║   ██║╚██╗ ██╔╝██╔══╝  ██╔══██╗
╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗    ╚██████╔╝ ╚████╔╝ ███████╗██║  ██║
 ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝     ╚═════╝   ╚═══╝  ╚══════╝╚═╝  ╚═╝

{Style.reset}""")