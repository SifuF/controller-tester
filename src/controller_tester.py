#####################################
## Xbox controller tester by SifuF ##
#####################################

import pygame
import math

pygame.init()
pygame.display.set_caption('Xbox controller tester by SifuF')

img = pygame.image.load('icon.png')
pygame.display.set_icon(img)

screen = pygame.display.set_mode([1000, 600])
pad_one = pygame.image.load('one.png')
pad_360 = pygame.image.load('360.png')
pad_og = pygame.image.load('og.png')
pygame.font.init()

joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]

if len(joysticks) == 0:
    print("Error: No controller connected!")
    exit()

running = True
x = 0
y = 0
m = 1
i = 0
triggers = False

posX_one = [266, 725, 283, 605, 372, 342, 402, 372, 495, 415, 535, 710, 653, 766, 120, 795]
posY_one = [65, 178, 303, 300, 270, 330, 100, 170, 235, 123, 179, 440]

posX_360 = [266, 732, 265, 596, 351, 321, 381, 351, 490, 388, 551, 713, 654, 774, 150, 775]
posY_360 = [65, 168, 306, 283, 253, 313, 171, 161, 225, 110, 166, 451]

posX_og = [266, 720, 271, 660, 312, 282, 342, 312, 495, 425, 520, 706, 655, 755, 175, 740]
posY_og = [65, 205, 362, 348, 318, 378, 230, 410, 265, 165, 215, 440]

joy_type = 0

if joysticks[0].get_name() == "Xbox One Controller":
    joy_type = 0
    posX = posX_one
    posY = posY_one
    pad = pad_one
elif joysticks[0].get_name() == "Xbox 360 Controller":
    joy_type = 1
    posX = posX_360
    posY = posY_360
    pad = pad_360
else:
    joy_type = 2
    posX = posX_og
    posY = posY_og
    pad = pad_og

rumble_surf = pygame.Surface((60, 60), pygame.SRCALPHA)

