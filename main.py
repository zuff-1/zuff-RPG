

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


def test_renderer():
    world, player, renderer = create_define_all_object()
    renderer.render_from_player(player, world)

test_renderer()