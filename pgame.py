import random
class Player:
    def __init__(self):
        self.energy = 10
        self.coin = 0
        self.billpaid = False
        self.worked = False
        self.day = 0
        self.sick = False
        self.eaten = False
        

player = Player()

def mainpage() -> None:
    print('You come to the town square')
    if(player.sick == False):
        print(f'Current Stats:\nEnergy: {player.energy}\nCoins: {player.coin}')
    elif(player.sick == True):
        print("You are sick. Visit the clinic to get cured")
        print(f'Current Stats:\nEnergy: {player.energy}\nCoins: {player.coin}')
    st_choice()


def st_choice() -> None:
    print("Choose action:\n1. Work a job\n2. Eat at the restaurant [+5 energy -? coin]\n3. Pay today's inn bill [-2 coin]\n4.Sleep at the inn\n5. Visit the clinic \n6. Buy the house! [100 coins]\n7. Save game\n8. Load game")
    action = input('Enter chosen action number[1,2,3,4,5,6,7,8]: ')
    if(action == '1'):
        job()
    elif(action == '2'):
        eat()
    elif(action == '3'):
        innbill()
    elif(action == '4'):
        sleep()
    elif(action == '5'):
        clinic()
    elif(action == '6'):
        win_check()
    elif(action == '7'):
        save()
    elif(action == '8'):
        load()
    else:
        print('Invalid choice. Please choose again')
        st_choice()
    print('--------------------------------------------------')

def clinic() -> None:
    if(player.sick == False):
        print("You are not sick, come back if you get sick")
    elif(player.sick == True):
        print("It seems you caught a cold. You will get better if you take some medicine")
        print("Will you buy medicine? [-2 coins]\n1.Yes\n2.No")
        action = input('Enter chosen action number[1,2]: ')
        if(action == '1'):
            if(player.coin < 2):
                print('Not enough coins')
            else:
                print("Your cold has been cured [-2 coins]")
                player.coin -= 2
                player.sick = False



def win_check() -> None:
    if(player.coin >= 100):
        print('Congrats! You won!')
        game_over()
    else:
        print('Not enough coins to pay the debt!')
    print('--------------------------------------------------')
        

def job() -> None:
    print('Where would you like to work?')
    print('1. Fish in the pond [+0-4 coin -1 energy]')
    print('2. Work as a barkeep [+5 coin -2 energy]')
    print('3. Work as a Labourer [+8 coin -5 energy]')
    print('4. Nevermind')
    action = input('Enter chosen action number[1,2,3,4]: ')
    if(action == '1'):
        fish()
    elif(action == '2'):
        bar()
    elif(action == '3'):
        Labour()
    elif(action not in ('1','2','3','4')):
        print('Invalid choice. Try again')
        job()

def fish() -> None:
    if(player.energy < 1):
        print('Too low energy to fish')
    else:
        if(player.worked == True):
            print("You've already worked today")
        else:
            player.worked = True
            player.energy -= 1
            fishcoin = random.randrange(0,5)
            if(fishcoin == 0):
                print("You couldn't catch any fish")
            else:
                print(f"You caught some fish. You made {fishcoin} coins! [+{fishcoin} coins]")
                player.coin += fishcoin
    print('--------------------------------------------------')

def Labour() -> None:
    if(player.energy < 5):
        print('Too low energy to work')
    else:
        if(player.worked == False):
            print('You worked as a labourer [+8 coins -5 energy]')
            player.coin += 8
            player.energy -= 5
            player.worked = True
        
        else:
            print("You've already worked today")
    print('--------------------------------------------------')

def bar() -> None:
    if(player.energy < 2):
        print('Too low energy to work')
    else:
        if(player.worked == False):
            print('You worked your shift at the bar [+5 coins -2 energy]')
            player.coin += 5
            player.energy -= 2
            player.worked = True
        
        else:
            print("You've already worked today")
    print('--------------------------------------------------')


def eat_check(cost:int) -> None:
    if player.eaten == True:
        print("You have already eaten today")
    else:
        if(player.coin < cost):
            print("Not enough coins")
        else:
            if(player.sick == False):
                print(f'You eat food [+5 energy -{cost} coin]')
                player.energy += 5
                player.coin -= cost
            elif(player.sick == True):
                print(f"You eat food but due to sickness you couldn't get as much energy [+3 energy -{cost} coin]")
                player.energy += 3
                player.coin -= cost


