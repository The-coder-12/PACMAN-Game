import pygame
import sys
import random

pygame.init()

#Screen dimensions
w = 800
h = 500
#Creating the screen
dis = pygame.display.set_mode((w, h))
pygame.display.set_caption("PACMAN")
#Uploading the images
#Pacman image
pacman = pygame.image.load("PACMAN-removebg-preview.png")
pacman1 = pygame.transform.scale(pacman, (80, 60))
#Ghost images
#Red ghost
redghost = pygame.image.load("ghost-removebg-preview.png")
redghost1 = pygame.transform.scale(redghost, (50, 50))
#Orange ghost

#Cyan ghost

#Pink ghost

#Pellets
#Normal pellet
pellet0 = pygame.image.load("pellet-removebg-preview.png")
pellet1 = pygame.transform.scale(pellet0, (25, 25))
#Power pellet

#Game variables
pacmanspeed = 10
score = 0
pacman_rect = pacman1.get_rect(center= (w / 2, h / 2))
# pellets = [pygame.Rect(random.randint(0, w - 50), random.randint(0, h - 50), 25, 25) for i in range(20)]
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)
#Adding multiple ghosts
ghosts = []
ghost_no = 4
ghostspeeds = [1, 2, 3, 4]

#Function to generate pellets
def generate_pellets():
    return[pygame.Rect(random.randint(0, w - 50), random.randint(0, h - 50), 25, 25) for i in range(20)]

pellets = generate_pellets()
for i in range(ghost_no):
    redghost_rect = redghost1.get_rect(center=(random.randint(0, w), random.randint(0, h)))
    ghosts.append(redghost_rect)

#Rendering the font
def font_render(text, font, color, x, y):
    textsurface = font.render(text, True, color)
    text_rect = textsurface.get_rect(center= (x, y))
    dis.blit(textsurface, text_rect)

#Main variable and game loop
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    #Moving the pacman
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        pacman_rect.y -= pacmanspeed
    if keys[pygame.K_DOWN]:
        pacman_rect.y += pacmanspeed
    if keys[pygame.K_LEFT]:
        pacman_rect.x -= pacmanspeed
    if keys[pygame.K_RIGHT]:
        pacman_rect.x += pacmanspeed

    #Moving the ghosts
    for i, redghost_rect in enumerate(ghosts):
        ghostspeed = ghostspeeds[i]
        if redghost_rect.x < pacman_rect.x:
            redghost_rect.x += ghostspeed
        elif redghost_rect.x > pacman_rect.x:
            redghost_rect.x -= ghostspeed
        if redghost_rect.y < pacman_rect.y:
            redghost_rect.y += ghostspeed
        elif redghost_rect.y > pacman_rect.y:
            redghost_rect.y -= ghostspeed

    #Collision detection
    #Chapter 1: Collision with the pellet
    for pellet in pellets:
        if pacman_rect.colliderect(pellet):
            pellets.remove(pellet)
            score += 10

    if not pellets:
        pellets = generate_pellets()

    #Chapter 2: Collision with the ghost
    if pacman_rect.colliderect(redghost_rect):
        run = False
        print("Ghosts win!")

    #Chapter 3: Set the borders
    if pacman_rect.left < 0:
        pacman_rect.left = 0
    if pacman_rect.right > w:
        pacman_rect.right = w
    if pacman_rect.top < 0:
        pacman_rect.top = 0
    if pacman_rect.bottom > h:
        pacman_rect.bottom = h

    dis.fill((0, 0, 0))
    dis.blit(pacman1, pacman_rect)
    for ghost in ghosts:
        dis.blit(redghost1, ghost)
    for pellet in pellets:
        dis.blit(pellet1, pellet)
    font_render(f"Score: " + str(score), font, (255, 255, 255), 200, 100)
    pygame.display.update()
    clock.tick(30)