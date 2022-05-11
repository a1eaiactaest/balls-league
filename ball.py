from pygame.sprite import Sprite
import pygame

#from game import Game
from player import Player

class Ball(Sprite):
  def __init__(self, game):
    super().__init__()

    self.game = game
    self.screen_rect = self.game.screen.get_rect()
    self.settings = self.game.settings
    self.position = self.settings.ball_position
    self.size = self.settings.ball_size
    self.color = self.settings.ball_color
    self.radius = self.settings.ball_border_radius

    self.margin = self.size[0]/2

    self.rect = pygame.Rect(self.position[0]-self.margin, self.position[1], self.size[0], self.size[1])
    self.rect.centerx = self.screen_rect.centerx
    self.rect.centery = self.screen_rect.centery

  def draw(self, ball, players, player_one, player_two, goalpost_one, goalpost_two):
    collision = pygame.sprite.spritecollideany(ball, players)
    if collision == player_one:
      print("player one")
    if collision == player_two:
      print("player two")
    if collision == goalpost_one:
      pass
    if collision == goalpost_two:
      pass

    pygame.draw.rect(self.game.screen, self.color, self.rect, border_radius=self.radius)
  

