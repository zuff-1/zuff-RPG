


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
        for row in range(self.render_distance):
            print("")
            for column in range(self.render_distance):
                render_target = [
                    player.position[0]
                    + (column - (((self.render_distance+1)//2)-1)),
                    player.position[1]
                    + (row - (((self.render_distance+1)//2)-1))
                ]
                if tuple(render_target) not in world.dict:
                    world.assign_new_terrain(*render_target)
                    
                    print(
                        world.dict
                        [tuple(render_target)]
                        ["terrain"]
                        [0],
                        end = "")
                else:
                    print(
                        world.dict
                        [tuple(render_target)]
                        ["terrain"]
                        [0],
                        end = "")

    
