class Band():
  pass


class Musician:
  pass


class Guitarist(Musician):
  instrument = 'guitar'
  role = 'Guitarist'
  def __init__(self, name):
    self.name = name

  def __str__(self):
    return f"My name is {self.name} and I play {self.instrument}"

  def __repr__(self): 
    return f"{self.role} instance. Name = {self.name}"


class Bassist(Musician):
  instrument = 'guitar'
  role = 'Guitarist'
  def __init__(self, name):
    self.name = name

  def __str__(self):
    return f"My name is {self.name} and I play {self.instrument}"

  def __repr__(self): 
    return f"{self.role} instance. Name = {self.name}"



class Drummer(Musician):
  pass