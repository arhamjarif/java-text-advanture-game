energy = 10
money = 0
billpaid = False
worked = False
action = 0


def mainpage() -> None:
    global energy,money
    print('You come to the town square')
    print(f'Current Stats:\nEnergy: {energy}\n Money: {money}')
    st_choice()


def st_choice() -> None:
    print("Choose action:\n1. Work as a barkeep [+5 coins -2 energy]\n2. Eat at the restaurant [+5 energy -2 coin]\n3. Pay today's inn bill [-2 coin]\n4.Sleep at the inn\n5. Pay off debt [100 coins]")
    action = input('Enter chosen action number[1,2,3,4]: ')
    if(action == '1'):
        work()
    elif(action == '2'):
        eat()
    elif(action == '3'):
        innbill()
    elif(action == '4'):
        sleep()
    elif(action == '5'):
        win_check()
    else:
        print('Invalid choice. Please choose again')
        st_choice()
def win_check() -> None:
    if(money >= 100)
        print('Congrats! You won!\nPlay again?')
        game_over()
    else:
        print('Not enough money to pay the debt!')
        
def work() -> None:
    global money,energy,worked
    if(energy < 2):
        print('Too low energy to work')
    else:
        if(worked == False):
            print('You worked your shift at the bar\n+5 coin -2 energy')
            money += 5
            energy -= 2
            worked = True
        
        else:
            print("You've already worked your shift today")

def eat() -> None:
    global money,energy
    if(money < 2):
        print('Too little money to eat')
    else:
        print('You ate your fill at the restaurant\n+5 energy -2 coin')
        money -= 2
        energy += 5
    

def innbill() -> None:
    global money,billpaid
    if(money < 2):
        print('Too little money to pay rent')
    else:
        print("You paid today's inn bill\n-2 coin")
        money -= 2
        billpaid = True
    

def sleep() -> None:
    global billpaid,worked
    if(billpaid == True):
        print('You retired for the day')
        worked = False
        billpaid = False
        
    else:
        print('You forgot to pay the bill today and was kicked out of the inn\nGAME OVER\n Would you like to play again?')
        game_over()
        
def game_over() -> None:
    global energy,money,billpaid,worked,action
    print('Choose action: \n1. Yes\n2. No')
    action = input('Enter chosen action number[1,2]: ')
    if(action == '1'):
        energy = 10
        money = 0
        billpaid = False
        worked = False
        action = 0
        
    elif(action == '2'):
        quit()
    else:
        print('Invalid choice. Please choose again')
        game_over()

while(1):
    mainpage()

