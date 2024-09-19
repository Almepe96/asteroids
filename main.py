import pygame
from constants import *

def main():
    pygame.init
    pygame.time.Clock
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    while True:
        for event in pygame.event.get():
             if event.type == pygame.QUIT:
                  return
             
        screen.fill("black")
        pygame.display.flip()
    pygame.time.Clock.tick(60)
    dt = pygame.time.Clock.tick()/1000

if __name__ == "__main__":
    main()
