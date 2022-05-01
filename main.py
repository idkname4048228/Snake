import os
import time
import keyboard


from Snake_lib.Map import Map
from Snake_lib.Snake import Snake
from Snake_lib.Point import Point


def main():
    testSnake = Snake(5, 3, [0, 9])
    testPoint = Point()

    testMap = Map(testSnake, testPoint)
    
    direction = 0

    testSnake.change_direction(direction)

    def loop():
        while testSnake.long != 10 and testSnake.alive:
            testSnake.unit_move()
            testMap.is_snake_die()
            if not(testSnake.alive):
                break

            testMap.display()
            time.sleep(0.2)
            os.system("cls")
            testMap.is_snake_die()

        if testSnake.long == 10:
            print("Goal!!")
        else:
            print("Death")

    def change_direction_by_keyboard(pressKey):
        global direction
        if pressKey.event_type == 'down' and pressKey.name == 'right' and testSnake.directionCode != 2:
            direction = 0
            testSnake.change_direction(direction)

        if pressKey.event_type == 'down' and pressKey.name == 'down' and testSnake.directionCode != 3:
            direction = 1
            testSnake.change_direction(direction)

        if pressKey.event_type == 'down' and pressKey.name == 'left' and testSnake.directionCode != 0:
            direction = 2
            testSnake.change_direction(direction)

        if pressKey.event_type == 'down' and pressKey.name == 'up' and testSnake.directionCode != 1:
            direction = 3
            testSnake.change_direction(direction)

    keyboard.hook(change_direction_by_keyboard)

    loop()


if __name__ == '__main__':
    main()

