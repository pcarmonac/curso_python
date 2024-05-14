import pygame

# Inicializar pygame
pygame.init()

# Asignar tamaño de la pantalla
size = (700, 500)
screen = pygame.display.set_mode(size)

# Asignar título de la ventana
pygame.display.set_caption("Mi juego Pong")

# Asignar posición inicial de la pelota
ball_pos = [350, 250]

# Asignar velocidad inicial de la pelota
ball_vel = [5, 5]

# Asignar posición inicial de las raquetas
paddle1_pos = [20, 200]
paddle2_pos = [660, 200]

# Asignar tamaño de las raquetas
paddle_size = [20, 100]

# Asignar colores
white = (255, 255, 255)
black = (0, 0, 0)

# Iniciar bucle del juego
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Mover la pelota
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]

    # Revisar colisiones con los bordes
    if ball_pos[0] <= 0 or ball_pos[0] >= size[0]:
        ball_vel[0] = -ball_vel[0]
    if ball_pos[1] <= 0 or ball_pos[1] >= size[1]:
        ball_vel[1] = -ball_vel[1]

    # Revisar colisiones con las raquetas
    if (ball_pos[0] <= paddle1_pos[0] + paddle_size[0] and
            ball_pos[1] >= paddle1_pos[1] and
            ball_pos[1] <= paddle1_pos[1] + paddle_size[1]):
        ball_vel[0] = -ball_vel[0]
    if (ball_pos[0] >= paddle2_pos[0] and
            ball_pos[1] >= paddle2_pos[1] and
            ball_pos[1] <= paddle2_pos[1] + paddle_size[1]):
        ball_vel[0] = -ball_vel[0]

    # Controlar movimiento de las raquetas con el teclado
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        paddle1_pos[1] -= 5
    if keys[pygame.K_DOWN]:
        paddle1_pos[1] += 5
    if keys[pygame.K_w]:
        paddle2_pos[1] -= 5
    if keys[pygame.K_s]:
        paddle2_pos[1] += 5

    # Limitar movimiento de las raquetas dentro de
