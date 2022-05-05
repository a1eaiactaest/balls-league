from pygame.sprite import Sprite
import pygame

class Ball(Sprite):
  def __init__(self, game):
    super().__init__()

    self.game = game
    self.settings = self.game.settings
    self.position = self.settings.ball_position
    self.size = self.settings.ball_size
    self.color = self.settings.ball_color
    self.radius = self.settings.ball_border_radius

    self.margin = self.size[0]/2

    self.rect = pygame.Rect(self.position[0]-self.margin, self.position[1], self.size[0], self.size[1])

  def draw(self):
    pygame.draw.rect(self.game.screen, self.color, self.rect, border_radius=self.radius)
  

