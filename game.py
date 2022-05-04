#!/usr/bin/env python3
import sys
import pygame

from settings import Settings
from player import Player
from goalpost import GoalPost

class Button:
  def __init__(self):
    raise NotImplementedError

  def update(self):
    raise NotImplementedError

class Game:
  def __init__(self):
    self.settings = Settings()
    self.clock = pygame.time.Clock()

    pygame.init()
    pygame.display.set_caption("Balls")

    self.screen = pygame.display.set_mode(self.settings.screen_size)
    self.screen_rect = self.screen.get_rect()

    self.player_one = Player(self, self.screen_rect.bottom-50)
    self.player_two = Player(self, self.screen_rect.top+50)

    self.goalpost_one = GoalPost(self, self.screen_rect.midtop) 
    self.goalpost_two = GoalPost(self, self.screen_rect.midbottom) 

  def _check_events(self):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        sys.exit()
      
  def _update_screen(self):
    # Draw stuff here
    self.player_one.draw()
    self.player_two.draw()
    self.goalpost_one.draw()
    self.goalpost_two.draw()

    pygame.display.flip()

  def run_game(self):
    while True:
      self._check_events()
      # Update things

      self._update_screen()
      self.clock.tick(60)

if __name__ == "__main__":
  game = Game()
  game.run_game()

