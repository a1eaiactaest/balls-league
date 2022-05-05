class Scoreboard:
  def __init__(self, game):
    self.game = game

    self.score = [0,0]

  def update(self):
    raise NotImplementedError
