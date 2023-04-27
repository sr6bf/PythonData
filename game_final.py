
import pygame
import gamebox

'''
GAME DESCRIPTION:
A 2-player PacMan-eque game where two people compete against each other to have their characters “eat” the most fruit within two minutes. They must navigate through a maze to collect the fruits.
Character moves at a constant speed. 
Scoreboard on the top to keep track of how many points each player has accumulated. 

User Input:
    Character moves based on keys
    Player 1: up/down/left/right arrows
    Player 2: A, S, W, D
Game Over
    Game “ends” when the timer runs out, everything stops in place. 
    Shows “game over” on the screen
    OR if all fruits are eaten before timer, game over is displayed
Display size: – DONE
    800 x 600 pixels (may be smaller depending on maze design challenges)
    Camera remains constant
    Graphic Images – 
Characters: each get a different local image, with unique design to the player
    Character begin the game in set position, end the game where they are
    Maze: maze design made of walls in a solid color
    Each collectible is a graphic, like a coin or apple
    “Scoreboard” visually displays points accumulated between each player. Visible at all times. 

GameOver restart 
    When timer ends, game over, with option to restart by pressing a key
    Press spacebar to restart
Two player simultaneously 
    Two players play against each other to compete under time limit for most collectibles
    Different design between the players to differentiate between them
Timer 
    Eat up things in a two minute time frame
    Whoever collects the most collectibles in a certain time frame wins 
    Displayed on the screen at all times. 
Collectibles : (player “eats” up thing,
    Collectible disappears from view when character touches it, this adds a “point” to the character and counts as “eating” the collectible. 
    Will code for the removal of the collectible when the character is a certain distance away from it
    Collectibles are evenly dispersed in regions where there are no maze walls 
    Relatively small in size, smaller than the character sprite


For the fruit: put where there is NO wall. For loop the walls→if a coordinate is not with the fruits, put the fruit there. 

'''

game_button = True ##on = game goes, off = game done,
camera = gamebox.Camera(800,600)

pac1 = gamebox.from_image(750,300, "chara_2.png")
pac2 = gamebox.from_image(50,300, 'chara_1.png')
##fruit = gamebox.from_image(100,300, 'cherry.png')

score = 0
player_speed = 10

collectibles = [
    # Above wall 1
    gamebox.from_image(75, 100, 'cherry.png'),
    gamebox.from_image(140, 100, 'cherry.png'),
    gamebox.from_image(205, 100, 'cherry.png'),

    ##In front of player 1
    gamebox.from_image(150, 450, 'cherry.png'),
    gamebox.from_image(150, 375, 'cherry.png'),
    gamebox.from_image(150, 300, 'cherry.png'),
    gamebox.from_image(200, 260, 'cherry.png'),
    #Next to wall 1
    gamebox.from_image(275,180, 'cherry.png'),
    gamebox.from_image(275, 260, 'cherry.png'),
    gamebox.from_image(275, 100, 'cherry.png'),

    #Next to wall 3
    gamebox.from_image(400,180, 'cherry.png'),
    gamebox.from_image(400, 260, 'cherry.png'),


    #Next to wall 6
    gamebox.from_image(85, 525, 'cherry.png'),
    gamebox.from_image(135, 525, 'cherry.png'),
    gamebox.from_image(185, 525, 'cherry.png'),
    gamebox.from_image(235, 525, 'cherry.png'),
    gamebox.from_image(250, 470, 'cherry.png'),
    gamebox.from_image(250, 420, 'cherry.png'),
    gamebox.from_image(250, 370, 'cherry.png'),
    gamebox.from_image(320, 370, 'cherry.png'),
    gamebox.from_image(385, 370, 'cherry.png'),

    #Next to wall 7
    gamebox.from_image(385, 420, 'cherry.png'),
    gamebox.from_image(385, 470, 'cherry.png'),
    gamebox.from_image(385, 525, 'cherry.png'),
    gamebox.from_image(435, 525, 'cherry.png'),
    gamebox.from_image(485, 525, 'cherry.png'),
    gamebox.from_image(535, 525, 'cherry.png'),
    gamebox.from_image(585, 525, 'cherry.png'),

    # Wall 8 and 7

    gamebox.from_image(500, 225, 'cherry.png'),
    gamebox.from_image(560, 225, 'cherry.png'),
    gamebox.from_image(500, 350,'cherry.png'),
    gamebox.from_image(500, 425,'cherry.png'),


    ## Top Wall 2
    gamebox.from_image(400,40, 'cherry.png'),
    gamebox.from_image(400+75, 40, 'cherry.png'),
    gamebox.from_image(400+75*2, 40, 'cherry.png'),
    gamebox.from_image(400+75*3, 40, 'cherry.png'),
    gamebox.from_image(400+75*4, 40, 'cherry.png'),
    gamebox.from_image(400+75*5, 40, 'cherry.png'),
    gamebox.from_image(400-75, 40, 'cherry.png'),
    gamebox.from_image(400-75*2, 40, 'cherry.png'),
    gamebox.from_image(400-75*3, 40, 'cherry.png'),
    gamebox.from_image(400-75*4, 40, 'cherry.png'),
    gamebox.from_image(400+75*5, 115, 'cherry.png'),
    gamebox.from_image(400+75*4, 115, 'cherry.png'),
    gamebox.from_image(400+75*3, 115, 'cherry.png'),
    gamebox.from_image(400+75*2, 115, 'cherry.png'),
    gamebox.from_image(400+75, 115, 'cherry.png'),
    gamebox.from_image(400, 115, 'cherry.png'),

    ##Left Side Wall 10
    gamebox.from_image(625, 525, 'cherry.png'),
    gamebox.from_image(625, 450, 'cherry.png'),
    gamebox.from_image(625, 375, 'cherry.png'),
    gamebox.from_image(625, 300, 'cherry.png'),
    gamebox.from_image(625, 225, 'cherry.png'),

    ##Right Side Wall 10
    gamebox.from_image(700, 525, 'cherry.png'),
    gamebox.from_image(700, 450, 'cherry.png'),
    gamebox.from_image(700, 375, 'cherry.png'),
    gamebox.from_image(700, 300, 'cherry.png'),
    gamebox.from_image(700, 225, 'cherry.png')

]


