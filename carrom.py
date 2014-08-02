import pygame, random
# from pygame.locals import *

def drawCorners():
    pygame.draw.circle(screen, BLACK, [border, border], pocketrad)
    pygame.draw.circle(screen, BLACK, [wid-border, border], pocketrad)
    pygame.draw.circle(screen, BLACK, [border, wid-border], pocketrad)
    pygame.draw.circle(screen, BLACK, [wid-border, wid-border], pocketrad)
    return

def drawGotiW(screen, x, y):
    pygame.draw.circle(screen, WHITE, [x, y], gotirad)
    pygame.draw.circle(screen, BLACK, [x, y], gotirad, 1)
    return

def drawGotiB(screen, x, y):
    pygame.draw.circle(screen, (30, 30, 30), [x, y], gotirad)
    return

class Goti(pygame.sprite.Sprite):
    """
    This class represents the goti.
    It derives from the "Sprite" class in Pygame.
    """
    def __init__(self, color, width, height):
        """ Constructor. Pass in the color of the block,
        and its x and y position. """
 
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)
 
        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = pygame.Surface([width, height])
        self.image.fill(WOOD)
        pygame.draw.ellipse(self.image, color, [0, 0, width, height])
        # Fetch the rectangle object that has the dimensions of the image
        # image.
        # Update the position of this object by setting the values
        # of rect.x and rect.y
        self.rect = self.image.get_rect()
        self.velx = 2
        self.vely = 1
        self.collided = False
    
    def reset_pos(self):
        """ Reset position to the top of the screen, at a random x location.
        Called by update() or the main program loop if there is a collision.
        """
        self.rect.y = random.randrange(border, wid-border)
        self.rect.x = random.randrange(border, wid-border)
 
    def update(self):
        """ Called each frame. """
        # Move block down one pixel
        self.rect.x += self.velx
        self.rect.y += self.vely
        # If block is too far down, reset to top of screen.
        if self.rect.y > wid-border/2-gotirad:
            self.vely = -1*abs(self.vely)
        elif self.rect.y<border/2:
            self.vely = abs(self.vely)
        if self.rect.x > wid-border/2-gotirad:
            self.velx = -1*abs(self.velx)
        elif self.rect.x<border/2:
            self.velx = abs(self.velx)

class Striker(Goti):
    """ The player class derives from Block, but overrides the 'update' 
    functionality with new a movement function that will move the block 
    with the mouse. """
    def update(self):
        # Get the current mouse position. This returns the position
        # as a list of two numbers.
        pos = pygame.mouse.get_pos()
        # Fetch the x and y out of the list, 
        # just like we'd fetch letters out of a string.
        # Set the player object to the mouse location
        self.rect.x = pos[0]
        self.rect.y = pos[1]

# Define some constants
BLACK    = (   0,   0,   0)
BROWN    = (  50,   0,   0)
WHITE    = ( 255, 255, 255)
WOOD     = ( 220, 200, 150)
BLUE     = (   0,   0, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
PI = 3.141592653
border = 70
# Set the width and height of the screen [width, height]
size = (700, 700)
wid = size[0]
strikerrad = 40
strikerx = 350
strikery = 350
pocketrad = 25
gotirad = 32
svelx = 3
svely = 5
friction = 1
fps = 60;

pygame.init()
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Carrom")




goti_list = pygame.sprite.Group()
all_sprites_list = pygame.sprite.Group()
striker = Striker(BLUE, strikerrad, strikerrad)
all_sprites_list.add(striker)
for i in range(20):
    # This represents a block
    goti = Goti(RED, gotirad, gotirad)
 
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
pygame.draw.rect(screen, BROWN, [0, 0, wid, wid], border)
pygame.display.update()


while not done:
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop

    # screen.blit(background, (0, 0))
    screen.fill(WOOD)

    pygame.draw.rect(screen, BROWN, [0, 0, wid, wid], border)
    # drawCorners()

    all_sprites_list.update()

    for goti in goti_list:
        t_list = []
        for t in goti_list:
            if t!=goti:
                t_list.append(t)

        temp_hit_list = pygame.sprite.spritecollide(goti, t_list, False)
        for hitGoti in temp_hit_list:
            if not goti.collided and not hitGoti.collided:
                hitGoti.velx, goti.velx = goti.velx, hitGoti.velx
                hitGoti.vely, goti.vely = goti.vely, hitGoti.vely
                goti.collided, hitGoti.collided = True, True

    for t in goti_list:
        t.collided = False

    goti_hit_list = pygame.sprite.spritecollide(striker, goti_list, False)

    for goti in goti_hit_list:
        goti.velx = -1*goti.velx
        goti.vely = -1*goti.vely
        
    all_sprites_list.draw(screen)



    # if fps>0:
    #     strikerx += svelx
    #     strikery += svely
    #     # fps -= friction
    # if strikery > wid-border/2-strikerrad or strikery < border/2+strikerrad:
    #     svely = svely * -1
    # if strikerx > wid-border/2-strikerrad or strikerx < border/2+strikerrad:
    #     svelx = svelx * -1
    # pygame.draw.circle(screen, BLUE, [strikerx, strikery], strikerrad)
    # pygame.draw.circle(screen, BLACK, [strikerx, strikery], strikerrad, 2)
    
    pygame.display.flip()
    # Limit to input frames per second
    clock.tick(fps)

pygame.quit()