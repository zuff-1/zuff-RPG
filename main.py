

import time
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


    for i in range(200):
        function_clear_screen()
        entity_manager.Entity.change_location(player, [i, 0])
        renderer_2d.Renderer.render_from_player(renderer, player, world)
        time.sleep(0.1)


test_initialization()




