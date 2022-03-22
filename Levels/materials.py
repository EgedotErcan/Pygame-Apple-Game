import pygame

def get_food(x,y):
    food = pygame.image.load("Levels/materials/apple.png")
    food = pygame.transform.scale(food,(50,50))
    return [food,x,y,pygame.Rect(x+20,y+23,16,17)]