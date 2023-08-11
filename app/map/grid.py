from app.map.tile import Tile   

class Grid():

    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.selected_unit = None
        self.grid = self.create_grid(self.rows, self.columns)

    def create_grid(self, rows, columns):
        grid = []
        for i in range(rows):
            line = []
            for j in range(columns):
                line.append(Tile(i, j, 16, 16))
            grid.append(line)
        return grid

    def get_tile_from_pos(self, pos):
        for tile in self.grid:
            if (tile.x, tile.y) == (pos[0], pos[1]):
                return tile

    def get_unit_from_pos(self, pos):
        return self.get_tile_from_pos.occupying_unit

    def draw(self, display):
        for row in self.grid:
            for tile in row:
                tile.draw(display)
