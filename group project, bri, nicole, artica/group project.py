
from gamelib import *

game = Game(800,500,"Zombie Adventure Park",60)

opening = Image("images\\opening.jpg",game)
opening.resizeTo(game.width, game.height)
count = 0
game.setBackground(opening)

story = Image("images\\StoryLine.png",game)
story.resizeTo(game.width, game.height)

player = Animation("images\\guns.png",3,game,403/3,178,5)
player.moveTo(mouse.x, mouse.y)

woman = Sound("sound\\woman.wav",1)
gun = Sound("sound\\gun.wav",2)

enemy1 = []
for times in range (2):
    enemy1.append(Image("images\\zombie1.png",game))

for e in enemy1:
    x = randint (-900,-10)
    y = randint(300, 400)
    e.moveTo( x, y )
    e.setSpeed(2,-90)
    e.resizeBy(5)

enemy2 = []
for times in range (3):
    enemy2.append(Image("images\\zombie2.png",game))

for e2 in enemy2:
    x = randint (-900, -10)
    y = randint(300,  400)
    e2.moveTo( x, y )
    e2.setSpeed(2,-90)
    e2.resizeBy(-13)

enemy3 = []
for times in range (2):
    enemy3.append(Image("images\\zombie3.png",game))

for e3 in enemy3:
    x = randint (-900,-10)
    y = randint(300, 400)
    e3.moveTo( x, y )
    e3.setSpeed(2,-90)
    e3.resizeBy(5)

enemy4 = []
for times in range (3):
    enemy4.append(Image("images\\zombie4.png",game))

for e4 in enemy4:
    x = randint (-900,-10)
    y = randint(300, 400)
    e4.moveTo( x, y )
    e4.setSpeed(2,-90)
    e4.resizeBy(5)

enemy5 = []
for times in range (3):
    enemy5.append(Image("images\\zombie5.png",game))
for e5 in enemy5:
    x = randint(-900,-10)
    y = randint(300, 400)
    e5.moveTo( x, y )
    e5.setSpeed(2,-90)
    e5.resizeBy(-30)

enemy6 = []
for times in range (3):
    enemy6.append(Image("images\\zombie6.jpg.png",game))

for e6 in enemy6:
    x = randint(-900,-10)
    y = randint(300, 400)
    e6.moveTo( x, y )
    e6.setSpeed(2,-90)
    e6.resizeBy(-30)

enemy7 = []
for times in range (3):
    enemy7.append(Image("images\\zombie7.png",game))
for e7 in enemy7:
    x = randint(-900,-10)
    y = randint(300, 400)
    e7.moveTo( x, y )
    e7.setSpeed(2,-90)
    e7.resizeBy(-30)




    



    


LevelOne = Image("images\\levelone.jpg",game)
game.setBackground(LevelOne)
LevelTwo = Image("images\\leveltwo.jpg",game)
Winning = Image("images\\winning.png",game)
Winning.resizeTo(game.width, game.height)
title = Image("images\\goodlogo.png",game)
opening.draw()
title.resizeBy(10)
title.draw()
game.drawText("Press [SPACE] to play",300,400)
game.update(1)
game.wait(K_SPACE)
story.draw()
game.drawText("PRESS [ESC] TO CONTINUE",470,470)
game.drawText("LEFT CLICK TO SHOOT", 450,450)
game.update(1)
game.wait(K_ESCAPE)



while not game.over:
    game.processInput()
    game.drawBackground()
    woman.play()
    for e in enemy1:
        e.move()
        if player.collidedWith(e) and mouse.LeftButton:
            #gun.play()
            count += 1
            game.score+=1
            e.visible=False
        if e.isOffScreen("right"):
            x = randint (-900,-10)
            y = randint(300, 400)
            e.moveTo( x, y )
            
            
    
        
    for e2 in enemy2:
        e2.move()
        if player.collidedWith(e2) and mouse.LeftButton:
            #gun.play()
            count += 1
            e2.visible = False
            game.score+=1
        if e2.isOffScreen("right"):
            x = randint (-900,-10)
            y = randint(300, 400)
            e2.moveTo( x, y )
       
    for e3 in enemy3:
        e3.move()
        if player.collidedWith(e3) and mouse.LeftButton:
            #gun.play()
            count += 1
            e3.visible = False
            game.score+=1
        if e3.isOffScreen("right"):
            x = randint (-900,-10)
            y = randint(300, 400)
            e3.moveTo( x, y )
       
       
    if count >= 7:
        game.setBackground(LevelTwo)
        '''e2.visible=True

        for e2 in enemy2:
            e2.move()
            e2.setSpeed(2,-90)
            if player.collidedWith(e2) and mouse.LeftButton:
                e2.moveTo(850,550)
                count += 1
                game.score+=1
                e2.speed+=2
                

            if e2.isOffScreen("right"):
                x = randint (-900,-10)
                y = randint(300, 400)
                e2.moveTo( x, y )'''


        for e5 in enemy5:
            e5.move()
            e5.setSpeed(3,-90)
            if player.collidedWith(e5) and mouse.LeftButton:
                #gun.play()
                e5.moveTo(850,550)
                count += 1
                game.score+=1
                e5.speed+=8
                

            if e5.isOffScreen("bottom"):
                x = randint (-900,-10)
                y = randint(300, 400)
                e6.moveTo( x, y )
        
        
        for e6 in enemy6:
            e6.move()
            e6.setSpeed(3,-90)
            if player.collidedWith(e6) and mouse.LeftButton:
                #gun.play()
                e6.moveTo(850,550)
                count += 1
                game.score+=1
                e6.speed+=8
                

            if e6.isOffScreen("bottom"):
                x = randint (-900,-10)
                y = randint(300, 400)
                e6.moveTo( x, y )


         
        for e7 in enemy7:
            e7.move()
            e7.setSpeed(3,-90)
            if player.collidedWith(e7) and mouse.LeftButton:
                #gun.play()
                e7.moveTo(850,550)
                count += 1
                game.score+=1
                e7.speed+=8
                

            if e7.isOffScreen("bottom"):
                x = randint (-900,-10)
                y = randint(300, 400)
                e7.moveTo( x, y )
        



    if count >= 16:
        e6.visible=False
        
       
        game.setBackground(Winning)
        player.visible=False
        
        
      
        
       
       
        
       
       
        
            



    game.displayScore()

    player.moveTo(mouse.x, mouse.y)

    
    
    
   
    
    
    

    game.update(60)
game.quit()
    
