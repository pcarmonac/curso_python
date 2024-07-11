import pygame
import random

# Inicializar pygame
pygame.init()

# Colores
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# Configuración de la pantalla
WIDTH = 800
HEIGHT = 600
CELL_SIZE = 20
GRID_WIDTH = WIDTH // CELL_SIZE
GRID_HEIGHT = HEIGHT // CELL_SIZE

# Crear la pantalla
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Reloj para controlar la velocidad del juego
clock = pygame.time.Clock()

class Snake:
    def __init__(self):
        self.body = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
        self.direction = (0, -1)

    def move(self):
        head = self.body[0]
        new_head = ((head[0] + self.direction[0]) % GRID_WIDTH, 
                    (head[1] + self.direction[1]) % GRID_HEIGHT)
        self.body.insert(0, new_head)

    def grow(self):
        self.body.append(self.body[-1])

    def check_collision(self):
        return self.body[0] in self.body[1:]

    def draw(self):
        for segment in self.body:
            pygame.draw.rect(screen, GREEN, (segment[0] * CELL_SIZE, 
                                             segment[1] * CELL_SIZE, 
                                             CELL_SIZE, CELL_SIZE))

class Food:
    def __init__(self):
        self.position = self.generate_position()

    def generate_position(self):
        return (random.randint(0, GRID_WIDTH - 1), 
                random.randint(0, GRID_HEIGHT - 1))

    def draw(self):
        pygame.draw.rect(screen, RED, (self.position[0] * CELL_SIZE, 
                                       self.position[1] * CELL_SIZE, 
                                       CELL_SIZE, CELL_SIZE))

def main():
    snake = Snake()
    food = Food()
    score = 0
    game_over = False

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and snake.direction != (0, 1):
                    snake.direction = (0, -1)
                elif event.key == pygame.K_DOWN and snake.direction != (0, -1):
                    snake.direction = (0, 1)
                elif event.key == pygame.K_LEFT and snake.direction != (1, 0):
                    snake.direction = (-1, 0)
                elif event.key == pygame.K_RIGHT and snake.direction != (-1, 0):
                    snake.direction = (1, 0)

        snake.move()

        if snake.body[0] == food.position:
            snake.grow()
            food.position = food.generate_position()
            score += 1

        if snake.check_collision():
            game_over = True

        screen.fill(BLACK)
        snake.draw()
        food.draw()

        # Mostrar puntuación
        font = pygame.font.Font(None, 36)
        text = font.render(f"Score: {score}", True, WHITE)
        screen.blit(text, (10, 10))

        pygame.display.flip()
        clock.tick(10)  # Controla la velocidad del juego

    print(f"Game Over! Final Score: {score}")
    pygame.quit()

if __name__ == "__main__":
    main()