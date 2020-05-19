
import os
import random
import sys

from move import BodyArea, Move


class Library:

    # arms = None
    # legs = None
    # core = None

    def __init__(self):
        self.arms = set()
        self.legs = set()
        self.core = set()

    def add(self, move):
        if move.get_area().is_arms():
            self.arms.add(move)
        elif move.get_area().is_legs():
            self.legs.add(move)
        elif move.get_area().is_core():
            self.core.add(move)
        else:
            raise Exception("not a valid body area type")

    def random_set(self, area, num):
        try:
            if area.is_arms():
                return random.sample(self.arms, num)
            elif area.is_legs():
                return random.sample(self.legs, num)
            else:
                return random.sample(self.core, num)
        except:
            raise Exception("tried to draw too many exercises from the library")


# define some useful instances of BodyArea

arms = BodyArea("arms") 
legs = BodyArea("legs")
core = BodyArea("core")


# NEEDS: name, area, base_reps, delta

# LEGS

jump_squat = Move("Jump Squat", legs, 10, 3)

lunge = Move("Lunges (left and right)", legs, 20, 10)

donkey_kick = Move("Donkey Kick (with 15 lbs weight, left and right)", legs, 20, 10)

pistol_squat = Move("Pistol Squat", legs, 5, 2)

all_legs = [jump_squat, lunge, donkey_kick, pistol_squat]

# ARMS

pushup = Move("Pushup", arms, 3, 1)

tricep_dips = Move("Tricep Chair Dips", arms, 10, 3)

chin_up = Move("Chin Up", arms, 1, 1)

pull_up = Move("Pull Up", arms, 1, 1)

arm_raise = Move("Side Arm Raise (with 8 lbs weight, left and right)", arms, 10, 3)

all_arms = [pushup, tricep_dips, chin_up, pull_up, arm_raise]

# CORE

forearm_plank = Move("Forearm Plank (minutes)", core, 1, 0.5)

high_plank = Move("High Plank (minutes)", core, 0.5, 0.5)

russian_twist = Move("Russian Twist (minutes)", core, 1, 0.5)

mountain_climbers = Move("Mountain Climbers (minutes)", core, 1, 0.5)

dead_bug = Move("Dead Bug", core, 40, 20)

crunches = Move("Crunches", core, 30, 5)

plank_hip_dips = Move("Plank with Hip Dips (minutes)", core, 1, 0.5)

all_core = [forearm_plank, high_plank, russian_twist, mountain_climbers, 
            dead_bug, crunches, plank_hip_dips]


# LIBRARIES

my_library = Library()

for move in all_legs:
    my_library.add(move)

for move in all_arms:
    my_library.add(move)

for move in all_core:
    my_library.add(move)

def return_library():
    return my_library


