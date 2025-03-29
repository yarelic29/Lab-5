from car import Car


class Porsche(Car):
    def __init__(self, automatic: bool, offroad: bool,speed):
        super().__init__(True, True, 4, 180)
        self.automatic = automatic
        self.offroad = offroad
        self.speed = speed