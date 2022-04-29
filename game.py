#!/usr/bin/env python3
import sys
import pygame

from settings import Settings
from rocket import Rocket

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
    self.background = pygame.image.load("assets/bg.png")
    self.background_rect = self.background.get_rect()
    self.screen.blit(self.background, self.background_rect)

    self.rocket = Rocket(self)

  def _check_events(self):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        sys.exit()
      
  def _update_screen(self):
    # Draw stuff here
    self.rocket.show()

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

