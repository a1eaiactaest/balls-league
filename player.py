import pygame
from pygame.sprite import Sprite

class Player(Sprite):
  def __init__(self, game, player_y):
    super().__init__()

    self.settings = game.settings
    self.screen = game.screen
    self.color = self.settings.player_color

    self.player_x = self.settings.player_x
    self.player_y = player_y
    
  def draw(self):
    self.rect = pygame.draw.circle(self.screen, self.color, (self.player_x, self.player_y), 25)

  def update(self):
    raise NotImplementedError


