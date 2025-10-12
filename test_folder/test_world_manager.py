

import pytest
import game_engine_folder.world_manager as world_manager
import game_engine_folder.entity_manager as entity_manager
import game_logic_folder.terrain_generation as terrain_generation




def world():
    return world_manager.World()
world = world()

def player():
    return entity_manager.Player(position=[0, 0])
player = player()


def test_make_new_coordinate():
    world.make_new_coordinate(0, 0)

def test_assign_terrain():
    terrain = terrain_generation.TerrainGeneration.generate_tile()
    world.assign_terrain(0, 0, terrain)

def test_generate_terrain():
    world.generate_terrain(0, 0)

def test_initialize_world():
    world.initialize_world(player)

def test_assign_entity():
    world.assign_entity(player)

