# libraries
from random import randint
from time import sleep
from colored import Fore, Back, Style

# modules
from names import *

class Entity:
    def __init__(self, lvl, name):
        self.lvl = lvl
        self.hp = randint(3,5)*lvl
        self.name = name

        self.attack = self.lvl * 2

    def stats(self):
        print (f"{Fore.yellow_1}᪣ LEVEL{Style.reset}", self.lvl)
        print (f"{Fore.red}♥ HEALTH{Style.reset}", self.hp)
   
class Player(Entity):
    def __init__(self, lvl, name, maxhp):
        Entity.__init__(self, lvl, name)
        self.maxhp = 5
        self.hp = self.maxhp
        self.dg = 2

    def get_stats(self):
        print(f"{Fore.green}")
        print (f"NAME{Style.reset}", self.name)
        self.stats()
        print (f"{Fore.red}⚔ DAMAGE{Style.reset}", self.dg)
        print(f"{Style.reset}")

coins = (0)

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
        self.name = enemyname[self.enemy_class][lvl-1]
        return self

'''
[Option 1]={SHOP}========[Apple [4 coins] +10 health]
[Option 2]     ('-')     [Apple [4 coins] +10 health]
[option 3]===============[Apple [4 coins] +10 health]

(Leave)
'''

class Shop:

    def __init__(self):
        self.name = list(tradername.keys())[randint(0,len(tradername)-1)]
        self.lvl = user.lvl

        print ("")
        print (f"{Fore.medium_orchid}Hello my name is {self.name} {Fore.aquamarine_3}{tradername[self.name][randint(0, 2)]}")
        print (f"{Fore.grey_42}answer (trade) if you want to trade{Style.reset}")
        print ("")

        into = input(">?>")

        if into == "trade":
            self.trade(user.lvl)
    
    def createStock(self, lvl):
        stocklvl = randint(1,3)*lvl
        if randint(0,1) == 0:
            stock = [stocklvl,"♥ Health",tradeshealth[randint(0,len(tradeshealth)-1)]]
        else:
            stock = [stocklvl,"⚔ Damage",tradesdamage[randint(0,len(tradesdamage)-1)]]
        return stock

    def trade(self, traderlvl):
        stock1 = self.createStock(traderlvl)
        stock2 = self.createStock(traderlvl)
        stock3 = self.createStock(traderlvl)

        print ("")
        print (f"[Option 1 ꥟ ]=(SHOP)========{Style.reset}[ {Fore.aquamarine_3}{stock1[2]}{Style.reset} [{Fore.yellow_1} {stock1[0]*5} ⛃ Coins {Style.reset}] {Fore.red}+{stock1[0]} {stock1[1]}{Style.reset}")
        print (f"[Option 2 ꥟ ]     ('-')     [{Style.reset} {Fore.aquamarine_3}{stock2[2]}{Style.reset} [{Fore.yellow_1} {stock2[0]*5} ⛃ Coins {Style.reset}] {Fore.red}+{stock2[0]} {stock2[1]}{Style.reset}")
        print (f"[Option 3 ꥟ ]==============={Style.reset}[ {Fore.aquamarine_3}{stock3[2]}{Style.reset} [{Fore.yellow_1} {stock3[0]*5} ⛃ Coins {Style.reset}] {Fore.red}+{stock3[0]} {stock3[1]}{Style.reset}")
        print("")

        print (f"{Fore.grey_42}to buy an item answer the option, example (1){Style.reset}")
        print("")

        into = input(">?>")


def createEnemy(lvl):
    return Enemy(lvl,"").set_enemy(lvl)

def createXpLimit(lvl):
    return (lvl * 50) + ((lvl * lvl) / 5) - 0.5
        
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
            print (f"\t{Fore.green}-=𑗕(Correct)𑗕=-{Style.reset}")
            print ("")
            return True
        else:
            print (f"\t{Fore.red}-=𑗕(Wrong)𑗕=-{Style.reset}")
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
            print (f"\t{Fore.green}-=𑗕(Correct)𑗕=-{Style.reset}")
            print ("")
            return True
        else:
            print (f"\t{Fore.red}-=𑗕(!Wrong!)𑗕=-{Style.reset}")
            print ("")
            return False

