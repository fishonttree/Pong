import pygame
import sys


class PingPong:
    def __init__(self):
        pygame.init()

        self.width = 1000
        self.height = 600

        pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Ping Pong')

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            pygame.display.flip()


if __name__ == '__main__':
    my_game = PingPong()
    my_game.run_game()