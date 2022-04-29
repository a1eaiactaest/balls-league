import pygame
from pygame.sprite import Sprite

class Rocket(Sprite):
  def __init__(self, game):
    self.settings = game.settings
    self.screen = game.screen
    
    self.image = pygame.image.load("assets/rocket.png")
    self.rect = self.image.get_rect()

  def show(self):
    self.screen.blit(self.image, self.rect)

  def update(self):
    raise NotImplementedError


