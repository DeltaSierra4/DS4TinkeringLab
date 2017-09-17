import pygame

'''
Created on Jul 24, 2017

@author: DeltaSierra4_
'''


pygame.init() #Initializes all objects in the pygame library.
#This makes the library ready to use for us.

screen = pygame.display.set_mode((900,600))
#Initializes the screen object. This sets the display of your game.
#900 x 700 is the size of this window

#If you run the program at this point, you get a blank window.

finished = False #Boolean variable one-way flag which decides whether the game is finished or not.
x = 10
y = 110
endMarkerX = 855
endMarkerY = 355

playerImage = pygame.image.load("you.png") #loads an image into the game.
playerImage = pygame.transform.scale(playerImage,(30,30)) #This scales the image to the same size as the blue rectangle
playerImage = playerImage.convert_alpha() #This sets the image ready to use.
#you can use convert() instead, but that doesn't put into consideration the background of the blip you're using.

backgroundImage = pygame.image.load("checkerboardGreyWhiteLevelOne.png")
backgroundImage = pygame.transform.scale(backgroundImage,(900,500))
screen.blit(backgroundImage,(0,0))
#Draws your background

winMessages = ["","That was easy, eh?","Now to add some challenge...","Some bullets don't want to move.","Oops, I flipped a switch.", "Woah, you actually beat that!"]
#Some messages to display when you win each stage

bulletImage = pygame.image.load("bullet.png")
bulletImage = pygame.transform.scale(bulletImage,(20,20))
bulletImage = bulletImage.convert_alpha()
deadBulletImage = pygame.image.load("empty.png")
deadBulletImage = pygame.transform.scale(deadBulletImage,(20,20))
deadBulletImage = deadBulletImage.convert_alpha()


#the bounce variables allow the bullets to "bounce" off walls.
level = 1
death = 0

font = pygame.font.SysFont("Arial", 50)
#Allows us to access the fonts in our system


frame = pygame.time.Clock() #Sets frame rate


bullet1X = 265
bullet1Y = 215
bounce1 = 1
bullet2X = 365
bullet2Y = 265
bounce2 = 1
bullet3X = 415
bullet3Y = 215
bounce3 = 1
bullet4X = 465
bullet4Y = 265
bounce4 = 1
bullet5X = 515
bullet5Y = 215
bounce5 = 1
bullet6X = 615
bullet6Y = 265
bounce6 = 1 
bullet7X = 215
bullet7Y = 65
bounce7 = 1 
bullet8X = 215
bullet8Y = 415
bounce8 = 1
bullet9X = 665
bullet9Y = 65
bounce9 = 1 
bullet10X = 665
bullet10Y = 415
bounce10 = 1
bullet11X = 265
bullet11Y = 165
bounce11x = 1
bounce11y = 1
bullet12X = 265
bullet12Y = 215
bounce12x = 1
bounce12y = 1
bullet13X = 265
bullet13Y = 265
bounce13x = 1
bounce13y = 1
bullet14X = 265
bullet14Y = 315
bounce14x = 1
bounce14y = 1
bullet15X = 615
bullet15Y = 165
bounce15x = 1
bounce15y = 1
bullet16X = 615
bullet16Y = 215
bounce16x = 1
bounce16y = 1
bullet17X = 615
bullet17Y = 265
bounce17x = 1
bounce17y = 1
bullet18X = 615
bullet18Y = 315
bounce18x = 1
bounce18y = 1

def checkClear(x, y, endMarkerX, endMarkerY):
    cleared = False
    if y >= endMarkerY and y + 30 <= endMarkerY + 40 and x >= endMarkerX and x + 30 <= endMarkerX + 40:  
        x = 10
        y = 110
        cleared = True
    #The above code checks if the player's marker has reached the red end marker.
    #If the top left tip (represented by y) is within the red square, you win.
    #You also win if the bottom left tip (represented by y+30) is within the red square.
    #The textWin.get_width() call is to set the text in the center of the screen.
    
    return cleared, x, y

def pichuunLvl1(x, y, b1X, b1Y, b2X, b2Y):
    global death
    if y+30 >= b1Y and y <= b1Y+20 and x+30 >= b1X and x <= b1X+20:  
        x = 10
        y = 110
        death += 1
        frame.tick(10000) 
        screen.fill((0,0,0))
    elif y+30 >= b2Y and y <= b2Y+20 and x+30 >= b2X and x <= b2X+20:
        x = 10
        y = 110
        death += 1
        frame.tick(10000) 
        screen.fill((0,0,0))
    #The above code checks if the player has been hit by a bullet.
    #The name of the function comes from the sound the player makes in Touhou upon being hit by a bullet.
    return x, y

