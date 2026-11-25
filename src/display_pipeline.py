import numpy as np
from dataclasses import dataclass

@dataclass
class DisplayRegisters:
    scx: int = 0          # Background X scroll (0-255)
    scy: int = 0          # Background Y scroll (0-255)
    wx: int = 7           # Window X position + 7 (7 = left edge)
    wy: int = 0           # Window Y position (0-143)
    lcdc_bg_enable: bool = True
    lcdc_win_enable: bool = True
    lcdc_obj_enable: bool = True

class DisplayFrameController:
    """
    Translates Tile-Map Memory (256x256) into an LCD Display Frame (160x144)
    using vectorized buffer operations compatible with GPU shader pipelines.
    """
    LCD_WIDTH = 160
    LCD_HEIGHT = 144
    MAP_SIZE = 256
    TILE_SIZE = 8

    def __init__(self):
        self.bg_canvas = np.zeros((self.MAP_SIZE, self.MAP_SIZE), dtype=np.uint8)
        self.win_canvas = np.zeros((self.MAP_SIZE, self.MAP_SIZE), dtype=np.uint8)
        self.obj_canvas = np.zeros((self.LCD_HEIGHT, self.LCD_WIDTH), dtype=np.uint8)

        self.bg_priority_map = np.zeros((self.MAP_SIZE, self.MAP_SIZE), dtype=np.uint8)
        self.oam_priority_map = np.zeros((self.LCD_HEIGHT, self.LCD_WIDTH), dtype=np.uint8)

        self.palette_rgba = np.array([,  # Index 0 (Lightest),  # Index 1,  # Index 2,  # Index 3 (Darkest)
        ], dtype=np.uint8)

    def load_tile_map(self, tile_map_32x32: np.ndarray, tile_data_table: dict, target: str = "BG"):
        """Decodes a 32x32 tile index grid into a 256x256 pixel canvas."""
        canvas = self.bg_canvas if target == "BG" else self.win_canvas
        for ty in range(32):
            for tx in range(32):
                tile_id = int(tile_map_32x32[ty, tx])
                tile_pixels = tile_data_table.get(tile_id, np.zeros((8, 8), dtype=np.uint8))
                y0, y1 = ty * self.TILE_SIZE, (ty + 1) * self.TILE_SIZE
                x0, x1 = tx * self.TILE_SIZE, (tx + 1) * self.TILE_SIZE
                canvas[y0:y1, x0:x1] = tile_pixels

    def render_lcd_frame(self, regs: DisplayRegisters) -> np.ndarray:
        """Composites Background, Window, and Object layers into a 160x144 RGBA8 frame."""
        if regs.lcdc_bg_enable:
            y_idx = (np.arange(self.LCD_HEIGHT) + regs.scy) % self.MAP_SIZE
            x_idx = (np.arange(self.LCD_WIDTH) + regs.scx) % self.MAP_SIZE
            bg_frame = self.bg_canvas[np.ix_(y_idx, x_idx)]
            bg_prio = self.bg_priority_map[np.ix_(y_idx, x_idx)]
        else:
            bg_frame = np.zeros((self.LCD_HEIGHT, self.LCD_WIDTH), dtype=np.uint8)
            bg_prio = np.zeros((self.LCD_HEIGHT, self.LCD_WIDTH), dtype=np.uint8)

        composited_indices = bg_frame.copy()
        win_x_start = regs.wx - 7
        win_y_start = regs.wy

        if regs.lcdc_win_enable and 0 <= regs.wx <= 166 and 0 <= regs.wy <= 143:
            win_line_counter = 0
            for screen_y in range(win_y_start, self.LCD_HEIGHT):
                if screen_y < 0:
                    continue
                draw_x_start = max(0, win_x_start)
                if draw_x_start < self.LCD_WIDTH:
                    width = self.LCD_WIDTH - draw_x_start
                    src_x_offset = draw_x_start - win_x_start
                    composited_indices[screen_y, draw_x_start:self.LCD_WIDTH] = (
                        self.win_canvas[win_line_counter, src_x_offset:src_x_offset + width]
                    )
                win_line_counter += 1

        if regs.lcdc_obj_enable:
            obj_visible = self.obj_canvas > 0
            bg_wins = (composited_indices > 0) & ((bg_prio == 1) | (self.oam_priority_map == 1))
            draw_obj = obj_visible & (~bg_wins)
            composited_indices = np.where(draw_obj, self.obj_canvas, composited_indices)

        return self.palette_rgba[composited_indices]

if __name__ == "__main__":
    controller = DisplayFrameController()
    sample_tile = np.tile(np.array(, dtype=np.uint8), (8, 1))
    tile_table = {1: sample_tile}
    tile_map = np.ones((32, 32), dtype=np.uint8)

    controller.load_tile_map(tile_map, tile_table, target="BG")
    regs = DisplayRegisters(scx=16, scy=8, wx=87, wy=100)
    frame = controller.render_lcd_frame(regs)
    print(f"LCD Frame Generated | Shape: {frame.shape} | Dtype: {frame.dtype}")
