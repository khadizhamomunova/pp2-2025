import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Game Settings
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
GRID_SIZE = 20
FPS = 10

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (225, 0, 0)
GREEN = (0, 180, 0)
BLUE = (30, 144, 255)
YELLOW = (255, 215, 0)

# Directions
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# Fonts
font_large = pygame.font.SysFont('Arial', 48)
font_small = pygame.font.SysFont('Arial', 24)

# Initialize screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Advanced Snake Game')

# Clock
clock = pygame.time.Clock()

# High Score
try:
    with open('high_score.txt', 'r') as f:
        high_score = int(f.read())
except:
    high_score = 0

# Snake Class
class Snake:
    def __init__(self):
        self.positions = [((SCREEN_WIDTH // 2), (SCREEN_HEIGHT // 2))]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.length = 1
        self.color = GREEN
        self.score = 0

    def head_position(self):
        return self.positions[0]

    def move(self):
        x, y = self.head_position()
        dx, dy = self.direction
        new_position = ((x + dx * GRID_SIZE) % SCREEN_WIDTH, (y + dy * GRID_SIZE) % SCREEN_HEIGHT)
        if new_position in self.positions[2:]:
            self.reset()
        else:
            self.positions.insert(0, new_position)
            if len(self.positions) > self.length:
                self.positions.pop()

    def reset(self):
        global high_score
        if self.score > high_score:
            high_score = self.score
            with open('high_score.txt', 'w') as f:
                f.write(str(high_score))
        self.__init__()

    def draw(self, surface):
        for p in self.positions:
            rect = pygame.Rect(p[0], p[1], GRID_SIZE, GRID_SIZE)
            pygame.draw.rect(surface, self.color, rect)

    def handle_keys(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Pause functionality
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    return 'pause'
                elif event.key == pygame.K_UP:
                    if self.direction != DOWN:
                        self.direction = UP
                elif event.key == pygame.K_DOWN:
                    if self.direction != UP:
                        self.direction = DOWN
                elif event.key == pygame.K_LEFT:
                    if self.direction != RIGHT:
                        self.direction = LEFT
                elif event.key == pygame.K_RIGHT:
                    if self.direction != LEFT:
                        self.direction = RIGHT

# Food Class
class Food:
    def __init__(self, obstacles, snake_positions):
        self.position = (0, 0)
        self.color = RED
        self.randomize_position(obstacles, snake_positions)

    def randomize_position(self, obstacles, snake_positions):
        while True:
            self.position = (
                random.randint(0, (SCREEN_WIDTH - GRID_SIZE) // GRID_SIZE) * GRID_SIZE,
                random.randint(0, (SCREEN_HEIGHT - GRID_SIZE) // GRID_SIZE) * GRID_SIZE
            )
            if self.position not in obstacles and self.position not in snake_positions:
                break

    def draw(self, surface):
        rect = pygame.Rect(self.position[0], self.position[1], GRID_SIZE, GRID_SIZE)
        pygame.draw.rect(surface, self.color, rect)

# Obstacle Class
class Obstacle:
    def __init__(self, level):
        self.positions = []
        self.color = BLUE
        self.generate_obstacles(level)

    def generate_obstacles(self, level):
        num_obstacles = level * 5
        for _ in range(num_obstacles):
            x = random.randint(0, (SCREEN_WIDTH - GRID_SIZE) // GRID_SIZE) * GRID_SIZE
            y = random.randint(0, (SCREEN_HEIGHT - GRID_SIZE) // GRID_SIZE) * GRID_SIZE
            self.positions.append((x, y))

    def draw(self, surface):
        for p in self.positions:
            rect = pygame.Rect(p[0], p[1], GRID_SIZE, GRID_SIZE)
            pygame.draw.rect(surface, self.color, rect)

def draw_grid(surface):
    for y in range(0, SCREEN_HEIGHT, GRID_SIZE):
        pygame.draw.line(surface, BLACK, (0, y), (SCREEN_WIDTH, y))
    for x in range(0, SCREEN_WIDTH, GRID_SIZE):
        pygame.draw.line(surface, BLACK, (x, 0), (x, SCREEN_HEIGHT))

def main():
    snake = Snake()
    level = 1
    obstacles = Obstacle(level)
    food = Food(obstacles.positions, snake.positions)
    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()

    running = True
    paused = False
    global FPS

    while running:
        clock.tick(FPS)
        action = snake.handle_keys()
        if action == 'pause':
            paused = not paused

        if not paused:
            snake.move()
            if snake.head_position() in obstacles.positions:
                snake.reset()

            if snake.head_position() == food.position:
                snake.length += 1
                snake.score += 1
                food.randomize_position(obstacles.positions, snake.positions)
                if snake.score % 5 == 0:
                    level += 1
                    FPS += 2
                    obstacles = Obstacle(level)
            surface.fill(WHITE)
            draw_grid(surface)
            snake.draw(surface)
            food.draw(surface)
            obstacles.draw(surface)
            screen.blit(surface, (0, 0))

            # Display score and level
            score_text = font_small.render(f"Score: {snake.score}", True, BLACK)
            level_text = font_small.render(f"Level: {level}", True, BLACK)
            high_score_text = font_small.render(f"High Score: {high_score}", True, BLACK)
            screen.blit(score_text, (5, 5))
            screen.blit(level_text, (5, 30))
            screen.blit(high_score_text, (5, 55))

            pygame.display.update()
        else:
            # Pause screen
            pause_text = font_large.render("Paused", True, YELLOW)
            screen.blit(pause_text, (SCREEN_WIDTH // 2 - pause_text.get_width() // 2,
                                     SCREEN_HEIGHT // 2 - pause_text.get_height() // 2))
            pygame.display.update()

if __name__ == "__main__":
    main()