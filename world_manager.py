

import random
import sys
import os
import time


class class_terrain_generator:

    def generate_tile ():
        if random.random() < 0.1:
            return "V"
        else:
            return "_"


class class_world:
    
    def __init__ (self, name):
        self.name = name
        self.world_dict = {}
        self.class_terrain_generator = class_terrain_generator

    def assign_new_tile(self, cords_x, cords_y):
        tile = self.class_terrain_generator.generate_tile()
        self.world_dict[cords_x, cords_y] = tile