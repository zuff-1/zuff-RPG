





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