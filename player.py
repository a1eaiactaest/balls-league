import pygame
from pygame.sprite import Sprite

class Player(Sprite):
  def __init__(self, game, color, player_y):
    super().__init__()

    self.settings = game.settings
    self.screen = game.screen
    self.screen_rect = self.screen.get_rect()
    self.color = color
    self.radius = self.settings.player_border_radius

    self.player_x = self.settings.player_x
    self.player_y = player_y

    self.moving_right = False
    self.moving_left = False
    self.moving_down = False
    self.moving_up = False
    self.rect = pygame.Rect(self.player_x, self.player_y, self.settings.player_width, self.settings.player_height)

    
  def draw(self):
    pygame.draw.rect(self.screen, self.color, self.rect, border_radius=self.radius)

  def update(self):
    if self.moving_right and self.rect.right < self.screen_rect.right:
      self.rect.x += self.settings.player_speed
  
    if self.moving_left and self.rect.left > self.screen_rect.left:
      self.rect.x -= self.settings.player_speed

    if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
      self.rect.y += self.settings.player_speed

    if self.moving_up and self.rect.top > self.screen_rect.top:
      self.rect.y -= self.settings.player_speed

