# This code is a property of ASEEM RAJ BARANWAL and SACHIN GROVER
# Copyright (c) 2014


# importing modules and definitions
import pygame, random
from pygame.locals import *
from definitions import *
from math import *
from button import *
# scores of all the 4 players
score = [0, 0, 0, 0]

wht=[0,0,0,0]
blk=[0,0,0,0]

# Initialize GUI
pygame.init()

# the most awesome font in the world
font = pygame.font.Font(None, 34)
text = ''

# function to draw pockets at corners and also the striker arenas
def drawCorners():
    pygame.draw.circle(screen, BLACK, [2*border/3, 2*border/3], pocketrad)
    pygame.draw.circle(screen, BLACK, [wid-2*border/3, 2*border/3], pocketrad)
    pygame.draw.circle(screen, BLACK, [2*border/3, wid-2*border/3], pocketrad)
    pygame.draw.circle(screen, BLACK, [wid-2*border/3, wid-2*border/3], pocketrad)
    # top
    pygame.draw.rect(screen, BLACK, [strikerrad+pocketrad+border, pocketrad+border, wid-2*(strikerrad+pocketrad+border), gotirad], 1)
    pygame.draw.line(screen, BLACK,(strikerrad+pocketrad+border, pocketrad+border+gotirad-2),(wid-(strikerrad+pocketrad+border),pocketrad+border+gotirad-2),2)
    pygame.draw.circle(screen, RED, (strikerrad+pocketrad+border,pocketrad+border+gotirad/2),gotirad/2)
    pygame.draw.circle(screen, BLACK, (strikerrad+pocketrad+border,pocketrad+border+gotirad/2),gotirad/2,2)
    pygame.draw.circle(screen, RED, (wid-(strikerrad+pocketrad+border),pocketrad+border+gotirad/2),gotirad/2)
    pygame.draw.circle(screen, BLACK, (wid-(strikerrad+pocketrad+border),pocketrad+border+gotirad/2),gotirad/2,2)
    # right
    pygame.draw.rect(screen, BLACK, [wid-pocketrad-border-gotirad,strikerrad+pocketrad+border, gotirad, wid-2*(strikerrad+pocketrad+border)], 1)
    pygame.draw.line(screen, BLACK,(wid-pocketrad-border-gotirad,strikerrad+pocketrad+border),(wid-pocketrad-border-gotirad,wid-strikerrad-pocketrad-border),2)
    pygame.draw.circle(screen, RED, (wid-pocketrad-border-gotirad/2,strikerrad+pocketrad+border),gotirad/2)
    pygame.draw.circle(screen, BLACK, (wid-pocketrad-border-gotirad/2,strikerrad+pocketrad+border),gotirad/2,2)
    pygame.draw.circle(screen, RED, (wid-pocketrad-border-gotirad/2,wid-strikerrad-pocketrad-border),gotirad/2)
    pygame.draw.circle(screen, BLACK, (wid-pocketrad-border-gotirad/2,wid-strikerrad-pocketrad-border),gotirad/2,2)
    # left
    pygame.draw.rect(screen, BLACK, [pocketrad+border,strikerrad+pocketrad+border, gotirad, wid-2*(strikerrad+pocketrad+border)], 1)
    pygame.draw.line(screen, BLACK,(pocketrad+border+gotirad-2,strikerrad+pocketrad+border),(pocketrad+border+gotirad-2,wid-strikerrad-pocketrad-border),2)
    pygame.draw.circle(screen, RED, (pocketrad+border+gotirad/2,strikerrad+pocketrad+border),gotirad/2)
    pygame.draw.circle(screen, BLACK, (pocketrad+border+gotirad/2,strikerrad+pocketrad+border),gotirad/2,2)
    pygame.draw.circle(screen, RED, (pocketrad+border+gotirad/2,wid-strikerrad-pocketrad-border),gotirad/2)
    pygame.draw.circle(screen, BLACK, (pocketrad+border+gotirad/2,wid-strikerrad-pocketrad-border),gotirad/2,2)
    # bottom
    pygame.draw.rect(screen, BLACK, [strikerrad+pocketrad+border, wid-pocketrad-border-gotirad, wid-2*(strikerrad+pocketrad+border), gotirad], 1)
    pygame.draw.line(screen, BLACK,(strikerrad+pocketrad+border, wid-pocketrad-border-gotirad),(wid-(strikerrad+pocketrad+border),wid-pocketrad-border-gotirad),2)
    pygame.draw.circle(screen, RED, (strikerrad+pocketrad+border,wid-pocketrad-border-gotirad/2),gotirad/2)
    pygame.draw.circle(screen, BLACK, (strikerrad+pocketrad+border,wid-pocketrad-border-gotirad/2),gotirad/2,2)
    pygame.draw.circle(screen, RED, (wid-(strikerrad+pocketrad+border),wid-pocketrad-border-gotirad/2),gotirad/2)
    pygame.draw.circle(screen, BLACK, (wid-(strikerrad+pocketrad+border),wid-pocketrad-border-gotirad/2),gotirad/2,2)
    return

