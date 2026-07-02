import random
class Player:
    def __init__(self):
        self.energy = 10
        self.money = 0
        self.billpaid = False
        self.worked = False
        self.action = 0
Player = Player()

def mainpage() -> None:
    print('You come to the town square')
    print(f'Current Stats:\nEnergy: {Player.energy}\n Money: {Player.money}')
    st_choice()


def st_choice() -> None:
    print("Choose action:\n1. Work as a barkeep [+5 coins -2 energy]\n2. Eat at the restaurant [+5 energy -2 coin]\n3. Pay today's inn bill [-2 coin]\n4.Sleep at the inn\n5. Pay off debt [100 coins]")
    Player.action = input('Enter chosen action number[1,2,3,4]: ')
    if(Player.action == '1'):
        work()
    elif(Player.action == '2'):
        eat()
    elif(Player.action == '3'):
        innbill()
    elif(Player.action == '4'):
        sleep()
    elif(Player.action == '5'):
        win_check()
    else:
        print('Invalid choice. Please choose again')
        st_choice()
def win_check() -> None:
    if(Player.money >= 100):
        print('Congrats! You won!\nPlay again?')
        game_over()
    else:
        print('Not enough money to pay the debt!')
        
def work() -> None:
    if(Player.energy < 2):
        print('Too low energy to work')
    else:
        if(Player.worked == False):
            print('You worked your shift at the bar\n+5 coin -2 energy')
            Player.money += 5
            Player.energy -= 2
            Player.worked = True
        
        else:
            print("You've already worked your shift today")

def eat() -> None:
    if(Player.money < 2):
        print('Too little money to eat')
    else:
        print('You ate your fill at the restaurant\n+5 energy -2 coin')
        Player.money -= 2
        Player.energy += 5
    

def innbill() -> None:
    if(Player.money < 2):
        print('Too little money to pay rent')
    else:
        print("You paid today's inn bill\n-2 coin")
        Player.money -= 2
        Player.billpaid = True
    

def sleep() -> None:
    if(Player.billpaid == True):
        print('You retired for the day')
        Player.worked = False
        Player.billpaid = False
        
    else:
        print('You forgot to pay the bill today and was kicked out of the inn\nGAME OVER\n Would you like to play again?')
        game_over()
        
def game_over() -> None:
    print('Choose action: \n1. Yes\n2. No')
    Player.action = input('Enter chosen action number[1,2]: ')
    if(Player.action == '1'):
        Player.energy = 10
        Player.money = 0
        Player.billpaid = False
        Player.worked = False
        Player.action = 0
        
    elif(Player.action == '2'):
        quit()
    else:
        print('Invalid choice. Please choose again')
        game_over()

while(1):
    mainpage()

