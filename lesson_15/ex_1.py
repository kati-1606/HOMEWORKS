# 1_Dice Rolling Simulator:
# Develop a simple dice rolling simulator.
# Generate random numbers between 1 and 6 to
# simulate the roll of a six-sided die using the random module
import random

def roll_dice(num_dice):
   result = []
   for i in range(num_dice):
      result.append(random.randint(1,6))
   return result

print(roll_dice(1))