def pichuunLvl2(x, y, b1X, b1Y, b2X, b2Y, b3X, b3Y, b4X, b4Y, b5X, b5Y, b6X, b6Y):
    global death
    if y+30 >= b1Y and y <= b1Y+20 and x+30 >= b1X and x <= b1X+20:  
        x = 10
        y = 110
        death += 1
        frame.tick(10000) 
        screen.fill((0,0,0))
    elif y+30 >= b2Y and y <= b2Y+20 and x+30 >= b2X and x <= b2X+20:
        x = 10
        y = 110
        death += 1
        frame.tick(10000) 
        screen.fill((0,0,0))
    elif y+30 >= b3Y and y <= b3Y+20 and x+30 >= b3X and x <= b3X+20:  
        x = 10
        y = 110
        death += 1
        frame.tick(10000) 
        screen.fill((0,0,0))
    elif y+30 >= b4Y and y <= b4Y+20 and x+30 >= b4X and x <= b4X+20:
        x = 10
        y = 110
        death += 1
        frame.tick(10000) 
        screen.fill((0,0,0))
    elif y+30 >= b5Y and y <= b5Y+20 and x+30 >= b5X and x <= b5X+20:  
        x = 10
        y = 110
        death += 1
        frame.tick(10000) 
        screen.fill((0,0,0))
    elif y+30 >= b6Y and y <= b6Y+20 and x+30 >= b6X and x <= b6X+20:
        x = 10
        y = 110
        death += 1
        frame.tick(10000) 
        screen.fill((0,0,0))
    return x, y

def pichuunLvl3(x, y, b1X, b1Y, b2X, b2Y, b3X, b3Y, b4X, b4Y, b5X, b5Y, b6X, b6Y, b7X, b7Y, b8X, b8Y, b9X, b9Y, b10X, b10Y):
    global death
    if y+30 >= b1Y and y <= b1Y+20 and x+30 >= b1X and x <= b1X+20:  
        x = 10
        y = 110
        death += 1
        frame.tick(10000) 
        screen.fill((0,0,0))
    elif y+30 >= b2Y and y <= b2Y+20 and x+30 >= b2X and x <= b2X+20:
        x = 10
        y = 110
        death += 1
        frame.tick(10000) 
        screen.fill((0,0,0))
    elif y+30 >= b3Y and y <= b3Y+20 and x+30 >= b3X and x <= b3X+20:  
        x = 10
        y = 110
        death += 1
        frame.tick(10000) 
        screen.fill((0,0,0))
    elif y+30 >= b4Y and y <= b4Y+20 and x+30 >= b4X and x <= b4X+20:
        x = 10
        y = 110
        death += 1
        frame.tick(10000) 
        screen.fill((0,0,0))
    elif y+30 >= b5Y and y <= b5Y+20 and x+30 >= b5X and x <= b5X+20:  
        x = 10
        y = 110
        death += 1
        frame.tick(10000) 
        screen.fill((0,0,0))
    elif y+30 >= b6Y and y <= b6Y+20 and x+30 >= b6X and x <= b6X+20:
        x = 10
        y = 110
        death += 1
        frame.tick(10000) 
        screen.fill((0,0,0))
    elif y+30 >= b7Y and y <= b7Y+20 and x+30 >= b7X and x <= b7X+20:  
        x = 10
        y = 110
        death += 1
        frame.tick(10000) 
        screen.fill((0,0,0))
    elif y+30 >= b8Y and y <= b8Y+20 and x+30 >= b8X and x <= b8X+20:
        x = 10
        y = 110
        death += 1
        frame.tick(10000) 
        screen.fill((0,0,0))
    elif y+30 >= b9Y and y <= b9Y+20 and x+30 >= b9X and x <= b9X+20:  
        x = 10
        y = 110
        death += 1
        frame.tick(10000) 
        screen.fill((0,0,0))
    elif y+30 >= b10Y and y <= b10Y+20 and x+30 >= b10X and x <= b10X+20:
        x = 10
        y = 110
        death += 1
        frame.tick(10000) 
        screen.fill((0,0,0))
    return x, y

