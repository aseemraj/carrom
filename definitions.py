import pygame
from math import *

# Define some constants
BLACK    = (   0,   0,   0)
LBROWN   = (  80,  30,   0)
DBROWN   = (  50,  20,   0)
DGRAY    = (  30,  30,  30)
WHITE    = ( 255, 255, 255)
WOOD     = ( 220, 200, 150)
BLUE     = (   0,   0, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
PI = 3.141592653
LEFT = 1
RIGHT = 3
border = 70

strikerrad = 40
pocketrad = 30
gotirad = 26
gotispeedx = 0
gotispeedy = 0
friction = 0.1
fps = 70;

# Set the width and height of the screen [width, height]
scrsize = (720, 720)
wid = scrsize[0]
mod = lambda v: sqrt(v[0] * v[0] + v[1] * v[1])

class Goti(pygame.sprite.Sprite):
    """
    This class represents the goti.
    It derives from the "Sprite" class in Pygame.
    """
    def __init__(self, color):
        """ Constructor. Pass in the color of the block,
        and its x and y position. """
 
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)
 
        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = pygame.Surface([gotirad, gotirad])
        self.image.fill(WOOD)
        self.image.set_colorkey(WOOD)
        if color==BLACK:
            self.isWhite = False
            for i in range(gotirad/2):
                pygame.draw.ellipse(self.image, (5*i, 5*i, 5*i), [i, i, gotirad-2*i, gotirad-2*i])
                pygame.draw.ellipse(self.image, BLACK, [0, 0, gotirad, gotirad], 2)
        elif color==WHITE:
            self.isWhite = True
            for i in range(gotirad/2):
                pygame.draw.ellipse(self.image, (255-5*i, 255-5*i, 255-5*i), [i, i, gotirad-2*i, gotirad-2*i])
                pygame.draw.ellipse(self.image, WHITE, [0, 0, gotirad, gotirad], 2)
        # Fetch the rectangle object that has the dimensions of the image
        # image.
        # Update the position of this object by setting the values
        # of rect.x and rect.y
        self.rect = self.image.get_rect()
        self.rad = gotirad/2
        self.velx = gotispeedx
        self.vely = gotispeedy
        self.collided = False

    def update(self):
        """ Called each frame. """
        # Move block down one pixel
        self.rect.x += self.velx
        self.rect.y += self.vely
        # If block is too far down, reset to top of screen.
        if self.rect.y > wid-border/2-gotirad:
            self.rect.y = wid - border/2 - gotirad - 1
            self.vely = -1*abs(self.vely)
        elif self.rect.y<border/2:
            self.rect.y = border/2 + 1
            self.vely = abs(self.vely)
        if self.rect.x > wid-border/2-gotirad:
            self.rect.x = wid - border/2 - gotirad - 1
            self.velx = -1*abs(self.velx)
        elif self.rect.x<border/2:
            self.rect.x = border/2 + 1
            self.velx = abs(self.velx)
        if mod([self.velx, self.vely])==0:
            self.velx = 0
            self.vely = 0
        else:
            self.velx = self.velx - friction * self.velx / mod([self.velx, self.vely])  # friction acts in a direction
            self.vely = self.vely - friction * self.vely / mod([self.velx, self.vely])  # opposite to velocity
            if abs(self.velx)<friction:
                self.velx = 0
            if abs(self.vely)<friction:
                self.vely = 0

class Striker(Goti):
    """ The player class derives from Block, but overrides the 'update' 
    functionality with new a movement function that will move the block 
    with the mouse. """
    def __init__(self):
        """ Constructor. Pass in the color of the block,
        and its x and y position. """
 
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)
 
        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = pygame.Surface([strikerrad, strikerrad])
        self.image.fill(WOOD)
        self.image.set_colorkey(WOOD)
        for i in range(strikerrad/2):
            pygame.draw.ellipse(self.image, (5*i, 5*i, 100+5*i), [i, i, strikerrad-2*i, strikerrad-2*i])
        # pygame.draw.ellipse(self.image, color, [0, 0, strikerrad, strikerrad])
        pygame.draw.ellipse(self.image, BLACK, [0, 0, strikerrad, strikerrad], 2)
        # Fetch the rectangle object that has the dimensions of the image
        # image.
        # Update the position of this object by setting the values
        # of rect.x and rect.y
        self.velx = 0
        self.vely = 0
        self.rect = self.image.get_rect()
        self.rad = strikerrad/2
        self.collided = False
        self.state = 0
        self.player = 0

    def update(self):
        # User is still placing the striker
        if self.state==0:
            pos = pygame.mouse.get_pos()
            if self.player==0 or self.player==2:
                self.rect.x = pos[0]-strikerrad/2
                if self.player==0:
                    self.rect.y = wid-pocketrad-border-gotirad/2-strikerrad/2
                else:
                    self.rect.y = pocketrad+border+gotirad/2-strikerrad/2
                if pos[0]>wid-(strikerrad/2+pocketrad+border+gotirad):
                    self.rect.x = wid-(strikerrad+pocketrad+border+gotirad)
                elif pos[0]<pocketrad+border+gotirad+strikerrad/2:
                    self.rect.x = pocketrad+border+gotirad
            else:
                self.rect.y = pos[1]-strikerrad/2
                if self.player==1:
                    self.rect.x = wid-pocketrad-border-gotirad/2-strikerrad/2
                else:
                    self.rect.x = pocketrad+border+gotirad/2-strikerrad/2
                if pos[1]>wid-(strikerrad/2+pocketrad+border+gotirad):
                    self.rect.y = wid-(strikerrad+pocketrad+border+gotirad)
                elif pos[1]<pocketrad+border+gotirad+strikerrad/2:
                    self.rect.y = pocketrad+border+gotirad

        # User launched the striker
        elif self.state==2:
            self.rect.x += self.velx
            self.rect.y += self.vely
            if self.rect.y > wid-border/2-gotirad:
                self.rect.y = wid - border/2 - gotirad - 1
                self.vely = -1*abs(self.vely)
            elif self.rect.y<border/2:
                self.rect.y = border/2 + 1
                self.vely = abs(self.vely)
            if self.rect.x > wid-border/2-gotirad:
                self.rect.x = wid - border/2 - gotirad - 1
                self.velx = -1*abs(self.velx)
            elif self.rect.x<border/2:
                self.rect.x = border/2 + 1
                self.velx = abs(self.velx)
            if mod([self.velx, self.vely])==0:
                self.velx = 0
                self.vely = 0
            else:
                self.velx = self.velx - friction * self.velx / mod([self.velx, self.vely])  # friction acts in a direction
                self.vely = self.vely - friction * self.vely / mod([self.velx, self.vely])  # opposite to velocity
                if abs(self.velx)<friction:
                    self.velx = 0
                if abs(self.vely)<friction:
                    self.vely = 0
