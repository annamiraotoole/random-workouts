

import os

import sys

import move


class Person():

    # name = None
    # fitness = None # how many deltas above the base number of reps for each exercise

    def __init__(self, name, fitness):
        self.name = name
        self.fitness = fitness

    def get_fitness(self):
        return self.fitness

    def increase_fitness(self, num):
        self.fitness += num

    def decrease_fitness(self, num):
        self.fitness -= num


cian = Person("Cian", 3)

annamira = Person("Annamira", 0)