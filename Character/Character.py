import pygame
import json 

class Character:
    def __init__(self):
        self.C_X = 300
        self.C_Y = 500
        self.C_Load_Files()

        self.C_Gold = self.C_Dictionary["Gold"]
        self.C_Food = self.C_Dictionary["Food"]
        self.C_Scale = (200,148)
        self.C_Status = "idle"
        self.C_Time = pygame.time.get_ticks()

        self.C_path = "Character/Character_Data/sprite/"

        self.C_Direction = False
        self.C_Action_Mode = False
        self.C_İs_Jump = False
        self.C_Jump_Velocity = 10
        self.C_Speed = 8

        self.C_Animation = False 
        
        ###### STATUS idle #######
        self.C_idle_1 = pygame.image.load(self.C_path+"adventurer-idle-00.png").convert_alpha()
        self.C_idle_2 = pygame.image.load(self.C_path+"adventurer-idle-01.png").convert_alpha()
        self.C_idle_3 = pygame.image.load(self.C_path+"adventurer-idle-02.png").convert_alpha()
        self.C_idle_4 = pygame.image.load(self.C_path+"adventurer-idle-03.png").convert_alpha()
        self.C_idle_Animation = 0
        self.C_idle_1 = pygame.transform.scale(self.C_idle_1,self.C_Scale)
        self.C_idle_2 = pygame.transform.scale(self.C_idle_2,self.C_Scale)
        self.C_idle_3 = pygame.transform.scale(self.C_idle_3,self.C_Scale)
        self.C_idle_4 = pygame.transform.scale(self.C_idle_4, self.C_Scale)
        self.C_idle_delay = 205
        self.C_idle_list = [
            self.C_idle_1,
            self.C_idle_2,
            self.C_idle_3,
            self.C_idle_4
        ]

        ###### STATUS idle_sword #######
        self.C_idle_sword_1 = pygame.image.load(self.C_path+"adventurer-idle-2-00.png").convert_alpha()
        self.C_idle_sword_2 = pygame.image.load(self.C_path+"adventurer-idle-2-01.png").convert_alpha()
        self.C_idle_sword_3 = pygame.image.load(self.C_path+"adventurer-idle-2-02.png").convert_alpha()
        self.C_idle_sword_4 = pygame.image.load(self.C_path+"adventurer-idle-2-03.png").convert_alpha()
        self.C_idle_sword_Animation = 0
        self.C_idle_sword_1 = pygame.transform.scale(self.C_idle_sword_1, self.C_Scale)
        self.C_idle_sword_2 = pygame.transform.scale(self.C_idle_sword_2, self.C_Scale)
        self.C_idle_sword_3 = pygame.transform.scale(self.C_idle_sword_3, self.C_Scale)
        self.C_idle_sword_4 = pygame.transform.scale(self.C_idle_sword_4, self.C_Scale)
        self.C_idle_sword_delay = 205
        self.C_idle_sword_list = [
            self.C_idle_sword_1,
            self.C_idle_sword_2,
            self.C_idle_sword_3,
            self.C_idle_sword_4
        ]

        ###### STATUS run #######
        self.C_run_1 = pygame.image.load(self.C_path+"adventurer-run-00.png").convert_alpha()
        self.C_run_2 = pygame.image.load(self.C_path+"adventurer-run-01.png").convert_alpha()
        self.C_run_3 = pygame.image.load(self.C_path+"adventurer-run-02.png").convert_alpha()
        self.C_run_4 = pygame.image.load(self.C_path+"adventurer-run-03.png").convert_alpha()
        self.C_run_5 = pygame.image.load(self.C_path+"adventurer-run-04.png").convert_alpha()
        self.C_run_6 = pygame.image.load(self.C_path+"adventurer-run-05.png").convert_alpha()
        self.C_run_Animation = 0
        self.C_run_1 = pygame.transform.scale(self.C_run_1, self.C_Scale)
        self.C_run_2 = pygame.transform.scale(self.C_run_2, self.C_Scale)
        self.C_run_3 = pygame.transform.scale(self.C_run_3, self.C_Scale)
        self.C_run_4 = pygame.transform.scale(self.C_run_4, self.C_Scale)
        self.C_run_5 = pygame.transform.scale(self.C_run_5, self.C_Scale)
        self.C_run_6 = pygame.transform.scale(self.C_run_6, self.C_Scale)
        self.C_run_delay = 180
        self.C_run_list = [
            self.C_run_1,
            self.C_run_2,
            self.C_run_3,
            self.C_run_4,
            self.C_run_5,
            self.C_run_6
        ]
    
    ####### DRAW SWORD ########
        self.C_draw_sword_1 = pygame.image.load(self.C_path+"adventurer-swrd-drw-00.png").convert_alpha()
        self.C_draw_sword_2 = pygame.image.load(self.C_path+"adventurer-swrd-drw-01.png").convert_alpha()
        self.C_draw_sword_3 = pygame.image.load(self.C_path+"adventurer-swrd-drw-02.png").convert_alpha()
        self.C_draw_sword_4 = pygame.image.load(self.C_path+"adventurer-swrd-drw-03.png").convert_alpha()
        self.C_draw_sword_Animation = 0
        self.C_draw_sword_1 = pygame.transform.scale(self.C_draw_sword_1, self.C_Scale)
        self.C_draw_sword_2 = pygame.transform.scale(self.C_draw_sword_2, self.C_Scale)
        self.C_draw_sword_3 = pygame.transform.scale(self.C_draw_sword_3, self.C_Scale)
        self.C_draw_sword_4 = pygame.transform.scale(self.C_draw_sword_4, self.C_Scale)
        self.C_draw_sword_delay = 60
        self.C_draw_sword_list = [
            self.C_draw_sword_1,
            self.C_draw_sword_2,
            self.C_draw_sword_3,
            self.C_draw_sword_4
        ]
    
    ####### DRAW SWORD-back #########
        self.C_sword_shte_1 = pygame.image.load(self.C_path+"adventurer-swrd-shte-00.png").convert_alpha()
        self.C_sword_shte_2 = pygame.image.load(self.C_path+"adventurer-swrd-shte-01.png").convert_alpha()
        self.C_sword_shte_3 = pygame.image.load(self.C_path+"adventurer-swrd-shte-02.png").convert_alpha()
        self.C_sword_shte_4 = pygame.image.load(self.C_path+"adventurer-swrd-shte-03.png").convert_alpha()
        self.C_sword_shte_Animation = 0
        self.C_sword_shte_1 = pygame.transform.scale(self.C_sword_shte_1, self.C_Scale)
        self.C_sword_shte_2 = pygame.transform.scale(self.C_sword_shte_2, self.C_Scale)
        self.C_sword_shte_3 = pygame.transform.scale(self.C_sword_shte_3, self.C_Scale)
        self.C_sword_shte_4 = pygame.transform.scale(self.C_sword_shte_4, self.C_Scale)
        self.C_sword_shte_delay = 60
        self.C_sword_shte_list = [
            self.C_sword_shte_1,
            self.C_sword_shte_2,
            self.C_sword_shte_3,
            self.C_sword_shte_4
        ]

    ###### ATTACK1 #######
        self.C_attack1_1 = pygame.image.load(self.C_path+"adventurer-attack1-00.png").convert_alpha()
        self.C_attack1_2 = pygame.image.load(self.C_path+"adventurer-attack1-01.png").convert_alpha()
        self.C_attack1_3 = pygame.image.load(self.C_path+"adventurer-attack1-02.png").convert_alpha()
        self.C_attack1_4 = pygame.image.load(self.C_path+"adventurer-attack1-03.png").convert_alpha()
        self.C_attack1_5 = pygame.image.load(self.C_path+"adventurer-attack1-04.png").convert_alpha()
        self.C_attack1_Animation = 0
        self.C_attack1_1 = pygame.transform.scale(self.C_attack1_1, self.C_Scale)
        self.C_attack1_2 = pygame.transform.scale(self.C_attack1_2, self.C_Scale)
        self.C_attack1_3 = pygame.transform.scale(self.C_attack1_3, self.C_Scale)
        self.C_attack1_4 = pygame.transform.scale(self.C_attack1_4, self.C_Scale)
        self.C_attack1_5 = pygame.transform.scale(self.C_attack1_5, self.C_Scale)
        self.C_attack1_delay = 90
        self.C_attack1_list = [
            self.C_attack1_1,
            self.C_attack1_2,
            self.C_attack1_3,
            self.C_attack1_4,
            self.C_attack1_5
        ]

        ######## JUMP #########
        self.C_jump_1 = pygame.image.load(self.C_path+"adventurer-jump-00.png").convert_alpha()
        self.C_jump_2 = pygame.image.load(self.C_path+"adventurer-jump-01.png").convert_alpha()
        self.C_jump_3 = pygame.image.load(self.C_path+"adventurer-jump-02.png").convert_alpha()
        self.C_jump_4 = pygame.image.load(self.C_path+"adventurer-jump-03.png").convert_alpha()
        self.C_jump_5 = pygame.image.load(self.C_path+"adventurer-fall-00.png").convert_alpha()
        self.C_jump_6 = pygame.image.load(self.C_path+"adventurer-fall-01.png").convert_alpha()
        self.C_jump_Animation = 0
        self.C_jump_1 = pygame.transform.scale(self.C_jump_1, self.C_Scale)
        self.C_jump_2 = pygame.transform.scale(self.C_jump_2, self.C_Scale)
        self.C_jump_3 = pygame.transform.scale(self.C_jump_3, self.C_Scale)
        self.C_jump_4 = pygame.transform.scale(self.C_jump_4, self.C_Scale)
        self.C_jump_5 = pygame.transform.scale(self.C_jump_5, self.C_Scale)
        self.C_jump_6 = pygame.transform.scale(self.C_jump_6, self.C_Scale)
        self.C_jump_delay = 130
        self.C_jump_list = [
            self.C_jump_1,
            self.C_jump_2,
            self.C_jump_3,
            self.C_jump_4,
            self.C_jump_5,
            self.C_jump_6
        ]

        ######## ATTACK 3 #######
        self.C_attack3_1 = pygame.image.load(self.C_path+"adventurer-attack3-00.png").convert_alpha()
        self.C_attack3_2 = pygame.image.load(self.C_path+"adventurer-attack3-01.png").convert_alpha()
        self.C_attack3_3 = pygame.image.load(self.C_path+"adventurer-attack3-02.png").convert_alpha()
        self.C_attack3_4 = pygame.image.load(self.C_path+"adventurer-attack3-03.png").convert_alpha()
        self.C_attack3_5 = pygame.image.load(self.C_path+"adventurer-attack3-04.png").convert_alpha()
        self.C_attack3_6 = pygame.image.load(self.C_path+"adventurer-attack3-05.png").convert_alpha()
        self.C_attack3_Animation = 0
        self.C_attack3_1 = pygame.transform.scale(self.C_attack3_1, self.C_Scale)
        self.C_attack3_2 = pygame.transform.scale(self.C_attack3_2, self.C_Scale)
        self.C_attack3_3 = pygame.transform.scale(self.C_attack3_3, self.C_Scale)
        self.C_attack3_4 = pygame.transform.scale(self.C_attack3_4, self.C_Scale)
        self.C_attack3_5 = pygame.transform.scale(self.C_attack3_5, self.C_Scale)
        self.C_attack3_6 = pygame.transform.scale(self.C_attack3_6, self.C_Scale)
        self.C_attack3_delay = 90
        self.C_attack3_list = [
            self.C_attack3_1,
            self.C_attack3_2,
            self.C_attack3_3,
            self.C_attack3_4,
            self.C_attack3_5,
            self.C_attack3_6
        ]

    def Animations(self,delay,animations_number,animations_limit,condition = False,action_mode_end=False,status_mode_end = "idle"):
        if (pygame.time.get_ticks() - self.C_Time) > delay:
                animations_number += 1
                if animations_number == animations_limit:
                    animations_number = 0

                    if condition:
                        self.C_Action_Mode = action_mode_end
                        self.C_Status = status_mode_end
                        self.C_Animation = False


                self.C_Time = pygame.time.get_ticks()
        return animations_number

    def C_Save_Files(self):
        self.C_Dictionary = {
            "Gold": self.C_Gold,
            "Food": self.C_Food
        }
        json.dump(self.C_Dictionary,open("Character/Character_Data.txt","w"))

    def C_Load_Files(self):
        self.C_Dictionary = json.load(open("Character/Character_Data.txt"))



    def Draw(self,window):

        if self.C_Status == "idle":
            window.blit(pygame.transform.flip(self.C_idle_list[self.C_idle_Animation],self.C_Direction,False),(self.C_X,self.C_Y))
        elif self.C_Status == "idle_sword":
            window.blit(pygame.transform.flip(self.C_idle_sword_list[self.C_idle_sword_Animation],self.C_Direction,False),(self.C_X,self.C_Y))
        elif self.C_Status == "run":
            window.blit(pygame.transform.flip(self.C_run_list[self.C_run_Animation],self.C_Direction,False),(self.C_X,self.C_Y))
        elif self.C_Status == "draw_sword":
            window.blit(pygame.transform.flip(self.C_draw_sword_list[self.C_draw_sword_Animation],self.C_Direction,False),(self.C_X,self.C_Y))
        elif self.C_Status == "draw_sword_back":
            window.blit(pygame.transform.flip(self.C_sword_shte_list[self.C_sword_shte_Animation],self.C_Direction,False),(self.C_X,self.C_Y))
        elif self.C_Status == "attack1":
            window.blit(pygame.transform.flip(self.C_attack1_list[self.C_attack1_Animation],self.C_Direction,False),(self.C_X,self.C_Y))
        elif self.C_Status == "attack3":
            window.blit(pygame.transform.flip(self.C_attack3_list[self.C_attack3_Animation],self.C_Direction,False),(self.C_X,self.C_Y))
        elif self.C_Status == "jump":
            window.blit(pygame.transform.flip(self.C_jump_list[self.C_jump_Animation],self.C_Direction,False),(self.C_X,self.C_Y))
            
        #pygame.draw.rect(window,(0,0,255),(self.C_X+65,self.C_Y+25,67,125),3)


    def GameLoop(self,key,mouse):

        self.Key = key
        self.Mouse = mouse
        self.C_Save_Files()

        ######## KEYBOARD CONTROLS #######
        if self.C_Animation == False : 
            if self.Key[pygame.K_d]:
                self.C_Status = "run"
                self.C_Direction = False
                self.C_X += self.C_Speed
                

            elif self.Key[pygame.K_a]:
                self.C_Status = "run"
                self.C_Direction = True
                self.C_X -= self.C_Speed
                

            elif self.Key[pygame.K_r]:
                if self.C_Action_Mode == False:
                    self.C_Status = "draw_sword"
                    self.C_Animation = True
                elif self.C_Action_Mode == True:
                    self.C_Status = "draw_sword_back"
                    self.C_Animation = True

            elif self.Mouse[0] == 1 :
                self.C_Status = "attack1"
                self.C_Animation = True
            
            elif self.Key[pygame.K_SPACE]:
                self.C_Status = "jump"
                self.C_Animation = True
                
            
            elif self.Mouse[2] == 1:
                self.C_Status = "attack3"
                self.C_Animation = True


            else:
                if self.C_Animation == False:
                    if self.C_Action_Mode == True:
                        self.C_Status ="idle_sword"
                    else:
                        self.C_Status = "idle"
            
            
        
        ###### ANİMATİONS #######
        if self.C_Action_Mode == False :
            if self.C_Status == "idle":
                self.C_idle_Animation = self.Animations(self.C_idle_delay,self.C_idle_Animation,4)

            elif self.C_Status == "run":
                self.C_run_Animation = self.Animations(self.C_run_delay,self.C_run_Animation,6)
                self.C_Speed = 8

            elif self.C_Status == "draw_sword":
                self.C_draw_sword_Animation = self.Animations(self.C_draw_sword_delay,self.C_draw_sword_Animation,4,self.C_Animation,True,"idle_sword")
            
            elif self.C_Status == "attack1":
                self.C_attack1_Animation = self.Animations(self.C_attack1_delay,self.C_attack1_Animation,5,self.C_Animation,True,"idle_sword")

            elif self.C_Status == "attack3":
                self.C_attack3_Animation = self.Animations(self.C_attack3_delay,self.C_attack3_Animation,6,self.C_Animation,True,"idle_sword")

            elif self.C_Status == "jump":
                self.C_jump_Animation = self.Animations(self.C_jump_delay,self.C_jump_Animation,6,self.C_Animation,False,"idle")

        elif self.C_Action_Mode == True :
            if self.C_Status == "idle_sword":
                self.C_idle_sword_Animation = self.Animations(self.C_idle_sword_delay,self.C_idle_sword_Animation,4)

            elif self.C_Status == "run":
                self.C_run_Animation = self.Animations(self.C_run_delay,self.C_run_Animation,6)
                self.C_Speed = 6

            elif self.C_Status == "draw_sword_back":
                self.C_sword_shte_Animation = self.Animations(self.C_sword_shte_delay,self.C_sword_shte_Animation,4,self.C_Animation,False,"idle")

            elif self.C_Status == "attack1":
                self.C_attack1_Animation = self.Animations(self.C_attack1_delay,self.C_attack1_Animation,5,self.C_Animation,True,"idle_sword")

            elif self.C_Status == "attack3":
                self.C_attack3_Animation = self.Animations(self.C_attack3_delay,self.C_attack3_Animation,6,self.C_Animation,True,"idle_sword")

            elif self.C_Status == "jump":
                self.C_jump_Animation = self.Animations(self.C_jump_delay,self.C_jump_Animation,6,self.C_Animation,True,"idle_sword")



    def get_rect(self):
        return pygame.Rect(self.C_X+65,self.C_Y+25,63,125)
    
            

