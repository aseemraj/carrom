import pygame, random
from pygame.locals import *
from definitions import *
from math import *
# from numpy import *
score = [0, 0, 0, 0]

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

def drawBorder():
    for i in range(0, border/2, 3):
        if i%2==0:
            pygame.draw.rect(screen, LBROWN, [i, i, wid-2*i, wid-2*i], 3)
        else:
            pygame.draw.rect(screen, DBROWN, [i, i, wid-2*i, wid-2*i], 3)
    return

def inPocket(obj):
    nearx = min(abs(obj.rect.x-2*border/3), abs(obj.rect.x-wid+2*border/3))
    neary = min(abs(obj.rect.y-2*border/3), abs(obj.rect.y-wid+2*border/3))
    if nearx<pocketrad/2 and neary<pocketrad/2:
        return True
    return False

def resolveCollision(obj1, obj2):
    c1 = [obj1.rect.x+obj1.rad, obj1.rect.y+obj1.rad]
    c2 = [obj2.rect.x+obj2.rad, obj2.rect.y+obj2.rad]
    distx = abs(c1[0]-c2[0])
    disty = abs(c1[1]-c2[1])
    dist = [abs(c1[0]-c2[0]), abs(c1[1]-c2[1])]
    if mod(dist)==0:
        costheta = 1
        sintheta = 0
    else:
        costheta = abs(distx)/mod(dist)
        sintheta = abs(disty)/mod(dist)
    if mod(dist)<obj1.rad + obj2.rad:
        diff = obj1.rad + obj2.rad - mod(dist)
        if obj2.rect.x>=obj1.rect.x:
            obj2.rect.x += ceil(diff*costheta)
        else:
            obj1.rect.x += ceil(diff*costheta)
        if obj2.rect.y>obj1.rect.y:
            obj2.rect.y += ceil(diff*costheta)
        else:
            obj1.rect.y += ceil(diff*costheta)

    v1x, v1y = obj1.velx, obj1.vely
    v2x, v2y = obj2.velx, obj2.vely
    obj1.velx = v1x*sintheta*sintheta + v2x*costheta*costheta + costheta*sintheta*(v2y-v1y)
    obj2.velx = v1x*costheta*costheta + v2x*sintheta*sintheta + costheta*sintheta*(v1y-v2y)
    obj1.vely = sintheta*costheta*(v1x-v2x) + v1y*costheta*costheta + v2y*sintheta*sintheta
    obj2.vely = sintheta*costheta*(v1x-v2x) + v1y*sintheta*sintheta + v2y*costheta*costheta
    for obj in [obj1, obj2]:
        if mod([obj.velx, obj.vely])==0:
            obj.velx = 0
            obj.vely = 0
        else:
            obj.velx = obj.velx - friction * obj.velx / mod([obj.velx, obj.vely])  # friction acts in a direction
            obj.vely = obj.vely - friction * obj.vely / mod([obj.velx, obj.vely])  # opposite to velocity
            if abs(obj.velx)<friction:
                obj.velx = 0
            if abs(obj.vely)<friction:
                obj.vely = 0


pygame.init()
screen = pygame.display.set_mode(scrsize)
pygame.display.set_caption("Carrom")

goti_list = pygame.sprite.Group()
all_sprites_list = pygame.sprite.Group()
striker = Striker()
all_sprites_list.add(striker)

for i in range(10):
    # This represents a block
    goti = Goti(BLACK)
    # Set a random location for the block
    goti.rect.x = random.randrange(border, wid-border)
    goti.rect.y = random.randrange(border, wid-border)
    # Add the goti to the list of objects
    goti_list.add(goti)
    all_sprites_list.add(goti)
for i in range(10):
    # This represents a block
    goti = Goti(WHITE)
    # Set a random location for the block
    goti.rect.x = random.randrange(border, wid-border)
    goti.rect.y = random.randrange(border, wid-border)
    # Add the goti to the list of objects
    goti_list.add(goti)
    all_sprites_list.add(goti)

done = False    # loop till close button clicked
clock = pygame.time.Clock()

background = pygame.image.load('data/back.jpg').convert()

# main screen creation
screen.blit(background, (0, 0))
pygame.display.update()


while not done:
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
            if striker.state==0:
                striker.state = 1
            elif striker.state==1:
                striker.state = 2
                cstriker = [striker.rect.x+strikerrad/2, striker.rect.y+strikerrad/2]
                pos = pygame.mouse.get_pos()
                striker.velx = (cstriker[0] - pos[0])/4
                striker.vely = (cstriker[1] - pos[1])/4

        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == RIGHT:
            striker.state = 0

    # screen.blit(background, (0, 0))
    screen.fill(WOOD)

    # pygame.draw.rect(screen, BROWN, [0, 0, wid, wid], border)
    drawBorder()
    drawCorners()

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
        if pos[0]>border+strikerrad+gotirad and pos[0]<wid-(border+strikerrad+gotirad) and pos[1]>border+strikerrad+gotirad and pos[1]<wid-(border+strikerrad+gotirad):
            pygame.draw.line(screen, RED,(cstriker[0],cstriker[1]),(pos[0],pos[1]),5)
        else:
            pygame.draw.line(screen, GREEN,(cstriker[0],cstriker[1]),(pos[0],pos[1]),5)

    foul = False
    # striker hits a goti
    if striker.state==2:
        for goti in goti_list:
            if pygame.sprite.collide_circle(goti, striker):
                resolveCollision(striker, goti)
            if inPocket(striker):
                foul = True
                # goti.velx = -1*goti.velx
                # goti.vely = -1*goti.vely
    
    chplayer = True
    for disk in all_sprites_list:
        if disk.velx!=0 or disk.vely!=0:
            chplayer = False
            break

    chance = False
    for goti in goti_list:
        goti.collided = False
        if inPocket(goti):
            if goti.isWhite:
                score[striker.player] += 20
            else:
                score[striker.player] += 10
            chance = True
            goti_list.remove(goti)
            all_sprites_list.remove(goti)

    if chplayer and striker.state==2:
        striker.state = 0
        if foul:
            print "Foul by player ", striker.player
            score[striker.player] -= 10
            fgoti = Goti(BLACK)
            fgoti.rect.x = wid/2-gotirad/2
            fgoti.rect.y = wid/2-gotirad/2
        if not chance:
            striker.player = (striker.player+1)%4
        for e in range(4):
            print "Player ", e+1, ": ", score[e]
        print "\n"

    all_sprites_list.draw(screen)


    pygame.display.flip()
    # Limit to input frames per second
    clock.tick(fps)

pygame.quit()