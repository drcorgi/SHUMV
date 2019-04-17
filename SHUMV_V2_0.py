from pyb import Pin
class Buzzer:
    def init(self):
    #初始化
        MyMapperDict= {'Buzzer' : Pin.cpu.E2}
        Pin.dict(MyMapperDict)#映射引脚使用cpu的PE2
        self.pin = Pin('Buzzer',Pin.OUT_PP)

    def on(self):
    #开
        self.pin.value(1)
    def  off(self):
    #关
        self.pin.value(0)


class Laser:
    def init(self):
    #初始化
        MyMapperDict= {'Laser' : Pin.cpu.C2}
        Pin.dict(MyMapperDict)#映射引脚使用cpu的PC2
        self.pin = Pin('Laser',Pin.OUT_PP)

    def on(self):
    #开
        self.pin.value(1)
    def  off(self):
    #关
        self.pin.value(0)

