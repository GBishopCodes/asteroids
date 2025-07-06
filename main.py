import sys
import pygame
from constants import *
from player import *
from asteroidfield import *
from asteroid import Asteroid
from circleshape import CircleShape

def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (drawable, updatable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (drawable, updatable)

    AsteroidField()

    main_player = Player(SCREEN_WIDTH / 2 , SCREEN_HEIGHT / 2, shots)
    time_keeper = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))
        for guy in drawable:
            guy.draw(screen)
        updatable.update(dt)
        for asteroid in asteroids:
            if main_player.collision_check(asteroid):
                print("Game over!")
                sys.exit()
        for asteroid in asteroids:
            for shot in shots:
                if shot.collision_check(asteroid):
                    asteroid.split()
                    shot.kill()
        pygame.display.flip()
        dt = time_keeper.tick(60) / 1000

if __name__ == "__main__":
    main()
