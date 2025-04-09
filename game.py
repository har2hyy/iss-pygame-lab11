import pygame
import random

pygame.init()

WIDTH = 1300
HEIGHT = 800

screen = pygame.display.set_mode((WIDTH, HEIGHT))

running = True

phineas_image = pygame.image.load("assets/images/phineas_flipped.png")
isabella_image = pygame.image.load("assets/images/isabella.png")
background_image = pygame.image.load("assets/images/background.jpg")  # Load the background image

phineas_x = 0
phineas_y = 0
isabella_x = 1100
isabella_y = 0


phineas_vx = isabella_vx = 20
phineas_vy = isabella_vy = 0

gravity = 7000

p_width = phineas_image.get_width()
p_height = phineas_image.get_height()
i_height = isabella_image.get_height()
i_width = isabella_image.get_width()

clock = pygame.time.Clock()

rects = []

phineas_score = 0
isabella_score = 0
pink_rects = []

font = pygame.font.SysFont(None, 36)

phineas_can_jump = True  # Track if Phineas can jump
isabella_can_jump = True  # Track if Isabella can jump

while running:

    dt = clock.tick(60) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    # Phineas jump logic
    if keys[pygame.K_UP]:
        if phineas_can_jump:
            phineas_vy = -2100
            phineas_can_jump = False
    else:
        phineas_can_jump = True

    # Isabella jump logic
    if keys[pygame.K_w]:
        if isabella_can_jump:
            isabella_vy = -2100
            isabella_can_jump = False
    else:
        isabella_can_jump = True

    if keys[pygame.K_RIGHT]:
        phineas_x += phineas_vx
    if keys[pygame.K_LEFT]:
        phineas_x -= phineas_vx

    if keys[pygame.K_d]:
        isabella_x += isabella_vx
    if keys[pygame.K_a]:
        isabella_x -= isabella_vx

    screen.blit(background_image, (0, 0))  # Draw the background image

    if random.randint(0, 2000) > 1800:
        rects.append(pygame.rect.Rect(WIDTH, random.randint(0, HEIGHT), 10, 100))
    
    if random.randint(0, 2000) > 1900:
        pink_rects.append(pygame.rect.Rect(WIDTH, random.randint(0, HEIGHT), 10, 100))
    
    for rect in rects[:]:
        pygame.draw.rect(screen, (0, 255, 0), rect)

    phineas_rect = pygame.rect.Rect(phineas_x, phineas_y, p_width, p_height)

    for rect in rects:
        if phineas_rect.colliderect(rect):
            rects.remove(rect)
            phineas_score += 1
            
        rect.x -= 10

    isabella_rect = pygame.rect.Rect(isabella_x, isabella_y, i_width, i_height)
    for pink_rect in pink_rects[:]:
        pygame.draw.rect(screen, (255, 192, 203), pink_rect)
        if isabella_rect.colliderect(pink_rect):
            pink_rects.remove(pink_rect)
            isabella_score += 1
        pink_rect.x -= 10

    screen.blit(phineas_image, (phineas_x, phineas_y))
    screen.blit(isabella_image, (isabella_x, isabella_y))

    phineas_vy += gravity * dt
    isabella_vy += gravity * dt

    phineas_y += phineas_vy * dt
    isabella_y += isabella_vy * dt

    # Ensure Phineas stays within bounds
    if phineas_y > HEIGHT - p_height:
        phineas_y = HEIGHT - p_height
        phineas_vy = 0
    if phineas_y < 0:
        phineas_y = 0
        phineas_vy = 0
    if phineas_x > WIDTH - p_width:
        phineas_x = WIDTH - p_width
    if phineas_x < 0:
        phineas_x = 0

    # Ensure Isabella stays within bounds
    if isabella_y > HEIGHT - i_height:
        isabella_y = HEIGHT - i_height
        isabella_vy = 0
    if isabella_y < 0:
        isabella_y = 0
        isabella_vy = 0
    if isabella_x > WIDTH - i_width:
        isabella_x = WIDTH - i_width
    if isabella_x < 0:
        isabella_x = 0

    score_text_phineas = font.render(f"Phineas Score: {phineas_score}", True, (255, 255, 255))
    score_text_isabella = font.render(f"Isabella Score: {isabella_score}", True, (255, 255, 255))
    screen.blit(score_text_phineas, (10, 10))
    screen.blit(score_text_isabella, (10, 50))

    pygame.display.flip()

print(f"Phineas score: {phineas_score}")
print(f"Isabella score: {isabella_score}")

pygame.quit()