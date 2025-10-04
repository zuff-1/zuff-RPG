
import user_interface
import central_registry
import entity_manager

class class_player_input:

    def gameplay_state_input():
        while True:
            user_input = user_interface.class_user_interface.gameplay_state_ui()
            player_object = central_registry.central_registry["class_object_player"]
            if user_input == "w":
                entity_manager.class_entitiy_behavior.entity_move(player_object, 0, 1)
            elif user_input == "a":
                entity_manager.class_entitiy_behavior.entity_move(player_object, -1, 0)
            elif user_input == "s":
                entity_manager.class_entitiy_behavior.entity_move(player_object, 0, -1)
            elif user_input == "d":
                entity_manager.class_entitiy_behavior.entity_move(player_object, 1, 0)
            else:
                user_interface.class_user_interface.invalid_input()
                pass