barriers = [
    ## outer walls
    gamebox.from_color(400, 0, "blue", 1000, 30),
    gamebox.from_color(800,500, 'blue', 30, 1500), ##right side
    gamebox.from_color(0,100,'blue',30,1500), ##left side
    gamebox.from_color(300, 600, 'blue', 1500, 30), ##floor

    ## maze_walls
    gamebox.from_color(400,75, 'blue',600, 15), ##wall 2
    gamebox.from_color(100, 150, 'blue', 200, 15), ## wall 1
    gamebox.from_color(310,200,'blue',15,250), ##wall 3
    gamebox.from_color(270,320,'blue',200,15), ## wall 4
    gamebox.from_color(178,375,'blue',15,125), ##wall 5
    gamebox.from_color(275,520,'blue',15,150), ##wall 6
    gamebox.from_color(430, 400, 'blue', 15, 100), ##wall 7
    gamebox.from_color(430,217, 'blue', 15, 100), ##wall 8
    gamebox.from_color(545, 175, 'blue', 225,15), ## wall 9
    gamebox.from_color(650, 450, 'blue', 15, 550) ## wall 10

]

measure_time = 0
timer = 60
points1 = 0
points2 = 0

def tick(keys):
    global measure_time, timer, game_button, pac2, pac1, barriers, points1, points2, collectibles
    if game_button:
        camera.clear('black')
        camera.draw(gamebox.from_text(100, 200, 'Player1: ' + str(points1), 40, 'red', bold=True, italic=False))
        camera.draw(gamebox.from_text(100, 250, 'Player2: ' + str(points2), 40, 'red', bold=True, italic=False))
        camera.draw(pac2)
        camera.draw(pac1)
        if(points1 + points2) == 58:
            game_button = False

        for fruit in collectibles:
            if pac2.touches(fruit):
                fruit.x = -500
                fruit.y = 0
                points2 += 1
            if pac1.touches(fruit):
                points1 += 1
                fruit.x = -500
                fruit.y = 0

            #### ^^trying to display scores when player touches cherries, but right now score are continuously increasing despite if statemetn
            camera.draw(fruit)

        for wall in barriers:
            if pac2.touches(wall):
                pac2.move_to_stop_overlapping(wall)
            if pac1.touches(wall):
                pac1.move_to_stop_overlapping(wall)
            camera.draw(gamebox.from_text(400,400,str(timer) + ' seconds', 75, 'red', bold=True, italic = False))
            camera.draw(wall)

        if pygame.K_UP in keys:
            pac1.y -= player_speed
        if pygame.K_DOWN in keys:
            pac1.y += player_speed
        if pygame.K_LEFT in keys:
            pac1.x -= player_speed
        if pygame.K_RIGHT in keys:
            pac1.x += player_speed
            ## Player 2 Controls
        if pygame.K_w in keys:
            pac2.y -= player_speed
        if pygame.K_s in keys:
            pac2.y += player_speed
        if pygame.K_a in keys:
            pac2.x -= player_speed
        if pygame.K_d in keys:
            pac2.x += player_speed
    else:
        camera.x = 400
        camera.y = 300

        pac1.yspeed = 0
        pac1.xspeed = 0
        pac2.yspeed = 0
        pac2.xspeed = 0
        if(points1 > points2):
            camera.draw(gamebox.from_text(400, 300, " Player 1 wins!", 60, 'red', bold=True,
                                      italic=False))
        elif (points1 < points2):
            camera.draw(gamebox.from_text(400, 300, " Player 2 wins!", 60, 'red', bold=True,
                                  italic=False))
        else:
            camera.draw(gamebox.from_text(400, 300, "It’s a tie!!", 60, 'red', bold = True, italic = False))
        camera.draw(gamebox.from_text(400, 500, " Game Over. Press spacebar to restart", 50, 'red', bold=True,
                                      italic=False))
        camera.display()
        if pygame.K_SPACE in keys:
            game_button = True
            points1 = 0
            points2 = 0

            collectibles = [
                # Above wall 1
                gamebox.from_image(75, 100, 'cherry.png'),
                gamebox.from_image(140, 100, 'cherry.png'),
                gamebox.from_image(205, 100, 'cherry.png'),

                ##In front of player 1
                gamebox.from_image(150, 450, 'cherry.png'),
                gamebox.from_image(150, 375, 'cherry.png'),
                gamebox.from_image(150, 300, 'cherry.png'),
                gamebox.from_image(200, 260, 'cherry.png'),
                # Next to wall 1
                gamebox.from_image(275, 180, 'cherry.png'),
                gamebox.from_image(275, 260, 'cherry.png'),
                gamebox.from_image(275, 100, 'cherry.png'),

                # Next to wall 3
                gamebox.from_image(400, 180, 'cherry.png'),
                gamebox.from_image(400, 260, 'cherry.png'),

                # Next to wall 6
                gamebox.from_image(85, 525, 'cherry.png'),
                gamebox.from_image(135, 525, 'cherry.png'),
                gamebox.from_image(185, 525, 'cherry.png'),
                gamebox.from_image(235, 525, 'cherry.png'),
                gamebox.from_image(250, 470, 'cherry.png'),
                gamebox.from_image(250, 420, 'cherry.png'),
                gamebox.from_image(250, 370, 'cherry.png'),
                gamebox.from_image(320, 370, 'cherry.png'),
                gamebox.from_image(385, 370, 'cherry.png'),

                # Next to wall 7
                gamebox.from_image(385, 420, 'cherry.png'),
                gamebox.from_image(385, 470, 'cherry.png'),
                gamebox.from_image(385, 525, 'cherry.png'),
                gamebox.from_image(435, 525, 'cherry.png'),
                gamebox.from_image(485, 525, 'cherry.png'),
                gamebox.from_image(535, 525, 'cherry.png'),
                gamebox.from_image(585, 525, 'cherry.png'),

                # Wall 8 and 7

                gamebox.from_image(500, 225, 'cherry.png'),
                gamebox.from_image(560, 225, 'cherry.png'),
                gamebox.from_image(500, 350, 'cherry.png'),
                gamebox.from_image(500, 425, 'cherry.png'),

                ## Top Wall 2
                gamebox.from_image(400, 40, 'cherry.png'),
                gamebox.from_image(400 + 75, 40, 'cherry.png'),
                gamebox.from_image(400 + 75 * 2, 40, 'cherry.png'),
                gamebox.from_image(400 + 75 * 3, 40, 'cherry.png'),
                gamebox.from_image(400 + 75 * 4, 40, 'cherry.png'),
                gamebox.from_image(400 + 75 * 5, 40, 'cherry.png'),
                gamebox.from_image(400 - 75, 40, 'cherry.png'),
                gamebox.from_image(400 - 75 * 2, 40, 'cherry.png'),
                gamebox.from_image(400 - 75 * 3, 40, 'cherry.png'),
                gamebox.from_image(400 - 75 * 4, 40, 'cherry.png'),
                gamebox.from_image(400 + 75 * 5, 115, 'cherry.png'),
                gamebox.from_image(400 + 75 * 4, 115, 'cherry.png'),
                gamebox.from_image(400 + 75 * 3, 115, 'cherry.png'),
                gamebox.from_image(400 + 75 * 2, 115, 'cherry.png'),
                gamebox.from_image(400 + 75, 115, 'cherry.png'),
                gamebox.from_image(400, 115, 'cherry.png'),

                ##Left Side Wall 10
                gamebox.from_image(625, 525, 'cherry.png'),
                gamebox.from_image(625, 450, 'cherry.png'),
                gamebox.from_image(625, 375, 'cherry.png'),
                gamebox.from_image(625, 300, 'cherry.png'),
                gamebox.from_image(625, 225, 'cherry.png'),

                ##Right Side Wall 10
                gamebox.from_image(700, 525, 'cherry.png'),
                gamebox.from_image(700, 450, 'cherry.png'),
                gamebox.from_image(700, 375, 'cherry.png'),
                gamebox.from_image(700, 300, 'cherry.png'),
                gamebox.from_image(700, 225, 'cherry.png')

            ]
            pac2 = gamebox.from_image(750, 300, "chara_2.png")
            pac1 = gamebox.from_image(50, 300, 'chara_1.png')
            measure_time = 0
            timer = 60


    camera.display()

    measure_time += 1
    if measure_time % 30 == 0:
        timer -= 1
    if timer < 0:
        game_button = False



gamebox.timer_loop(30, tick)