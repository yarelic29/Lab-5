from pickup_truck import pickup_truck

class RamPickupTruck(RamPickupTruckickupTruck):
    def __init__(self, tires: int, weight: int, speed: int):
        super().__init__(tires, weight, 118)
        self.manufacturer = 'Ram'