def pichuunLvl4and5(x, y, b1X, b1Y, b2X, b2Y, b3X, b3Y, b4X, b4Y, b5X, b5Y, b6X, b6Y, b7X, b7Y, b8X, b8Y, b9X, b9Y, b10X, b10Y, b11X, b11Y, b12X, b12Y, b13X, b13Y, b14X, b14Y, b15X, b15Y, b16X, b16Y, b17X, b17Y, b18X, b18Y):
    global death
    if y+30 >= b1Y and y <= b1Y+20 and x+30 >= b1X and x <= b1X+20:  
        x = 10
        y = 110
        death += 1
        frame.tick(10000) 
        screen.fill((0,0,0))
    elif y+30 >= b2Y and y <= b2Y+20 and x+30 >= b2X and x <= b2X+20:
        x = 10
        y = 110
        death += 1
        frame.tick(10000) 
        screen.fill((0,0,0))
    elif y+30 >= b3Y and y <= b3Y+20 and x+30 >= b3X and x <= b3X+20:  
        x = 10
        y = 110
        death += 1
        frame.tick(10000) 
        screen.fill((0,0,0))
    elif y+30 >= b4Y and y <= b4Y+20 and x+30 >= b4X and x <= b4X+20:
        x = 10
        y = 110
        death += 1
        frame.tick(10000) 
        screen.fill((0,0,0))
    elif y+30 >= b5Y and y <= b5Y+20 and x+30 >= b5X and x <= b5X+20:  
        x = 10
        y = 110
        death += 1
        frame.tick(10000) 
        screen.fill((0,0,0))
    elif y+30 >= b6Y and y <= b6Y+20 and x+30 >= b6X and x <= b6X+20:
        x = 10
        y = 110
        death += 1
        frame.tick(10000) 
        screen.fill((0,0,0))
    elif y+30 >= b7Y and y <= b7Y+20 and x+30 >= b7X and x <= b7X+20:  
        x = 10
        y = 110
        death += 1
        frame.tick(10000) 
        screen.fill((0,0,0))
    elif y+30 >= b8Y and y <= b8Y+20 and x+30 >= b8X and x <= b8X+20:
        x = 10
        y = 110
        death += 1
        frame.tick(10000) 
        screen.fill((0,0,0))
    elif y+30 >= b9Y and y <= b9Y+20 and x+30 >= b9X and x <= b9X+20:  
        x = 10
        y = 110
        death += 1
        frame.tick(10000) 
        screen.fill((0,0,0))
    elif y+30 >= b10Y and y <= b10Y+20 and x+30 >= b10X and x <= b10X+20:
        x = 10
        y = 110
        death += 1
        frame.tick(10000) 
        screen.fill((0,0,0))
    elif y+30 >= b11Y and y <= b11Y+20 and x+30 >= b11X and x <= b11X+20:
        x = 10
        y = 110
        death += 1
        frame.tick(10000) 
        screen.fill((0,0,0))
    elif y+30 >= b12Y and y <= b12Y+20 and x+30 >= b12X and x <= b12X+20:
        x = 10
        y = 110
        death += 1
        frame.tick(10000) 
        screen.fill((0,0,0))
    elif y+30 >= b13Y and y <= b13Y+20 and x+30 >= b13X and x <= b13X+20:
        x = 10
        y = 110
        death += 1
        frame.tick(10000) 
        screen.fill((0,0,0))
    elif y+30 >= b14Y and y <= b14Y+20 and x+30 >= b14X and x <= b14X+20:
        x = 10
        y = 110
        death += 1
        frame.tick(10000) 
        screen.fill((0,0,0))
    elif y+30 >= b15Y and y <= b15Y+20 and x+30 >= b15X and x <= b15X+20:
        x = 10
        y = 110
        death += 1
        frame.tick(10000) 
        screen.fill((0,0,0))
    elif y+30 >= b16Y and y <= b16Y+20 and x+30 >= b16X and x <= b16X+20:
        x = 10
        y = 110
        death += 1
        frame.tick(10000) 
        screen.fill((0,0,0))
    elif y+30 >= b17Y and y <= b17Y+20 and x+30 >= b17X and x <= b17X+20:
        x = 10
        y = 110
        death += 1
        frame.tick(10000) 
        screen.fill((0,0,0))
    elif y+30 >= b18Y and y <= b18Y+20 and x+30 >= b18X and x <= b18X+20:
        x = 10
        y = 110
        death += 1
        frame.tick(10000) 
        screen.fill((0,0,0))
    return x, y

