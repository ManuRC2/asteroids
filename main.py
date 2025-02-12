import pygame
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *
from player import Player
from shot import Shot

def main():
    # initialization
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = updatable
    Shot.containers = (updatable, drawable, shots)

    player = Player(x=SCREEN_WIDTH / 2,
                    y=SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    

    while True:
        # quit event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # updating
        updatable.update(dt)

        for a in asteroids:
            if a.checkColission(player):
                print("Game over!")
                return

        # rendering
        screen.fill(color="black")
        for d in drawable:
            d.draw(screen)
        pygame.display.flip()

        # fps
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
