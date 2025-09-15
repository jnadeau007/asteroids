# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
import sys
from shot import Shot

updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
asteroids = pygame.sprite.Group()
shots = pygame.sprite.Group()
Player.containers = (updatable, drawable)
Asteroid.containers = (updatable, drawable, asteroids)
Shot.containers = (updatable, drawable, shots)
AsteroidField.containers = (updatable)

def main():
    pygame.init()
    time_clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y, PLAYER_RADIUS)
    asteroid_field = AsteroidField()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 
            
        screen.fill('black')
        for ele in drawable:
            ele.draw(screen)
        updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.detect_collisions(player):
                print('Game over!')
                sys.exit()
        pygame.display.flip()
        dt = time_clock.tick(60) / 1000




if __name__ == "__main__":
    main()
