from car import Car
from sportcar import Sportscar 

if __name__ == '__main__':
    print('new dawn,new day')
    my_car = Car(True,True, 4, 100)
    print('acessories:' +str(my_car.accessories))
    my_car.add_accessories('dashcam', 'leather interior', 'tinted windows','hula girl')
    print('accessories: ' + str(my_car.accessories))

    my_sportscar = Sportscar('red', True,200)
    print(my_sportscar)

    race = []
    race.append(my_car)
    race.append(my_sportscar)
    