1.将SHUMV_V2_0.py文件拷贝到openmv根目录。
2.import之后初始化即可使用，参考buzzer&laser_test.py
from SHUMV_V2_0 import Buzzer
from SHUMV_V2_0 import Laser

mybuzzer = Buzzer()
mybuzzer.init()#初始化
mylaser = Laser()
mylaser.init()#初始化

while(True):
    mybuzzer.off()#关
    mylaser.on()#开
