"""
    This day's project is a space game, like Space Invaders.
    It uses pygame and classes.
    Keybindings:
        A / Left Arrow:   move left
        D / Right Arrow:  move right
        Space:            shoot
"""
import random
import math
import pygame as pg
from pygame import mixer


class Ship:
    """ Parent class and used by Player """
    speed = 0.2

    def __init__(self, image: str):
        self.image = pg.image.load(image)
        self.pos_x = 0
        self.pos_y = 0
        self.pos_x_changed = 0

    def set_spawn(self):
        """ Sets the spawn point for the player at middle bottom """
        self.pos_x = screen.get_width() / 2 - self.image.get_width() / 2
        self.pos_y = screen.get_height() - self.image.get_height() - SCREEN_BOUNDS


class Enemy(Ship):
    """ Class that inherits from Ship. It's used by Enemies """
    speed = 0.4
    pos_y_changed = 70

    def set_spawn(self):
        """ Sets a random spawn point for the enemy """
        self.pos_x = random.randint(
            0, screen.get_width() - self.image.get_width()
        )
        self.pos_y = random.randint(50, 100)


class Bullet(Ship):
    """ Class that inherits from Ship. It's used by Bullets """
    pos_y_changed = -0.2

    def set_spawn(self):
        """ Sets the bullet spawn point in front of the player ship """
        self.pos_x = player.pos_x + player.image.get_width() / 4
        self.pos_y = player.pos_y


# Pygame initialization
pg.init()

# Screen and icon setup
screen = pg.display.set_mode((600, 800))
background_image = pg.image.load("assets/background.jpg")
icon = pg.image.load("assets/ufo.png")
SCREEN_BOUNDS = 50

# Set title and icon
pg.display.set_caption("Space shooter")
pg.display.set_icon(icon)

# Set music and sounds
mixer.music.load("assets/background.mp3")
mixer.music.play(-1)
bullet_sound = mixer.Sound("assets/bullet.mp3")
hit_sound = mixer.Sound("assets/hit.mp3")

# Set score and font
SCORE = 0
font = pg.font.Font("freesansbold.ttf", 32)
score_pos = (10, 10)

# Set end game font
font_end_game = pg.font.Font("freesansbold.ttf", 40)
font_end_game.set_bold(True)
end_game_text_pos = (screen.get_width()/4, screen.get_height()/4)

# Player setup
player = Ship("assets/space-ship.png")
player.set_spawn()
bullet = Bullet("assets/bullet.png")

# Enemies setup
TOTAL_ENEMIES = 8
enemies = []
for i in range(TOTAL_ENEMIES):
    enemies.append(Enemy("assets/enemy.png"))
    enemies[i].set_spawn()
    enemies[i].pos_x_changed = enemies[i].speed


def check_hit(obj_1: tuple, obj_2: tuple):
    """ Checks if the distance of two objects are under 50 pixels
    :param obj_1: tuple with the position of first object
    :param obj_2: tuple with the position of second object
    :return: True if distance under 50 pixels, False if not
    """
    operations = (
        math.pow(obj_1[1] - obj_1[0], 2), math.pow(obj_2[1] - obj_2[0], 2)
    )
    distance = math.sqrt(operations[0] + operations[1])
    return distance < 50


def show_score():
    """ Creates the score text and prints it in the screen """
    score_text = font.render(f"Total score: {SCORE}", True, (255, 255, 255))
    screen.blit(score_text, score_pos)


def player_killed():
    """ Stops the music, creates the end game text and prints it if the player is killed """
    globals()["END"] = True
    mixer.music.stop()
    end_game_text = font_end_game.render("GAME OVER", True, (255, 255, 255))
    screen.blit(end_game_text, end_game_text_pos)


# Game loop
IS_EXECUTING = True
while IS_EXECUTING:
    # Print background
    screen.blit(background_image, (0, 0))
    # Event checker
    for event in pg.event.get():
        match event.type:
            # Close window
            case pg.QUIT:
                IS_EXECUTING = False
            # Key is pressed
            case pg.KEYDOWN:
                match event.key:
                    case pg.K_LEFT | pg.K_a:
                        player.pos_x_changed = -player.speed
                    case pg.K_RIGHT | pg.K_d:
                        player.pos_x_changed = player.speed
                    case pg.K_SPACE:
                        if bullet is None:
                            bullet = Bullet("assets/bullet.png")
                            bullet.set_spawn()
                            bullet_sound.play()
            # Key is released
            case pg.KEYUP:
                if event.key in (pg.K_LEFT, pg.K_RIGHT, pg.K_a, pg.K_d):
                    player.pos_x_changed = 0

    # Player movement and bounds
    player.pos_x += player.pos_x_changed
    player.pos_x = max(player.pos_x, SCREEN_BOUNDS)
    player.pos_x = min(player.pos_x, screen.get_width() - player.image.get_width() - SCREEN_BOUNDS)

    # Enemy movement and bounds
    for enemy in enemies:
        # Check end game
        player_hit = check_hit((player.pos_x, enemy.pos_x), (player.pos_y, enemy.pos_y))
        if player_hit:
            for new_enemy in enemies:
                new_enemy.pos_y = 2000
            player_killed()
            IS_EXECUTING = False
            break
        enemy.pos_x += enemy.pos_x_changed
        if enemy.pos_x <= 0:
            enemy.pos_x_changed = enemy.speed
            enemy.pos_y += enemy.pos_y_changed
        elif enemy.pos_x >= screen.get_width() - enemy.image.get_width():
            enemy.pos_x_changed = -enemy.speed
            enemy.pos_y += enemy.pos_y_changed
        if bullet is not None:
            # Check hit
            hit = check_hit((bullet.pos_x, enemy.pos_x), (bullet.pos_y, enemy.pos_y))
            if hit:
                hit_sound.play()
                bullet = None
                SCORE += 1
                enemy.set_spawn()
                continue
            # Bullet movement and print
            if bullet.pos_y < 0:
                bullet = None
            else:
                bullet.pos_y += bullet.pos_y_changed
                screen.blit(bullet.image, (bullet.pos_x, bullet.pos_y))
        screen.blit(enemy.image, (enemy.pos_x, enemy.pos_y))

    # Print
    screen.blit(player.image, (player.pos_x, player.pos_y))
    show_score()

    # Update display
    pg.display.update()
