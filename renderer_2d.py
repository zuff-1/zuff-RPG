


import world_manager
import entity_manager


class Renderer:

    def __init__(
            self,
            render_distance,
            ):
        self.render_distance = render_distance
    
    def render_from_player(
            self,
            player: entity_manager.Player,
            world: world_manager.World,     
            ):
        
        half = self.render_distance // 2

        for row in range(self.render_distance):
            print("")
            for column in range(self.render_distance):
                render_target = [
                    player.position[0] + (column - half),
                    player.position[1] - (row - half),
                ]
                if tuple(render_target) not in world.dict:
                    world.assign_new_terrain(*render_target)
                else:
                    pass
                if not(
                    world.dict
                    [tuple(render_target)]
                    ["entity"]
                    ): 
                    text = (
                        world.dict
                        [tuple(render_target)]
                        ["terrain"]
                        [0],
                        )
                    text = text[0]
                    print(text.center(2), end = "")
                else:
                    text = (
                        world.dict
                        [tuple(render_target)]
                        ["entity"]
                        [0].sprite
                        )
                    text = text[0]
                    print(text.center(2), end = "")