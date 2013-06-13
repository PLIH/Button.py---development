
import pygame, Buttons



def texts(toPrint):
    font = pygame.font.SysFont("None", 30)
    label = font.render(toPrint, 1, (255,255,255))
    return label

def main():
    pygame.init()

    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Button Test")

    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((200,155,70))
    

    #Buttons?
    button1 = Buttons.Button()

    
    clock = pygame.time.Clock()
    keepGoing = True
    caption = ""

    while keepGoing:
        clock.tick(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                    if button1.onClick(pygame.mouse.get_pos()):
                        caption = "Give me a command!"

                        
        screen.blit(background, (0, 0))
        #button1.alpha_circle(screen, (107,142,35),50,25,150,135)
        button1.invisiSquare(screen, 150, 135, 50, 25, 0, " 5 ", (255,255,255))

        myLabel = texts(caption)
        screen.blit(myLabel, (450,450))
        pygame.display.flip()

if __name__ == "__main__": main()
