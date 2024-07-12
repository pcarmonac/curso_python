import pygame
import random

# Inicializar Pygame
pygame.init()

# Configuración de la pantalla
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders")

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Jugador
player_width = 50
player_height = 50
player = pygame.Rect(WIDTH // 2 - player_width // 2, HEIGHT - player_height - 10, player_width, player_height)
player_speed = 5

# Disparos
bullet_width = 5
bullet_height = 15
bullets = []
bullet_speed = 7

# Alienígenas
alien_width = 50
alien_height = 50
aliens = []
alien_speed = 1
for i in range(5):
    for j in range(5):
        alien = pygame.Rect(100 + i * 100, 50 + j * 70, alien_width, alien_height)
        aliens.append(alien)

# Puntuación
score = 0
font = pygame.font.Font(None, 36)

# Función para dibujar al jugador
def draw_player():
    pygame.draw.rect(screen, GREEN, player)

# Función para dibujar los disparos
def draw_bullets():
    for bullet in bullets:
        pygame.draw.rect(screen, WHITE, bullet)

# Función para dibujar los alienígenas
def draw_aliens():
    for alien in aliens:
        pygame.draw.rect(screen, RED, alien)

# Función para mover los alienígenas
def move_aliens():
    global alien_speed
    for alien in aliens:
        alien.x += alien_speed
        if alien.left <= 0 or alien.right >= WIDTH:
            alien_speed *= -1
            for a in aliens:
                a.y += 20
            break

# Bucle principal del juego
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullet = pygame.Rect(player.centerx - bullet_width // 2, player.top, bullet_width, bullet_height)
                bullets.append(bullet)

    # Movimiento del jugador
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.left > 0:
        player.x -= player_speed
    if keys[pygame.K_RIGHT] and player.right < WIDTH:
        player.x += player_speed

    # Movimiento de los disparos
    for bullet in bullets[:]:
        bullet.y -= bullet_speed
        if bullet.bottom < 0:
            bullets.remove(bullet)

    # Movimiento de los alienígenas
    move_aliens()

    # Colisiones
    for bullet in bullets[:]:
        for alien in aliens[:]:
            if bullet.colliderect(alien):
                bullets.remove(bullet)
                aliens.remove(alien)
                score += 10
                break

    # Dibujar en la pantalla
    screen.fill(BLACK)
    draw_player()
    draw_bullets()
    draw_aliens()

    # Mostrar puntuación
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    # Verificar condición de victoria
    if not aliens:
        victory_text = font.render("¡Victoria!", True, WHITE)
        screen.blit(victory_text, (WIDTH // 2 - 50, HEIGHT // 2))

    # Verificar condición de derrota
    for alien in aliens:
        if alien.bottom >= player.top:
            game_over_text = font.render("Game Over", True, WHITE)
            screen.blit(game_over_text, (WIDTH // 2 - 70, HEIGHT // 2))
            running = False

    # Actualizar la pantalla
    pygame.display.flip()
    clock.tick(60)

pygame.quit()