# initialize the game board
def initialise():
    #pygame.draw.circle(screen,BLACK, (wid/2,wid/2),border,2)
    cx=wid/2
    cy=wid/2
    r3b2=(3**0.5)/2 
    pygame.draw.line(screen,BLACK,(cx,cy+2.5*gotirad),(cx,cy-2.5*gotirad),3)
    pygame.draw.line(screen,BLACK,(cx-r3b2*2.5*gotirad,cy-1.25*gotirad),(cx+r3b2*2.5*gotirad,cy+1.25*gotirad),3)
    pygame.draw.line(screen,BLACK,(cx+r3b2*2.5*gotirad,cy-1.25*gotirad),(cx-r3b2*2.5*gotirad,cy+1.25*gotirad),3)
    pygame.draw.circle(screen, BLACK, (wid-(strikerrad+pocketrad+border),wid-pocketrad-border-gotirad/2),gotirad/2,3)
    pygame.draw.circle(screen,BLACK,(cx,cy),int(2.5*gotirad),3)
    pygame.draw.circle(screen,BLACK,(cx,cy),gotirad/2,3)
    pygame.draw.circle(screen,BLACK,(cx,cy),int(1.5*gotirad),3)
    # Small Circles
    pygame.draw.circle(screen,BLACK, (strikerrad+pocketrad+int(0.87*border),wid-pocketrad-int(1.17*border)-gotirad/2),int(0.35*gotirad),1)
    pygame.draw.circle(screen,BLACK, (wid-(strikerrad+pocketrad+int(0.87*border)),pocketrad+int(1.17*border)+gotirad/2),int(0.35*gotirad),1)
    pygame.draw.circle(screen,BLACK, (strikerrad+pocketrad+int(0.87*border),pocketrad+int(1.17*border)+gotirad/2),int(0.35*gotirad),1)
    pygame.draw.circle(screen,BLACK, (wid-(strikerrad+pocketrad+int(0.87*border)),wid-pocketrad-int(1.17*border)-gotirad/2),int(0.35*gotirad),1)

    # Foul lines
    rad=pocketrad
    pygame.draw.line(screen, BLACK,(3*rad/(2**0.5)+border/2,3*rad/(2**0.5)+border/2),(2.75*border,2.75*border),3)
    pygame.draw.line(screen, BLACK,(wid-(3*rad/(2**0.5)+border/2),3*rad/(2**0.5)+border/2),(wid-2.75*border,2.75*border),3)
    pygame.draw.line(screen, BLACK,(3*rad/(2**0.5)+border/2,wid-(3*rad/(2**0.5)+border/2)),(2.75*border,wid-2.75*border),3)
    pygame.draw.line(screen, BLACK,(wid-(3*rad/(2**0.5)+border/2),wid-(3*rad/(2**0.5)+border/2)),(wid-2.75*border,wid-2.75*border),3)

    pygame.draw.circle(screen, RED, (wid/2,wid/2),gotirad/2)

    #Foul Arcs
    rec=[]
    pygame.draw.arc(screen, BLACK,[2*border,2*border, 80, 80], -5*pi/4+0.8, 3*pi/4-0.8, 2)
    pygame.draw.arc(screen, BLACK,[wid-2.87*border,2*border, 80, 80], -7*pi/4+0.8, pi/4-0.8, 2)
    pygame.draw.arc(screen, BLACK,[2*border,wid-2.87*border, 80, 80], -3*pi/4+0.8, 5*pi/4-0.8, 2)
    pygame.draw.arc(screen, BLACK,[wid-2.87*border,wid-2.87*border, 80, 80], -1*pi/4+0.8, 7*pi/4-0.8, 2)
    
