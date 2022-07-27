import pygame
import time
import math
r = True
while r:
    pygame.init()

    screen = pygame.display.set_mode((500,600))

    GREY = (150,150,150)
    WHITE = (255,255,255)
    BLACK = (0,0,0)
    RED  = (255,0,0)
    BLUE = (214, 234, 248)

    running = True
    running1 = True

    font = pygame.font.SysFont("sans",50)
    text_1 = font.render("+",True,BLACK)
    text_2 = font.render("-",True,BLACK)
    text_3 = font.render("+",True,BLACK)
    text_4 = font.render("-",True,BLACK)
    text_5 = font.render("Start",True,BLACK)
    text_6 = font.render("Reset",True,BLACK)
    text_7 = font.render("Stop",True,BLACK)
    text_8 = font.render("+",True,BLACK)
    text_9 = font.render("-",True,BLACK)
    text_10 = font.render(">",True,BLACK)
    text_11 = font.render("<",True,BLACK)

    total_secs = 0
    start = False
    start1 = False
    total = 0

    sound = pygame.mixer.Sound("Tieng-chuong-het-gio-reng-www_tiengdong_com.mp3")

    clock = pygame.time.Clock()
    while running:

        pygame.display.set_caption("đồng hồ đém ngược")


        clock.tick(10)

        screen.fill(GREY)

        mouse_x,mouse_y = pygame.mouse.get_pos()


        pygame.draw.rect(screen,WHITE,(100,50,50,50))
        pygame.draw.rect(screen,WHITE,(100,200,50,50))
        pygame.draw.rect(screen,WHITE,(200,50,50,50))
        pygame.draw.rect(screen,WHITE,(200,200,50,50))
        pygame.draw.rect(screen,WHITE,(300,50,150,50))
        pygame.draw.rect(screen,WHITE,(300,150,150,50))
        pygame.draw.rect(screen,WHITE,(300,240,150,60))
        pygame.draw.rect(screen,WHITE,(0,50,50,50))
        pygame.draw.rect(screen,WHITE,(0,200,50,50))

        pygame.draw.rect(screen,BLUE,(450,350,50,50))
        screen.blit(text_10,(460,350))

        screen.blit(text_1,(100,50))
        screen.blit(text_2,(100,200))
        screen.blit(text_3,(200,50))
        screen.blit(text_4,(200,200))
        screen.blit(text_5,(300,50))
        screen.blit(text_6,(300,150))
        screen.blit(text_7,(300,240))
        screen.blit(text_8,(0,50))
        screen.blit(text_9,(0,200))

        pygame.draw.rect(screen,BLACK,(50,520,400,50))
        pygame.draw.rect(screen,WHITE,(60,530,380,30))

        pygame.draw.circle(screen,BLACK,(250,400),100)
        pygame.draw.circle(screen,WHITE,(250,400),95)
        pygame.draw.circle(screen,BLACK,(250,400),5)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running1 = False
                running = False
                r = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    pygame.mixer.pause()
                    if (0<mouse_x<50) and (50<mouse_y<100):
                        if start == False:
                            pygame.draw.rect(screen,RED,(0,50,50,50))
                            screen.blit(text_8,(0,50))
                            total_secs += 3600
                            total = total_secs
                    if (0<mouse_x<50) and (200<mouse_y<250):
                        if start == False:
                            pygame.draw.rect(screen,RED,(0,200,50,50))
                            screen.blit(text_9,(0,200))
                            total_secs -=3600
                            total = total_secs
                    if (100< mouse_x <150) and (50<mouse_y<100):
                        if start == False:
                            pygame.draw.rect(screen,RED,(100,50,50,50))
                            screen.blit(text_1,(100,50))
                            total_secs += 60
                            total = total_secs
                    if (100<mouse_x<150) and (200<mouse_y<250):
                        if start == False:
                            pygame.draw.rect(screen,RED,(100,200,50,50))
                            screen.blit(text_2,(100,200))
                            total_secs -= 60
                            total = total_secs
                    if (200<mouse_x<250) and (50 < mouse_y<100):
                        if start == False:
                            pygame.draw.rect(screen,RED,(200,50,50,50))
                            screen.blit(text_3,(200,50))
                            total_secs += 1
                            total = total_secs
                    if (200<mouse_x<250) and (200 < mouse_y<250):
                        if start == False:
                            pygame.draw.rect(screen,RED,(200,200,50,50))
                            screen.blit(text_4,(200,200))
                            total_secs -=1
                            total = total_secs
                    if (300<mouse_x<450) and (50<mouse_y<100):
                        if start == False:
                            pygame.draw.rect(screen,RED,(300,50,150,50))
                            screen.blit(text_5,(300,50))
                            total = total_secs
                            start = True
                    if (300<mouse_x<450) and (150<mouse_y<200):
                        if start == False:
                            pygame.draw.rect(screen,RED,(300,150,150,50))
                            screen.blit(text_6,(300,150))
                            total_secs = 0
                    if (300<mouse_x<450) and (240<mouse_y<300):
                        if start == True:
                            pygame.draw.rect(screen,RED,(300,240,150,60))
                            screen.blit(text_7,(300,240))
                            start=False
                            total = total_secs
                    if (450<mouse_x<500) and (350<mouse_y<400):
                        running1=True
                        total_secs = 0
                        running=False
                            

        if start:
            total_secs -= 1
            if total_secs == 0:
                start = False
                pygame.mixer.Sound.play(sound)
            time.sleep(1)
                

        if total_secs < 0:
            total_secs = 0

        times = total_secs // 3600
        mins = (total_secs - times*3600) // 60
        if total_secs > 3600:
            secs = (total_secs - ((mins*60)+(times*3600)))
        if total_secs < 3600:
            secs = total_secs- mins*60

        time_now = str(times)+":"+str(mins) + ":" + str(secs)
        text_time = font.render(time_now,True,BLACK)
        screen.blit(text_time,(70,120))

        x_sec = 250 + 90* math.sin(6 * secs * math.pi/180)
        y_sec = 400 - 90*math.cos(6 * secs * math.pi/180)
        pygame.draw.line(screen,GREY,(250,400),(int(x_sec),int(y_sec)))

        x_min = 250 + 60* math.sin(6 * mins * math.pi/180)
        y_min = 400 - 60*math.cos(6 * mins * math.pi/180)
        pygame.draw.line(screen,BLACK,(250,400),(int(x_min),int(y_min)))

        x_time = 250 + 40* math.sin(6 * times * math.pi/180)
        y_time = 400 - 40*math.cos(6 * times * math.pi/180)
        pygame.draw.line(screen,RED,(250,400),(int(x_time),int(y_time)))

        if total != 0:
            pygame.draw.rect(screen,RED,(60,530,int(380*(total_secs/total)),30))

        pygame.display.flip()

    while running1:

        pygame.display.set_caption("đồng hồ đém lên")
        clock.tick(10)

        screen.fill(GREY)

        mouse_x,mouse_y = pygame.mouse.get_pos() 

        pygame.draw.rect(screen,WHITE,(300,50,150,50))
        pygame.draw.rect(screen,WHITE,(300,150,150,50))
        pygame.draw.rect(screen,WHITE,(300,240,150,60))
        pygame.draw.rect(screen,BLUE,(0,350,50,50))

        screen.blit(text_5,(300,50))
        screen.blit(text_6,(300,150))
        screen.blit(text_7,(300,240))
        screen.blit(text_11,(10,350))

        pygame.draw.circle(screen,BLACK,(250,400),100)
        pygame.draw.circle(screen,WHITE,(250,400),95)
        pygame.draw.circle(screen,BLACK,(250,400),5)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running1 = False
                r = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if (300<mouse_x<450) and (50<mouse_y<100):
                        if start1 == False:
                            pygame.draw.rect(screen,RED,(300,50,150,50))
                            screen.blit(text_5,(300,50))
                            total = total_secs
                            start1 = True
                    if (300<mouse_x<450) and (150<mouse_y<200):
                        if start1 == False:
                            pygame.draw.rect(screen,RED,(300,150,150,50))
                            screen.blit(text_6,(300,150))
                            total_secs = 0
                    if (300<mouse_x<450) and (240<mouse_y<300):
                        if start1 == True:
                            pygame.draw.rect(screen,RED,(300,240,150,60))
                            screen.blit(text_7,(300,240))
                            start1=False
                    if (0<mouse_x<50) and (350<mouse_y<400):
                        running = True
                        total_secs = 0
                        running1 = False

        if start1:
            total_secs += 1
            time.sleep(1)

        times = total_secs // 3600
        mins = (total_secs - times*3600) // 60
        if total_secs > 3600:
            secs = (total_secs - ((mins*60)+(times*3600)))
        if total_secs < 3600:
            secs = total_secs- mins*60

        time_now = str(times)+":"+str(mins) + ":" + str(secs)
        text_time = font.render(time_now,True,BLACK)
        screen.blit(text_time,(70,120))

        x_sec = 250 + 90* math.sin(6 * secs * math.pi/180)
        y_sec = 400 - 90*math.cos(6 * secs * math.pi/180)
        pygame.draw.line(screen,GREY,(250,400),(int(x_sec),int(y_sec)))

        x_min = 250 + 60* math.sin(6 * mins * math.pi/180)
        y_min = 400 - 60*math.cos(6 * mins * math.pi/180)
        pygame.draw.line(screen,BLACK,(250,400),(int(x_min),int(y_min)))

        x_time = 250 + 40* math.sin(6 * times * math.pi/180)
        y_time = 400 - 40*math.cos(6 * times * math.pi/180)
        pygame.draw.line(screen,RED,(250,400),(int(x_time),int(y_time)))

        
        

        pygame.display.flip()

    pygame.quit()
