'''
Created on Aug 31, 2017

@author: DeltaSierra4_
'''

import pygame
import random

class PokerCard:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
        if value >= 2 and value <= 7:
            self.up = False
        else:
            self.up = True
        
        if value == 1:
            self.name = "Ace of " + suit
        elif value == 11:
            self.name = "Jack of " + suit
        elif value == 12:
            self.name = "Queen of " + suit
        elif value == 13:
            self.name = "King of " + suit
        else:
            self.name = str(value) + " of " + suit
        
    suitList = ["clubs", "diamonds", "spades", "hearts"]
    
deckOfCards = []
for i in range(0,4):
    for j in range(1,14):
        deckOfCards.append(PokerCard(PokerCard.suitList[i],j))


shuffledDeckOfCards = []
for i in range(0,52):
    randomCard = deckOfCards[random.randint(0,len(deckOfCards)-1)]
    shuffledDeckOfCards.append(randomCard)
    deckOfCards.remove(randomCard)
    
#for i in range(0,len(shuffledDeckOfCards)):
#    print shuffledDeckOfCards[i].name

playerHand = []
computerHand = []
discards = []

for i in [0,1]:
    playerDraw = shuffledDeckOfCards[len(shuffledDeckOfCards)-1]
    computerDraw = shuffledDeckOfCards[len(shuffledDeckOfCards)-2]
    playerHand.append(playerDraw)
    computerHand.append(computerDraw)
    shuffledDeckOfCards.remove(playerDraw)
    shuffledDeckOfCards.remove(computerDraw)

totalData = [] #Just something I'm adding in for a machine learning project.

finished = False

while not finished:
    playerScore = 0
    computerScore = 0
    while len(shuffledDeckOfCards) > 12:
        playerUp = ""
        computerUp = ""
        
        if playerHand[0].up:
            playerUp += "up"
            if playerHand[1].up:
                playerUp += " and up"
            else:
                playerUp += " and down"
        else:
            playerUp += "down"
            if playerHand[1].up:
                playerUp += " and up"
            else:
                playerUp += " and down"
            
        if computerHand[0].up:
            computerUp += "up"
            if computerHand[1].up:
                computerUp += " and up"
            else:
                computerUp += " and down"
        else:
            computerUp += "down"
            if computerHand[1].up:
                computerUp += " and up"
            else:
                computerUp += " and down"
        
        print "Your cards up/down: " + playerUp
        print "Computer's cards up/down: " + computerUp
        
        print "Your choices are: 1)" + playerHand[0].name + ", 2) " + playerHand[1].name
        choiceNumber = raw_input("Type the number of choice you wish to play here.")
        while choiceNumber != "1" and choiceNumber != "2":
            print "You typed in an invalid choice." 
            print "Your choices are: 1)" + playerHand[0].name + ", 2) " + playerHand[1].name
            choiceNumber = raw_input("Type the number of choice you wish to play here.")
        playerChoice = None
        if choiceNumber == "1":
            playerChoice = playerHand[0]
        else:
            playerChoice = playerHand[1]
        print "Your choice: " + playerChoice.name 
        computerChoice = computerHand[random.randint(0,1)]
        print "Computer's choice: " + computerChoice.name
        
        playerWin = False
        computerWin = False
        
        if computerChoice.value == 1 and playerChoice.value != 2:
            print "Computer wins."
            computerScore += 1
            computerWin = True
        elif (playerChoice.value != 1 or playerChoice.value != 2) and playerChoice.value > computerChoice.value:
            print "You win."
            playerScore += 1
            playerWin = True
        elif playerChoice.value == 1 and computerChoice.value != 2:
            print "You win."
            playerScore += 1
            playerWin = True
        elif playerChoice.value == 2 and computerChoice.value == 1:
            print "You win."
            playerScore += 1
            playerWin = True
        elif playerChoice.value == computerChoice.value:
            print "It's a draw."
        else:
            print "Computer wins."
            computerScore += 1
            computerWin = True
        
        thisTurn = [len(shuffledDeckOfCards), playerUp, computerUp, playerHand[0].value, playerHand[1].value, computerHand[0].value, computerHand[1].value, playerChoice.value, computerChoice.value, playerWin, computerWin]
        totalData.append(thisTurn)
        
        playerHand.remove(playerChoice)
        computerHand.remove(computerChoice)
        playerDraw = shuffledDeckOfCards[len(shuffledDeckOfCards)-1]
        computerDraw = shuffledDeckOfCards[len(shuffledDeckOfCards)-2]
        playerHand.append(playerDraw)
        computerHand.append(computerDraw)
        shuffledDeckOfCards.remove(playerDraw)
        shuffledDeckOfCards.remove(computerDraw)
    
    print "total scores: Player: " + str(playerScore) + ", Computer: " + str(computerScore)
    if playerScore > computerScore:
        print "The player wins the game!"
    elif playerScore == computerScore:
        print "The game ends in a draw."
    else:
        print "The computer wins the game!"
    
    print "Would you like to play one more time?"
    checkFinish = raw_input("Type Y to play again, or N to quit.")
    while checkFinish.upper() != "Y" and checkFinish.upper() != "N" or not checkFinish.isalpha():
        print "That was an incorrect input"
        checkFinish = raw_input("Type Y to play again, or N to quit.")
    
    if checkFinish.upper() == "N":
        finished = True
        for item in totalData:
            print item