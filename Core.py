import pygame
import sys
from Levels.Test_Level import Test_Level

sys.path.append("/")

pygame.init()
class Core:
    def __init__(self):
        self.w_width = 1280
        self.w_height = 720
        self.window = pygame.display.set_mode((self.w_width,self.w_height))
        pygame.display.set_caption("ilkoyunum")

        self.Current_Level = Test_Level(self.w_width,self.w_height)


        self.clock = pygame.time.Clock()


    def draw(self):

        self.Current_Level.Draw(self.window)
        self.clock.tick(80)
        pygame.display.update()


    def game_loop(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "QUIT"
        self.key = pygame.key.get_pressed()
        if self.key[pygame.K_ESCAPE]:
            return "ESC"
        self.Mouse = pygame.mouse.get_pressed()
        

        self.Current_Level.GameLoop(self.key,self.Mouse)
        self.draw()


game = Core()

while True:
    game_status = game.game_loop()
    if game_status is not None:
        break

pygame.quit()
