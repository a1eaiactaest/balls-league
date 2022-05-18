import pygame

class Scoreboard:
  def __init__(self, game):
    self.game = game
    self.settings = self.game.settings
    self.screen = self.game.screen
    self.screen_rect = self.screen.get_rect()

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
    player_one_score_text = font.render((f"{self.score[0]}"), True, white, black)
    player_two_score_text = font.render((f"{self.score[1]}"), True, white, black)
    self.screen.blit(player_one_score_text, (0, (self.settings.screen_height/2)+25))
    self.screen.blit(player_two_score_text, (0, (self.settings.screen_height/2)-50))
