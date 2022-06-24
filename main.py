import pygame
import random

pygame.init()

SIZE = (480, 640)
LIVES = 3

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
GRAY = (140,140,140)
GREEN = (0, 255, 0)

FPS = 60

PLAYER_X = 240 - 30
PLAYER_Y = 200

ENEMY_X = 180
ENEMY_Y = 500

LIFE_X = 180
LIFE_Y = 5000

LIFE_CENTER = (LIFE_X, LIFE_Y)
LIFE_RADIUS = 15

ENEMY_CENTER = (ENEMY_X,ENEMY_Y)
ENEMY_RADIUS = 15

LIFE_PICKUP_SOUND = pygame.mixer.Sound("sounds/pickupLife.wav")
ENEMY_HIT_SOUND = pygame.mixer.Sound("sounds/hitHurt.wav")

COINS = 0

WIN = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Dasher")
        

running = True

clock = pygame.time.Clock()

while running:

    WIN.fill(GRAY)
    player = pygame.draw.rect(WIN, WHITE, pygame.Rect(PLAYER_X, PLAYER_Y, 60, 60))
    enemy = pygame.draw.circle(WIN, RED, ENEMY_CENTER, ENEMY_RADIUS)
    extra_life = pygame.draw.circle(WIN, GREEN, LIFE_CENTER, LIFE_RADIUS)

    font = pygame.font.Font('freesansbold.ttf', 32)
    text_surface = font.render(('LIVES: ' + str(LIVES)), False, BLACK)
    game_over_text = font.render("Game Over!", False, WHITE)
    WIN.blit(text_surface, (0,0))

    enemy_collide = player.colliderect(enemy)
    life_collide = player.colliderect(extra_life)

    if enemy_collide == True:
        ENEMY_Y = 650
        ENEMY_X = random.randint(10, 470)
        ENEMY_HIT_SOUND.play()
        LIVES -= 1
        enemy_collide = False
        print(str(LIVES))

    if life_collide == True:
        LIFE_Y = 5000
        LIFE_X = random.randint(10, 470)
        LIFE_PICKUP_SOUND.play()
        LIVES += 1
        life_collide = False
        print(str(LIVES))

    if LIVES <= 0:
        WIN.fill(BLACK)
        WIN.blit(game_over_text, (155, 300))
        PLAYER_Y = 6000

    ENEMY_Y -= 10
    LIFE_Y -= 10
    ENEMY_CENTER = (ENEMY_X,ENEMY_Y)
    LIFE_CENTER = (LIFE_X, LIFE_Y)

    if ENEMY_Y < 0:
        ENEMY_Y = 650
        ENEMY_X = random.randint(10, 470)

    if LIFE_Y < 0:
        LIFE_Y = 5000
        LIFE_X = random.randint(10, 470)

    for event in pygame.event.get():      
        
        if event.type == pygame.QUIT:

            running = False
    
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        while PLAYER_X > 0:
            PLAYER_X -= 10
            break
    if keys[pygame.K_RIGHT]:
        while PLAYER_X < 420:
            PLAYER_X += 10
            break

    clock.tick(FPS)

    pygame.display.flip()

pygame.quit()
