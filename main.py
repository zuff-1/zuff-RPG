

import sys
import os

import central_registry
import world_manager
import entity_manager
import renderer_2d

def function_clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def function_enter_to_continue():
    input("\nPress Enter to continue...")

def create_define_all_object():
    (
    central_registry.
    CentralRegistryControls.
    set_central_registry(
        "overworld",
        world_manager.World("overworld")
        )
    )
    (
    central_registry.
    CentralRegistryControls.
    set_central_registry(
        "player",
        entity_manager.Player(
            "zuff",
            [0, 0],
            "overworld",
            )
        )
    )
    (
    central_registry.
    CentralRegistryControls.
    set_central_registry(
        "renderer",
        renderer_2d.Renderer(11)
        )
    )
    world =(
        central_registry.
        CentralRegistryControls.
        get_central_registry("overworld")
        )
    player =(
        central_registry.
        CentralRegistryControls.
        get_central_registry("player")
        )
    renderer =(
        central_registry.
        CentralRegistryControls.
        get_central_registry("renderer")
        )
    
    return world, player, renderer


def test_initialization():
    world, player, renderer = create_define_all_object()
    world_manager.World.initialize_world(
        world,
        player,
        renderer.render_distance
        )
    world_manager.World.assign_entity(world, player)
    renderer_2d.Renderer.render_from_player(renderer, player, world)


test_initialization()













## Notes for next session
#
## General concept infos and reads:
# player has position attribute but is actually not yet in world.dict
# player can't be placed in world.dict immediately because nothing exists there initially
# 
# terrain generation fully relies on renderer
#
### ACTUAL GUIDE FOR NEXT SESSION:
#
##### Initial Spawn Process (to put player in world.dict)
# 1. generate from player spawn, use player.position to render and generate initial terrain
# 2. initial terrain is generated, place player in world.dict
##### Make New Renderer
# - render_initialization only renders terrain for initialization purposes
# - once player is in world.dict: use NEW RENDER FUNCTION (That you're gonna make)
# - NEW RENDER FUNCTION checks if theres entity,
# if there is, it renders entity, if there isn't it renders terrain.
##### Movement Gaming
# - Now that you render entity correctly and have the player in world.dict
# you can use the data in world.dict and finally move around. Goodluck

# final note-ultra important
# render_initialization shouldn't be a render method, it should be removed.
# initial terrain generation should be handled in the world object, still based on player spawn.
# its gonna be a new World method, only used after player object has been created.
# its gonna be like render_initialization but without printing.