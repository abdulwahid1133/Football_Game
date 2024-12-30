import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 128, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)

# Create screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Multiplayer Football Game")

# Players
player1 = pygame.Rect(100, HEIGHT // 2 - 25, 50, 50)  # Player 1 (Red)
player2 = pygame.Rect(WIDTH - 150, HEIGHT // 2 - 25, 50, 50)  # Player 2 (Blue)

# Ball
ball = pygame.Rect(WIDTH // 2 - 15, HEIGHT // 2 - 15, 30, 30)  # Ball (Yellow)
ball_speed = [random.choice([-4, 4]), random.choice([-4, 4])]  # Ball speed

# Goals
goal_left = pygame.Rect(0, HEIGHT // 3, 20, HEIGHT // 3)
goal_right = pygame.Rect(WIDTH - 20, HEIGHT // 3, 20, HEIGHT // 3)

# Speeds
player_speed = 5

# Scores
score1 = 0
score2 = 0

# Clock and timer
clock = pygame.time.Clock()
game_time = 60  # Game time in seconds
start_ticks = pygame.time.get_ticks()

# Game loop
running = True
while running:
    screen.fill(GREEN)  # Draw the field

    # Draw goals
    pygame.draw.rect(screen, BLACK, goal_left)
    pygame.draw.rect(screen, BLACK, goal_right)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player 1 movement (Arrow keys)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and player1.top > 0: player1.y -= player_speed
    if keys[pygame.K_DOWN] and player1.bottom < HEIGHT: player1.y += player_speed
    if keys[pygame.K_LEFT] and player1.left > 0: player1.x -= player_speed
    if keys[pygame.K_RIGHT] and player1.right < WIDTH: player1.x += player_speed

    # Player 2 movement (WASD keys)
    if keys[pygame.K_w] and player2.top > 0: player2.y -= player_speed
    if keys[pygame.K_s] and player2.bottom < HEIGHT: player2.y += player_speed
    if keys[pygame.K_a] and player2.left > 0: player2.x -= player_speed
    if keys[pygame.K_d] and player2.right < WIDTH: player2.x += player_speed

    # Ball movement
    ball.x += ball_speed[0]
    ball.y += ball_speed[1]

    # Ball collision with walls
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed[1] = -ball_speed[1]
    if ball.left <= 0 or ball.right >= WIDTH:
        ball_speed[0] = -ball_speed[0]

    # Ball collision with players
    if ball.colliderect(player1) or ball.colliderect(player2):
        ball_speed[0] = -ball_speed[0]
        ball_speed[1] = random.choice([-4, 4])

    # Scoring
    if ball.colliderect(goal_left):
        score2 += 1
        ball.center = (WIDTH // 2, HEIGHT // 2)  # Reset ball
        ball_speed = [random.choice([-4, 4]), random.choice([-4, 4])]  # Reset speed

    if ball.colliderect(goal_right):
        score1 += 1
        ball.center = (WIDTH // 2, HEIGHT // 2)  # Reset ball
        ball_speed = [random.choice([-4, 4]), random.choice([-4, 4])]  # Reset speed

    # Draw players and ball
    pygame.draw.rect(screen, RED, player1)
    pygame.draw.rect(screen, BLUE, player2)
    pygame.draw.ellipse(screen, YELLOW, ball)

    # Display scores
    font = pygame.font.Font(None, 74)
    text1 = font.render(str(score1), True, WHITE)
    text2 = font.render(str(score2), True, WHITE)
    screen.blit(text1, (WIDTH // 4, 10))
    screen.blit(text2, (3 * WIDTH // 4, 10))

    # Timer
    elapsed_time = (pygame.time.get_ticks() - start_ticks) // 1000
    remaining_time = max(0, game_time - elapsed_time)
    timer_text = font.render(f"Time: {remaining_time}", True, WHITE)
    screen.blit(timer_text, (WIDTH // 2 - 100, 10))

    if remaining_time == 0:
        running = False  # End the game when the timer reaches 0

    # Update display
    pygame.display.flip()

    # Control frame rate
    clock.tick(30)

# End screen
screen.fill(BLACK)
end_text = font.render("Game Over!", True, WHITE)
screen.blit(end_text, (WIDTH // 2 - 150, HEIGHT // 2 - 50))
pygame.display.flip()
pygame.time.wait(3000)

# Quit Pygame
pygame.quit()
