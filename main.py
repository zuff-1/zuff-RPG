

import random
import sys
import os
import time

import world_manager
import entity_manager
import user_interface
import renderer
import central_registry
import input_manager


def function_clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def function_enter_to_continue():
    return input("\nPress Enter to continue...")


class_object_overworld = central_registry.set_central_registry(
    "class_object_overworld",
    world_manager.class_world("Overworld")
)

class_object_player = central_registry.set_central_registry(
    "class_object_player",
    entity_manager.class_player("zuff")
)

class_object_renderer = central_registry.set_central_registry(
    "class_object_renderer",
    renderer.class_renderer(11)
)


def main_sequence():
    user_interface.class_user_interface.start_menu()
    while True:
        function_clear_screen()
        class_object_renderer.render_from_player(
            class_object_overworld,
            class_object_player)
        input_manager.class_player_input.gameplay_state_input()
        


main_sequence()