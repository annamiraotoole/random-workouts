
import os
import sys


class BodyArea:

    def __init__(self, area):
        if (area != "legs") or (area != "arms") or (area != "core"):
            self.area = "no body area defined"
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

    # name = None
    # body_area = None
    # base_reps = None
    # #max_sets = None
    # rep_delta = None
    # description = "No description."

    def __init__(self, name, area, base_reps, delta, description="No description."):
        self.name = name
        self.body_area = area
        self.base_reps = base_reps
        self.rep_delta = delta
        self.description = description

    def get_area(self):
        return self.body_area

    def set_description(self, description):
        self.description = description

    def get_description(self):
        return self.description

    def get_area(self):
        return self.body_area.get_area()