def eat() -> None:
    cost = random.randrange(0,4)
    match cost:
        case 0:
            print("Sorry, sold out today [You couldn't eat]")
        case 1:
            print("We got an overflow on food today! Cheap prices! Eat up! Only 1 coin a meal!")
            print('Eat food?\n1. Yes\n2. No')
            action = input('Enter chosen action number[1,2]: ')
            if(action == '1'):
                eat_check(1)
        case 2:
            print("We got some decent food today. Come eat. It'll cost you 2 coin a meal today")
            print('Eat food?\n1. Yes\n2. No')
            action = input('Enter chosen action number[1,2]: ')
            if(action == '1'):
                eat_check(2)
        case 3:
            print("We got a shortage of food today. You can eat but it'll cost you 3 coin a meal")
            print('Eat food?\n1. Yes\n2. No')
            action = input('Enter chosen action number[1,2]: ')
            if(action == '1'):
                eat_check(3)
    print('--------------------------------------------------')



def innbill() -> None:
    if(player.coin < 2 and player.billpaid != True):
        print('Too little coin to pay rent')
    else:
        print("You paid today's inn bill\n[-2 coin]")
        player.coin -= 2
        player.billpaid = True
    print('--------------------------------------------------')
    




def sleep() -> None:
    if(player.billpaid == False):
        print('You forgot to pay the bill today and was kicked out of the inn\nGAME OVER')
        game_over()

    else:
        print('You retired for the day')
        event = random.randrange(1,101)
        if(1 <= event <= 50):
            print('Nothing Happened')
        elif(51 <= event <= 55):
            print('You caught a cold! [You are now sick]')
            player.sick = True
        elif(56 <= event <= 60):
            print('You found a dropped pouch of coins on your way home! [+5 coins]')
            player.coin += 5
        elif(61 <= event <= 80):
            print('A thief robbed you of some coins! [-3 coins]')
            if(player.coin >= 3):
                player.coin -= 3
            else:
                player.coin = 0
        elif(81 <= event <= 90):
            print('You found some coins on your way home! [+2 coins]')
            player.coin += 2
        elif(91 <= event <= 100):
            print("You couldn't sleep well tonight [-3 energy]")
            player.energy -= 3
        player.worked = False
        player.billpaid = False
    print('--------------------------------------------------')
    player.day += 1
    print(f'Day:{player.day}')




def game_over() -> None:
    print('Would you like to play again?')
    print('Choose action: \n1. Yes\n2. No')
    action = input('Enter chosen action number[1,2]: ')
    if(action == '1'):
        player.energy = 10
        player.coin = 0
        player.billpaid = False
        player.worked = False
        player.day = 0
        player.sick = False
        player.eaten = False
        
    elif(player.action == '2'):
        quit()
    else:
        print('Invalid choice. Please choose again')
        game_over()
    print('--------------------------------------------------')



def save() -> None:
    with open("savefile.txt", "wt") as file:
        file.write(f"{player.energy},{player.coin},{player.billpaid},{player.worked},{player.day},{player.sick},{player.eaten}")
    print("Your game has been saved")
    print('--------------------------------------------------------------------------')

def load() -> None:
    try:
        with open("savefile.txt") as file:
            for line in file:
                line = line.strip()
                fields = line.split(",")
            
            player.energy = int(fields[0])
            player.coin = int(fields[1])
            player.billpaid = (fields[2] == "True")
            player.worked = (fields[3] == "True")
            player.day = int(fields[4])
            player.sick = (fields[5] == "True")
            player.eaten = (fields[6] == "True")
        print("Your game has been loaded")
        print(f"Day:{player.day}")
    except FileNotFoundError:
        print("No save file found")
    print('--------------------------------------------------------------------------')






print('--------------------------------------------------------------------------')
print("You're a young man who have just come to the big city from the countryside who wish to make settle in the city and make a place for yourself. Will you be able to scrounge up enough money to buy yourself a home and take the first step?")
print('--------------------------------------------------------------------------')
while(1):
    mainpage()
    if(player.energy <= 0):
        print("You ran out of energy and collapsed from overexhaustion\nGAME OVER")
        game_over()


