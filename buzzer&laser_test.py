
import time
import pyb
from pyb import LED
from pyb import Pin
from SHUMV_V2_0 import Buzzer
from SHUMV_V2_0 import Laser


mybuzzer = Buzzer()
mybuzzer.init()
mylaser = Laser()
mylaser.init()

while(True):
    mybuzzer.off()
    mylaser.on()

