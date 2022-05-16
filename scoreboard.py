import pygame

class Scoreboard:
  def __init__(self, game):
    self.game = game
    self.screen = self.game.screen

    self.score = [0,0]

  def player_one_scores(self):
    self.score[0] += 1

  def player_two_scores(self):
    self.score[1] += 1

  def reset(self):
    self.score = [0,0]

  def update(self):
    black = (0, 0, 0)
    white = (255, 255, 255)
    font = pygame.font.Font('freesansbold.ttf', 32)
    text = font.render((f"{self.score[0]}:{self.score[1]}"), True, white, black)
    self.screen.blit(text, (5,3))
