import pygame
pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("player")

running = True
while running:
 
    screen.fill((255,255,255)) 
    pygame.draw.line(screen, ("red"), (50, 480), (550, 480), 40)
    pygame.draw.polygon(screen,("red"),((200,100),(400,250),(200,400)))
    
    pygame.display.update()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()


