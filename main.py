# Donovan Farley-Freeman
# 10/9/24
# Creating a simulation that simulates



from ecosystem import *
from time import sleep

DAYS_SIMULATED = 1
RIVER_SIZE = 15
START_BEARS = 112
START_FISH = 113

def BearFishRiver():

  revir = River(RIVER_SIZE, START_BEARS, START_FISH)
  print(revir)
  '''day = 0
  done = False
  for day in range(DAYS_SIMULATED):
    print(f"\n\nDay: {day+1}")
    print(revir)
    print(f"\nStarting Poplation: {revir.population} animals")
    done = revir.new_day()
    print(f"Ending Poplation: {revir.population} animals")
    print(revir)
    day += 1
    sleep(5)'''

if __name__ == "__main__":
  BearFishRiver()