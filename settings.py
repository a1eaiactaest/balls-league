from colors import Colors as colors

class Settings:
  def __init__(self):
    # Screen
    self.screen_width, self.screen_height = (600, 900)
    self.screen_size = (self.screen_width, self.screen_height)

    # Player
    self.player_width, self.player_height = (50,50)
    self.player_size = (self.player_width, self.player_height)
    self.player_border_radius = self.player_width//2

    self.player_speed = 5

    self.player_x = (self.screen_width/2) - self.player_width/2
    """
    Set player_y as object parameter, it's not fixed.
    """

    # Goal Post
    self.goal_post_color = colors.WHITE
    self.goal_post_width, self.goal_post_height = (200, 20)
    self.goal_post_size = (self.goal_post_width, self.goal_post_height)

    # Ball
    self.ball_x = self.screen_width/2
    self.ball_y = self.screen_height/2
    self.ball_position = (self.ball_x, self.ball_y)

    self.ball_width, self.ball_height = (25,25)
    self.ball_size = (self.ball_width, self.ball_height)
    self.ball_border_radius = self.ball_width//2
    
    self.ball_color = colors.WHITE