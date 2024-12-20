import pygame
import random
import time

# Initialize Pygame
pygame.init()

# Set screen dimensions
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

# Define dice faces (0-9)
dice_faces = [i for i in range(10)]
colors = {"black":(255, 255, 255), "white":(0, 0, 0), "red":(255, 0, 0), "green":(0, 255, 0), "blue":(0, 0, 255)}

# Function to roll the dice
def roll_dice():
	return random.choice(dice_faces)

def render(text, color, y, x):
	screen.blit(font.render(text, True, colors[color]), (y, x))

def render16(text, color, y, x):
	for c in text:
		screen.blit(font.render(c, True, colors[color]), (y, x))
		y += 28

# Main game loop
time_step_ms = 1000
start_delay_ms = 2000

start_ms = time.time() * 1000 + start_delay_ms

running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	# Calculate step to display
	step = int((time.time() * 1000 - start_ms) // time_step_ms)

	# Clear screen
	screen.fill((0, 0, 0))

	# Roll the dice
	rolled_number = roll_dice()

	# Draw the rolled number on the screen
	font = pygame.font.Font(None, 30)
	render(str(step), "black", screen_width // 20, screen_height // 20)
	render("output:", "black", screen_width // 20, screen_height // 10 + 8)
	render("answer:", "black", screen_width // 20, screen_height // 5  + 8)
	
	font = pygame.font.Font(None, 64)
	render16("2411754603145530", "black", screen_width // 4.5, screen_height // 10)

	# 5611504432025052
	answer = ""
	for _ in range(16):
		answer += str(roll_dice())
	render16(answer, "red", screen_width // 4.5, screen_height // 5)

	# Update the screen
	pygame.display.flip()

# Quit Pygame
pygame.quit()

# animer digits avec png
# https://search.brave.com/search?q=animation+digit+0+to+9+python&source=llmSuggest&summary=1&conversation=bfdb3853b0a7c8538b16e7
# 3d animation avec manim
# https://manimclass.com/3d-manim-animations/