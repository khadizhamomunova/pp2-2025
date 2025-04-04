import pygame
pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("ball")

x, y = 250, 250
radius = 25
speed = 20 

running = True
while running:

    
    screen.fill((255,255,255))
    
    pygame.draw.circle(screen, ("Red"), (x, y), radius)  
    

   
    pygame.display.update()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            # Проверяем, можно ли двигать вверх
            if event.key == pygame.K_UP and y - speed - radius >= 0:
                y -= speed  # двигаем круг вверх
            # Проверяем, можно ли двигать вниз
            elif event.key == pygame.K_DOWN and y + speed + radius <= 600:
                y += speed  # двигаем круг вниз
            # Проверяем, можно ли двигать влево
            elif event.key == pygame.K_LEFT and x - speed - radius >= 0:
                x -= speed  # двигаем круг влево
            # Проверяем, можно ли двигать вправо
            elif event.key == pygame.K_RIGHT and x + speed + radius <= 600:
                x += speed  # двигаем круг вправо