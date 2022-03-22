import pygame




class Enemy:
    def __init__(self):
        self.E_x = 400
        self.E_y = 500

        self.E_Scale = (200,148)

        self.E_Status = ""
        self.E_Time = pygame.time.get_ticks()

        self.E_Direction = False
        self.E_Speed = 3
        self.E_Action_Mode = False
        self.E_Path = ""

        ###### İDLE ######

    



    def Draw(self):
        pass

    

    def GameLoop(self):
        pass