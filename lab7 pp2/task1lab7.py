import pygame
pygame.init()
screen = pygame.display.set_mode((600, 500))
pygame.display.set_caption("Clock")
icon = pygame.image.load("lab7 pp2/clock.png")
icon = pygame.transform.scale(icon, (600, 500))
hand1 = pygame.image.load("lab7 pp2/min_hand.png")
hand1 = pygame.transform.scale(hand1, (600, 500))
hand2 = pygame.image.load("lab7 pp2/sec_hand.png")
hand2 = pygame.transform.scale(hand2, (600, 500))

running = True
while running:
    screen.blit(icon, (0, 0)) 
    screen.blit(hand1, (0, 0)) 
    screen.blit(hand2, (0, 0)) 

    
    pygame.display.update()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()