# Created from AI with prompt in Brave: https://search.brave.com/search?q=pygame+show+casino+rolling+number&source=desktop&summary=1&conversation=117962a6ffdc052a128b75
import pygame
import random

# Initialize Pygame
pygame.init()

# Set screen dimensions
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

# Define dice faces (1-6)
dice_faces = [1, 2, 3, 4, 5, 6]

# Function to roll the dice
def roll_dice():
    return random.choice(dice_faces)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear screen
    screen.fill((255, 255, 255))

    # Roll the dice
    rolled_number = roll_dice()

    # Draw the rolled number on the screen
    font = pygame.font.Font(None, 72)
    text = font.render(str(rolled_number), True, (0, 0, 0))
    screen.blit(text, (screen_width // 2, screen_height // 2))

    # Update the screen
    pygame.display.flip()

# Quit Pygame
pygame.quit()