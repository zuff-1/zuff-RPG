

import user_interface_folder.user_interface as user_interface





class UserInputManager:
    @staticmethod
    def player_movement(
            user_input
            ):
        valid = [
            "w",
            "a",
            "s",
            "d",
            ]
        user_input = (
        UserInputManager.
        input_safeguard(
            valid,
            user_input,
            "Invalid input, use w,a,s,d.",
            )
        )
        input_map = {
            "w": [0, 1],
            "a": [-1, 0],
            "s": [0, -1],
            "d": [1, 0],
            }
        return input_map[user_input]


    def input_safeguard(
            valid_inputs,
            user_input,
            invalid_prompt = "Invalid input, try again.",
            ):
        if user_input in valid_inputs:
            return user_input
        else:
            while True:
                print(invalid_prompt)
                new_input = (
                user_interface.
                UserInterface.
                input_ui()
                )
                if new_input in valid_inputs:
                    return new_input