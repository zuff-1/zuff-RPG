

import sys

import central_registry



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

    def change_location(
            self,
            target_position,
            ):
        world = (
        central_registry.
        central_registry[self.world]
        )
        obj = world.dict[
            tuple(self.position)
            ][
            "entity"
            ].pop()
        
        world.dict[
            tuple(target_position)
            ][
            "entity"
            ].append(obj)
        self.position = target_position


class Player(Entity):
    def __init__(
            self,
            name = "Default Name",
            position = None,
            world = "Default World",
            sprite = "Default Sprite",
            ):
        super().__init__(
            name,
            position,
            world,
            sprite,
            )
        
    def move(self, dx, dy):
        target_position = [
            self.position[0] + dx,
            self.position[1] + dy,
            ]
        Entity.change_location(
            self,
            target_position,
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
    pass