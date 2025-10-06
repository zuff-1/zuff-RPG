

import sys





class Entity:
    def __init__(
            self,
            name = None,
            position = None,
            world = "overworld",
            sprite = "☺",
            ):
        self.name = name
        self.position = position
        self.world = world
        self.sprite = sprite
        
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
            world = "overworld",
            sprite = "☺",
            ):
        super().__init__(
            name,
            position,
            world,
            sprite,
            )
        

def test_Player():
    player = Player(
        "zuff",
        [0, 0],
        "overworld"
        )
    
    print(player.name)
    print(player.position)
    print(player.world)


if __name__ == "__main__":
    test_Player()