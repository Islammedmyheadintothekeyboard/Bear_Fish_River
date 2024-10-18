from random import randint


class River:

  def __init__(self, size, num_bears, num_fish):
    self.bears = num_bears
    self.fish = num_fish
    self.size = size
    self.river = [["🟦 "]*size for loop in range(size)]
    self.animals = []
    self.population = 0
    self.__InitialPop()

  def __str__(self):
    ReturnedString = ""
    for IconRowInd in range(len(self.river)):
      for IconInd in range(len(self.river[IconRowInd])):
        ReturnedString += str(self.river[IconRowInd][IconInd])
        if (IconInd%self.size) == (self.size-1):
          ReturnedString += "\n"

    return ReturnedString

  def place_baby(self, babys):
    while len(babys) > (self.size**2 - self.population):
      del babys[-1]

    babyind = 0
    while babyind != len(babys):
      randy = randint(0, self.size-1)
      randx = randint(0, self.size-1)
      if self.river[randy][randx] == "🟦 ":
        self.river[randy][randx] = babys[babyind]
        babys[babyind].x = randx
        babys[babyind].y = randy
        self.animals.append(babys[babyind])
        babyind += 1
        self.population += 1

  def __InitialPop(self):
    self.place_baby([Fish() for loop in range(self.fish)])
    self.place_baby([Bear() for loop in range(self.bears)])

  def new_day(self):
    babys = []
    for row in range(self.size):
      for column in range(self.size):
        if self.river[column][row] != "🟦 ":
          animal = self.river[column][row]
          animal.move(self)

          if self.river[animal.y][animal.x] != "🟦 ":
            baby = animal.collision(self, column, row)
            if baby is not None:
              babys.append(baby)
          
          if isinstance(animal, type(Bear())) is True:
            animal.starve(self, column, row)
          
          self.redraw_cells(animal, column, row)

    self.place_baby(babys)
            


  def redraw_cells(self, animal, y, x):
    self.river[animal.y][animal.x] = animal
    self.river[y][x] = "🟦 "

  def death(self, animal):
    self.river[animal.y][animal.x] = "🟦 "
    self.population -= 1



class Animal:
  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.bred_today = False

  def breed(self, OthAnimal):
    if (self.bred_today is False) and (OthAnimal.bred_today is False):
      if isinstance(self, type(Bear())) is True:
        baby = Bear()
      else:
        baby = Fish()
      
    else:
      baby = None
    return baby

  def move(self, riverobj):
    if randint(1,2) == 1:
      if self.x == 0:
        self.x += 1
      elif self.x == riverobj.size-1:
        self.x -= 1
      else:
        if randint(1,2) == 1:
          self.x += 1
        else:
          self.x -= 1

    else:
      if self.y == 0:
        self.y += 1
      elif self.y == riverobj.size-1:
        self.y -= 1
      else:
        if randint(1,2) == 1:
          self.y += 1
        else:
          self.y -= 1

  def collision(self, riverobj, y, x):

    #The animal's coordinate points that this current animal is moving to
    OthAnimal = riverobj.river[self.y][self.x]
    if isinstance(OthAnimal, type(self)) is True:
      baby = self.breed(OthAnimal)
      self.y = y
      self.x = x
      return baby

    elif isinstance(OthAnimal, type(self)) is False:
      if isinstance(self, type(Bear())) is True:
        self.consume(riverobj)
        return None
      else:
        return None


class Bear(Animal):
  def __init__(self):
    self.max_lives = 3
    self.lives = self.max_lives
    self.eaten_today = False
    super().__init__(0,0)

  def __str__(self):
    return "🐻‍❄ "

  def starve(self, riverobj, y, x):
    if self.eaten_today is False:
      self.lives -= 1
      if self.lives == 0:
        self.y = y
        self.x = x
        riverobj.death(self)

  def consume(self, riverobj):
    riverobj.death(riverobj.river[self.y][self.x])
    self.eaten_today = True

class Fish(Animal):
  def __init__(self):
    super().__init__(0,0)

  def __str__(self):
    return "🐠 "