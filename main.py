"""
for i in range(snake.step):
    snake.move
    if snake.have_eaten_point:
        map.generate_point()
"""


import os
import time
import keyboard
import threading


from Snake_lib.Map import Map, Snake


def main():
    testSnake = Snake(1, 3, [0, 9])

    testMap = Map(testSnake, testPoint)

    direction = 0

    testSnake.change_direction(direction)

    testMap.set_protal()

    def reduce_protalTime():
        while testSnake.alive:
            time.sleep(1)
            testMap.reduce_protalTime()

    def loop():
        while testSnake.long != 30 and testSnake.alive:
            testSnake.move()
            testMap.is_snake_die()
            if not (testSnake.alive):
                break

            testMap.display()
            time.sleep(0.4)
            os.system("cls")

        if testSnake.long == 10:
            print("Goal!!")
        else:
            print("Death")

    def change_direction_by_keyboard(pressKey):
        global direction
        if pressKey.event_type == "down" and pressKey.name == "shift":
            if testSnake.step < 5:
                testSnake.step += 1
        elif pressKey.event_type == "down" and pressKey.name == "right shift":
            if testSnake.step > 1:
                testSnake.step -= 1

        elif (
            pressKey.event_type == "down"
            and pressKey.name == "right"
            and testSnake.directionCode != 2
        ):
            direction = 0
            testSnake.change_direction(direction)

        elif (
            pressKey.event_type == "down"
            and pressKey.name == "down"
            and testSnake.directionCode != 3
        ):
            direction = 1
            testSnake.change_direction(direction)

        elif (
            pressKey.event_type == "down"
            and pressKey.name == "left"
            and testSnake.directionCode != 0
        ):
            direction = 2
            testSnake.change_direction(direction)

        elif (
            pressKey.event_type == "down"
            and pressKey.name == "up"
            and testSnake.directionCode != 1
        ):
            direction = 3
            testSnake.change_direction(direction)

    keyboard.hook(change_direction_by_keyboard)

    thread_reduce = threading.Thread(target=reduce_protalTime)  # 例項化一個執行緒物件，使執行緒執行這個函式
    thread_loop = threading.Thread(target=loop)  # 例項化一個執行緒物件，使執行緒執行這個函式

    thread_reduce.start()
    thread_loop.start()

    thread_reduce.join()
    thread_loop.join()


if __name__ == "__main__":

    main()
