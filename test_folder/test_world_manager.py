

import pytest
import game_engine_folder.world_manager as world_manager
import entity_manager




def world():
    return world_manager.World()
world = world()

def player():
    return entity_manager.Player(position=[0, 0])
player = player()



def test_generate_tile():
    (
    world_manager.
    TerrainGeneration.
    generate_tile()
    )

def test_assign_new_terrain():
    (
    world.assign_new_terrain(0, 0)
    )

def test_initialize_world():
    (
    world.initialize_world(player)
    )

def test_assign_entity():
    (
    world.assign_entity(player)
    )

