import pygame
import time
import random
 
pygame.init()
 
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)

scr_width = 800
scr_height = 600
 
screen = pygame.display.set_mode((scr_width, scr_height))
pygame.display.set_caption('Ant Trap')

pygame.mixer.music.load("ant music.wav")
pygame.mixer.music.play(-1)

clock = pygame.time.Clock()
 
ant_block = 10
speed = 15
 
font = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("bahnschrift", 35)
 
 
def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, red)
    screen.blit(value, [0, 0])
 
 
 
def Ant(ant_block, ant_list):
    for x in ant_list:
        pygame.draw.rect(screen, black, [x[0], x[1], ant_block, ant_block])

trapImg=pygame.image.load("spiderweb.png")
def trap1(x,y):
    screen.blit(trapImg,(x,y)) 
def trap2(x,y):
    screen.blit(trapImg,(x,y))
def trap3(x,y):
    screen.blit(trapImg,(x,y))
def trap4(x,y):
    screen.blit(trapImg,(x,y))
def trap5(x,y):
    screen.blit(trapImg,(x,y))

foodImg=pygame.image.load("food.png") 
def food1(x,y):
    screen.blit(foodImg,(x,y))
def food2(x,y):
    screen.blit(foodImg,(x,y))
def food3(x,y):
    screen.blit(foodImg,(x,y))
def food4(x,y):
    screen.blit(foodImg,(x,y))
 
def message(msg, color):
    mesg = font.render(msg, True, color)
    screen.blit(mesg, [scr_width / 6, scr_height / 3])
 
 
def gameLoop():
    game_over = False
    game_close = False
 
    x1 = scr_width / 2
    y1 = scr_height / 2
 
    x1_change = 0
    y1_change = 0
 
    ant_list = []
    Length = 1
 
    food1x=round(random.randrange(0,scr_width-ant_block)/10)*10
    food1y=round(random.randrange(0,scr_height-ant_block)/10)*10
    food2x=round(random.randrange(2,scr_width-ant_block)/10)*10
    food2y=round(random.randrange(2,scr_height-ant_block)/10)*10
    food3x=round(random.randrange(4,scr_width-ant_block)/10)*10
    food3y=round(random.randrange(4,scr_height-ant_block)/10)*10
    food4x=round(random.randrange(5,scr_width-ant_block)/10)*10
    food4y=round(random.randrange(5,scr_height-ant_block)/10)*10

    trap1x=round(random.randrange(0, scr_width - 20) / 10.0) * 10.0
    trap1y=round(random.randrange(0, scr_height - 20) / 10.0) * 10.0
    trap2x=round(random.randrange(1,scr_width-ant_block)/10)*10
    trap2y=round(random.randrange(1,scr_height-ant_block)/10)*10
    trap3x=round(random.randrange(2,scr_width-ant_block)/10)*10
    trap3y=round(random.randrange(2,scr_height-ant_block)/10)*10
    trap4x=round(random.randrange(3,scr_width-ant_block)/10)*10
    trap4y=round(random.randrange(3,scr_height-ant_block)/10)*10
    trap5x=round(random.randrange(5,scr_width-ant_block)/10)*10
    trap5y=round(random.randrange(5,scr_height-ant_block)/10)*10

    
    while not game_over:
        while game_close == True:
            screen.fill(black)
            message("Game Over! Press Y-Play Again or N-Quit", red)
            Your_score(Length - 1)
            pygame.mixer.music.stop()
            end_gamesound=pygame.mixer.Sound("end_game.mp3")
            pygame.mixer.Sound.play(end_gamesound)
            pygame.display.update() 
 
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_n:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_y:
                        gameLoop()
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -ant_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = ant_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -ant_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = ant_block
                    x1_change = 0
        if x1 >= scr_width or x1 < 0 or y1 >= scr_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        screen.fill(green)
        trap1(trap1x,trap1y)
        trap2(trap2x,trap2y)
        trap3(trap3x,trap3y)
        trap4(trap4x,trap4y)
        trap5(trap5x,trap5y)
        food1(food1x,food1y)
        food2(food2x,food2y)
        food3(food3x,food3y)
        food4(food4x,food4y)
        ant_Head = []
        ant_Head.append(x1)
        ant_Head.append(y1)
        ant_list.append(ant_Head)
        if len(ant_list) > Length:
            del ant_list[0]
 
        for x in ant_list[:-1]:
            if x == ant_Head:
                game_close = True
 
        Ant(ant_block, ant_list)
        Your_score(Length - 1)
 
        pygame.display.update()
        if Length==0:
            game_close= True
 
        if x1 == food1x and y1 == food1y:
            food1x = round(random.randrange(0, scr_width - ant_block) / 10) * 10
            food1y = round(random.randrange(0, scr_height - ant_block) / 10) * 10
            Length += 1
        if x1 == food2x and y1 == food2y:
            food2x = round(random.randrange(2, scr_width - ant_block) / 10) * 10
            food2y = round(random.randrange(2, scr_height - ant_block) / 10) * 10
            Length += 1
        if x1 == food3x and y1 == food3y:
            food3x = round(random.randrange(4, scr_width - ant_block) / 10) * 10
            food3y = round(random.randrange(4, scr_height - ant_block) / 10) * 10
            Length += 1
        if x1 == food4x and y1 == food4y:
            food4x = round(random.randrange(5, scr_width - ant_block) / 10) * 10
            food4y = round(random.randrange(5, scr_height - ant_block) / 10) * 10
            Length += 1
        if x1 == trap1x and y1 == trap1y:
            trap1x = round(random.randrange(0, scr_width - 20) / 10) * 10
            trap1y = round(random.randrange(0, scr_height - 20) / 10) * 10
            Length -= 1
        if x1 == trap2x and y1 == trap2y:
            trap2x = round(random.randrange(1, scr_width - 20) / 10) * 10
            trap2y = round(random.randrange(1, scr_height - 20) / 10) * 10
            Length -= 1
        if x1 == trap3x and y1 == trap3y:
            trap3x = round(random.randrange(2, scr_width - 20) / 10) * 10
            trap3y = round(random.randrange(2, scr_height - 20) / 10) * 10
            Length -= 1
        if x1 == trap4x and y1 == trap4y:
            trap4x = round(random.randrange(3, scr_width - 20) / 10) * 10
            trap4y = round(random.randrange(3, scr_height - 20) / 10) * 10
            Length -= 1
        if x1 == trap5x and y1 == trap5y:
            trap5x = round(random.randrange(5, scr_width - 20) / 10) * 10
            trap5y = round(random.randrange(5, scr_height - 20) / 10) * 10
            Length -= 1
        clock.tick(speed)
 
    pygame.quit()
    quit()
 
 
gameLoop()
