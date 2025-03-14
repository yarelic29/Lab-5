class Car:
    def __init__(self, head_lights: bool, tail_lights: bool,tires: int):
        self.head_lights = head_lights
        self.tail_lights = tail_lights
        self.tires = tires
        self.accessories = []

    def drive(self, location: str):
        return 'the car drives to ' +location + ' on ' + str(self.tires) + 'wheels!'
        
    def add_accessories(self, *args):
        for arg in args:
            self.accessories.append(arg)