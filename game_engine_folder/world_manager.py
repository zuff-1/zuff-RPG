

import sys
import random

import entity_manager


class TerrainGeneration:
    
    def generate_tile():
        rng = random.random()
        if rng < 0.03:
            return "V"
        elif rng < 0.1:
            return "v"
        elif rng < 0.15:
            return ";"
        elif rng < 0.2:
            return ","
        else:
            return "."


class World:

    def __init__(
            self,
            name = "Default Name",
            ):
        self.name = name
        self.dict = {}

    def assign_new_terrain(
            self,
            cords_x,
            cords_y,
            ):
        self.dict[
            cords_x,
            cords_y,
            ] = {}
        self.dict[
            cords_x,
            cords_y,
            ][
            "terrain"
            ] = [
            TerrainGeneration.
            generate_tile()
            ]
        
        self.dict[cords_x, cords_y,][       # here is where all dict defaults are placed.
            "entity"
            ] = []
        
    def initialize_world(
            self,
            player: entity_manager.Player,
            render_distance = 12,
            ):
        
        half = render_distance // 2

        for row in range(render_distance):
            print("")
            for column in range(render_distance):
                generate_target = [
                    player.position[0]
                    + (column - half),
                    player.position[1]
                    - (row - half),
                ]
                if tuple(generate_target) not in self.dict:
                    World.assign_new_terrain(self, *generate_target)
                else:
                    pass
    
    def assign_entity(
            self,
            entity: entity_manager.Entity,
            ):
        if not self.dict[
            tuple(entity.position)
            ][
            "entity"
            ]:
            self.dict[
                tuple(entity.position)
                ][
                "entity"
                ] = [entity]
        else:
            print("Theres already an entity on tile!!! fix NOWWWW")
            sys.exit()

