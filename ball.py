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

    self.vector = pygame.Vector2(self.rect.centerx, self.rect.centery)
    self.velocity = 0

  def vector_update(self):
    self.vector.xy = self.rect.center

  def _out_of_bounds(self):
    if self.rect.left <= self.screen_rect.left:
      return True
    
    elif self.rect.right >= self.screen_rect.right:
      return True

    elif self.rect.bottom >= self.screen_rect.bottom:
      return True

    elif self.rect.top <= self.screen_rect.top:
      return True

    else: 
      return False

  def moving(self, power, player):
    if not self._out_of_bounds():
      vector_deal = player.vector - self.vector
      vector_deal[1] = vector_deal[1]*(-1)
      
      cord_sum = vector_deal[0] + vector_deal[1]

      print(vector_deal)

      if self.rect.centery > player.rect.centery:
        self.rect.centery += (cord_sum/vector_deal[1])*power
        print(self.rect.centerx)
        print(player.rect.centerx)
      elif self.rect.centery == player.rect.centery:
        pass
      else:
        self.rect.y += (cord_sum/vector_deal[1])*power
      
      if self.rect.centerx > player.rect.centerx:
        print(vector_deal[0])
        print(self.rect.centerx)
        print(player.rect.centerx)
        self.rect.x -= (cord_sum/vector_deal[0])*power
      elif self.rect.centerx == player.rect.centerx:
        pass
      else:
        self.rect.x -= (cord_sum/vector_deal[0])*power

    self.vector_update()

  def reset(self):
    self.rect.centerx = self.screen_rect.centerx
    self.rect.centery = self.screen_rect.centery

  def draw(self):
    player_collision = pygame.sprite.spritecollideany(self, self.game.players)
    goalpost_collision = pygame.sprite.spritecollideany(self, self.game.goal_posts)


    if player_collision == self.game.player_one:
      self.moving(6, self.game.player_one)
    if player_collision == self.game.player_two:
      self.moving(6, self.game.player_two)

    if goalpost_collision == self.game.goalpost_one:
      self.game.scoreboard.player_one_scores()
      self.game.reset_positions()
    if goalpost_collision == self.game.goalpost_two:
      self.game.scoreboard.player_two_scores()
      self.game.reset_positions()

    pygame.draw.rect(self.game.screen, self.color, self.rect, border_radius=self.radius)
  

