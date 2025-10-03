import msvcrt

while True:
    if msvcrt.kbhit():
        key = msvcrt.getch().decode("utf-8").lower()
        if key == "w":
            print("Up")
        elif key == "s":
            print("Down")
        elif key == "a":
            print("Left")
        elif key == "d":
            print("Right")