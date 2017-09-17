import pygame

'''
Created on Jul 28, 2017

@author: DeltaSierra4_
'''

class QueenCoord:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def checkAnswer(qcount): #Checks if your answer is correct. qcount is the number of queen pieces left.
    if qcount == 0: #This function will only work if all queen pieces have been used.
        for i in range(0,8):
            for j in range(i+1,8):
                if queenObject[i].x == queenObject[j].x or queenObject[i].y == queenObject[j].y:
                    #Checks if two queen pieces have matching x or y coordinates. If they do, then they can attack each other; therefore, the game will indicate that it's not the correct setup.
                    screen.blit(lostTheGame,(410,250))
                    screen.blit(lostTheGame2,(410,255 + lostTheGame.get_height()))
                    screen.blit(lostTheGame3,(410,260 + lostTheGame.get_height()*2))
                    screen.blit(resetGame,(410,265 + lostTheGame.get_height()*3))
                    pressedKeys2 = pygame.key.get_pressed()
                    return False
                    #Blit fail message and reset.
                elif abs(queenObject[i].x - queenObject[j].x) == abs(queenObject[i].y - queenObject[j].y): #If the queen pieces are on the same diagonal line, they can still attack each other.
                    #Two pieces will be on the same diagonal line if their delta x and delta y have equal absolute values.
                    screen.blit(lostTheGame,(410,250))
                    screen.blit(lostTheGame2,(410,255 + lostTheGame.get_height()))
                    screen.blit(lostTheGame3,(410,260 + lostTheGame.get_height()*2))
                    screen.blit(resetGame,(410,265 + lostTheGame.get_height()*3))
                    pressedKeys2 = pygame.key.get_pressed()
                    return False
        #The current board has no pieces sharing same x or y coordinates or on the same diagonal line. You pass the test.
        return True

pygame.init()

screen = pygame.display.set_mode((600,480))

queenPiece = pygame.image.load("chessQueenIcon.png")  
queenPiece = queenPiece.convert_alpha() 
#Image credits to wikimedia commons (URL: https://commons.wikimedia.org/wiki/File:Chess_queen_icon.png)

backgroundImage = pygame.image.load("chessboard.png")
backgroundImage = pygame.transform.scale(backgroundImage,(600,400))
screen.blit(backgroundImage,(0,0))

boardCursor = pygame.image.load("cursor.png") 
boardCursor = pygame.transform.scale(boardCursor,(50,50)) 
boardCursor = boardCursor.convert_alpha() 

clearGrey = pygame.image.load("greySquare.png")
clearGrey = clearGrey.convert_alpha()
clearWhite = pygame.image.load("whiteSquare.png")
clearWhite = clearWhite.convert_alpha()

font = pygame.font.SysFont("Arial", 36)
promptFont = pygame.font.SysFont("Arial", 20)
winLoseFont = pygame.font.SysFont("Arial", 28)
frame = pygame.time.Clock()

queenCounter = 8

promptQuiz = promptFont.render("Place eight different queen pieces so that they cannot attack one another.", False,(255,255,255))
escapeReminder = promptFont.render("Press ESC to leave the game, or press Space to reset.", False, (128,0,255))
lostTheGame = winLoseFont.render("I'm sorry, that", False, (255,0,0))
lostTheGame2 = winLoseFont.render("is not the", False, (255,0,0))
lostTheGame3 = winLoseFont.render("correct setup", False, (255,0,0))
wonTheGame = winLoseFont.render("Congratulations!", False, (128,255,0))
wonTheGame2 = winLoseFont.render("That is the", False, (128,255,0))
wonTheGame3 = winLoseFont.render("correct setup.", False, (128,255,0))
resetGame = winLoseFont.render("Press Space to retry.", False, (0,0,0))

screen.blit(backgroundImage,(0,0))

boardState = [[False, False, False, False, False, False, False, False],[False, False, False, False, False, False, False, False],[False, False, False, False, False, False, False, False],[False, False, False, False, False, False, False, False],[False, False, False, False, False, False, False, False],[False, False, False, False, False, False, False, False],[False, False, False, False, False, False, False, False],[False, False, False, False, False, False, False, False]]
#2d Array of booleans indicating whether a board is occupied by a queen piece or not.
queenObject = []
#Currently empty array of queen objects that will be filled when a queen is placed.
solutions = []
#Currently empty array of all solutions found by player.
#There are 92 total solutions to the queens problem. Find them all to unlock a special code!