def bar(type,max,current,power):
    if type == "lvl":
        bar = ("")
        for i in range(20):
            if current > max/20 * i:
                bar += "#"
            else:
                bar += f"{Fore.grey_42}="
        print (f'{Fore.yellow_1}Lvl {power}᪣{Style.reset} <({Fore.spring_green_1}{bar}{Style.reset})> {Fore.yellow_1}Lvl {power+1}᪣{Style.reset}')
    elif type == "money":
        current = current - moneystatus[moneystatus.index(power)][0]
        max = moneystatus[moneystatus.index(power)][1] - moneystatus[moneystatus.index(power)][0]
        bar = ("")
        for i in range(10):
            if current > max/10 * i:
                bar += "🞛"
            else:
                bar += f"{Fore.grey_42}🞚"
        print (f'{Fore.yellow_1}{power} {moneystatus[moneystatus.index(power)][0]} <({Fore.yellow_1}{bar})> {Fore.yellow_1}{moneystatus[moneystatus.index(power)][1]} {moneystatus[moneystatus.index(power)+1]}')
    else:
        print ("🮕ERROR🮕 (bar index not found)")

def enemyencounter(player):
    global xp
    global maxxp
    global coins

    enemy = createEnemy(player.lvl)
    print ("")
    print (f"{Fore.medium_orchid}-=(ENEMY=ENCOUNTER)=-) {Style.reset}")
    enemy.get_stats()

    while enemy.hp > 0 and player.hp > 0:
        correct = Mathcombat()
        sleep(0.5)
        if correct:
            enemy.hp -= player.dg
            print ("")
            if enemy.hp >= 1:
                print (f'{Fore.medium_orchid}You damaged {Fore.red}{enemy.name}{Fore.medium_orchid} for {Fore.yellow_1}{player.dg} Damage{Fore.medium_orchid}, leaving {Fore.red}{enemy.name}{Fore.medium_orchid} at {Fore.red}{enemy.hp} Health{Style.reset}')
            else:
                xpgain = (enemy.lvl * 5) + (randint(0,5) / 2)
                print (f'{Fore.medium_orchid}You killed {Fore.red}{enemy.name}{Fore.medium_orchid} and gained {Fore.yellow_1}+{xpgain} ✨ XP{Fore.medium_orchid} and {Fore.yellow_1}+{2*enemy.lvl} ⛃ Coins{Style.reset}')
                print (f"{Fore.grey_42}to check your wallet use the (wallet) command{Style.reset}")
                xp += xpgain
                coins += (2*enemy.lvl)
                if xp >= maxxp:
                    player.lvl += 1
                    print ("")
                    print ("-=(᪣LEVEL UP᪣)=-")
                    print ("⚔ Damage + 2")
                    print ("♥ Health + 2")
                    print ("-=(᪣LEVEL UP᪣)=-")
                    print (f"{Fore.grey_42}to check your stats use the (stats) command{Style.reset}")
                    maxxp = createXpLimit(player.lvl)
                    player.dg += 2
                else:
                    print ("")
                    bar("lvl", maxxp, xp, player.lvl)
                    print (f"{Fore.medium_orchid}you need {Fore.yellow_1}{maxxp - xp}✨ XP{Fore.medium_orchid} more to level up{Style.reset}")
                    print ("")
                user.maxhp = 3 + (player.lvl * 2)
                user.hp = user.maxhp
        else:
            player.hp -= enemy.lvl * 2
            print ("")
            if player.hp >= 1:
                print (f'{Fore.medium_orchid}You have been damaged by {Fore.red}{enemy.name}{Fore.medium_orchid} for {Fore.yellow_1}{enemy.lvl * 2} Damage{Fore.medium_orchid}, leaving {Fore.green}Yourself{Fore.medium_orchid} at {Fore.red}{player.hp} Health{Style.reset}')
                print ("")
            else:
                print (f'{Fore.red}☠You were killed by {Fore.red}{enemy.name}☠{Style.reset}')

user = Player(1,"player",5)

def wallet(coins):
    print("")
    print (f'{Fore.medium_orchid}You have {Fore.yellow_1}{coins} ⛃ Coins{Style.reset}')
    print("")

xp = 0
maxxp = createXpLimit(user.lvl)

