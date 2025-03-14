from car import Car 


class pickup_truck(Car):
    def __init__(self,tires: int,weight: int):
        super().__init__(True,True,tires)
        self.weight =weight
