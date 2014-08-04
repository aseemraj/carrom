import pygame, random
# from pygame.locals import *
from definitions import *
from math import *
# from numpy import *


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

pygame.init()
screen = pygame.display.set_mode(scrsize)
pygame.display.set_caption("Carrom")

goti_list = pygame.sprite.Group()
all_sprites_list = pygame.sprite.Group()
bullet_list = pygame.sprite.Group()
striker = Striker(BLUE)
all_sprites_list.add(striker)

for i in range(10):
    # This represents a block
    goti = Goti(DGRAY)
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
score = 0
screen.blit(background, (0, 0))
pygame.display.update()


t_list = pygame.sprite.Group()
while not done:
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop
        elif event.type == pygame.MOUSEBUTTONDOWN:
            bullet = Bullet()
            bullet.rect.x = striker.rect.x
            bullet.rect.y = striker.rect.y
            # Add the bullet to the lists
            all_sprites_list.add(bullet)
            bullet_list.add(bullet)

    # screen.blit(background, (0, 0))
    screen.fill(WOOD)

    # pygame.draw.rect(screen, BROWN, [0, 0, wid, wid], border)
    drawBorder()
    drawCorners()

    all_sprites_list.update()


    for bullet in bullet_list:
        # See if it hit a block
        hit_list = pygame.sprite.spritecollide(bullet, goti_list, True)
        # For each block hit, remove the bullet and add to the score
        for goti in hit_list:
            bullet_list.remove(bullet)
            all_sprites_list.remove(bullet)
            score += 1
            print(score)
        # Remove the bullet if it flies up off the screen
        if bullet.rect.y < -10:
            bullet_list.remove(bullet)
            all_sprites_list.remove(bullet)


    for goti in goti_list:
        hitObj = pygame.sprite.spritecollideany(goti, goti_list)
        if hitObj is not None:
            c1 = [hitObj.rect.x+gotirad/2, hitObj.rect.y+gotirad/2]
            c2 = [goti.rect.x+gotirad/2, goti.rect.y+gotirad/2]

            hitObj.velx, goti.velx = goti.velx, hitObj.velx
            hitObj.vely, goti.vely = goti.vely, hitObj.vely

    # striker hits a goti
    goti_hit_list = pygame.sprite.spritecollide(striker, goti_list, False)
    for goti in goti_hit_list:
        goti.velx = -1*goti.velx
        goti.vely = -1*goti.vely

    cstriker = [striker.rect.x+strikerrad/2, striker.rect.y+strikerrad/2]
    all_sprites_list.draw(screen)

    pygame.display.flip()
    # Limit to input frames per second
    clock.tick(fps)

pygame.quit()