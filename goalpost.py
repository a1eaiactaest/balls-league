import pygame
from pygame.sprite import Sprite

class GoalPost(Sprite):
  def __init__(self, game, position):
    super().__init__()

    self.game = game
    self.position = position

    self.screen = self.game.screen
    self.settings = self.game.settings

    self.color = self.settings.goal_post_color
    self.size = self.settings.goal_post_size
    self.width, self.height = self.size

    self.rect = pygame.Rect(0, 0, self.width, self.height)
    self.rect.center = position

  def draw(self):
    pygame.draw.rect(self.screen, self.color, self.rect)
