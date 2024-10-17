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
    print(self.river)
  def __str__(self):
    ReturnedString = ""
    for IconRowInd in range(len(self.river)):
      for IconInd in range(len(self.river[IconRowInd])):
        ReturnedString += self.river[IconRowInd][IconInd]
        if (IconInd%self.size) == 14:
          ReturnedString += "\n"

    return ReturnedString



def new_day(self):
  babys = []
  for row in range(size):
    for column in range(size):
      if self.river[column][row] != "🟦 ":
        animal = self.river[column][row]
        animal.move(self)

        if self.river[animal.y][animal.x] != "🟦 ":
          baby = animal.collision(self, column, row)
          if baby is not None:
            babys.append(baby)
        
        if isinstance(animal, Bear()) is True:
          animal.starve(self)
        
        self.redraw_cell()

  self.place_baby(babys)
          


  def redraw_cells(self, animal, y, x):
    self.river[animal.y][animal.x] = animal
    self.river[y][x] = "🟦 "

  def death(self, AnimalPutDown):
    del AnimalPutDown

  def __InitialPop(self):
    self.place_baby([Fish() for loop in range(self.fish)])
    self.place_baby([Bear() for loop in range(self.bears)])

  def place_baby(self, babys):
    while len(babys) != self.population:
      del babys[-1]

    babyind = 0
    while babyind != len(babys):
      randy = randint(0, self.size-1)
      randx = randint(0, self.size-1)
      if self.river[randy][randx] == "🟦 ":
        self.river[randy][randx] = babys[babyind]
        babyind += 1
        self.population += 1
        self.animals.append(babys[babyind])




class Animal:
  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.bred_today = False

  def breed(self, OthAnimal):
    if (self.bred_today is False) and (OthAnimal.bred_today is False):
      if isinstance(self, Bear()) is True:
        baby = Bear()
      else:
        baby = Fish()
      
    else:
      baby = None
    return baby

  def move(self, riverobj):
    if self.x == 0:
      self.x += 1
    elif self.x == riverobj.size:
      self.x -= 1
    else:
      if randint(1,2) == 1:
        self.x += 1
      else:
        self.x -= 1

    if self.y == 0:
      self.y += 1
    elif self.y == riverobj.size:
      self.y -= 1
    else:
      if randint(1,2) == 1:
        self.y += 1
      else:
        self.y -= 1

  def collision(self, riverobj):

    #The animal's coordinate points that this current animal is moving to
    OthAnimal = riverobj.river[self.y][self.x]
    if isinstance(othanimal, self) is True:
      self.breed(othanimal)
      return baby

    elif isinstance(othanimal, self) is False:
      self.consume(riverobj)
      return None


class Bear(Animal):
  def __init__(self):
    self.max_lives = 3
    self.lives = self.max_lives
    self.eaten_today = False

  def __str__(self):
    return "🐻‍❄ "

  def starve(self, riverobj):
    if self.eaten_today is False:
      self.lives -= 1
      if self.lives == 0:
        riverobj.death(self)
        try:
          print(self)
        except:
          print("ANIMAL SELF DIE")

  def consume(self, riverobj):
    riverobj.death(riverobj.river[self.y][self.x])
    try:
      print(riverobj.river[self.y][self.x])
    except:
      print("ANIMAL DIED")
    self.eaten_today = True

class Fish(Animal):
  def __str__(self):
    return "🐠 "