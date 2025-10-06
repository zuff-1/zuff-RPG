

import sys
import random

import entity_manager


class TerrainGeneration:

    def generate_tile():
        if random.random() < 0.1:
            return "V"
        else:
            return "_"


class World:

    def __init__(self, name):
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
            ]["terrain"] = [
                TerrainGeneration.
                generate_tile()
                ]
        
        self.dict[cords_x, cords_y,][
            "entity"] = []
        

        
    def initialize_world(
            self,
            player: entity_manager.Player,
            render_distance,
            ):
        for row in range(render_distance):
            for column in range(render_distance):
                generate_target = [
                    player.position[0]
                    + (column - (((render_distance + 1) // 2) - 1)),
                    player.position[1]
                    + (row - (((render_distance + 1) // 2) - 1)),
                    ]
                if tuple(generate_target) not in self.dict:
                    self.assign_new_terrain(*generate_target)
                else:
                    pass
    
    def assign_entity(
            self,
            entity: entity_manager.Entity,
            ):
        if not self.dict[
            tuple(entity.position)
            ]["entity"]:
            self.dict[
                tuple(entity.position)
                ]["entity"] = [entity]
        else:
            print("Theres already an entity on tile!!! fix NOWWWW")
            sys.exit()


def test_World():
    overworld = World("balls")
    overworld.assign_new_terrain(3, 5)

    print(f"self.name = {overworld.name}")
    print(f"generated terrain: {overworld.dict[3, 5]["terrain"][0]}")
    print(f"self.dict = {overworld.dict}")


def test_TerrainGeneration():
    tile = TerrainGeneration.generate_tile()
    print(tile)


if __name__ == "__main__":
    test_World()
