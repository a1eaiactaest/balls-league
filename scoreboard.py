import pygame

class Scoreboard:
  def __init__(self, game):
    self.game = game

    self.score = [0,0]

  def update(self):
    green = (64, 247, 32)
    yellow = (255, 247, 0)
    font = pygame.font.Font('freesansbold.ttf', 32)
    text = font.render('Result', True, green, yellow)
    text.get_rect()
