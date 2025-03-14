from car import Car
from sportcar import Sportscar 

if __name__ == '__main__':
    print('new dawn,new day')
    my_car = Car(True,True, 4)
    print('acessories:' +str(my_car.accessories))
    my_car.add_accessories('dashcam', 'leather interior', 'tinted windows','hula girl')
    print('accessories: ' + str(my_car.accessories))

    my_sportscar = Sportscar('red', True)
    print(my_sportscar)