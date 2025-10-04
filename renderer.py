

import random
import sys
import os
import time


class class_renderer:

    def __init__ (self, render_distance):
        self.render_distance = render_distance

    def render_from_player (self,
                            world,
                            player):
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
        print("")

