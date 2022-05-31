class Colors:
  BLACK = (0,0,0)
  WHITE = (255, 255, 255)
  RED = (255, 0, 0)
  MAGENTA = (212, 103, 221)
  CYAN = (103, 221, 186)

  def make_list():
    return [attr for attr in dir(Colors) if not callable(getattr(Colors,attr)) and not attr.startswith("__")]
