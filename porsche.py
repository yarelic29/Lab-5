from car import Car


class porsche(Car):
    def __init__(self,speed: int, automatic: bool, offroad: bool):
        super().__init__(True,True,4)
        self.speed = speed
        self.automatic = automatic
        self.offroad = offroad