

import sys

import game_engine_folder.entity_manager as entity_manager
import game_logic_folder.terrain_generation as terrain_generation


class World:

    def __init__(
            self,
            name = "Default Name",
            ):
        self.name = name
        self.dict = {}

    def make_new_coordinate(
            self,
            cords_x,
            cords_y,
            ):
        self.dict[
            cords_x,
            cords_y,
            ] = {}
        
        self.dict[cords_x, cords_y,][
            "entity"
            ] = []
        self.dict[cords_x, cords_y,][
            "terrain"
            ] = []

    def assign_terrain(
            self,
            cords_x,
            cords_y,
            new_terrain,
            ):       
        self.dict[
            cords_x,
            cords_y,
            ][
            "terrain"
            ] = [
            new_terrain
            ]
    
    def generate_terrain(
            self,
            cords_x,
            cords_y,
            ):
        self.make_new_coordinate(
            cords_x,
            cords_y,
            )
        
        new_terrain = (
            terrain_generation.
            TerrainGeneration.
            generate_tile()
            )

        self.assign_terrain(
            cords_x,
            cords_y,
            new_terrain,
            )


    def initialize_world(
            self,
            player: entity_manager.Player,
            render_distance = 12,
            ):
        
        half = render_distance // 2

        for row in range(render_distance):
            print("")
            for column in range(render_distance):
                generate_target = [
                    player.position[0]
                    + (column - half),
                    player.position[1]
                    - (row - half),
                ]
                if tuple(generate_target) not in self.dict:
                    World.generate_terrain(self, *generate_target)
                else:
                    pass
    
    def assign_entity(
            self,
            entity: entity_manager.Entity,
            ):
        if not self.dict[
            tuple(entity.position)
            ][
            "entity"
            ]:
            self.dict[
                tuple(entity.position)
                ][
                "entity"
                ] = [entity]
        else:
            print("Theres already an entity on tile!!! fix NOWWWW")
            sys.exit()

