import pygame, sys


WIDTH, HEIGHT = 800, 800
class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((HEIGHT, WIDTH))

    def update(self):
        pygame.display.update()
        self.screen.fill((255,255,255))

    def run(self):
        while True:
            self.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit
                    sys.exit()

if __name__ == "__main__":
    app = Game()
    app.run()