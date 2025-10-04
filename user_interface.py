

import os
import time


def function_clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def function_enter_to_continue():
    return input("\nPress Enter to continue...")


class class_user_interface:

    def start_menu():
        function_clear_screen()
        print("Welcome to zuff RPG!")
        print("")
        print("Inputs:")
        print("")
        print("- wasd to move")
        print("- /exit")
        print("")
        function_enter_to_continue()

    def gameplay_state_ui():
        print ("Input: ", end="")
        user_input = input()
        return user_input

    def invalid_input():
        print("Invalid input, try again. (2s)", end="\r")
        time.sleep(2)
        print(" " * 100, end="\r")