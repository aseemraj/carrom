import pygame
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
