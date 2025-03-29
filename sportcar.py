from car import Car 


class Sportscar(Car):
    def __init__(self, body:str, automatic: bool,speed):
        super().__init__(True, True, 4, 200)
        self.body = body
        self.automatic = automatic
        self.speed = speed

    def __str__(self):
        return f'body: {self.body}, tires: {str(self.tires)},accessories: {str(self.accessories)}'