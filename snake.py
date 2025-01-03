import pygame
import random

# Inisialisasi Pygame
pygame.init()

# Konstanta
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400
GRID_SIZE = 20
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE

# Warna Palet Soft atau Pastel
WHITE = (255, 255, 255)
PASTEL_GREEN = (107, 142, 35)
PASTEL_BLUE = (173, 216, 230)
PASTEL_YELLOW = (255, 255, 153)

# Fungsi utama
def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Snake Game")

    clock = pygame.time.Clock()

    while True:
        # Main menu
        main_menu(screen)

        # Inisialisasi permainan
        snake = Snake()
        food = Food()
        snake_color = WHITE

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        # Pause menu
                        pause_menu(screen)
                    elif event.key == pygame.K_UP:
                        snake.change_direction(0, -1)
                    elif event.key == pygame.K_DOWN:
                        snake.change_direction(0, 1)
                    elif event.key == pygame.K_LEFT:
                        snake.change_direction(-1, 0)
                    elif event.key == pygame.K_RIGHT:
                        snake.change_direction(1, 0)

            snake.move()
            snake.check_collision(food)
            screen.fill(PASTEL_BLUE)
            snake.draw(screen, snake_color)
            food.draw(screen, PASTEL_YELLOW)
            pygame.display.update()
            clock.tick(10)

# Kelas Ular
class Snake:
    def __init__(self):
        self.body = [(5, 5)]
        self.direction = (1, 0)

    def change_direction(self, x, y):
        if (x, y) != (-self.direction[0], -self.direction[1]):
            self.direction = (x, y)

    def move(self):
        new_head = (self.body[0][0] + self.direction[0], self.body[0][1] + self.direction[1])
        self.body.insert(0, new_head)

    def check_collision(self, food):
        if self.body[0] == food.position:
            food.randomize_position()
        else:
            self.body.pop()

    def draw(self, screen, color):
        for segment in self.body:
            x, y = segment
            pygame.draw.rect(screen, color, pygame.Rect(x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE))

# Kelas Makanan
class Food:
    def __init__(self):
        self.position = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))

    def randomize_position(self):
        self.position = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))

    def draw(self, screen, color):
        x, y = self.position
        pygame.draw.rect(screen, color, pygame.Rect(x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE))

# Menu Utama
def main_menu(screen):
    menu = True
    while menu:
        screen.fill(PASTEL_GREEN)
        font = pygame.font.Font(None, 36)
        title_text = font.render("Snake Game", True, WHITE)
        start_text = font.render("Press SPACE to Start", True, WHITE)
        screen.blit(title_text, (150, 150))
        screen.blit(start_text, (110, 200))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    menu = False
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

# Menu Jeda
def pause_menu(screen):
    paused = True
    while paused:
        screen.fill(PASTEL_GREEN)
        font = pygame.font.Font(None, 36)
        pause_text = font.render("Paused", True, WHITE)
        resume_text = font.render("Press SPACE to Resume", True, WHITE)
        screen.blit(pause_text, (170, 150))
        screen.blit(resume_text, (110, 200))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    paused = False
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

if __name__ == "__main__":
    main()
