import pygame
import random
import sys
from pygame import mixer

pygame.init()

# Screen width and height
width, height = 800, 600
block_size = 17
border_width = 10

# Create screen and name the icon
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("FACE RECOG")

# background sound
mixer.music.load("background.wav")
mixer.music.play(-1)



# Use image for icon
icon = pygame.image.load("uno.jpg")
pygame.display.set_icon(icon)

# Colors
red = (255, 0, 0)


def random_position(width, height, block_size, border_width):
    return [
        random.randint(border_width // block_size, (width - block_size - border_width) // block_size) * block_size,
        random.randint(border_width // block_size, (height - block_size - border_width) // block_size) * block_size
    ]


# Snake random position
snake_pos = [(100,50),(120,50),(140,50)]
direction = "RIGHT"
snake_radius = block_size // 2

# Food
foodImg = pygame.image.load("circle.png")
foodX, foodY = random_position(width, 500, block_size, border_width)

# Player catches the food
food_width = foodImg.get_width()
food_height = foodImg.get_height()


def food(x, y):
    screen.blit(foodImg, (x, y))


def is_collision(x1, y1, x2, y2, w1, h1, w2, h2):
    return (x1 < x2 + w2 and
            x1 + w1 > x2 and
            y1 < y2 + h2 and
            y1 + h1 > y2)


def draw_snake(snake_pos):
    for pos in snake_pos:
        pygame.draw.circle(screen, red, pos, snake_radius)


def move(snake_pos, direction):
    head_x, head_y = snake_pos[0]
    if direction == 'UP':
        new_head = [head_x, head_y - block_size]
    elif direction == 'DOWN':
        new_head = [head_x, head_y + block_size]
    elif direction == 'LEFT':
        new_head = [head_x - block_size, head_y]
    elif direction == 'RIGHT':
        new_head = [head_x + block_size, head_y]

    snake_pos = [new_head] + snake_pos[:-1]
    return snake_pos




#snake overlay and maet the tail
def sel_collision(snake_pos):
    head = snake_pos[0]
    return head in snake_pos[1:]

#score
score_value = 0
font = pygame.font.Font("freesansbold.ttf",32)

textX = 10
textY = 10

def show_score(x,y):
    score = font.render("score :" + str(score_value),True,( 10,255, 0))
    screen.blit(score,(x,y))

#Game Over
Over_font = pygame.font.Font("freesansbold.ttf",64)
overX = 200
overy = 250

def Game_Over(x,y):
    over_text = Over_font.render("GAME OVER", True, (160, 32, 240))
    screen.blit(over_text, (x,y))

# snake eat the food sound
food_wav = mixer.Sound("eat_wav.mp3")

# Game Over sound
game_over_sound =  mixer.Sound("game_oversound1.wav")

running = True
clock = pygame.time.Clock()

while running:
    screen.fill((0,0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != 'DOWN':
                direction = 'UP'
            elif event.key == pygame.K_DOWN and direction != 'UP':
                direction = 'DOWN'
            elif event.key == pygame.K_LEFT and direction != 'RIGHT':
                direction = 'LEFT'
            elif event.key == pygame.K_RIGHT and direction != 'LEFT':
                direction = 'RIGHT'


    snake_pos = move(snake_pos, direction)

    # Check boundaries
    if sel_collision(snake_pos):
        running = False
        Game_Over(overX, overy)
        game_over_sound.play()
        pygame.display.update()
        pygame.time.wait(1000)
        # pygame.quit()
        # sys.exit()

    # Check for collision with food
    if is_collision(snake_pos[0][0], snake_pos[0][1], foodX, foodY, block_size, block_size, food_width, food_height):
        foodX, foodY = random_position(width, height, block_size, border_width)
        snake_pos.append(snake_pos[-1][:])
        score_value +=1
        food_wav.play()

    draw_snake(snake_pos)
    food(foodX, foodY)


    show_score(textX,textY)

    pygame.display.update()
    clock.tick(6)
