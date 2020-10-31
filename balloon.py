import pygame

# Set the width and the height of the window
(width, height) = (300, 300)
# movement in pixels
vel = 5
# set the screen fro pygame to the width and height tuple defined above
# set the name of the pygame project at the top of the window
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Sky Balloons')
# game time
clock = pygame.time.Clock()
# Load my char image
character = pygame.image.load(r'/Users/txt-17/PycharmProjects/PyGame/sky_balloons/sprites/balloon.png')
# get the rectangle of character
player_rect = character.get_rect()
# Load the enemy players
obstacle = pygame.image.load(r'/Users/txt-17/PycharmProjects/PyGame/sky_balloons/sprites/spike_flyer.png')
obs_rect = obstacle.get_rect()
obs_rect.x = 100
obs_rect.y = 270

# Background image
background = pygame.image.load(r'/Users/txt-17/PycharmProjects/PyGame/sky_balloons/sprites/sky.png')

block = pygame.Rect(200, 100, 80, 80)


# Game Loop
def game_loop():
    # Boolean to see if game is running
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        # Movement - this changes the position of the
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_rect.x -= vel
            elif event.key == pygame.K_RIGHT:
                player_rect.x += vel
            elif event.key == pygame.K_UP:
                player_rect.y -= vel
            elif event.key == pygame.K_DOWN:
                player_rect.y += vel

        # Add sprites
        screen.blit(background, [0, 0])
        screen.blit(character, (player_rect.x, player_rect.y))
        screen.blit(obstacle, (obs_rect.x, obs_rect.y))

        # call collide method here
        # checking for collision with obstacle in this case game over
        # to make it visible i will show the red box around our balloon
        if player_rect.colliderect(obs_rect):
            print('hit- game over')
            pygame.draw.rect(screen, (255, 0, 0), player_rect, 4)
            running = False

        # flip will allow us to display the graphics and allow us to see the change
        pygame.display.flip()
        clock.tick(60)


game_loop()
pygame.quit()

