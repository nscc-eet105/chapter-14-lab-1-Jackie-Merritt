#Jackie-Merritt_Chp14-Lab1_7/13/2025
#import vehicle as v
class V:
    def __init__(self):
        self.__current_speed = 0
        

    def decelerate(self):
        print("Decelerating...")
        self.__current_speed -= 1

    def accelerate(self):
        print("Accelerating...")
        self.__current_speed += 1

    def display_speed(self):
        print(f'Current speed: {self.__current_speed}')

def main():
    Vehicle = V()
    Vehicle.accelerate()
    Vehicle.display_speed()
    Vehicle.accelerate()
    Vehicle.display_speed()
    print()
    Vehicle.decelerate()
    Vehicle.display_speed()
    Vehicle.decelerate()
    Vehicle.display_speed()


main()



