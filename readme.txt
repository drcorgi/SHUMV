1.��SHUMV_V2_0.py�ļ�������openmv��Ŀ¼��
2.import֮���ʼ������ʹ�ã��ο�buzzer&laser_test.py
from SHUMV_V2_0 import Buzzer
from SHUMV_V2_0 import Laser

mybuzzer = Buzzer()
mybuzzer.init()#��ʼ��
mylaser = Laser()
mylaser.init()#��ʼ��

while(True):
    mybuzzer.off()#��
    mylaser.on()#��
