### librarys ###

from sense_hat import SenseHat
from time import sleep

### varibles ###

sh = SenseHat()
running = True
last_value = 0
current_value = 0
hard_stops = 0
hard_accels = 0

### main program ###

while running:
    sh.clear(0, 255, 0)
    last_value = current_value
    current_value = sh.accel_raw['y']
    if current_value <= last_value / 2:
        sh.clear(255, 0, 0)
        hard_stops = hard_stops + 1
    sleep(1)
