import pygame

# basic window settings
pygame.init()
W_WIDTH, W_HEIGHT = 1280, 720
screen = pygame.display.set_mode((W_WIDTH, W_HEIGHT))
pygame.display.set_caption("Space Shooter")

is_running = True

# sprites and shapes
square = pygame.Surface((100, 100))
player_model = pygame.image.load("images/player.png")


# main loop
while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
    screen.fill("grey")
    screen.blit(square, (0, 0))
    screen.blit(player_model, (100, 100))
    pygame.display.update()


pygame.quit()
