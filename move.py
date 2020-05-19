
import random
import sys


class BodyArea:

    area = None

    def __init__(self, area):
        if (area != "legs") or (area != "arms") or (area != "core"):
            raise Exception("not a valid exercise body area")
        else:
            self.area = area

    def get_area(self):
        return self.area

    def is_arms(self):
        if self.area == "arms":
            return True
        else:
            return False

    def is_legs(self):
        if self.area == "legs":
            return True
        else:
            return False

    def is_core(self):
        if self.area == "core":
            return True
        else:
            return False



class Move:

    name = None
    body_area = None
    base_reps = None
    #max_sets = None
    rep_delta = None
    description = "No description."

    def __init__(self, name, area, base_reps, delta):
        self.name = name
        self.body_area = area
        self.base_reps = base_reps
        self.rep_delta = delta

    def set_description(self, description):
        self.description = description

    def get_description(self):
        return self.description

    def get_area(self):
        return body_area.area


class Library:

    arms = None
    legs = None
    core = None

    def __init__(self):
        self.arms = set()
        self.legs = set()
        self.core = set()

    def add(self, move):
        if move.body_area.is_arms():
            self.arms.add(move)
        elif move.body_area.is_legs():
            self.legs.add(move)
        else:
            self.core.add(move)

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





