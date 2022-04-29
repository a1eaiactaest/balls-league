#!/usr/bin/env python3
import sys
import pygame

from settings import Settings
from sprite import Rocket

class Rocket:
  def __init__(self):
    raise NotImplementedError

  def update(self):
    raise NotImplementedError

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
    pygame.display.set_caption("Rocket")

  
    self.screen = pygame.display.set_mode(self.settings.screen_size)
    self.bg = pygame.image.load("assets/bg.png")

    self.screen.blit(self.bg,((-425),00))

  def _check_events(self):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        sys.exit()
      
  def _update_screen(self):
    # Draw stuff here
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

