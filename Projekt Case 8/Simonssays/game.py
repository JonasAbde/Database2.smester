import pygame
import random
import time

pygame.init()
WIDTH, HEIGHT = 600, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simon's Game")

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)

red_button = pygame.Rect(50, 50, 200, 200)
green_button = pygame.Rect(350, 50, 200, 200)
blue_button = pygame.Rect(50, 350, 200, 200)
yellow_button = pygame.Rect(350, 350, 200, 200)

sequence = []
player_sequence = []
score = 0

def draw_buttons():
    pygame.draw.rect(win, RED, red_button)
    pygame.draw.rect(win, GREEN, green_button)
    pygame.draw.rect(win, BLUE, blue_button)
    pygame.draw.rect(win, YELLOW, yellow_button)

def blink_button(color):
    colors = {"red": RED, "green": GREEN, "blue": BLUE, "yellow": YELLOW}
    button_map = {"red": red_button, "green": green_button, "blue": blue_button, "yellow": yellow_button}
    pygame.draw.rect(win, WHITE, button_map[color])
    pygame.display.update()
    time.sleep(0.5)
    pygame.draw.rect(win, colors[color], button_map[color])
    pygame.display.update()
    time.sleep(0.5)

def play_sequence():
    for color in sequence:
        blink_button(color)

def add_random_color():
    color = random.choice(["red", "green", "blue", "yellow"])
    sequence.append(color)
    play_sequence()

def run_game(socketio):
    global score
    running = True
    add_random_color()

    while running:
        win.fill((0, 0, 0))
        draw_buttons()

        font = pygame.font.SysFont(None, 50)
        score_text = font.render(f"Score: {score}", True, WHITE)
        win.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, 10))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if red_button.collidepoint(mouse_pos):
                    player_sequence.append("red")
                elif green_button.collidepoint(mouse_pos):
                    player_sequence.append("green")
                elif blue_button.collidepoint(mouse_pos):
                    player_sequence.append("blue")
                elif yellow_button.collidepoint(mouse_pos):
                    player_sequence.append("yellow")

                if player_sequence == sequence[:len(player_sequence)]:
                    if len(player_sequence) == len(sequence):
                        score += 1
                        player_sequence.clear()
                        add_random_color()
                        socketio.emit('update', {'score': score, 'sequence': sequence})
                else:
                    sequence.clear()
                    player_sequence.clear()
                    score = 0
                    add_random_color()
                    socketio.emit('update', {'score': score, 'sequence': sequence})