finished = False
while not finished:
    for event in pygame.event.get(): #pygame.event is a sub-library containing all 'event' objects in pygame.
        if event.type == pygame.QUIT:
            #events have 'type' attributes. Yes, events are objects after all.
            #QUIT is a predefined object. -pygame doc
            finished = True     

    
    pressedKeys = pygame.key.get_pressed()
    if pressedKeys[pygame.K_ESCAPE]:
        finished = True
    elif pressedKeys[pygame.K_SPACE]:
        pygame.init()

        screen = pygame.display.set_mode((600,480))
        
        queenPiece = pygame.image.load("chessQueenIcon.png")  
        queenPiece = queenPiece.convert_alpha() 
        #Image credits to wikimedia commons (URL: https://commons.wikimedia.org/wiki/File:Chess_queen_icon.png)
        
        backgroundImage = pygame.image.load("chessboard.png")
        backgroundImage = pygame.transform.scale(backgroundImage,(600,400))
        screen.blit(backgroundImage,(0,0))
        
        boardCursor = pygame.image.load("cursor.png") 
        boardCursor = pygame.transform.scale(boardCursor,(50,50)) 
        boardCursor = boardCursor.convert_alpha() 
        
        clearGrey = pygame.image.load("greySquare.png")
        clearGrey = clearGrey.convert_alpha()
        clearWhite = pygame.image.load("whiteSquare.png")
        clearWhite = clearWhite.convert_alpha()
        
        font = pygame.font.SysFont("Arial", 36)
        promptFont = pygame.font.SysFont("Arial", 20)
        winLoseFont = pygame.font.SysFont("Arial", 28)
        frame = pygame.time.Clock()
        
        queenCounter = 8
        
        promptQuiz = promptFont.render("Place eight different queen pieces so that they cannot attack one another.", False,(255,255,255))
        escapeReminder = promptFont.render("Press ESC to leave the game, or press Space to reset.", False, (128,0,255))
        lostTheGame = winLoseFont.render("I'm sorry, that", False, (255,0,0))
        lostTheGame2 = winLoseFont.render("is not the", False, (255,0,0))
        lostTheGame3 = winLoseFont.render("correct setup", False, (255,0,0))
        wonTheGame = winLoseFont.render("Congratulations!", False, (128,255,0))
        wonTheGame2 = winLoseFont.render("That is the", False, (128,255,0))
        wonTheGame3 = winLoseFont.render("correct setup.", False, (128,255,0))
        resetGame = winLoseFont.render("Press R to retry.", False, (0,0,0))
        
        screen.blit(backgroundImage,(0,0))
        
        boardState = [[False, False, False, False, False, False, False, False],[False, False, False, False, False, False, False, False],[False, False, False, False, False, False, False, False],[False, False, False, False, False, False, False, False],[False, False, False, False, False, False, False, False],[False, False, False, False, False, False, False, False],[False, False, False, False, False, False, False, False],[False, False, False, False, False, False, False, False]]
        queenObject = []
        continue
    
    
    screen.blit(backgroundImage,(0,0))
    #Blits the chessboard
    screen.blit(promptQuiz,(300-promptQuiz.get_width()/2,410))
    screen.blit(escapeReminder,(300-escapeReminder.get_width()/2,415+promptQuiz.get_height()))
    #Blits the prompts of the queen problem and controls to quit/reset
    
    for i in range(8):
        for j in range(8):
            if boardState[i][j]:
                screen.blit(queenPiece,(50*i,50*j))
                #If a Queen has been placed previously at a certain square, this block blits the queen on the board.
    
    mouseX, mouseY = pygame.mouse.get_pos()
    for i in range(8):
        for j in range(8):
            if mouseX >= 50*i and mouseX <= 50*i+49 and mouseY >=50*j and mouseY <= 50*j+49:
                screen.blit(boardCursor,(50*i,50*j))
                #This block moves the cursor of your queen based on which square it's pointing at.
    
    mousePress = pygame.event.wait()
    if mousePress.type == pygame.MOUSEBUTTONDOWN and mousePress.button == 1 and queenCounter > 0:
        mouseXHit, mouseYHit = pygame.mouse.get_pos()
        iIndex = mouseXHit/50 
        jIndex = mouseYHit/50
        #Each square is 50 x 50, so to determine its index simply divide the position of the click by 50.
        if mouseXHit >= 0 and mouseXHit <= 399 and mouseYHit >= 0 and mouseYHit <= 399:
            if not boardState[iIndex][jIndex]: #Checks if the board is open in the clicked position.
                #If the board is open in the position, place a queen piece there. If not, ignore the click.
                queenCounter -= 1
                #Since a queen is used up, reduce the number of queen by 1
                screen.blit(queenPiece,(50*iIndex,50*jIndex))
                boardState[iIndex][jIndex] = True
                queenObject.append(QueenCoord(iIndex,jIndex))
    

    queenCountIndicator = font.render("Queen pieces", False, (255,255,0))
    queenCountIndicator2 = font.render("remaining: " + str(queenCounter), False, (255,255,0))
    screen.blit(queenCountIndicator,(410,30))
    screen.blit(queenCountIndicator2,(410,35 + queenCountIndicator.get_height()))
    #Displays how many queens are remaining at your disposal
    
    correct = checkAnswer(queenCounter)
    if correct:
        #If all queen pieces do not share x or y coordinates and all queen pieces are not on the same diagonal line. 
        screen.blit(wonTheGame,(410,250))
        screen.blit(wonTheGame2,(410,255 + wonTheGame.get_height()))
        screen.blit(wonTheGame3,(410,260 + wonTheGame.get_height()*2))
        solutions.append(boardState)
    
    if len(solutions) == 92:
        #There are a total of 92 solutions to this game. If you find them all, you win a special prize!
        break
    
    pygame.display.flip()
    #This updates the screen. Simply drawing the object isn't enough.
    frame.tick(10)

#The last break statement above will lead you to a new screen where a special code is displayed for the special prize.
while not finished:
    for event in pygame.event.get(): #pygame.event is a sub-library containing all 'event' objects in pygame.
        if event.type == pygame.QUIT:
            #events have 'type' attributes. Yes, events are objects after all.
            #QUIT is a predefined object. -pygame doc
            finished = True  
    screen.fill((255,255,255))
    allClear = promptFont.render("Congratulations! You found all 92 solutions to the Queens problem!", False,(0,0,0))
    allClear2 = promptFont.render("PM this code to Vincent Yang for a prize: SKCOR521SC", False,(0,0,0))        
    screen.blit(allClear,(300 - (allClear.get_width())/2,100))
    screen.blit(allClear2,(300 - (allClear2.get_width())/2,130 + lostTheGame.get_height()))
    pygame.display.flip()
    #This updates the screen. Simply drawing the object isn't enough.
    frame.tick(10)
