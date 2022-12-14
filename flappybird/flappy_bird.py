import pygame
from random import *
pygame.init()
WIDTH,HEIGHT = 400,600
screen= pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("flappy_bird")
running = True
GREEN = (0,200,0)
BLUE = (0,0,255)
RED = (255,0,0)
BLACK = (0,0,0)
YELLOW = (255,255,0)

clock = pygame.time.Clock()

TUBE_WIDTH = 50
BULE_SPEED = 4
TUBE_VELOCITY = 3
TUBE_GAP = 150

BIRD_X = 50
bird_y = 400
BIRD_WIDTH = 35
BIRD_HEIGHT = 35

tube1_x = 600
tube2_x = 800
tube3_x = 1000

tube1_height = randint(100,400)
tube2_height = randint(100,400)
tube3_height = randint(100,400)
bule1_height = randint(600,1000)
bule2_height = randint(600,1000)
bule3_height = randint(600,1000)
bule7_height = randint(0,600)
bule8_height = randint(0,600)
bule9_height = randint(0,600)
bird_drop_velocity = 0
GRAVITY = 0.5

score = 0
font = pygame.font.SysFont("sans",20)

tube1_pass = False
tube2_pass = False
tube3_pass = False

pausing = False
background = pygame.image.load("background_flappy_bird.png")
flappy_bird = pygame.image.load("flappy_bird.png")
flappy_bird = pygame.transform.scale(flappy_bird,(BIRD_WIDTH,BIRD_HEIGHT))
bule = pygame.image.load("missile.png")

while running:
    clock.tick(60)
    screen.fill("GREEN")
    screen.blit(background,(0,0))
    
    tube1_rect = pygame.draw.rect(screen,BLUE,(tube1_x,0,TUBE_WIDTH,tube1_height))
    tube2_rect = pygame.draw.rect(screen,BLUE,(tube2_x,0,TUBE_WIDTH,tube2_height))
    tube3_rect = pygame.draw.rect(screen,BLUE,(tube3_x,0,TUBE_WIDTH,tube3_height))

    tube1_rect_inv = pygame.draw.rect(screen,BLUE,(tube1_x,tube1_height+TUBE_GAP,TUBE_WIDTH,HEIGHT-tube1_height+TUBE_GAP))
    tube2_rect_inv = pygame.draw.rect(screen,BLUE,(tube2_x,tube2_height+TUBE_GAP,TUBE_WIDTH,HEIGHT-tube2_height+TUBE_GAP))
    tube3_rect_inv = pygame.draw.rect(screen,BLUE,(tube3_x,tube3_height+TUBE_GAP,TUBE_WIDTH,HEIGHT-tube3_height+TUBE_GAP))

    bulet1 = screen.blit(bule,(bule1_height,bule7_height))
    bulet2 = screen.blit(bule,(bule2_height,bule8_height))
    bulet3 = screen.blit(bule,(bule3_height,bule9_height))
        
    sand = pygame.draw.rect(screen,YELLOW,(0,550,400,50))

    tube1_x -= TUBE_VELOCITY
    tube2_x -= TUBE_VELOCITY
    tube3_x -= TUBE_VELOCITY
    bule1_height -= BULE_SPEED
    bule2_height -= BULE_SPEED
    bule3_height -= BULE_SPEED
    
    bird_rect = screen.blit(flappy_bird,(BIRD_X,bird_y))

    bird_y += bird_drop_velocity
    bird_drop_velocity += GRAVITY

    if tube1_x < -TUBE_WIDTH:
        tube1_x = 550
        tube1_height = randint(100,400)
        tube1_pass  = False
    if tube2_x < -TUBE_WIDTH:
        tube2_x = 550
        tub2_height = randint(100,400)
        tube2_pass = False
    if tube3_x < -TUBE_WIDTH:
        tube3_x = 550
        tube3_height = randint(100,400)
        tube3_pass = False

    if bule1_height < -TUBE_WIDTH:
        bule1_height = randint(600,1000)
    if bule2_height < -TUBE_WIDTH:
        bule2_height = randint(600,1000)
    if bule3_height < -TUBE_WIDTH:
        bule3_height = randint(600,1000)

    score_text = font.render("Score: " + str(score),True,BLACK)
    screen.blit(score_text,(5,5))

    if tube1_x + TUBE_WIDTH <= BIRD_X and tube1_pass == False:
        score +=1
        tube1_pass = True
    if tube2_x + TUBE_WIDTH <= BIRD_X and tube2_pass == False:
        score +=1
        tube2_pass = True
    if tube3_x + TUBE_WIDTH <= BIRD_X and tube3_pass == False:
        score +=1
        tube3_pass = True
    
    for tube in [tube1_rect,tube2_rect,tube3_rect,tube1_rect_inv,tube2_rect_inv,tube3_rect_inv,sand,bulet1,bulet2,bulet3]:
        if bird_rect.colliderect(tube):
            pausing = True
            TUBE_VELOCITY = 0
            BULE_SPEED = 0
            bule1_height = randint(600,1000)
            bule2_height = randint(600,1000)
            bule3_height = randint(600,1000)
            bule7_height = randint(0,600)
            bule8_height = randint(0,600)
            bule9_height = randint(0,600)
            bird_drop_velocity = 0
            game_over_txt = font.render("Game over, score: "+str(score),True,BLACK)
            press_space_txt = font.render("Press Space to Continue",True,BLACK)
            screen.blit(game_over_txt,(200,300))
            screen.blit(press_space_txt,(170,400))
            

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if pausing:
                    bird_y = 400
                    TUBE_VELOCITY = 3
                    BULE_SPEED = 4
                    tube1_x = 600
                    tube2_x = 800
                    tube3_x = 1000
                    score =0
                    pausing = False
                bird_drop_velocity = 0
                bird_drop_velocity -= 10

    pygame.display.flip()
pygame.quit()