from car import Car 


class PickupTruck(Car):
    def __init__(self, tires: int, weight: int):
        super().__init__(True,True,tires, 75)
        self.weight =weight
