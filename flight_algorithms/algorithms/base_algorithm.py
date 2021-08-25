from abc import ABC, ABCMeta, abstractmethod
#from flight_algorithms.Flight import Flight
import random
import math
import sys

class FlightAlgorithm(metaclass=ABCMeta):
    def __init__(self, domain, fitness_function,seed=random.randint(10, 100),seed_init=True,init=[]):
        self.domain = domain
        self.fitness_function = fitness_function
        self.seed = seed
        self.seed_init = seed_init
        self.init = init
        if self.seed_init:
            # Set the seed for initial population only
            self.r_init = random.Random(seed)
        else:
            # Same seeds for both init and other random generators
            self.r_init = random.Random(seed)
            random.seed(seed)
        
        self.best_cost =0.0  # returned

    @abstractmethod
    def run(self, **kwargs) -> tuple:
        pass