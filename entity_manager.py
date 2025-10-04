

import random
import sys
import os
import time

import central_registry


class class_entity:

    def __init__ (self, name, position=None):
        self.name = name
        if position is not None:
            self.position = position
        else:
            self.position = [0, 0]


class class_player(class_entity):

    def __init__ (self, name, position=None):
        super().__init__(name, position)


class class_entitiy_behavior:

    def entity_move(self, change_x, change_y):
        old_key = (self.position[0], self.position[1])
        world_object = central_registry.central_registry["class_object_overworld"]
        entity_in_world_dict = world_object.world_dict[old_key].pop(1)
        self.position[0] += change_x
        self.position[1] += change_y
        new_key = (self.position[0], self.position[1])
        world_object.world_dict[new_key].append(entity_in_world_dict)