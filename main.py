# Donovan Farley-Freeman
# 10/9/24
# Creating a simulation that simulates



from ecosystem import *
from time import sleep

DAYS_SIMULATED = 30
RIVER_SIZE = 8
START_BEARS = 35
START_FISH = 35

def BearFishRiver():

  revir = River(RIVER_SIZE, START_BEARS, START_FISH)
  day = 0
  done = False
  for day in range(DAYS_SIMULATED):
    print(f"\n\nDay: {day+1}")
    print(revir)
    print(f"\nStarting Poplation: {revir.population} animals")
    done = revir.new_day()
    print(f"Ending Poplation: {revir.population} animals")
    print(revir)
    sleep(1)

if __name__ == "__main__":
  BearFishRiver()