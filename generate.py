
import random
import os
import sys

import person
from move import BodyArea
from library import Library, return_library


class Generator():

    def __init__(self, library, name=None, area=None):
        self.name = name
        self.area = area
        self.library = library

    def generate_circuit(self, area, size, person=None):

        n = random.randint(3, 4) # to be changed?
        circ = self.library.random_set(area, n)

        if person == None:
            deltas = 0
        else:
            deltas = person.get_fitness()

        print("Move Descriptions:")

        for m in circ:
            print(m.name)
            print(m.get_description())

        print("REPEAT CIRCUIT " + str(size) + " TIMES")

        for m in circ:
            print(m.name + ": " + str(m.base_reps + deltas*m.rep_delta) + " reps")


lib = return_library()

my_generator = Generator(lib)

