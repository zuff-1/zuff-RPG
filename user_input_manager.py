

import user_interface_folder.user_interface as user_interface





class UserInputManager:
    @staticmethod
    def player_movement(
            input
            ):
        if input == "w":
            return [0, 1]
        elif input == "a":
            return [-1, 0]
        elif input == "s":
            return [0, -1]
        elif input == "d":
            return [1, 0]
        else:
            (
            UserInputManager.
            input_safeguard
            )()
        
    def input_safeguard():
        while True:
            print("Invalid input, try again.")
            new_input = (
            user_interface.
            UserInterface.
            input_ui
            )
            return new_input
        
        pass