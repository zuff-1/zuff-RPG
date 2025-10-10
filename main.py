

import sys
import os

import central_registry
import game_engine_folder.world_manager as world_manager
import entity_manager
import renderer_2d
import user_interface_folder.user_interface as user_interface
import user_input_manager



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
            "☺",
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

world, player, renderer = create_define_all_object()




def test_initialization():
    world_manager.World.initialize_world(
        world,
        player,
        renderer.render_distance
        )
    world_manager.World.assign_entity(world, player)
    print("")
    print("w,a,s,d is the command to move around")
    print("/done is the command to exit")
    print("")
    input("Press Enter to Continue...")

    while True:
        function_clear_screen()
        renderer_2d.Renderer.render_from_player(renderer, player, world)
        print("")
        user_input = (
            user_interface.
            UserInterface.
            input_ui()
            )
        
        if user_input == "/done":
            sys.exit()

        delta_coords = (
            user_input_manager.
            UserInputManager.
            player_movement(
                user_input
                )
            )
        player.move(
            delta_coords[0], 
            delta_coords[1],
            )




test_initialization()




