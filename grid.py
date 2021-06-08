import pygame, constants

class Grid:
    def __init__(self, surface, pos, color, cell_size, scale):
        self.surface = surface
        self.pos_x, self.pos_y = pos
        self.color = color
        self.cell_size = cell_size

        self.scale = scale

        self.grid_width, self.grid_height = None, None
        self.nGridRows, self.nGridColumns = 0, 0

    def draw(self, rows, columns):
        self.grid_height, self.grid_width = rows* self.cell_size, columns* self.cell_size

        self.nGridRows, self.nGridColumns = rows, columns
        
        # rows
        for i in range(rows + 1):
            y = self.pos_y + (i* self.cell_size)
            pygame.draw.line(self.surface, self.color, [self.pos_x, y], [self.pos_x + self.grid_width, y])

        # columns
        for j in range(columns + 1):
            x = self.pos_x + (j* self.cell_size)
            pygame.draw.line(self.surface, self.color, [x, self.pos_y], [x, self.pos_y + self.grid_height])

    def zoom_out(self):
        self.cell_size -= 0.4

    def zoom_in(self):
        self.cell_size += 0.4

    def panOnMouseMotion(self, offSet, mousePos):
        mouse_x, mouse_y = mousePos
        offset_x, offset_y = offSet

        self.pos_x = mouse_x - offset_x
        self.pos_y = mouse_y - offset_y
