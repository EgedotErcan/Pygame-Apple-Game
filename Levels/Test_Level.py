import  pygame
from Character.Character import Character
from Levels.materials import *



class Test_Level:
    def __init__(self,w_width,w_height):
        self.bg = pygame.image.load("Levels/Levels_Data/Test_Level_Night/test_level_night.png").convert()
        self.bg = pygame.transform.scale(self.bg, (w_width, w_height))

        self.Character = Character()
        self.food_list = []
        self.food_list.append(get_food(600,585))
        self.food_list.append(get_food(700,585))
        self.food_list.append(get_food(800,585))
        self.food_list.append(get_food(900,585))
        self.food_list.append(get_food(1000,585))
    def Draw(self,window):
        window.blit(self.bg, (0, 0))
        for food in self.food_list:
            window.blit(food[0],(food[1],food[2]))
            #pygame.draw.rect(window,(0,0,220),(food[1]+20,food[2]+23,16,17),3)

        self.Character.Draw(window)


    def GameLoop(self,key,mouse):
        self.Character.GameLoop(key,mouse)
        print(self.Character.C_Food)

        for food in self.food_list:
            if (self.Character.get_rect().colliderect(food[3])):
                self.Character.C_Food += 5
                self.food_list.remove(food)
                
                
