import board, neopixel, time

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10)
GREEN = (0, 255, 0)
WHITE = (255,255,255)
ORANGE = (255, 165, 0)
BLACK = (0, 0, 0)
RED = (255,0,0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
INDIGO = (75,0,130)
VIOLET = (143, 0, 255)

while True:
    pixels.fill(RED)
    time.sleep(0.2)
    pixels.fill(ORANGE)
    time.sleep(0.2)
    pixels.fill(YELLOW)
    time.sleep(0.2)
    pixels.fill(GREEN)
    time.sleep(0.2)
    pixels.fill(BLUE)
    time.sleep(0.2)
    pixels.fill(INDIGO)
    time.sleep(0.2)
    pixels.fill(VIOLET)
    time.sleep(0.2)
    pixels.fill(BLACK)
    time.sleep(0.2)
    pixels.fill(WHITE)
    time.sleep(0.2)