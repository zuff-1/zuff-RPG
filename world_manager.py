

import random


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
