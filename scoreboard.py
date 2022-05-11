import pygame

class Scoreboard:
  def __init__(self, game):
    self.game = game

    self.score = [0,0]

  def update(self, screen, result_1, result_2):
    black = (0, 0, 0)
    white = (255, 255, 255)
    font = pygame.font.Font('freesansbold.ttf', 32)
    text = font.render((f"{result_1}:{result_2}"), True, white, black)
    self.screen.blit(text, (5,3))
