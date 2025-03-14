from pickup_truck import pickup_truck

class RamPickupTruck(PickupTruck):
    def __init__(self, tires: int, weight: int):
        super().__init__(tires, weight )
        self.manufacturer = 'Ram'