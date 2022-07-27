from turtle import left
import pygame,random
r = True
while r:
    pygame.init()
    HEIGHT = 780
    WIDTH = 800
    screen = pygame.display.set_mode((WIDTH,HEIGHT))
    BLACK = (0,0,0)
    RED = (255,0,0)
    WHITE = (255,255,255)
    GREEN = (0,255,0)
    YELLOW = (0,255,255)
    BLUE = (0,0,255)
    GREY = (120,120,120)
    start_running = True
    rect_x = WIDTH/2
    rect_y = HEIGHT / 2
    rect_x1 = WIDTH/2
    rect_y1 = HEIGHT / 2
    change_x = 0
    change_y = 0
    change_x1 = 0
    change_y1 = 0
    bullet1_x_right = random.randint(800,1000)
    bullet1_y_right = random.randint(0,760)
    bullet2_x_right = random.randint(800,1000)
    bullet2_y_right = random.randint(0,760)
    bullet3_x_right = random.randint(800,1000)
    bullet3_y_right = random.randint(0,760)
    bullet4_x_right = random.randint(800,1000)
    bullet4_y_right = random.randint(0,760)
    bullet5_x_right = random.randint(800,1000)
    bullet5_y_right = random.randint(0,760)
    bullet6_x_right = random.randint(800,1000)
    bullet6_y_right = random.randint(0,760)
    bullet7_x_right = random.randint(800,1000)
    bullet7_y_right = random.randint(0,760)
    bullet8_x_right = random.randint(800,1000)
    bullet8_y_right = random.randint(0,760)
    bullet9_x_right = random.randint(800,1000)
    bullet9_y_right = random.randint(0,760)
    bullet10_x_right = random.randint(800,1000)
    bullet10_y_right = random.randint(0,760)
    bullet1_x_left = random.randint(-230,-30)
    bullet1_y_left = random.randint(0,760)
    bullet2_x_left = random.randint(-230,-30)
    bullet2_y_left = random.randint(0,760)
    bullet3_x_left = random.randint(-230,-30)
    bullet3_y_left = random.randint(0,760)
    bullet4_x_left = random.randint(-230,-30)
    bullet4_y_left = random.randint(0,760)
    bullet5_x_left = random.randint(-230,-30)
    bullet5_y_left = random.randint(0,760)
    bullet6_x_left = random.randint(-230,-30)
    bullet6_y_left = random.randint(0,760)
    bullet7_x_left = random.randint(-230,-30)
    bullet7_y_left = random.randint(0,760)
    bullet8_x_left = random.randint(-230,-30)
    bullet8_y_left = random.randint(0,760)
    bullet9_x_left = random.randint(-230,-30)
    bullet9_y_left = random.randint(0,760)
    bullet10_x_left = random.randint(-230,-30)
    bullet10_y_left = random.randint(0,760)
    bullet1_x_up = random.randint(0,770)
    bullet1_y_up = random.randint(-230,-30)
    bullet2_x_up = random.randint(0,770)
    bullet2_y_up = random.randint(-230,-30)
    bullet3_x_up = random.randint(0,770)
    bullet3_y_up = random.randint(-230,-30)
    bullet4_x_up = random.randint(0,770)
    bullet4_y_up = random.randint(-230,-30)
    bullet5_x_up = random.randint(0,770)
    bullet5_y_up = random.randint(-230,-30)
    bullet6_x_up = random.randint(0,770)
    bullet6_y_up = random.randint(-230,-30)
    bullet7_x_up = random.randint(0,770)
    bullet7_y_up = random.randint(-230,-30)
    bullet8_x_up = random.randint(0,770)
    bullet8_y_up = random.randint(-230,-30)
    bullet9_x_up = random.randint(0,770)
    bullet9_y_up = random.randint(-230,-30)
    bullet10_x_up = random.randint(0,770)
    bullet10_y_up = random.randint(-230,-30)
    bullet1_x_down = random.randint(0,770)
    bullet1_y_down = random.randint(780,980)
    bullet2_x_down = random.randint(0,770)
    bullet2_y_down = random.randint(780,980)
    bullet3_x_down = random.randint(0,770)
    bullet3_y_down = random.randint(780,980)
    bullet4_x_down = random.randint(0,770)
    bullet4_y_down = random.randint(780,980)
    bullet5_x_down = random.randint(0,770)
    bullet5_y_down = random.randint(780,980)
    bullet6_x_down = random.randint(0,770)
    bullet6_y_down = random.randint(780,980)
    bullet7_x_down = random.randint(0,770)
    bullet7_y_down = random.randint(780,980)
    bullet8_x_down = random.randint(0,770)
    bullet8_y_down = random.randint(780,980)
    bullet9_x_down = random.randint(0,770)
    bullet9_y_down = random.randint(780,980)
    bullet10_x_down = random.randint(0,770)
    bullet10_y_down = random.randint(780,980)
    move_bullet_right = 2
    move_bullet_left = 2
    move_bullet_up = 2
    move_bullet_down = 2
    clock = pygame.time.Clock()
    score = 0
    font = pygame.font.SysFont("sans",30)
    start_score = False
    pausing = True
    score_red = 0
    running = False
    running1 = False
    score_green = 0
    pausing_red= False
    pausing_green = False
    move_score_red = 0
    move_score_green = 0
    score_best = 0
    ck = 4.5
    right2 = False
    right3 = False
    right4 = False
    right5 = False
    right6 = False
    right7 = False
    right8 = False
    right9 = False
    right10 = False
    
    left2 = False
    left3 = False
    left4 = False
    left5 = False
    left6 = False
    left7 = False
    left8 = False
    left9 = False
    left10 = False
    
    up2 = False
    up3 = False
    up4 = False
    up5 = False
    up6 = False
    up7 = False
    up8 = False
    up9 = False
    up10 = False
    down2 = False
    down3 = False
    down4 = False
    down5 = False
    down6 = False
    down7 = False
    down8 = False
    down9 = False
    down10 = False

    cright = True
    cyright= True
    
    while start_running:
        pygame.display.set_caption("chọn để bắt đầu trò chơi")
        screen.fill(GREY)
        pygame.draw.rect(screen,WHITE,(150,150,200,400))
        pygame.draw.rect(screen,BLACK,(155,155,190,390))
        pygame.draw.rect(screen,WHITE,(450,150,200,400))
        pygame.draw.rect(screen,BLACK,(455,155,190,390))
        font_1 = font.render("Tutorial",True,WHITE)
        font_2 = font.render("Play",True,WHITE)
        screen.blit(font_1,(190,310))
        screen.blit(font_2,(520,310))
        running = False
        running1 = False
        mouse_x,mouse_y = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                start_running = False
                r = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if (155<mouse_x<345) and (155<mouse_y<545):
                        running1=True
                        start_running = False
                    if (455<mouse_x<645) and (155<mouse_y<545):
                        running = True
                        start_running = False
        pygame.display.flip()
    while running:
        mouse_x,mouse_y=pygame.mouse.get_pos()
        pygame.display.set_caption("game 1 người vượt chường ngại vật")
        screen.fill(BLACK)
        clock.tick(60)
        font_score = font.render("Score: "+str(score),True,WHITE)
        screen.blit(font_score,(380,5))

        rect = pygame.draw.rect(screen,RED,(rect_x,rect_y,20,20))
        if cright:
            right2 = True
            right3 = True
            right4 = True
            right5 = True
            right6 = True
            right7 = True
            right8 = True
            right9 = True
            right10 = True
            left2 = True
            left3 = True
            left4 = True
            left5 = True
            left6 = True
            left7 = True
            left8 = True
            left9 = True
            left10 = True
            up2 = True
            up3 = True
            up4 = True
            up5 = True
            up6 = True
            up7 = True
            up8 = True
            up9 = True
            up10 = True
            down2 = True
            down3 = True
            down4 = True
            down5 = True
            down6 = True
            down7 = True
            down8 = True
            down9 = True
            down10 = True
            cright = False
        bullet1_right = pygame.draw.rect(screen,WHITE,(bullet1_x_right,bullet1_y_right,30,20))
        bullet1_x_right -= move_bullet_right
        if right2:
            bullet2_right = pygame.draw.rect(screen,WHITE,(bullet2_x_right,bullet2_y_right,30,20))
            bullet2_x_right -= move_bullet_right
        if right3:
            bullet3_right = pygame.draw.rect(screen,WHITE,(bullet3_x_right,bullet3_y_right,30,20))
            bullet3_x_right -= move_bullet_right
        if right4:
            bullet4_right = pygame.draw.rect(screen,WHITE,(bullet4_x_right,bullet4_y_right,30,20))
            bullet4_x_right -= move_bullet_right
        if right5:
            bullet5_right = pygame.draw.rect(screen,WHITE,(bullet5_x_right,bullet5_y_right,30,20))
            bullet5_x_right -= move_bullet_right
        if right6:
            bullet6_right = pygame.draw.rect(screen,WHITE,(bullet6_x_right,bullet6_y_right,30,20))
            bullet6_x_right -= move_bullet_right
        if right7:
            bullet7_right = pygame.draw.rect(screen,WHITE,(bullet7_x_right,bullet7_y_right,30,20))
            bullet7_x_right -= move_bullet_right
        if right8:
            bullet8_right = pygame.draw.rect(screen,WHITE,(bullet8_x_right,bullet8_y_right,30,20))
            bullet8_x_right -= move_bullet_right
        if right9:
            bullet9_right = pygame.draw.rect(screen,WHITE,(bullet9_x_right,bullet9_y_right,30,20))
            bullet9_x_right -= move_bullet_right
        if right10:
            bullet10_right = pygame.draw.rect(screen,WHITE,(bullet10_x_right,bullet10_y_right,30,20))
            bullet10_x_right -= move_bullet_right
        
        
        bullet1_left = pygame.draw.rect(screen,WHITE,(bullet1_x_left,bullet1_y_left,30,20))
        bullet1_x_left += move_bullet_left
        if left2:
            bullet2_left = pygame.draw.rect(screen,WHITE,(bullet2_x_left,bullet2_y_left,30,20))
            bullet2_x_left += move_bullet_left
        if left3:
            bullet3_left = pygame.draw.rect(screen,WHITE,(bullet3_x_left,bullet3_y_left,30,20))
            bullet3_x_left += move_bullet_left
        if left4:
            bullet4_left = pygame.draw.rect(screen,WHITE,(bullet4_x_left,bullet4_y_left,30,20))
            bullet4_x_left += move_bullet_left
        if left5:
            bullet5_left = pygame.draw.rect(screen,WHITE,(bullet5_x_left,bullet5_y_left,30,20))
            bullet5_x_left += move_bullet_left
        if left6:
            bullet6_left = pygame.draw.rect(screen,WHITE,(bullet6_x_left,bullet6_y_left,30,20))
            bullet6_x_left += move_bullet_left
        if left7:
            bullet7_left = pygame.draw.rect(screen,WHITE,(bullet7_x_left,bullet7_y_left,30,20))
            bullet7_x_left += move_bullet_left
        if left8:
            bullet8_left = pygame.draw.rect(screen,WHITE,(bullet8_x_left,bullet8_y_left,30,20))
            bullet8_x_left += move_bullet_left
        if left9:
            bullet9_left = pygame.draw.rect(screen,WHITE,(bullet9_x_left,bullet9_y_left,30,20))
            bullet9_x_left += move_bullet_left
        if left10:
            bullet10_left = pygame.draw.rect(screen,WHITE,(bullet10_x_left,bullet10_y_left,30,20))
            bullet10_x_left += move_bullet_left

        bullet1_up = pygame.draw.rect(screen,WHITE,(bullet1_x_up,bullet1_y_up,20,30))
        bullet1_y_up += move_bullet_up
        if up2:
            bullet2_up = pygame.draw.rect(screen,WHITE,(bullet2_x_up,bullet2_y_up,20,30))
            bullet2_y_up += move_bullet_up
        if up3:
            bullet3_up = pygame.draw.rect(screen,WHITE,(bullet3_x_up,bullet3_y_up,20,30))
            bullet3_y_up += move_bullet_up
        if up4:
            bullet4_up = pygame.draw.rect(screen,WHITE,(bullet4_x_up,bullet4_y_up,20,30))
            bullet4_y_up += move_bullet_up
        if up5:
            bullet5_up = pygame.draw.rect(screen,WHITE,(bullet5_x_up,bullet5_y_up,20,30))
            bullet5_y_up += move_bullet_up
        if up6:
            bullet6_up = pygame.draw.rect(screen,WHITE,(bullet6_x_up,bullet6_y_up,20,30))
            bullet6_y_up += move_bullet_up
        if up7:
            bullet7_up = pygame.draw.rect(screen,WHITE,(bullet7_x_up,bullet7_y_up,20,30))
            bullet7_y_up += move_bullet_up
        if up8:
            bullet8_up = pygame.draw.rect(screen,WHITE,(bullet8_x_up,bullet8_y_up,20,30))
            bullet8_y_up += move_bullet_up
        if up9:
            bullet9_up = pygame.draw.rect(screen,WHITE,(bullet9_x_up,bullet9_y_up,20,30))
            bullet9_y_up += move_bullet_up
        if up10:
            bullet10_up = pygame.draw.rect(screen,WHITE,(bullet10_x_up,bullet10_y_up,20,30))
            bullet10_y_up += move_bullet_up

        bullet1_down = pygame.draw.rect(screen,WHITE,(bullet1_x_down,bullet1_y_down,20,30))
        bullet1_y_down -= move_bullet_down
        if down2:
            bullet2_down = pygame.draw.rect(screen,WHITE,(bullet2_x_down,bullet2_y_down,20,30))
            bullet2_y_down -= move_bullet_down
        if down3:
            bullet3_down = pygame.draw.rect(screen,WHITE,(bullet3_x_down,bullet3_y_down,20,30))
            bullet3_y_down -= move_bullet_down
        if down4:
            bullet4_down = pygame.draw.rect(screen,WHITE,(bullet4_x_down,bullet4_y_down,20,30))
            bullet4_y_down -= move_bullet_down
        if down5:
            bullet5_down = pygame.draw.rect(screen,WHITE,(bullet5_x_down,bullet5_y_down,20,30))
            bullet5_y_down -= move_bullet_down
        if down6:
            bullet6_down = pygame.draw.rect(screen,WHITE,(bullet6_x_down,bullet6_y_down,20,30))
            bullet6_y_down -= move_bullet_down
        if down7:
            bullet7_down = pygame.draw.rect(screen,WHITE,(bullet7_x_down,bullet7_y_down,20,30))
            bullet7_y_down -= move_bullet_down
        if down8:
            bullet8_down = pygame.draw.rect(screen,WHITE,(bullet8_x_down,bullet8_y_down,20,30))
            bullet8_y_down -= move_bullet_down
        if down9:
            bullet9_down = pygame.draw.rect(screen,WHITE,(bullet9_x_down,bullet9_y_down,20,30))
            bullet9_y_down -= move_bullet_down
        if down10:
            bullet10_down = pygame.draw.rect(screen,WHITE,(bullet10_x_down,bullet10_y_down,20,30))
            bullet10_y_down -= move_bullet_down


        if cyright:
            right2 = False
            right3 = False
            right4 = False
            right5 = False
            right6 = False
            right7 = False
            right8 = False
            right9 = False
            right10 = False
            left2 = False
            left3 = False
            left4 = False
            left5 = False
            left6 = False
            left7 = False
            left8 = False
            left9 = False
            left10 = False
            up2 = False
            up3 = False
            up4 = False
            up5 = False
            up6 = False
            up7 = False
            up8 = False
            up9 = False
            up10 = False
            down2 = False
            down3 = False
            down4 = False
            down5 = False
            down6 = False
            down7 = False
            down8 = False
            down9 = False
            down10 = False
            cyright= False

        pygame.draw.rect(screen,YELLOW,(0,50,35,35))
        font_back = font.render("<",True,BLACK)
        screen.blit(font_back,(0,50))

        for i in [bullet1_right,bullet2_right,bullet3_right,bullet4_right,bullet5_right,bullet6_right,bullet7_right,bullet8_right,bullet9_right,bullet10_right,bullet1_left,bullet2_left,bullet3_left,bullet4_left,bullet5_left,bullet6_left,bullet7_left,bullet8_left,bullet9_left,bullet10_left,bullet1_up,bullet2_up,bullet3_up,bullet4_up,bullet5_up,bullet6_up,bullet7_up,bullet8_up,bullet9_up,bullet10_up,bullet1_down,bullet2_down,bullet3_down,bullet4_down,bullet5_down,bullet6_down,bullet7_down,bullet8_down,bullet9_down,bullet10_down]:
            if rect.colliderect(i):
                move_bullet_right = 0
                move_bullet_left = 0
                move_bullet_up = 0
                move_bullet_down = 0
                pausing = False

        if bullet1_x_right < -30:
            bullet1_x_right = random.randint(800,1000)
            bullet1_y_right = random.randint(0,760)
            if move_bullet_right <ck:
                move_bullet_right += 0.2
            if right9:
                right10=True
            if right8:
                right9 = True
            if right7:
                right8=True
            if right6:
                right7=True
            if right5:
                right6 = True
            if right4:
                right5 = True
            if right3:
                right4 = True
            if right2:
                right3 = True
            right2 = True
            score += 1
        if bullet2_x_right < -30:
            bullet2_x_right = random.randint(800,1000)
            bullet2_y_right = random.randint(0,760)
            if move_bullet_right <ck:
                move_bullet_right += 0.2
            score += 1
        if bullet3_x_right < -30:
            bullet3_x_right = random.randint(800,1000)
            bullet3_y_right = random.randint(0,760)
            if move_bullet_right <ck:
                move_bullet_right += 0.2
            score += 1
        if bullet4_x_right < -30:
            bullet4_x_right = random.randint(800,1000)
            bullet4_y_right = random.randint(0,760)
            if move_bullet_right <ck:
                move_bullet_right += 0.2
            score += 1
        if bullet5_x_right < -30:
            bullet5_x_right = random.randint(800,1000)
            bullet5_y_right = random.randint(0,760)
            if move_bullet_right <ck:
                move_bullet_right += 0.2
            score += 1
        if bullet6_x_right < -30:
            bullet6_x_right = random.randint(800,1000)
            bullet6_y_right = random.randint(0,760)
            if move_bullet_right <ck:
                move_bullet_right += 0.2
            score += 1
        if bullet7_x_right < -30:
            bullet7_x_right = random.randint(800,1000)
            bullet7_y_right = random.randint(0,760)
            if move_bullet_right <ck:
                move_bullet_right += 0.2
            score += 1
        if bullet8_x_right < -30:
            bullet8_x_right = random.randint(800,1000)
            bullet8_y_right = random.randint(0,760)
            if move_bullet_right <ck:
                move_bullet_right += 0.2
            score += 1
        if bullet9_x_right < -30:
            bullet9_x_right = random.randint(800,1000)
            bullet9_y_right = random.randint(0,760)
            if move_bullet_right <ck:
                move_bullet_right += 0.2
            score += 1
        if bullet10_x_right < -30:
            bullet10_x_right = random.randint(800,1000)
            bullet10_y_right = random.randint(0,760)
            if move_bullet_right <ck:
                move_bullet_right += 0.2
            score += 1



        if bullet1_x_left > 830:
            bullet1_x_left = random.randint(-230,-30)
            bullet1_y_left = random.randint(0,760)
            if move_bullet_left <ck:
                move_bullet_left += 0.2
            if left9:
                left10=True
            if left8:
                left9 = True
            if left7:
                left8=True
            if left6:
                left7=True
            if left5:
                left6 = True
            if left4:
                left5 = True
            if left3:
                left4 = True
            if left2:
                left3 = True
            left2 = True
            score += 1

        if bullet2_x_left > 830:
            bullet2_x_left = random.randint(-230,-30)
            bullet2_y_left = random.randint(0,760)
            if move_bullet_left <ck:
                move_bullet_left += 0.2
            score += 1

        if bullet3_x_left > 830:
            bullet3_x_left = random.randint(-230,-30)
            bullet3_y_left = random.randint(0,760)
            if move_bullet_left <ck:
                move_bullet_left += 0.2
            score += 1
        if bullet4_x_left > 830:
            bullet4_x_left = random.randint(-230,-30)
            bullet4_y_left = random.randint(0,760)
            if move_bullet_left <ck:
                move_bullet_left += 0.2
            score += 1
        if bullet5_x_left > 830:
            bullet5_x_left = random.randint(-230,-30)
            bullet5_y_left = random.randint(0,760)
            if move_bullet_left <ck:
                move_bullet_left += 0.2
            score += 1
        if bullet6_x_left > 830:
            bullet6_x_left = random.randint(-230,-30)
            bullet6_y_left = random.randint(0,760)
            if move_bullet_left <ck:
                move_bullet_left += 0.2
            score += 1
        if bullet7_x_left > 830:
            bullet7_x_left = random.randint(-230,-30)
            bullet7_y_left = random.randint(0,760)
            if move_bullet_left <ck:
                move_bullet_left += 0.2
            score += 1
        if bullet8_x_left > 830:
            bullet8_x_left = random.randint(-230,-30)
            bullet8_y_left = random.randint(0,760)
            if move_bullet_left <ck:
                move_bullet_left += 0.2
            score += 1
        if bullet9_x_left > 830:
            bullet9_x_left = random.randint(-230,-30)
            bullet9_y_left = random.randint(0,760)
            if move_bullet_left <ck:
                move_bullet_left += 0.2
            score += 1
        if bullet10_x_left > 830:
            bullet10_x_left = random.randint(-230,-30)
            bullet10_y_left = random.randint(0,760)
            if move_bullet_left <ck:
                move_bullet_left += 0.2
            score += 1
        

        if bullet1_y_up > 810:
            bullet1_x_up = random.randint(0,770)
            bullet1_y_up = random.randint(-230,-30)
            if move_bullet_up <ck:
                move_bullet_up += 0.2
            if up9:
                up10=True
            if up8:
                up9 = True
            if up7:
                up8=True
            if up6:
                up7=True
            if up5:
                up6 = True
            if up4:
                up5 = True
            if up3:
                up4 = True
            if up2:
                up3 = True
            up2 = True
            score += 1

        if bullet2_y_up > 810:
            bullet2_x_up = random.randint(0,770)
            bullet2_y_up = random.randint(-230,-30)
            if move_bullet_up < ck:
                move_bullet_up += 0.2
            score += 1

        if bullet3_y_up > 810:
            bullet3_x_up = random.randint(0,770)
            bullet3_y_up = random.randint(-230,-30)
            if move_bullet_up < ck:
                move_bullet_up += 0.2
            score += 1
        if bullet4_y_up > 810:
            bullet4_x_up = random.randint(0,770)
            bullet4_y_up = random.randint(-230,-30)
            if move_bullet_up < ck:
                move_bullet_up += 0.2
            score += 1
        if bullet5_y_up > 810:
            bullet5_x_up = random.randint(0,770)
            bullet5_y_up = random.randint(-230,-30)
            if move_bullet_up < ck:
                move_bullet_up += 0.2
            score += 1
        if bullet6_y_up > 810:
            bullet6_x_up = random.randint(0,770)
            bullet6_y_up = random.randint(-230,-30)
            if move_bullet_up < ck:
                move_bullet_up += 0.2
            score += 1
        if bullet7_y_up > 810:
            bullet7_x_up = random.randint(0,770)
            bullet7_y_up = random.randint(-230,-30)
            if move_bullet_up < ck:
                move_bullet_up += 0.2
            score += 1
        if bullet8_y_up > 810:
            bullet8_x_up = random.randint(0,770)
            bullet8_y_up = random.randint(-230,-30)
            if move_bullet_up < ck:
                move_bullet_up += 0.2
            score += 1
        if bullet9_y_up > 810:
            bullet9_x_up = random.randint(0,770)
            bullet9_y_up = random.randint(-230,-30)
            if move_bullet_up < ck:
                move_bullet_up += 0.2
            score += 1
        if bullet10_y_up > 810:
            bullet10_x_up = random.randint(0,770)
            bullet10_y_up = random.randint(-230,-30)
            if move_bullet_up < ck:
                move_bullet_up += 0.2
            score += 1


        if bullet1_y_down < -30:
            bullet1_x_down = random.randint(0,770)
            bullet1_y_down = random.randint(780,980)
            if move_bullet_down <ck:
                move_bullet_down += 0.2
            if down9:
                down10=True
            if down8:
                down9 = True
            if down7:
                down8=True
            if down6:
                down7=True
            if down5:
                down6 = True
            if down4:
                down5 = True
            if down3:
                down4 = True
            if down2:
                down3 = True
            down2 = True
            score += 1

        if bullet2_y_down < -30:
            bullet2_x_down = random.randint(0,770)
            bullet2_y_down = random.randint(780,980)
            if move_bullet_down < ck:
                move_bullet_down += 0.2
            score += 1

        if bullet3_y_down < -30:
            bullet3_x_down = random.randint(0,770)
            bullet3_y_down = random.randint(780,980)
            if move_bullet_down < ck:
                move_bullet_down += 0.2
            score += 1
        if bullet4_y_down < -30:
            bullet4_x_down = random.randint(0,770)
            bullet4_y_down = random.randint(780,980)
            if move_bullet_down < ck:
                move_bullet_down += 0.2
            score += 1
        if bullet5_y_down < -30:
            bullet5_x_down = random.randint(0,770)
            bullet5_y_down = random.randint(780,980)
            if move_bullet_down < ck:
                move_bullet_down += 0.2
            score += 1
        if bullet6_y_down < -30:
            bullet6_x_down = random.randint(0,770)
            bullet6_y_down = random.randint(780,980)
            if move_bullet_down < ck:
                move_bullet_down += 0.2
            score += 1
        if bullet7_y_down < -30:
            bullet7_x_down = random.randint(0,770)
            bullet7_y_down = random.randint(780,980)
            if move_bullet_down < ck:
                move_bullet_down += 0.2
            score += 1
        if bullet8_y_down < -30:
            bullet8_x_down = random.randint(0,770)
            bullet8_y_down = random.randint(780,980)
            if move_bullet_down < ck:
                move_bullet_down += 0.2
            score += 1
        if bullet9_y_down < -30:
            bullet9_x_down = random.randint(0,770)
            bullet9_y_down = random.randint(780,980)
            if move_bullet_down < ck:
                move_bullet_down += 0.2
            score += 1
        if bullet10_y_down < -30:
            bullet10_x_down = random.randint(0,770)
            bullet10_y_down = random.randint(780,980)
            if move_bullet_down < ck:
                move_bullet_down += 0.2
            score += 1


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                r = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if (0<mouse_x<35) and (50<mouse_y<85):
                        running = False
                        start_running = True
            if event.type == pygame.KEYDOWN:
                if pausing:
                    if event.key == pygame.K_UP:
                        change_y -= 6
                    if event.key == pygame.K_DOWN:
                        change_y += 6
                    if event.key == pygame.K_LEFT:
                        change_x -= 6
                    if event.key == pygame.K_RIGHT:
                        change_x += 6
                if event.key == pygame.K_SPACE:
                    if pausing == False:
                        pausing = True
                        bullet1_x_right = random.randint(800,1000)
                        bullet1_y_right = random.randint(0,760)
                        bullet2_x_right = random.randint(800,1000)
                        bullet2_y_right = random.randint(0,760)
                        bullet3_x_right = random.randint(800,1000)
                        bullet3_y_right = random.randint(0,760)
                        bullet4_x_right = random.randint(800,1000)
                        bullet4_y_right = random.randint(0,760)
                        bullet5_x_right = random.randint(800,1000)
                        bullet5_y_right = random.randint(0,760)
                        bullet6_x_right = random.randint(800,1000)
                        bullet6_y_right = random.randint(0,760)
                        bullet7_x_right = random.randint(800,1000)
                        bullet7_y_right = random.randint(0,760)
                        bullet8_x_right = random.randint(800,1000)
                        bullet8_y_right = random.randint(0,760)
                        bullet9_x_right = random.randint(800,1000)
                        bullet9_y_right = random.randint(0,760)
                        bullet10_x_right = random.randint(800,1000)
                        bullet10_y_right = random.randint(0,760)
                        bullet1_x_left = random.randint(-230,-30)
                        bullet1_y_left = random.randint(0,760)
                        bullet2_x_left = random.randint(-230,-30)
                        bullet2_y_left = random.randint(0,760)
                        bullet3_x_left = random.randint(-230,-30)
                        bullet3_y_left = random.randint(0,760)
                        bullet4_x_left = random.randint(-230,-30)
                        bullet4_y_left = random.randint(0,760)
                        bullet5_x_left = random.randint(-230,-30)
                        bullet5_y_left = random.randint(0,760)
                        bullet6_x_left = random.randint(-230,-30)
                        bullet6_y_left = random.randint(0,760)
                        bullet7_x_left = random.randint(-230,-30)
                        bullet7_y_left = random.randint(0,760)
                        bullet8_x_left = random.randint(-230,-30)
                        bullet8_y_left = random.randint(0,760)
                        bullet9_x_left = random.randint(-230,-30)
                        bullet9_y_left = random.randint(0,760)
                        bullet10_x_left = random.randint(-230,-30)
                        bullet10_y_left = random.randint(0,760)
                        bullet1_x_up = random.randint(0,770)
                        bullet1_y_up = random.randint(-230,-30)
                        bullet2_x_up = random.randint(0,770)
                        bullet2_y_up = random.randint(-230,-30)
                        bullet3_x_up = random.randint(0,770)
                        bullet3_y_up = random.randint(-230,-30)
                        bullet4_x_up = random.randint(0,770)
                        bullet4_y_up = random.randint(-230,-30)
                        bullet5_x_up = random.randint(0,770)
                        bullet5_y_up = random.randint(-230,-30)
                        bullet6_x_up = random.randint(0,770)
                        bullet6_y_up = random.randint(-230,-30)
                        bullet7_x_up = random.randint(0,770)
                        bullet7_y_up = random.randint(-230,-30)
                        bullet8_x_up = random.randint(0,770)
                        bullet8_y_up = random.randint(-230,-30)
                        bullet9_x_up = random.randint(0,770)
                        bullet9_y_up = random.randint(-230,-30)
                        bullet10_x_up = random.randint(0,770)
                        bullet10_y_up = random.randint(-230,-30)
                        bullet1_x_down = random.randint(0,770)
                        bullet1_y_down = random.randint(780,980)
                        bullet2_x_down = random.randint(0,770)
                        bullet2_y_down = random.randint(780,980)
                        bullet3_x_down = random.randint(0,770)
                        bullet3_y_down = random.randint(780,980)
                        bullet4_x_down = random.randint(0,770)
                        bullet4_y_down = random.randint(780,980)
                        bullet5_x_down = random.randint(0,770)
                        bullet5_y_down = random.randint(780,980)
                        bullet6_x_down = random.randint(0,770)
                        bullet6_y_down = random.randint(780,980)
                        bullet7_x_down = random.randint(0,770)
                        bullet7_y_down = random.randint(780,980)
                        bullet8_x_down = random.randint(0,770)
                        bullet8_y_down = random.randint(780,980)
                        bullet9_x_down = random.randint(0,770)
                        bullet9_y_down = random.randint(780,980)
                        bullet10_x_down = random.randint(0,770)
                        bullet10_y_down = random.randint(780,980)
                        move_bullet_right = 2
                        move_bullet_left = 2
                        move_bullet_up = 2
                        move_bullet_down = 2
                        right2 = False
                        right3 = False
                        right4 = False
                        right5 = False
                        right6 = False
                        right7 = False
                        right8 = False
                        right9 = False
                        right10 = False
                        left2 = False
                        left3 = False
                        left4 = False
                        left5 = False
                        left6 = False
                        left7 = False
                        left8 = False
                        left9 = False
                        left10 = False
                        up2 = False
                        up3 = False
                        up4 = False
                        up5 = False
                        up6 = False
                        up7 = False
                        up8 = False
                        up9 = False
                        up10 = False
                        down2 = False
                        down3 = False
                        down4 = False
                        down5 = False
                        down6 = False
                        down7 = False
                        down8 = False
                        down9 = False
                        down10 = False
                        cyright = True
                        cright = True
                        
                        score = 0

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    change_y = 0
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    change_x = 0

        if pausing == False:
           
            font_end = font.render("Game Over, Score: "+str(score),True,WHITE)
            font_continue = font.render("Press Space To Continue",True,WHITE)
            screen.blit(font_end,(50,100)) 
            screen.blit(font_continue,(50,160))
        if pausing:
            rect_y += change_y
            rect_x += change_x
            if rect_y <=0:
                rect_y = 0
            elif rect_y >= HEIGHT - 50:
                rect_y = HEIGHT - 50
            if rect_x <=0:
                rect_x = 0
            elif rect_x >= WIDTH - 50:
                rect_x = WIDTH -50
        pygame.display.flip()
    while running1:
        screen.fill(BLACK)
        pygame.display.set_caption("Tutorial")
        mouse_x,mouse_y = pygame.mouse.get_pos()
        font1 = pygame.font.SysFont("sans",20)
        font_text = font1.render("nút ^,v,<,> theo thứ tự là lên,xuống,trái,phải để điều khiển màu đỏ",True,RED)
        screen.blit(font_text,(5,5))
        pygame.draw.rect(screen,YELLOW,(0,130,35,35))
        font_back = font.render("<",True,BLACK)
        screen.blit(font_back,(0,130))     
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running1 = False
                r = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if (0<mouse_x<35) and (130<mouse_y<165):
                        running1 = False
                        start_running = True
        pygame.display.flip()



pygame.quit()