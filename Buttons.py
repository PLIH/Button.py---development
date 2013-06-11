#Source File Name: Buttons.py
#Author's Name: Paige Harvey
#Last Modified By: Paige Harvey
#Last Modified On: 2012-06-10
#Program Description: A buttons class for import
# Will have methods to create clickable rectangle, ellipses, and texts.

# Full working method list:
#   square + text
#   circle + text
#   square
#   circle
#   text
#   alpha square
#   alpha circle
#   invisiable square

import pygame

pygame.init()

class Button:

    #a funct for square & text

    #a funct for circle & text

    #a funct for square
    def square(self, surface, colour, length, height, x, y):
        pygame.draw.rect(surface, colour, (x,y,length,height), 0)
        self.rect = pygame.Rect(x,y,length,height)
        return surface

    #a funct for circle
    def circle(self, surface, colour, length, height, x, y):
        pygame.draw.ellipse(surface, colour, (x,y,length,height),0)
        self.rect = pygame.Rect(x,y,length,height)
        return surface

    #a funct for text
    def text(self, surface, text, colour, size, x, y):
        font = pygame.font.SysFont("None", size)
        myText = font.render(text, 1, colour)
        surface.blit(myText, (x,y))
        return surface

    #a funct for text + invisi square

    #an alpha square
    def alpha_square(self, surface, colour, length, height, x, y):
        for i in range(1,10):
            s = pygame.Surface((length+(i*2), height+(i*2)))
            s.fill(colour)
            alpha = (255/(i+2))
            if alpha <= 0:
                alpha = 1
            s.set_alpha(alpha)
            pygame.draw.rect(s, colour, (x-i,y-i,length+i,height+i),0)
            surface.blit(s,(x-i,y-i))
        pygame.draw.rect(surface, colour,(x,y,length,height),0)
        pygame.draw.rect(surface, (190,190,190), (x,y,length,height),1)
        self.rect = pygame.Rect(x,y,length,height)
        return surface

    #an alpha circle
    def alpha_circle(self, surface, colour, length, height, x, y):
        for i in range(1,10):
            s = pygame.Surface((length+(i*2), height+(i*2)))
            s.fill(colour)
            alpha = (255/(i+2))
            if alpha <= 0:
                alpha = 1
            s.set_alpha(alpha)
            pygame.draw.ellipse(s, colour, (x-i,y-i,length+i,height+i),0)
            surface.blit(s,(x-i,y-i))
        pygame.draw.ellipse(surface, colour,(x,y,length,height),0)
        pygame.draw.ellipse(surface, (190,190,190), (x,y,length,height),1)
        self.rect = pygame.Rect(x,y,length,height)
        return surface
    
    def onClick(self, mouse):
        if mouse[0] > self.rect.topleft[0]:
            if mouse[1] > self.rect.topleft[1]:
                if mouse[0] < self.rect.bottomright[0]:
                    if mouse[1] < self.rect.bottomright[1]:
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False