my_font = pygame.font.SysFont('arial', 25)
name_surf = my_font.render("Name: "+joysticks[0].get_name(), False, (120, 100, 200))
id_surf = my_font.render("GUID: "+joysticks[0].get_guid(), False, (120, 100, 200))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_z:
                m = 10

            if event.key == pygame.K_LEFT:
                x=x-m
                print("x=",x)
            if event.key == pygame.K_RIGHT:
                x=x+m
                print("x=",x)
            if event.key == pygame.K_UP:
                y=y-m
                print("y=",y)
            if event.key == pygame.K_DOWN:
                y=y+m
                print("y=",y)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_z:
                m = 1

    screen.fill((0, 0, 0))

    xl = 255-math.floor((joysticks[0].get_axis(4)+1)*128)
    xr = 255-math.floor((joysticks[0].get_axis(5)+1)*128)

    # analogue triggers
    # fix for triggers not initialising before first press
    if triggers :
        if joysticks[0].get_button(4):
            pygame.draw.circle(screen, (255, 0, 0), (posX[0], posY[0]+10*joysticks[0].get_axis(4)), 50)
        else:
            pygame.draw.circle(screen, (255, xl, xl), (posX[0], posY[0]+10*joysticks[0].get_axis(4)), 50)

        if joysticks[0].get_button(5):
            pygame.draw.circle(screen, (255, 0, 0), (posX[1], posY[0]+10*joysticks[0].get_axis(5)), 50)
        else:
            pygame.draw.circle(screen, (255, xr, xr), (posX[1], posY[0]+10*joysticks[0].get_axis(5)), 50)
    else :
        pygame.draw.circle(screen, (255, 255, 255), (posX[0], posY[0]-10), 50)
        pygame.draw.circle(screen, (255, 255, 255), (posX[1], posY[0]-10), 50)

    if joysticks[0].get_axis(4) < -0.1 or joysticks[0].get_axis(5) < -0.1 :
        triggers = True


    screen.blit(pad, (0,0))

    # analogue sticks
    if joysticks[0].get_button(8):
        pygame.draw.circle(screen, (255, 0, 255), (posX[2]+20*joysticks[0].get_axis(0), posY[1]+20*joysticks[0].get_axis(1)), 50)
    else:
        pygame.draw.circle(screen, (150, 0, 200), (posX[2]+20*joysticks[0].get_axis(0), posY[1]+20*joysticks[0].get_axis(1)), 50)

    if joysticks[0].get_button(9):
        pygame.draw.circle(screen, (255, 0, 255), (posX[3]+20*joysticks[0].get_axis(2),posY[2]+20*joysticks[0].get_axis(3)), 50)
    else:
        pygame.draw.circle(screen, (150, 0, 200), (posX[3]+20*joysticks[0].get_axis(2),posY[2]+20*joysticks[0].get_axis(3)), 50)

    # D-pad
    pygame.draw.rect(screen, (64,0,0),(posX[4],posY[3],30,30))
    if joysticks[0].get_hat(0)[0] == -1:
        pygame.draw.rect(screen, (255,0,0),(posX[5],posY[3],30,30))
    else:
        pygame.draw.rect(screen, (64,0,0),(posX[5],posY[3],30,30))
    
    if joysticks[0].get_hat(0)[0] == 1:    
        pygame.draw.rect(screen, (255,0,0),(posX[6],posY[3],30,30))
    else:
        pygame.draw.rect(screen, (64,0,0),(posX[6],posY[3],30,30))

    if joysticks[0].get_hat(0)[1] == 1:
        pygame.draw.rect(screen, (255,0,0),(posX[7],posY[4],30,30))
    else:
        pygame.draw.rect(screen, (64,0,0),(posX[7],posY[4],30,30))

    if joysticks[0].get_hat(0)[1] == -1:
        pygame.draw.rect(screen, (255,0,0),(posX[7],posY[5],30,30))
    else:
        pygame.draw.rect(screen, (64,0,0),(posX[7],posY[5],30,30))

    # start select home
    pygame.draw.circle(screen, (64, 64, 64), (posX[8], posY[6]), 30)
    if joysticks[0].get_button(6):
        pygame.draw.rect(screen, (255,0,0),(posX[9],posY[7],40,20))
    else:
        pygame.draw.rect(screen, (64,0,0),(posX[9],posY[7],40,20))
    
    if joysticks[0].get_button(7):
        pygame.draw.rect(screen, (255,0,0),(posX[10],posY[7],40,20))
    else:
        pygame.draw.rect(screen, (64,0,0),(posX[10],posY[7],40,20))

    # 4 colours
    if joysticks[0].get_button(0):
        pygame.draw.circle(screen, (0, 255, 0), (posX[11], posY[8]), 27)
    else:
        pygame.draw.circle(screen, (0, 100, 0), (posX[11]+x, posY[8]+y), 27)
    
    if joysticks[0].get_button(3):
        pygame.draw.circle(screen, (255, 200, 0), (posX[11], posY[9]), 27)
    else:
        pygame.draw.circle(screen, (100, 80, 0), (posX[11], posY[9]), 27)

    if joysticks[0].get_button(2):
        pygame.draw.circle(screen, (0, 0, 255), (posX[12], posY[10]), 27)
    else:
        pygame.draw.circle(screen, (0, 0, 100), (posX[12], posY[10]), 27)

    if joysticks[0].get_button(1):
        pygame.draw.circle(screen, (255, 0, 0), (posX[13], posY[10]), 27)
    else:
        pygame.draw.circle(screen, (100, 0, 0), (posX[13], posY[10]), 27)
    
    # OG black white
    if joy_type == 2:
        if joysticks[0].get_button(4):
            pygame.draw.circle(screen, (255, 255, 255), (posX[11]+45, posY[9]-35), 15)
        else:
            pygame.draw.circle(screen, (128, 128, 128), (posX[11]+45, posY[9]-35), 15)

        if joysticks[0].get_button(5):
            pygame.draw.circle(screen, (100, 100, 100), (posX[11]+80, posY[9]), 15)
        else:
            pygame.draw.circle(screen, (0, 0, 0), (posX[11]+80, posY[9]), 15)

    # rumble
    if joysticks[0].get_button(4):
        rumble_surf.fill((50,0,150))
        screen.blit(pygame.transform.rotate(rumble_surf, i), (posX[14],posY[11]))
        joysticks[0].rumble(1, 0, 100)
    else:
        joysticks[0].stop_rumble() 

    if joysticks[0].get_button(5):
        rumble_surf.fill((50,0,150))
        screen.blit(pygame.transform.rotate(rumble_surf, i), (posX[15],posY[11]))
        joysticks[0].rumble(0, 1, 100)
    else:
        joysticks[0].stop_rumble() 

    screen.blit(name_surf, (300,520))
    screen.blit(id_surf, (300,550))
    
    i=i+10
    if i>=360 :
        i = 0

    pygame.display.flip()

pygame.quit()
