import pygame
from constants import *
from player import *

def main():
    pygame.init
    pygame.time.Clock
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    #Initial arguments
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2   
    dt = 0
    clock = pygame.time.Clock()

    #Initial message
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    #Create Player

    player = Player(x, y)

    #Drawing loop
    while True:
        for event in pygame.event.get():
             if event.type == pygame.QUIT:
                  return
             
        #Screen drawer  
        screen.fill("black")

        #Player drawer
        player.draw(screen)
        #Dibujar
        pygame.display.flip()
        #Fps limiter
        dt = clock.tick(60)/1000







#Start function
if __name__ == "__main__":
    main()
