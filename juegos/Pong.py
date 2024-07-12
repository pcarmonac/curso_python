import pygame
import random

# Inicializar Pygame
pygame.init()

# Configuración de la pantalla
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Palas
PADDLE_WIDTH = 15
PADDLE_HEIGHT = 90
PADDLE_SPEED = 5

# Pelota
BALL_SIZE = 15
BALL_SPEED_X = 7
BALL_SPEED_Y = 7

# Crear palas
player = pygame.Rect(50, HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)
opponent = pygame.Rect(WIDTH - 50 - PADDLE_WIDTH, HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)

# Crear pelota
ball = pygame.Rect(WIDTH//2 - BALL_SIZE//2, HEIGHT//2 - BALL_SIZE//2, BALL_SIZE, BALL_SIZE)

# Velocidad de la pelota
ball_speed_x = BALL_SPEED_X * random.choice((1, -1))
ball_speed_y = BALL_SPEED_Y * random.choice((1, -1))

# Puntuaciones
player_score = 0
opponent_score = 0
font = pygame.font.Font(None, 36)

# Función para mover la pelota
def move_ball(ball):
    global ball_speed_x, ball_speed_y, player_score, opponent_score

    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Colisión con los bordes superior e inferior
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed_y *= -1

    # Puntuación
    if ball.left <= 0:
        opponent_score += 1
        ball_restart()
    if ball.right >= WIDTH:
        player_score += 1
        ball_restart()

    # Colisión con las palas
    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1

# Función para reiniciar la posición de la pelota
def ball_restart():
    global ball_speed_x, ball_speed_y
    ball.center = (WIDTH//2, HEIGHT//2)
    ball_speed_y *= random.choice((1, -1))
    ball_speed_x *= random.choice((1, -1))

# Bucle principal del juego
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Movimiento del jugador
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and player.top > 0:
        player.y -= PADDLE_SPEED
    if keys[pygame.K_DOWN] and player.bottom < HEIGHT:
        player.y += PADDLE_SPEED

    # Movimiento del oponente (IA simple)
    if opponent.top < ball.y:
        opponent.y += PADDLE_SPEED
    if opponent.bottom > ball.y:
        opponent.y -= PADDLE_SPEED

    # Mover la pelota
    move_ball(ball)

    # Dibujar en la pantalla
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, player)
    pygame.draw.rect(screen, WHITE, opponent)
    pygame.draw.ellipse(screen, WHITE, ball)
    pygame.draw.aaline(screen, WHITE, (WIDTH//2, 0), (WIDTH//2, HEIGHT))

    # Mostrar puntuaciones
    player_text = font.render(str(player_score), True, WHITE)
    opponent_text = font.render(str(opponent_score), True, WHITE)
    screen.blit(player_text, (WIDTH//4, 20))
    screen.blit(opponent_text, (3*WIDTH//4, 20))

    # Actualizar la pantalla
    pygame.display.flip()
    clock.tick(60)

pygame.quit()