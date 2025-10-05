

import sys





class Entity:
    def __init__(
            self,
            name = None,
            position = None,
            ):
        self.name = name
        self.position = position
        
        if self.position is None:
            print(f"Invalid entity position, fix NOWWWW")
            sys.exit()
        else:
            pass


class Player(Entity):
    def __init__(
            self,
            name = None,
            position = None,
            ):
        super().__init__(
            name,
            position,
            )
        

def test_Player():
    player = Player(
        "zuff",
        [0, 0]
        )
    print(player.name)
    print(player.position)


if __name__ == "__main__":
    test_Player()