import pygame

# Define some constants
BLACK    = (   0,   0,   0)
LBROWN   = (  70,   0,   0)
DBROWN   = (  20,   0,   0)
DGRAY    = (  30,  30,  30)
WHITE    = ( 255, 255, 255)
WOOD     = ( 220, 200, 150)
BLUE     = (   0,   0, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
PI = 3.141592653
border = 80

strikerrad = 45
pocketrad = 30
gotirad = 32
gotispeedx = 1.0
gotispeedy = 2.0
friction = 1.0
fps = 100;

# Set the width and height of the screen [width, height]
scrsize = (700, 700)
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
        pygame.draw.ellipse(self.image, color, [0, 0, gotirad, gotirad])
        pygame.draw.ellipse(self.image, BLACK, [0, 0, gotirad, gotirad], 2)
        # Fetch the rectangle object that has the dimensions of the image
        # image.
        # Update the position of this object by setting the values
        # of rect.x and rect.y
        self.rect = self.image.get_rect()
        self.velx = gotispeedx
        self.vely = gotispeedy
        self.collided = False
        self.radius = gotirad/2

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
    def __init__(self, color):
        """ Constructor. Pass in the color of the block,
        and its x and y position. """
 
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)
 
        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = pygame.Surface([strikerrad, strikerrad])
        self.image.fill(WOOD)
        self.image.set_colorkey(WOOD)
        pygame.draw.ellipse(self.image, color, [0, 0, strikerrad, strikerrad])
        pygame.draw.ellipse(self.image, BLACK, [0, 0, strikerrad, strikerrad], 2)
        # Fetch the rectangle object that has the dimensions of the image
        # image.
        # Update the position of this object by setting the values
        # of rect.x and rect.y
        self.rect = self.image.get_rect()
        self.velx = gotispeedx
        self.vely = gotispeedy
        self.collided = False
        self.radius = strikerrad/2

    def update(self):
        # Get the current mouse position. This returns the position
        # as a list of two numbers.
        pos = pygame.mouse.get_pos()
        # Fetch the x and y out of the list, 
        # just like we'd fetch letters out of a string.
        # Set the player object to the mouse location
        self.rect.x = pos[0]
        self.rect.y = pos[1]

class Bullet(pygame.sprite.Sprite):
    """ This class represents the bullet . """
    def __init__(self):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)
 
        self.image = pygame.Surface([4, 10])
        self.image.fill(BLACK)
 
        self.rect = self.image.get_rect()
 
    def update(self):
        """ Move the bullet. """
        self.rect.y -= 3

