import pygame.font

class Button:
  def __init__(self, game, position, size, button_str):
    self.screen = game.screen
    self.text_color = (30,30,30)
    self.button_color = (100, 170, 85)
    self.font = pygame.font.SysFont(None, 40)

    self.button_str = button_str

    self.width = size[0]
    self.height = size[1]
    self.rect = pygame.Rect(0, 0, self.width, self.height)
    self.rect.left= position[0]
    self.rect.top = position[1]

    self.prep_button()

  def prep_button(self):
    self.text_image = self.font.render(self.button_str, True, self.text_color, self.button_color)
    self.text_image_rect = self.text_image.get_rect()
    self.text_image_rect.center = self.rect.center

  def show_button(self):
    self.screen.fill(self.button_color, self.rect)
    self.screen.blit(self.text_image, self.text_image_rect)