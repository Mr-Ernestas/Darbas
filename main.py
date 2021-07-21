import pygame
import random
import math
from pygame import mixer

# Intialize the pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((800, 600))

# Background
background = pygame.image.load("Background.jpg")

# Background Music
mixer.music.load("Music.wav")
mixer.music.play(-1)

# Title and Icon
pygame.display.set_caption("Knowledge Fight")
icon = pygame.image.load("Teacher.png")
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load("Teacher.png")
playerX = 370
playerY = 536
playerX_change = 0

# Enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enmeyY_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load("Student.png"))
    enemyX.append(random.randint(0, 735))
    enemyY.append(random.randint(0, 150))
    enemyX_change.append(0.5)
    enmeyY_change.append(40)

# Book
bookImg = pygame.image.load("Book.png")
bookX = 0
bookY = 536
bookX_change = 0
bookY_change = 0.5
book_state = "ready"

# Score
score_value = 0
font = pygame.font.Font("freesansbold.ttf", 32)

textX = 10
testY = 10

# Game Over Text
over_font = pygame.font.Font("freesansbold.ttf", 64)


def show_score(x, y):
    score = font.render("Score :" + str(score_value), True, (255, 0, 0))
    screen.blit(score, (x, y))


def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 0, 0))
    screen.blit(over_text, (200, 250))


def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))


def fire(x, y):
    global book_state
    book_state = "fire"
    screen.blit(bookImg, (x + 16, y + 10))


def isCollision(enemyX, enemyY, bookX, bookY):
    distance = math.sqrt((math.pow(enemyX - bookX, 2)) + (math.pow(enemyY - bookY, 2)))
    if distance < 27:
        return True
    else:
        return False


# Game Loop
running = True
while running:

    # Colors = Red, Green, Blue
    screen.fill((0, 0, 0))

    # Bacground image
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Keystroke
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.5
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.5
            if event.key == pygame.K_SPACE:
                if book_state is "ready":
                    book_sound = mixer.Sound("Shot.wav")
                    book_sound.play()
                    bookX = playerX
                    fire(bookX, bookY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
    # Cheking for boundaries of player so it doesn't go out of bounds
    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    # Enemy Movement
    for i in range(num_of_enemies):

        # Game Over
        if enemyY[i] > 450:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            game_over_text()
            break

        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 0.2
            enemyY[i] += enmeyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -0.2
            enemyY[i] += enmeyY_change[i]

        # Collision
        collision = isCollision(enemyX[i], enemyY[i], bookX, bookY)
        if collision:
            hit_sound = mixer.Sound("Hit.wav")
            hit_sound.play()
            bookY = 536
            book_state = "ready"
            score_value += 10
            enemyX[i] = random.randint(0, 735)
            enemyY[i] = random.randint(50, 150)

        enemy(enemyX[i], enemyY[i], i)

    # Book Movement
    if bookY <= 0:
        bookY = 536
        book_state = "ready"

    if book_state is "fire":
        fire(bookX, bookY)
        bookY -= bookY_change

    player(playerX, playerY)
    show_score(textX, testY)
    pygame.display.update()
