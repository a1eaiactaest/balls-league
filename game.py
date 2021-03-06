#!/usr/bin/env python3
import sys
import pygame
from scoreboard import Scoreboard

from settings import Settings
from colors import Colors 
from player import Player
from goalpost import GoalPost
from ball import Ball
from button import Button, ColorChooser

class Game:
  def __init__(self):
    self.settings = Settings()
    self.clock = pygame.time.Clock()

    self.icon = pygame.image.load('assets/icon.png')

    pygame.init()
    pygame.display.set_caption("Balls League")
    pygame.display.set_icon(self.icon)

    self.screen = pygame.display.set_mode(self.settings.screen_size)
    self.screen_rect = self.screen.get_rect()

    self.game_active = False

    self.scoreboard = Scoreboard(self)
    self.play_button = Button(self, (200, 250), (100, 100), "Play")
    self.pause_button = Button(self, (self.screen_rect.right-100, self.screen_rect.top), (100, 30), "Pause")

    self.player_one = Player(self, Colors.MAGENTA, self.screen_rect.bottom-100)
    self.player_two = Player(self, Colors.CYAN, self.screen_rect.top+50)
    self.players = [self.player_one, self.player_two]

    self.goalpost_one = GoalPost(self, self.screen_rect.midtop) 
    self.goalpost_two = GoalPost(self, self.screen_rect.midbottom) 
    self.goal_posts = [self.goalpost_one, self.goalpost_two]

    self.ball = Ball(self)

  def reset_positions(self):
    self.ball.reset()
    self.player_one.reset()
    self.player_two.reset()

  def _check_events(self):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        sys.exit()

      elif event.type == pygame.KEYDOWN:
        # Player One
        if event.key == pygame.K_RIGHT:
          self.player_one.moving_right = True
        if event.key == pygame.K_LEFT:
          self.player_one.moving_left = True
        if event.key == pygame.K_DOWN:
          self.player_one.moving_down = True
        if event.key == pygame.K_UP:
          self.player_one.moving_up = True

        # Player Two
        if event.key == pygame.K_d:
          self.player_two.moving_right = True
        if event.key == pygame.K_a:
          self.player_two.moving_left = True
        if event.key == pygame.K_s:
          self.player_two.moving_down = True
        if event.key == pygame.K_w:
          self.player_two.moving_up = True

      elif event.type == pygame.KEYUP:
        # Player One
        if event.key == pygame.K_RIGHT:
          self.player_one.moving_right = False
        if event.key == pygame.K_LEFT:
          self.player_one.moving_left = False
        if event.key == pygame.K_DOWN:
          self.player_one.moving_down = False
        if event.key == pygame.K_UP:
          self.player_one.moving_up = False

        # Player Two
        if event.key == pygame.K_d:
          self.player_two.moving_right = False
        if event.key == pygame.K_a:
          self.player_two.moving_left = False
        if event.key == pygame.K_s:
          self.player_two.moving_down = False
        if event.key == pygame.K_w:
          self.player_two.moving_up = False

      elif event.type == pygame.MOUSEBUTTONDOWN:
        mouse_position = pygame.mouse.get_pos()
        # check for collision with buttons
        if self.play_button.rect.collidepoint(mouse_position):
          self.game_active = True
          print("GAME STARTED")

        if self.pause_button.rect.collidepoint(mouse_position):
          self.game_active = False
          print("GAME PAUSED")

      
  def _draw_field_lines(self):
    pygame.draw.line(self.screen, Colors.WHITE, (0, self.settings.screen_height/2), (self.settings.screen_width, self.settings.screen_height/2), 2)
    pygame.draw.circle(self.screen, Colors.WHITE, (self.screen_rect.centerx, self.screen_rect.centery), 80, width=2)

  def _update_screen(self):
    self.screen.fill(Colors.BLACK)
    # Draw stuff here
    self._draw_field_lines()

    self.player_one.draw()
    self.player_two.draw()

    self.goalpost_one.draw()
    self.goalpost_two.draw()

    self.ball.draw()

    self.scoreboard.update()

    if not self.game_active:
      self.play_button.show_button()
    else:
      self.pause_button.show_button()

    pygame.display.flip()

  def _update_players(self):
    for player in self.players:
      player.update()

  def run_game(self):
    while True:
      self._check_events()
      if self.game_active:
        # Update things
        self._update_players()

        vector_deal = self.player_one.vector - self.ball.vector
        vector_deal[1] = vector_deal[1]*(-1)

      self._update_screen()
      self.clock.tick(120)

if __name__ == "__main__":
  game = Game()
  game.run_game()

