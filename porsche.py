from car import Car


class porsche(Car):
    def __init__(self, automatic: bool, offroad: bool, speed: int):
        super().__init__(True,True,4, speed, 215)
        self.automatic = automatic
        self.offroad = offroad
        self.speed = speed 