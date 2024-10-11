from random import randint


class River:
  def __init__(self, size, num_bears, num_fish):
    self.bears = num_bears
    self.fish = num_fish
    self.size = size
    self.river = [["🟦 "]*size for loop in range(size)]
    self.animals = []
    self.population = 0
    print(self.river)
    self.__InitialPop()

  def __str__(self):
    ReturnedString = ""
    for IconRowInd in range(len(self.river)):
      for IconInd in range(len(self.river[IconRowInd])):
        ReturnedString += self.river[IconRowInd][IconInd]
        if (IconInd%self.size) == 14:
          ReturnedString += "\n"

    return ReturnedString



  def __InitialPop(self):
    PlacedB = False
    BearsPlaced = 0
    while (placedb is False) or (BearsPlaced >= self.bears):
      randy = randint(0, self.size-1)
      randx = randint(0, self.size-1)
      if self.river[randy][randx] != "🟦 ":
        placedb 
      else:
        self.river[randy][randx] = "🐻‍❄ "
        BearsPlaced += 1

    for fish in range(self.fish):
      randy = randint(0, self.size-1)
      randx = randint(0, self.size-1)
      self.river[randy][randx] = "🐠 "