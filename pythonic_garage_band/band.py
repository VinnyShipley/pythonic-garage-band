class Band():
  def __init__(self, name, members):
    self.name = name
    self.members = []

  def __band_members__(self):
    return self.name


  def __band_name__(self):
    for i in self:
      self.members.append(i)
    return self.members



class Musician(Band):
  def __init__(self, name):
    self.name = name



class Guitarist(Musician):
  instrument = 'guitar'
  role = 'Guitarist'
  def __init__(self, name):
    super().__init__(name)

  def __str__(self):
    return f"My name is {self.name} and I play {self.instrument}"

  def __repr__(self): 
    return f"{self.role} instance. Name = {self.name}"

  def get_instrument(self):
    return self.instrument



class Bassist(Musician):
  instrument = 'bass'
  role = 'Bassist'
  def __init__(self, name):
    self.name = name

  def __str__(self):
    return f"My name is {self.name} and I play {self.instrument}"

  def __repr__(self): 
    return f"{self.role} instance. Name = {self.name}"

  def get_instrument(self):
    return self.instrument



class Drummer(Musician):
  instrument = 'drums'
  role = 'Drummer'
  def __init__(self, name):
    self.name = name

  def __str__(self):
    return f"My name is {self.name} and I play {self.instrument}"

  def __repr__(self): 
    return f"{self.role} instance. Name = {self.name}"

  def get_instrument(self):
    return self.instrument