print (f'''
{Fore.rgb(243, 187, 243)}  ::::::::::: :::::::::: :::::::::     :::   :::   ::::::::::: ::::    :::     :::     :::           :::::::::  :::::::::   :::::::: 
{Fore.rgb(245, 132, 255)}     :+:     :+:        :+:    :+:   :+:+: :+:+:      :+:     :+:+:   :+:   :+: :+:   :+:           :+:    :+: :+:    :+: :+:    :+: 
{Fore.rgb(245, 132, 255)}    +:+     +:+        +:+    +:+  +:+ +:+:+ +:+     +:+     :+:+:+  +:+  +:+   +:+  +:+           +:+    +:+ +:+    +:+ +:+         
{Fore.medium_purple_3b}   +#+     +#++:++#   +#++:++#:   +#+  +:+  +#+     +#+     +#+ +:+ +#+ +#++:++#++: +#+           +#++:++#:  +#++:++#+  :#:          
{Fore.medium_purple_3b}  +#+     +#+        +#+    +#+  +#+       +#+     +#+     +#+  +#+#+# +#+     +#+ +#+           +#+    +#+ +#+        +#+   +#+#    
{Fore.purple_1a} #+#     #+#        #+#    #+#  #+#       #+#     #+#     #+#   #+#+# #+#     #+# #+#           #+#    #+# #+#        #+#    #+#     
{Fore.purple_1a}###     ########## ###    ###  ###       ### ########### ###    #### ###     ### ##########    ###    ### ###         ########

{Fore.rgb(245, 132, 255)}Made by MIXUS (1.0.7){Style.reset}
{Fore.grey_42}tips are in grey, press enter until a enemy attacks{Style.reset}
''')

#gameloop

while user.hp > 0:
    bar("money",None,2,"Broke")

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
    elif into == "wallet":
        wallet(coins)

    #CHEATS (u think ur so cool finding these codes ,Mr. ultimate haxxor)
    
    elif into == "madewithrealcheese":
        print ("")
        print (f"{Fore.dark_red_2}(☠(☠(ULTIMATE HAXXOR MODE ENABLED)☠)☠){Style.reset}")
        print ("")
        into = input(">INPUTCHEAT>")
        if into == "cheatxp":
            xpgain = (100) + (randint(0,5) / 2)
            xp += xpgain
            if xp >= maxxp:
                user.lvl += 1
                print ("")
                print (f"{Fore.yellow_1}-=(᪣LEVEL UP᪣)=-")
                print (f"{Fore.red}⚔ Damage + 2")
                print (f"{Fore.red}♥ Health + 2")
                print (f'{Fore.yellow_1}-=(᪣LEVEL UP᪣)=-{Style.reset}')
                print (f"{Fore.grey_42}to check your stats use the (stats) command{Style.reset}")
                print ("")
                maxxp = createXpLimit(user.lvl)
            else:
                print ("")
                bar("lvl", maxxp, xp, user.lvl)
                print ("")
            user.maxhp = 3 + (user.lvl * 2)
            user.hp = user.maxhp
        elif into == "cheatshop":
            Shop()
        elif into == "cheatcoin":
            coins = 999999999
            print (f"{Fore.yellow_1} +999999999 ⛃ Coins{Style.reset}")
        print ("")
if user.hp <= 0:
    print (f"""{Fore.dark_red_2}
     ██████╗  █████╗ ███╗   ███╗███████╗     ██████╗ ██╗   ██╗███████╗██████╗ 
    ██╔════╝ ██╔══██╗████╗ ████║██╔════╝    ██╔═══██╗██║   ██║██╔════╝██╔══██╗
    ██║  ███╗███████║██╔████╔██║█████╗      ██║   ██║██║   ██║█████╗  ██████╔╝
    ██║   ██║██╔══██║██║╚██╔╝██║██╔══╝      ██║   ██║╚██╗ ██╔╝██╔══╝  ██╔══██╗
    ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗    ╚██████╔╝ ╚████╔╝ ███████╗██║  ██║
     ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝     ╚═════╝   ╚═══╝  ╚══════╝╚═╝  ╚═╝

    {Style.reset}""")
else:
    print ("🮕ERROR🮕 (non death gameloop breakage)")