# model the arrangement in the beginning of a game
def beg_arrangement():
        cx=wid/2
        cy=wid/2
        r3=(3**0.5)
        col=[BLACK,WHITE]
        rad=gotirad/2
        
        g1 = Goti(MAROON)    
        g1.rect.x =cx-rad
        g1.rect.y =cy-rad
        goti_list.add(g1)
        all_sprites_list.add(g1)
        
        for i in range(2):
            g1 = Goti(col[i%2])
            g1.rect.x =cx-(((i+1)*(r3)*rad)+rad)
            g1.rect.y =cy-(i+2)*rad
            goti_list.add(g1)
            all_sprites_list.add(g1)
        for i in range(2):
            g1 = Goti(col[1])
            g1.rect.x =cx+(((i+1)*(r3)*rad)-rad) 
            g1.rect.y =cy+i*rad
            goti_list.add(g1)
            all_sprites_list.add(g1)
        for i in range(2):
            g1 = Goti(col[i%2])
            g1.rect.x =cx+(((i+1)*(r3)*rad)-rad) 
            g1.rect.y =cy-(i+2)*rad
            goti_list.add(g1)
            all_sprites_list.add(g1)
        for i in range(2):
            g1 = Goti(col[1])
            g1.rect.x =cx-(((i+1)*(r3)*rad)+rad) 
            g1.rect.y =cy+i*rad
            goti_list.add(g1)
            all_sprites_list.add(g1)
        for i in range(2):
            g1 = Goti(col[1])
            g1.rect.x =cx-rad
            g1.rect.y =cy-(2*i+3)*rad
            goti_list.add(g1)
            all_sprites_list.add(g1)
        for i in range(2):
            g1 = Goti(col[i%2])
            g1.rect.x =cx-rad
            g1.rect.y =cy+(2*i+1)*rad
            goti_list.add(g1)
            all_sprites_list.add(g1)
            
        g1 = Goti(col[0])
        g1.rect.x =cx-(4*rad*cos(3.14/6))-rad
        g1.rect.y =cy-rad
        goti_list.add(g1)
        all_sprites_list.add(g1)

        g1 = Goti(col[0])    
        g1.rect.x =cx+(4*rad*cos(3.14/6))-rad 
        g1.rect.y =cy-rad
        goti_list.add(g1)
        all_sprites_list.add(g1)

        g1 = Goti(col[0])    
        g1.rect.x =cx-(4*rad*cos(3.14/6)*sin(3.14/6))-rad
        g1.rect.y =cy+(4*rad*cos(3.14/6)*cos(3.14/6))-rad
        goti_list.add(g1)
        all_sprites_list.add(g1)

        g1 = Goti(col[0])    
        g1.rect.x =cx+(4*rad*cos(3.14/6)*sin(3.14/6))-rad
        g1.rect.y =cy+(4*rad*cos(3.14/6)*cos(3.14/6))-rad
        goti_list.add(g1)
        all_sprites_list.add(g1)

        g1 = Goti(col[0])    
        g1.rect.x =cx-(4*rad*cos(3.14/6)*sin(3.14/6))-rad
        g1.rect.y =cy-(4*rad*cos(3.14/6)*cos(3.14/6))-rad
        goti_list.add(g1)
        all_sprites_list.add(g1)

        g1 = Goti(col[0])    
        g1.rect.x =cx+(4*rad*cos(3.14/6)*sin(3.14/6))-rad
        g1.rect.y =cy-(4*rad*cos(3.14/6)*cos(3.14/6))-rad
        goti_list.add(g1)
        all_sprites_list.add(g1)

# Draw the wooden border of the carrom board
def drawBorder():
    for i in range(0, border/2, 3):
        pygame.draw.rect(screen, (15+2*i, 15+i, 0), [i, i, wid-2*i, wid-2*i])

    return

