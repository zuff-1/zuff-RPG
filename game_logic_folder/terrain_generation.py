

import random


class TerrainGeneration:
    
    def generate_tile():
        rng = random.random()
        if rng < 0.03:
            return "V"
        elif rng < 0.1:
            return "v"
        elif rng < 0.15:
            return ";"
        elif rng < 0.2:
            return ","
        else:
            return "."