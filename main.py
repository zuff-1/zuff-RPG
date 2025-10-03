

import random
import sys
import os

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

player1 = class_player("zuff")


class class_entitiy_behavior:

    def move ():
        pass


class class_terrain_generator:

    def generate_tile (self):
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
        tile = self.class_terrain_generator.generate_tile(self)
        self.world_dict[cords_x, cords_y] = tile

world_overworld = class_world("overworld")


class class_renderer:

    def __init__ (self, render_distance):
        self.render_distance = render_distance

    def render_from_player (self, world: class_world, player: class_player):
        for row in range(self.render_distance):
            print("")
            for column in range(self.render_distance):
                render_target = (
                player.position[0] +
                (column - (((self.render_distance+1)//2)-1)),
                player.position[1] +
                (row - (((self.render_distance+1)//2)-1))
                )

                if (row, column) == ((((self.render_distance+1)//2)-1),
                                    ((self.render_distance+1)//2)-1):
                    print("☺", end="")
                
                elif render_target not in world.world_dict:
                    world.assign_new_tile(*render_target)
                    print(world.world_dict[render_target], end="")
                else:
                    print(world.world_dict[render_target], end="")


renderer = class_renderer(11)


class user_interface:

    def start_menu():
        pass


def main_sequence():
    pass


renderer.render_from_player(world_overworld, player1)