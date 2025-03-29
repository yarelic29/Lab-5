from pickup_truck import PickupTruck

class RamPickupTruck():
    def __init__(self, tires: int, weight: int):
        super().__init__(tires, weight, 118)
        self.manufacturer = 'Ram'