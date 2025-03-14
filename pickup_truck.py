from car import Car 


class pickup_truck(Car):
    def __init__(self,tires: int,weight: int, speed: int):
        super().__init__(True,True,tires, speed, 75)
        self.weight =weight
