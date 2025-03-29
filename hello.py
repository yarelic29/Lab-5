from car import Car
from sportcar import Sportscar 
from pickup_truck import PickupTruck
from porsche import Porsche

if __name__ == '__main__':
    print('new dawn,new day')
    my_car = Car(True,True, 4, 100)
    print('acessories:' +str(my_car.accessories))
    my_car.add_accessories('dashcam', 'leather interior', 'tinted windows','hula girl')
    print('accessories: ' + str(my_car.accessories))

    my_sportscar = Sportscar('red', True,200)
    print(my_sportscar)

    my_pickup = PickupTruck(True,True, 75)
    print(my_pickup)

    my_porsche = Porsche(True, False, 120)
    print(my_porsche)

    race = []
    race.append(my_car)
    race.append(my_sportscar)
    race.append(my_porsche)
    race.append(my_pickup)

    winner = None
    current_speed = 0
    for car in race:
        if car.speed > current_speed:
            winner = car

    print('The winner is ' + str(type(winner)))
    