from django.shortcuts import render
from django.http import JsonResponse
import random

# Variables globales para el estado del juego
GRID_SIZE = 20
GRID_WIDTH = 20
GRID_HEIGHT = 20
snake = [(10, 10)]
food = (15, 15)
direction = (0, -1)
score = 0

def game(request):
    global snake, food, direction, score
    snake = [(10, 10)]
    food = (15, 15)
    direction = (0, -1)
    score = 0
    return render(request, 'game/game.html')

def move_snake(request):
    global snake, food, direction, score

    if request.method == 'POST':
        new_direction = request.POST.get('direction')
        if new_direction == 'left' and direction != (1, 0):
            direction = (-1, 0)
        elif new_direction == 'right' and direction != (-1, 0):
            direction = (1, 0)
        elif new_direction == 'up' and direction != (0, 1):
            direction = (0, -1)
        elif new_direction == 'down' and direction != (0, -1):
            direction = (0, 1)

    head = snake[0]
    new_head = ((head[0] + direction[0]) % GRID_WIDTH, (head[1] + direction[1]) % GRID_HEIGHT)

    if new_head == food:
        snake.insert(0, new_head)
        food = generate_food()
        score += 1
    else:
        snake = [new_head] + snake[:-1]

    game_over = check_collision()

    return JsonResponse({
        'snake': snake,
        'food': food,
        'score': score,
        'game_over': game_over
    })

def generate_food():
    while True:
        new_food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
        if new_food not in snake:
            return new_food

def check_collision():
    head = snake[0]
    return head in snake[1:]