def movement(pressedKeyList,x,y):
    global level
    if pressedKeyList[pygame.K_UP]:
        if pressedKeyList[pygame.K_LEFT]:
            y -= 2
            x -= 2
        elif pressedKeyList[pygame.K_RIGHT]:
            y -= 2
            x += 2
        else:
            y -= 2
    elif pressedKeyList[pygame.K_DOWN]:
        if pressedKeyList[pygame.K_LEFT]:
            y += 2
            x -= 2
        elif pressedKeyList[pygame.K_RIGHT]:
            y += 2
            x += 2
        else:
            y += 2
    elif pressedKeyList[pygame.K_LEFT]:
        if pressedKeyList[pygame.K_UP]:
            x -= 2
            y -= 2
        elif pressedKeyList[pygame.K_DOWN]:
            x -= 2
            y += 2
        else:
            x -= 2
    elif pressedKeyList[pygame.K_RIGHT]:
        if pressedKeyList[pygame.K_UP]:
            x += 2
            y -= 2
        elif pressedKeyList[pygame.K_DOWN]:
            x += 2
            y += 2        
        else:
            x += 2
    if level <= 5:
        return wallLevelOne(x, y)
    elif level <= 10:
        return wallLevelSix(x, y)
    else:
        return wall(x,y)
#Function to deal with all movements

def wall(x,y):
    if x > 870:
        x = 870
    elif x < 0:
        x = 0
    
    if y > 470:
        y = 470
    elif y < 0:
        y = 0
    
    return x,y

def wallLevelOne(x,y):
    if x > 870:
        x = 870
    elif x < 0:
        x = 0
    
    if y > 470:
        y = 470
    elif y < 0:
        y = 0
    
    if x < 200:
        if y <= 100:
            y = 100
        elif y >= 370:
            y = 370
    
    if x > 670:
        if y <= 100:
            y = 100
        elif y >= 370:
            y = 370 
    
    if y < 100:
        if x <= 202:
            x = 202
        elif x >= 668:
            x = 668
        
    if y > 370:
        if x <= 202:
            x = 202
        elif x >= 668:
            x = 668
    
    #The above block of codes prevent the player from going through walls or the edge of the map.
    return x, y 

def wallLevelSix(x,y):
    if x > 870:
        x = 870
    elif x < 0:
        x = 0
    
    if y > 470:
        y = 470
    elif y < 0:
        y = 0
    
    if x < 200:
        if y <= 100:
            y = 100
        elif y >= 370:
            y = 370
    
    if x > 670:
        if y <= 100:
            y = 100
        elif y >= 370:
            y = 370 
    
    if y < 100:
        if x <= 102:
            x = 102
        elif x >= 768:
            x = 768
        
    if y > 370:
        if x <= 102:
            x = 102
        elif x >= 768:
            x = 768
    
    #The above block of codes prevent the player from going through walls or the edge of the map.
    return x, y 


