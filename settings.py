from PIL import Image

def get_image_size(file_name):
  img = Image.open(file_name)
  return img.size

class Settings:
  def __init__(self):
    # Screen
    self.screen_width, self.screen_height = get_image_size('assets/bg.png')
    self.screen_size = (self.screen_width, self.screen_height)

    # Rocket 
    self.rocket_speed = 5

