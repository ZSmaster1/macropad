import board
import busio
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation

from kmk.modules.encoder import EncoderHandler

from kmk.extensions.display import Display, TextEntry
from kmk.extensions.display.ssd1306 import SSD1306

from kmk.extensions.RGB import RGB

keyboard = KMKKeyboard()

keyboard.col_pins = (board.D0, board.D1, board.D2)
keyboard.row_pins = (board.D3, board.D6, board.D7)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

#encoder

encoder_handler = EncoderHandler()

encoder_handler.pins = (
    (board.D8, board.D9),
)

encoder_handler.map = [
    ((KC.VOLD, KC.VOLU, None),),
]

keyboard.modules.append(encoder_handler)

#oled

i2c = busio.I2C(board.SCL, board.SDA)

display = Display(
    display=SSD1306(
        i2c=i2c,
        device_address=0x3C,
    ),
    width=128,
    height=64,
    dim_time=0,
)

display.entries = [
    TextEntry(text="MacroPad"),
]

keyboard.extensions.append(display)

#rgb

rgb = RGB(pixel_pin=board.D10, num_pixels=27)
keyboard.extensions.append(rgb)

#keymap

keyboard.keymap = [
    [KC.RGB_TOG, KC.RGB_HUI, KC.RGB_HUD], 
    [KC.RGB_MODE_SWIRL, KC.N5, KC.N6], 
    [KC.N1, KC.N2, KC.N3] 
]

if __name__ == "__main__":
    keyboard.go()