def bulletMovementLevelOne(b1x, b1y, bounce1, b2x, b2y, bounce2, b3x, b3y, bounce3, b4x, b4y, bounce4, b5x, b5y, bounce5, b6x, b6y, bounce6, b7x, b7y, bounce7, b8x, b8y, bounce8, b9x, b9y, bounce9, b10x, b10y, bounce10, b11x, b11y, bounce11x, bounce11y, b12x, b12y, bounce12x, bounce12y, b13x, b13y, bounce13x, bounce13y, b14x, b14y, bounce14x, bounce14y, b15x, b15y, bounce15x, bounce15y, b16x, b16y, bounce16x, bounce16y, b17x, b17y, bounce17x, bounce17y, b18x, b18y, bounce18x, bounce18y):
    global level
    b1y -= (3 + min(level-1,3)) * bounce1
    b2y += (3 + min(level-1,3)) * bounce2
    b3y -= (3 + min(level-1,3)) * bounce3
    b4y += (3 + min(level-1,3)) * bounce4
    b5y -= (3 + min(level-1,3)) * bounce5
    b6y += (3 + min(level-1,3)) * bounce6
    b7x += max(level*5/6,3) * bounce7
    b8x += max(level*5/6,3) * bounce8
    b9x -= max(level*5/6,3) * bounce9
    b10x -= max(level*5/6,3) * bounce10
    b11x += min((level/5)*5,3) * bounce11x
    b11y -= min((level/5)*5,3) * bounce11y
    b12x += min((level/5)*5,3) * bounce12x
    b12y -= min((level/5)*5,3) * bounce12y/2
    b13x += min((level/5)*5,3) * bounce13x
    b13y += min((level/5)*5,3) * bounce13y/2
    b14x += min((level/5)*5,3) * bounce14x
    b14y += min((level/5)*5,3) * bounce14y
    b15x -= min((level/5)*5,3) * bounce15x
    b15y -= min((level/5)*5,3) * bounce15y
    b16x -= min((level/5)*5,3) * bounce16x
    b16y -= min((level/5)*5,3) * bounce16y/2
    b17x -= min((level/5)*5,3) * bounce17x
    b17y += min((level/5)*5,3) * bounce17y/2
    b18x -= min((level/5)*5,3) * bounce18x
    b18y += min((level/5)*5,3) * bounce18y
    if b1y <= 0:
        b1y = 0
        bounce1 = bounce1 * -1
    if b2y <= 0:
        b2y = 0
        bounce2 = bounce2 * -1
    if b3y <= 0:
        b3y = 0
        bounce3 = bounce3 * -1
    if b4y <= 0:
        b4y = 0
        bounce4 = bounce4 * -1
    if b5y <= 0:
        b5y = 0
        bounce5 = bounce5 * -1
    if b6y <= 0:
        b6y = 0
        bounce6 = bounce6 * -1
    if b7x <= 200:
        b7x = 200
        bounce7 = bounce7 * -1
    if b8x <= 200:
        b8x = 200
        bounce8 = bounce8 * -1
    if b9x <= 200:
        b9x = 200
        bounce9 = bounce9 * -1
    if b10x <= 200:
        b10x = 200
        bounce10 = bounce10 * -1
    if b11x >= 430:
        b11x = 430
        bounce11x = bounce11x * -1
    if b11y <= 0:
        b11y = 0
        bounce11y = bounce11y * -1
    if b12x >= 430:
        b12x = 430
        bounce12x = bounce12x * -1
    if b12y <= 150:
        b12y = 150
        bounce12y = bounce12y * -1    
    if b13x >= 430:
        b13x = 430
        bounce13x = bounce13x * -1
    if b13y >= 330:
        b13y = 330
        bounce13y = bounce13y * -1
    if b14x >= 430:
        b14x = 430
        bounce14x = bounce14x * -1
    if b14y >= 480:
        b14y = 480
        bounce14y = bounce14y * -1    
    if b15x <= 450:
        b15x = 450
        bounce15x = bounce15x * -1
    if b15y <= 0:
        b15y = 0
        bounce15y = bounce15y * -1
    if b16x <= 450:
        b16x = 450
        bounce16x = bounce16x * -1
    if b16y <= 150:
        b16y = 150
        bounce16y = bounce16y * -1    
    if b17x <= 450:
        b17x = 450
        bounce17x = bounce17x * -1
    if b17y >= 330:
        b17y = 330
        bounce17y = bounce17y * -1
    if b18x <= 450:
        b18x = 450
        bounce18x = bounce18x * -1
    if b18y >= 480:
        b18y = 480
        bounce18y = bounce18y * -1
    
    if b1y >= 480:
        b1y = 480
        bounce1 = bounce1 * -1
    if b2y >= 480:
        b2y = 480
        bounce2 = bounce2 * -1
    if b3y >= 480:
        b3y = 480
        bounce3 = bounce3 * -1
    if b4y >= 480:
        b4y = 480
        bounce4 = bounce4 * -1
    if b5y >= 480:
        b5y = 480
        bounce5 = bounce5 * -1
    if b6y >= 480:
        b6y = 480
        bounce6 = bounce6 * -1
    if b7x >= 680:
        b7x = 680
        bounce7 = bounce7 * -1
    if b8x >= 680:
        b8x = 680
        bounce8 = bounce8 * -1
    if b9x >= 680:
        b9x = 680
        bounce9 = bounce9 * -1
    if b10x >= 680:
        b10x = 680
        bounce10 = bounce10 * -1
    if b11x <= 250:
        b11x = 250
        bounce11x = bounce11x * -1
    if b11y >= 180:
        b11y = 180
        bounce11y = bounce11y * -1
    if b12x <= 250:
        b12x = 250
        bounce12x = bounce12x * -1
    if b12y >= 230:
        b12y = 230
        bounce12y = bounce12y * -1    
    if b13x <= 250:
        b13x = 250
        bounce13x = bounce13x * -1
    if b13y <= 250:
        b13y = 250
        bounce13y = bounce13y * -1
    if b14x <= 250:
        b14x = 250
        bounce14x = bounce14x * -1
    if b14y <= 300:
        b14y = 300
        bounce14y = bounce14y * -1    
    if b15x >= 630:
        b15x = 630
        bounce15x = bounce15x * -1
    if b15y >= 180:
        b15y = 180
        bounce15y = bounce15y * -1
    if b16x >= 630:
        b16x = 630
        bounce16x = bounce16x * -1
    if b16y >= 230:
        b16y = 230
        bounce16y = bounce16y * -1    
    if b17x >= 630:
        b17x = 630
        bounce17x = bounce17x * -1
    if b17y <= 250:
        b17y = 250
        bounce17y = bounce17y * -1
    if b18x >= 630:
        b18x = 630
        bounce18x = bounce18x * -1
    if b18y <= 300:
        b18y = 300
        bounce18y = bounce18y * -1
    
    
    return b1x, b1y, bounce1, b2x, b2y, bounce2, b3x, b3y, bounce3, b4x, b4y, bounce4, b5x, b5y, bounce5, b6x, b6y, bounce6, b7x, b7y, bounce7, b8x, b8y, bounce8, b9x, b9y, bounce9, b10x, b10y, bounce10, b11x, b11y, bounce11x, bounce11y, b12x, b12y, bounce12x, bounce12y, b13x, b13y, bounce13x, bounce13y, b14x, b14y, bounce14x, bounce14y, b15x, b15y, bounce15x, bounce15y, b16x, b16y, bounce16x, bounce16y, b17x, b17y, bounce17x, bounce17y, b18x, b18y, bounce18x, bounce18y

