import pygame
import sys

# Set the width and the height of the window
(width, height) = (300, 300)
# Sprite width
char_width = 20
# set the screen fro pygame to the width and height tuple defined above
# set the name of the pygame project at the top of the window
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Sky Balloons')
# game time
clock = pygame.time.Clock()
# Load my char image
character = pygame.image.load(r'/Users/txt-17/PycharmProjects/PyGame/sky_balloons/sprites/balloon.png')
# Load the enemy players
obstacle = pygame.image.load(r'/Users/txt-17/PycharmProjects/PyGame/sky_balloons/sprites/spike_flyer.png')
background = pygame.image.load(r'/Users/txt-17/PycharmProjects/PyGame/sky_balloons/sprites/sky.png')


# This function will display my image
def my_char(x, y):
    screen.blit(character, (x, y))


# this function creates enemies
def create_enemies(x, y):
    screen.blit(obstacle, (x, y))


# Game Loop
def game_loop():
    # Set image position
    img_x = 20
    img_y = 30
    enemy_x = 100
    enemy_y = 88
    # Movement
    char_pos_x = 0
    char_pos_y = 0
    # Boolean to see if game is running
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        # Movement - this changes the position of the
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                char_pos_x = -4
            elif event.key == pygame.K_RIGHT:
                char_pos_x = 4
            elif event.key == pygame.K_UP:
                char_pos_y = -4
            elif event.key == pygame.K_DOWN:
                char_pos_y = 4

        # Checks if the keys have been released
        # if this logic is not added then we cannot
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                char_pos_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                char_pos_y = 0

        img_x += char_pos_x
        img_y += char_pos_y

        # Add sprites
        screen.blit(background, [0, 0])
        my_char(img_x, img_y)
        create_enemies(enemy_x, enemy_y)

        # bounding to the window
        if img_x > width - char_width:
            print('right bounce')
            img_x -= 5
        if img_y > width - char_width:
            print('bottom bounce')
            img_y -= 5
        if img_x < 0:
            print('left bounce')
            img_x = 0
        if img_y < 0:
            print('top bounce')
            img_y = 0

        # flip will allow us to display the graphics and allow us to see the change
        
        pygame.display.flip()
        clock.tick(60)


game_loop()
pygame.quit()

