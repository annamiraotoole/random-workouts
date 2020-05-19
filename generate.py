
import random

import person
import move


class Generator():

    name = None
    area = None
    library = None

    def __init__(self, library, name=None, area=None):
        self.name = name
        self.area = area
        self.library = library

    def generate_circuit(self, area, size, person=None):

        n = random.randint(3, 4) # to be changed?
        circ = library.random_set(area, n)

        if person == None:
            deltas = 0
        else:
            deltas = person.get_fitness()

        print("Move Descriptions:")

        for m in circ:
            print(m.name)
            print(m.get_description())

        for s in range(size):
            for m in circ:
                print(m.name + ": " + (m.base_reps + deltas*m.rep_delta) + " reps")



my_generator = Generator(my_library)