#def bulletMovement(b1x, b1y, bounce1, b2x, b2y, bounce2, b3x, b3y, bounce3, b4x, b4y, bounce4, b5x, b5y, b6x, b6y, b7x, b7y, b8x, b8y):
#Generic parameters for bullet movement function

clearState = False

while not finished:
    for event in pygame.event.get(): #pygame.event is a sub-library containing all 'event' objects in pygame.
        if event.type == pygame.QUIT:
            #events have 'type' attributes. Yes, events are objects after all.
            #QUIT is a predefined object. -pygame doc
            finished = True
    
    pressedKeys = pygame.key.get_pressed()
    #Returns the state of all pressed keys in the form of a list of booleans.
    #For details on the pygame.key objects, refer to the pygame documentation.
    #For instance, K_SPACE is given the number 32. Think of those uppercase named Constants from Javanotes. 

    x, y = movement(pressedKeys, x, y)
    bullet1X, bullet1Y, bounce1, bullet2X, bullet2Y, bounce2, bullet3X, bullet3Y, bounce3, bullet4X, bullet4Y, bounce4, bullet5X, bullet5Y, bounce5, bullet6X, bullet6Y, bounce6, bullet7X, bullet7Y, bounce7, bullet8X, bullet8Y, bounce8, bullet9X, bullet9Y, bounce9, bullet10X, bullet10Y, bounce10, bullet11X, bullet11Y, bounce11x, bounce11y, bullet12X, bullet12Y, bounce12x, bounce12y, bullet13X, bullet13Y, bounce13x, bounce13y, bullet14X, bullet14Y, bounce14x, bounce14y, bullet15X, bullet15Y, bounce15x, bounce15y, bullet16X, bullet16Y, bounce16x, bounce16y, bullet17X, bullet17Y, bounce17x, bounce17y, bullet18X, bullet18Y, bounce18x, bounce18y = bulletMovementLevelOne(bullet1X, bullet1Y, bounce1, bullet2X, bullet2Y, bounce2, bullet3X, bullet3Y, bounce3, bullet4X, bullet4Y, bounce4, bullet5X, bullet5Y, bounce5, bullet6X, bullet6Y, bounce6, bullet7X, bullet7Y, bounce7, bullet8X, bullet8Y, bounce8, bullet9X, bullet9Y, bounce9, bullet10X, bullet10Y, bounce10, bullet11X, bullet11Y, bounce11x, bounce11y, bullet12X, bullet12Y, bounce12x, bounce12y, bullet13X, bullet13Y, bounce13x, bounce13y, bullet14X, bullet14Y, bounce14x, bounce14y, bullet15X, bullet15Y, bounce15x, bounce15y, bullet16X, bullet16Y, bounce16x, bounce16y, bullet17X, bullet17Y, bounce17x, bounce17y, bullet18X, bullet18Y, bounce18x, bounce18y)        
    
    #rectOne = pygame.Rect(x, y, 30, 30) 
    #Rect() is not necessarily a method - it initializes a 'rectangle' object. Yes, it is a constructor.
    #Rect(x,y,width,height) are the parameters.
    #NB! THIS DOES NOT DRAW THE RECTANGLE ITSELF
    #You only initialized a rectangle object but in order to draw the rectangle you must use the pygame.draw feature as shown below.
    color = (0,0,255)
    
    rectTwo = pygame.Rect(endMarkerX, endMarkerY, 40, 40)
    color2 = (255, 0, 0)
    
    screen.blit(backgroundImage,(0,0))
    deathCounter = font.render("Death: " + str(death),False,(255,255,255))
    screen.blit(deathCounter,(450-deathCounter.get_width()/2,609-deathCounter.get_height()))
    levelCounter = font.render("Level: " + str(level),False,(255,255,0))
    screen.blit(levelCounter,(450-levelCounter.get_width()/2,618-levelCounter.get_height()*2))
    pygame.draw.rect(screen,color2,rectTwo)
    #pygame.draw.rect(Surface,color,rect) are the parameters.
    #Surface is a pygame.surface object where you want to draw the rectangle. Usually it is the display screen.
    #color is a tuple containing three values representing R,G,B.

    screen.blit(playerImage,(x,y))
    #This draws the image into the x,y coordinates.
    if level == 1:
        screen.blit(deadBulletImage,(bullet1X,bullet1Y))
        screen.blit(deadBulletImage,(bullet2X,bullet2Y))
        screen.blit(bulletImage,(bullet3X,bullet3Y))
        screen.blit(bulletImage,(bullet4X,bullet4Y))
        screen.blit(deadBulletImage,(bullet5X,bullet5Y))
        screen.blit(deadBulletImage,(bullet6X,bullet6Y))
        screen.blit(deadBulletImage,(bullet7X,bullet7Y))
        screen.blit(deadBulletImage,(bullet8X,bullet8Y))
        screen.blit(deadBulletImage,(bullet9X,bullet9Y))
        screen.blit(deadBulletImage,(bullet10X,bullet10Y))
        screen.blit(deadBulletImage,(bullet11X,bullet11Y))
        screen.blit(deadBulletImage,(bullet12X,bullet12Y))
        screen.blit(deadBulletImage,(bullet13X,bullet13Y))
        screen.blit(deadBulletImage,(bullet14X,bullet14Y))
        screen.blit(deadBulletImage,(bullet15X,bullet15Y))
        screen.blit(deadBulletImage,(bullet16X,bullet16Y))
        screen.blit(deadBulletImage,(bullet17X,bullet17Y))
        screen.blit(deadBulletImage,(bullet18X,bullet18Y))
    elif level == 2:
        screen.blit(bulletImage,(bullet1X,bullet1Y))
        screen.blit(bulletImage,(bullet2X,bullet2Y))
        screen.blit(bulletImage,(bullet3X,bullet3Y))
        screen.blit(bulletImage,(bullet4X,bullet4Y))
        screen.blit(bulletImage,(bullet5X,bullet5Y))
        screen.blit(bulletImage,(bullet6X,bullet6Y))
        screen.blit(deadBulletImage,(bullet7X,bullet7Y))
        screen.blit(deadBulletImage,(bullet8X,bullet8Y))
        screen.blit(deadBulletImage,(bullet9X,bullet9Y))
        screen.blit(deadBulletImage,(bullet10X,bullet10Y))
        screen.blit(deadBulletImage,(bullet11X,bullet11Y))
        screen.blit(deadBulletImage,(bullet12X,bullet12Y))
        screen.blit(deadBulletImage,(bullet13X,bullet13Y))
        screen.blit(deadBulletImage,(bullet14X,bullet14Y))
        screen.blit(deadBulletImage,(bullet15X,bullet15Y))
        screen.blit(deadBulletImage,(bullet16X,bullet16Y))
        screen.blit(deadBulletImage,(bullet17X,bullet17Y))
        screen.blit(deadBulletImage,(bullet18X,bullet18Y))
    elif level == 3:
        screen.blit(bulletImage,(bullet1X,bullet1Y))
        screen.blit(bulletImage,(bullet2X,bullet2Y))
        screen.blit(bulletImage,(bullet3X,bullet3Y))
        screen.blit(bulletImage,(bullet4X,bullet4Y))
        screen.blit(bulletImage,(bullet5X,bullet5Y))
        screen.blit(bulletImage,(bullet6X,bullet6Y))
        screen.blit(bulletImage,(bullet7X,bullet7Y))
        screen.blit(bulletImage,(bullet8X,bullet8Y))
        screen.blit(bulletImage,(bullet9X,bullet9Y))
        screen.blit(bulletImage,(bullet10X,bullet10Y))
        screen.blit(deadBulletImage,(bullet11X,bullet11Y))
        screen.blit(deadBulletImage,(bullet12X,bullet12Y))
        screen.blit(deadBulletImage,(bullet13X,bullet13Y))
        screen.blit(deadBulletImage,(bullet14X,bullet14Y))
        screen.blit(deadBulletImage,(bullet15X,bullet15Y))
        screen.blit(deadBulletImage,(bullet16X,bullet16Y))
        screen.blit(deadBulletImage,(bullet17X,bullet17Y))
        screen.blit(deadBulletImage,(bullet18X,bullet18Y))
    else:
        screen.blit(bulletImage,(bullet1X,bullet1Y))
        screen.blit(bulletImage,(bullet2X,bullet2Y))
        screen.blit(bulletImage,(bullet3X,bullet3Y))
        screen.blit(bulletImage,(bullet4X,bullet4Y))
        screen.blit(bulletImage,(bullet5X,bullet5Y))
        screen.blit(bulletImage,(bullet6X,bullet6Y))
        screen.blit(bulletImage,(bullet7X,bullet7Y))
        screen.blit(bulletImage,(bullet8X,bullet8Y))
        screen.blit(bulletImage,(bullet9X,bullet9Y))
        screen.blit(bulletImage,(bullet10X,bullet10Y))
        screen.blit(bulletImage,(bullet11X,bullet11Y))
        screen.blit(bulletImage,(bullet12X,bullet12Y))
        screen.blit(bulletImage,(bullet13X,bullet13Y))
        screen.blit(bulletImage,(bullet14X,bullet14Y))
        screen.blit(bulletImage,(bullet15X,bullet15Y))
        screen.blit(bulletImage,(bullet16X,bullet16Y))
        screen.blit(bulletImage,(bullet17X,bullet17Y))
        screen.blit(bulletImage,(bullet18X,bullet18Y))
                
    clearState, x, y = checkClear(x, y, endMarkerX, endMarkerY)
    if clearState:
        textWin = font.render(winMessages[level],False,(128,0,255))
        #Creates a font object with the desired text in your chosen font.
        level += 1
        if level == 6:
            backgroundImage = pygame.image.load("checkerboardGreyWhiteLevelSix.png")
            backgroundImage = pygame.transform.scale(backgroundImage,(900,500))
        elif level == 1:
            backgroundImage = pygame.image.load("checkerboardGreyWhite.png")
            backgroundImage = pygame.transform.scale(backgroundImage,(900,500))            
        screen.blit(textWin,(450-textWin.get_width()/2,250))
        pygame.display.flip()
        frame.tick(1) 
        screen.fill((0,0,0))
    else:
        if level == 1:
            x, y = pichuunLvl1(x, y, bullet3X, bullet3Y, bullet4X, bullet4Y)
        elif level == 2:
            x, y = pichuunLvl2(x, y, bullet1X, bullet1Y, bullet2X, bullet2Y, bullet3X, bullet3Y, bullet4X, bullet4Y, bullet5X, bullet5Y, bullet6X, bullet6Y)
        elif level == 3:
            x, y = pichuunLvl3(x, y, bullet1X, bullet1Y, bullet2X, bullet2Y, bullet3X, bullet3Y, bullet4X, bullet4Y, bullet5X, bullet5Y, bullet6X, bullet6Y, bullet7X, bullet7Y, bullet8X, bullet8Y, bullet9X, bullet9Y, bullet10X, bullet10Y)
        else:
            x, y = pichuunLvl4and5(x, y, bullet1X, bullet1Y, bullet2X, bullet2Y, bullet3X, bullet3Y, bullet4X, bullet4Y, bullet5X, bullet5Y, bullet6X, bullet6Y, bullet7X, bullet7Y, bullet8X, bullet8Y, bullet9X, bullet9Y, bullet10X, bullet10Y, bullet11X, bullet11Y, bullet12X, bullet12Y, bullet13X, bullet13Y, bullet14X, bullet14Y, bullet15X, bullet15Y, bullet16X, bullet16Y, bullet17X, bullet17Y, bullet18X, bullet18Y)



    pygame.display.flip()
    #This updates the screen. Simply drawing the object isn't enough.
    frame.tick(100) 
    #Sets a pause rate by frames per second.
    #If set to 30 it means there will be a pause of 1/30th of framerates.
    
    
    
    