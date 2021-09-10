import math

import pygame
import random
#initialize the pygame
pygame.init()

#game window

screen=pygame.display.set_mode((800,800))  #weight and height pixels

#title and icon
pygame.display.set_caption("Selen's first game trial")
icon=pygame.image.load('ghost.png')
pygame.display.set_icon(icon)

#background
background=pygame.image.load('3946.jpg')
background=pygame.transform.scale(background,(800,800))

#player
player_img=pygame.image.load('raphael.png')
player_img=pygame.transform.scale(player_img,(200,200))
playerX=150
playerY=550
playerX_change=0.5
playerY_change=0.5


def player(x,y):
    screen.blit(player_img,(x,y))

#sword
boom_img=pygame.image.load('sword.png')
boom_img=pygame.transform.scale(boom_img,(100,100))
boomX=[]
boomY = []
for i in range(2):
    boomX.append(0)
    boomY.append(550)
boomY_change=1.2
boom_state="ready"

def fire_boom():
    global boom_state
    boom_state="fire"
    screen.blit(boom_img,(boomX[0],boomY[0]+10))
    screen.blit(boom_img,(boomX[1],boomY[1]+10))


#score
score_value=0
font=pygame.font.Font('freesansbold.ttf',32)
textX=600
textY=10


def show_score(x,y):
    score=font.render("SCORE : " + str(score_value) ,True,(255,255,255))
    screen.blit(score,(x,y))

#game over text
game_over=False
def game_over_text():
    over_text=font.render("GAME OVER ",True,(255,255,255))
    screen.blit(over_text,(200,250))

#enemy
enemy_img = pygame.image.load('en128.png')
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 2

for i in range(num_of_enemies):
    enemyX.append(random.randint(0, 600))
    enemyY.append(random.randint(0, 400))
    enemyX_change.append(0.5)
    enemyY_change.append(0.5)

def enemy (x, y):
    screen.blit(enemy_img, (x, y))

#checking collision
def isCollision (eX, eY, bX, bY):
    if bY <= eY+100 and bX + 70 >= eX and eX + 100 >= bX:
        return True
    else:
        return False



#game loop
running=True
while running:
    # rgb values of background
    screen.fill((255, 255, 255))
    #background image
    screen.blit(background,(0,0))
    if game_over:
        game_over_text()
        pygame.display.update()
        continue
    #manage events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
        #if key stroke is pressed check whether its right ,or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if boom_state == "ready":
                    boomX[0] = playerX - 20
                    boomX[1] = playerX + 125
                    fire_boom()

    if playerX <= 0:
        playerX_change = 0.7
    elif playerX >= 600:
        playerX_change = -0.7

    playerX+=playerX_change

    #checking boundaries for both palyer and enemy
    if playerX<=0:
        playerX=0
    elif playerX>=600:
        playerX=600

    for i in range(num_of_enemies):
        if enemyX[i]<=0:
            enemyX_change[i]=0.7
            enemyY[i]+=enemyY_change[i]
        elif enemyX[i]>=600:
            enemyX_change[i]=-0.7
            enemyY[i] += enemyY_change[i]

        enemyX[i] += enemyX_change[i]

        # collision
        for j in range(2):
            collision = isCollision(enemyX[i], enemyY[i], boomX[j], boomY[j])
            if collision :
                boomY[0] = boomY[1] = 480
                boom_state = "ready"
                score_value += 1
                enemyX[i] = random.randint(0, 600)
                enemyY[i] = random.randint(0, 400)


        enemy(enemyX[i], enemyY[i])

    for i in range(2):
        # sword movement
        if boomY[i] <= 0:
            boomY[i] = 480
            boom_state = "ready"
        if boom_state == "fire":
            fire_boom()
            boomY[i] -= boomY_change

    if score_value == 3:
        game_over = True


    #call functions
    player(playerX,playerY)
    show_score(textX,textY)

    #update(it's important to add update function to update display attributes )
    pygame.display.update()
