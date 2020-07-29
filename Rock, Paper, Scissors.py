#Rock, Paper, Scissors By SOMMAYA HAQUE
import random

rss= 'Rock smashes scissors'
pwr= 'Paper wraps rock!'
scp= 'Scissors cut paper!'
playgame= 'Do you want to play again? '
    
play=input('Do you want to play rock, paper, scissors? ')
while play=='yes' or 'Yes':
    game= ['rock','paper','scissors']
    player= input('Choose rock, paper, scissors: ')
    computer= random.choice(game)
    if player==computer:
        print ("It's a tie!")
        play=input(playgame)
    if player=='rock' and computer=='paper':
        print(pwr,'Better luck next time!')
        play=input(playgame)
    elif player=='rock' and computer=='scissors':
        print(rss,'Good Job!')
        play=input(playgame)
    elif player=='paper' and computer=='rock':
        print(pwr,'Good job!')
        play=input(playgame)
    elif player=='paper' and computer=='scissors':
        print(scp,'Better luck next time!')
        play=input(playgame)
    elif player=='scissors' and computer=='paper':
        print(scp,'Good job')
        play=input(playgame)
    elif player=='scissors' and computer=='rock':
        print(rss,'Better luck next time!')
        play=input(playgame)