# Set screensize
screen = pygame.display.set_mode(scrsize)

pygame.display.set_caption("Carrom")

# Initialize a list of tangible objects
goti_list = pygame.sprite.Group()
all_sprites_list = pygame.sprite.Group()
striker = Striker()
all_sprites_list.add(striker)



done = False        # loop till close button clicked
foul = False        # Player pockets the striker
strikerfoul=False   # To check Striker fouls
queen_taken=False    # Check if queen needs a cover
clock = pygame.time.Clock()

# background = pygame.image.load('data/back.jpg').convert()

# main screen creation
# screen.blit(background, (0, 0))
pygame.display.update()

curr_player=1       # Current Player (Changing Player)
initial_flag=True
queen_flag=False    # Check if queen is pocketed

# The main event loop
while not done:
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
            if striker.state==0:
                striker.state = 1
                for goti in goti_list:
                    if pygame.sprite.collide_circle(goti, striker):
                        striker.state = 0
                        pygame.draw.circle(screen, RED, (striker.rect.centerx, striker.rect.centery), strikerrad+2, 2)
                        break
            elif striker.state==1:
                striker.state = 2
                cstriker = [striker.rect.x+strikerrad/2, striker.rect.y+strikerrad/2]
                pos = pygame.mouse.get_pos()
                striker.velx = (cstriker[0] - pos[0])/2
                striker.vely = (cstriker[1] - pos[1])/2

        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == RIGHT:
            striker.state = 0

    drawBorder()
    pygame.draw.rect(screen, WOOD, [border/2, border/2, wid-border, wid-border])
    if initial_flag:
        beg_arrangement()
        initial_flag=False
    drawCorners()
    initialise()

    all_sprites_list.update()

    for goti1 in goti_list:
        for goti2 in goti_list:
            if goti1 is not goti2 and pygame.sprite.collide_circle(goti1, goti2) and not goti1.collided and not goti2.collided:
                resolveCollision(goti1, goti2)
                goti1.collided, goti2.collided = True, True

    cstriker = [striker.rect.x+strikerrad/2, striker.rect.y+strikerrad/2]

    # striker is in angle select mode
    if striker.state==1:
        pos = pygame.mouse.get_pos()
        if pos[0]>border+strikerrad+gotirad and \
            pos[0]<wid-(border+strikerrad+gotirad) and \
            pos[1]>border+strikerrad+gotirad and \
            pos[1]<wid-(border+strikerrad+gotirad):
            pygame.draw.line(screen, RED,(cstriker[0],cstriker[1]),(pos[0],pos[1]),2)
        else:
            pygame.draw.line(screen, GREEN,(cstriker[0],cstriker[1]),(pos[0],pos[1]),2)


    # striker hits a goti
    playing=striker.player
    if striker.state==2:
        for goti in goti_list:
            if pygame.sprite.collide_circle(goti, striker):
                resolveCollision(striker, goti)
            if inPocket(striker):
                playing=striker.player
                all_sprites_list.remove(striker)
                strikerfoul = True
                
    # Goti is pocketed
    for goti in goti_list:
        goti.collided = False
        if queen_flag and inPocket(goti):
            score[striker.player] +=50
            queen_taken = True
            if goti.isWhite:
                score[striker.player] += 20
                wht[striker.player]+=1
            elif not goti.isQueen:
                score[striker.player] += 10
                blk[striker.player]+=1
            goti_list.remove(goti)
            all_sprites_list.remove(goti)
            curr_player=0

        elif not queen_flag and inPocket(goti):
            if goti.isWhite:
                score[striker.player] += 20
                wht[striker.player]+=1
            elif goti.isQueen:
                queen_flag=True
            else:
                score[striker.player] += 10
                blk[striker.player]+=1
            goti_list.remove(goti)
            all_sprites_list.remove(goti)
            curr_player=0

    if len(goti_list)==1:
        for q in goti_list:
            if q.isQueen:
                strikerfoul = True
            
    # Have all the things been stabilized?
    boardHalt = True
    for disk in all_sprites_list:
        if disk.velx!=0 or disk.vely!=0:
            boardHalt = False
            break


    if boardHalt and striker.state==2:
        striker.state = 0
        if not queen_taken and queen_flag and curr_player!=0:
            queen_flag = False
            g1=Goti(MAROON)
            g1.rect.x = wid/2 - gotirad/2
            g1.rect.y = wid/2 - gotirad/2
            goti_list.add(g1)
            all_sprites_list.add(g1)

        elif queen_taken and queen_flag:
            queen_flag = False

        striker.player = (striker.player + curr_player)%4
        curr_player=1
        
    # Everything ceases to move
    if boardHalt and strikerfoul:
        strikerfoul = False
        striker = Striker()
        striker.state = 0
        all_sprites_list.add(striker)
        if score[playing]>0:
            if blk[playing]>0:
                score[playing] -= 10
                blk[playing]-=1
                fgoti = Goti(BLACK)
                fgoti.rect.x, fgoti.rect.y = wid/2-gotirad/2, wid/2-gotirad/2
                all_sprites_list.add(fgoti)
                goti_list.add(fgoti)
            elif wht[playing]>0:
                score[playing] -= 20
                wht[playing]-=1
                fgoti = Goti(WHITE)
                fgoti.rect.x, fgoti.rect.y = wid/2-gotirad/2, wid/2-gotirad/2
                all_sprites_list.add(fgoti)
                goti_list.add(fgoti)
                
        curr_player=1
        striker.player = (playing + curr_player)%4
    

    # Draw everything again (a kind of update)
    all_sprites_list.draw(screen)

    pygame.draw.rect(screen, (0, 0, 0), [wid, 0, wid, wid])
    font = pygame.font.Font(None, 34)
    header = font.render("Score:", 5, (255, 255, 255))
    headerpos = header.get_rect()
    headerpos.centerx = 950
    headerpos.centery = 50
    screen.blit(header, headerpos)
    font = pygame.font.Font(None, 30)
    if playing==0:
        text = font.render("Player 1: " + str(score[0]), 80, (120, 120, 200))
    else:
        text = font.render("Player 1: " + str(score[0]), 80, (200, 200, 200))
    textpos = text.get_rect()
    textpos.centerx = 950
    textpos.centery = 100
    screen.blit(text, textpos)
    if playing==1:
        text = font.render("Player 2: " + str(score[1]), 80, (120, 120, 200))
    else:
        text = font.render("Player 2: " + str(score[1]), 80, (200, 200, 200))
    textpos = text.get_rect()
    textpos.centerx = 950
    textpos.centery = 150
    screen.blit(text, textpos)
    if playing==2:
        text = font.render("Player 3: " + str(score[2]), 80, (120, 120, 200))
    else:
        text = font.render("Player 3: " + str(score[2]), 80, (200, 200, 200))
    textpos = text.get_rect()
    textpos.centerx = 950
    textpos.centery = 200
    screen.blit(text, textpos)
    if playing==3:
        text = font.render("Player 4: " + str(score[3]), 80, (120, 120, 200))
    else:
        text = font.render("Player 4: " + str(score[3]), 80, (200, 200, 200))
    textpos = text.get_rect()
    textpos.centerx = 950
    textpos.centery = 250
    screen.blit(text, textpos)

    text = font.render("Striker Velocity: " + str(ceil(mod([striker.velx, striker.vely]) * 100)/100.0), 80, (120, 200, 120))
    textpos = text.get_rect()
    textpos.centerx = 950
    textpos.centery = 300
    screen.blit(text, textpos)
    
    if strikerfoul:
        text = font.render("Striker in Pocket. Foul", 80, (200, 120, 120))
        textpos = text.get_rect()
        textpos.centerx = 950
        textpos.centery = 400
        screen.blit(text, textpos)


    font = pygame.font.Font(None, 24)
    text = font.render("(c) 2014 Aseem Raj and Sachin Grover", 85, (150, 150, 150))
    textpos = text.get_rect()
    textpos.centerx = 950
    textpos.centery = 650
    screen.blit(text, textpos)

    pygame.display.flip()

    # Limit to input frames per second
    clock.tick(fps)

pygame.quit()
