import random
import sys
def getUserInput():
    userInput = input('chose Rock Paper or Scissors:')
    if userInput in ['Rock','rock','r','R','ROCK']:
        userInput = 'rock'
    if userInput in ['Paper','paper','p','P','PAPER']:
        userInput = 'paper'
    if userInput in ['Scissors','scissors','s','S','SCISSORS']:
        userInput = 'scissors'
    return (userInput)
def getSystemInput():
    systemInput = random.randint(1,3)
    if(systemInput == 1):
        return 'rock'
    elif(systemInput == 2):
        return 'paper'
    else:
        return 'scissors'
userScore = 0
systemScore = 0  
while(1):
    userInput = getUserInput()
    print('Your Choice:',userInput)
    systemInput = getSystemInput()
    print('Computer Choice:',systemInput)
    u = userInput
    s = systemInput
    if(u == s):
        print('It is a tie')
    elif((u =='rock' and s == 'scissors') or (u =='paper' and s == 'rock') 
       or (u =='scissors' and s == 'paper')):
       print('You beat computer')
       userScore+=1
    else:
        print('Computer beat you')
        systemScore+=1
    print('Your Score:',userScore)
    print('Computer Score:',systemScore)
    print('-----------------------')
    print('-----------------------')
    if(userScore == 3):
        print('-----------------------')
        print('******You Won!!!!******')
        print('-----------------------')
        print('-----------------------')
        print('-----------------------')
        choice = input('Do you want to continue y/n:')
        userScore = 0
        systemScore = 0  

        if choice in ['n','N','no','No','NO']:
            sys.exit()
    if(systemScore == 3):
        print('-----------------------')
        print('******You Lose!!!!******')
        print('-----------------------')
        print('-----------------------')
        print('-----------------------')
        choice = input('Do you want to continue y/n:')
        userScore = 0
        systemScore = 0  

        if choice in ['n','N','no','No','NO']:
            sys.exit()
        
    
