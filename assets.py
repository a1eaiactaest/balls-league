import pygame


import pygame

class Images():
    def __init__(self):
        self.background = pygame.image.load("assets/bg.png")
    
    def set_bg(self):
        pygame.display.blit(self.bg,(0,0))
