"""
main 要做的事
    Snake, Map 之間的橋樑
    Snake 換檔
    Snake 吃 Point 跟 Map 講
    Snake 進 Protal 跟 Map 講


for i in range(snake.step):
    snake.move
    if snake.have_eaten_point:
        map.generate_point()
"""


import os
import time
import keyboard
import threading


from Snake_lib.Map import Map
from Snake_lib.Snake import Snake
from Snake_lib.Point import Point
from Snake_lib.Protal import Protal


def main():
    testSnake = Snake(1, 0, [0, 3])
    testPoint = Point()
    testProtal = Protal()
    testMap = Map()

    testMap.set_snake(testSnake)
    testMap.set_point(testPoint)
    testMap.set_protal(testProtal)

    testMap.generate_point()
    testMap.generate_protal()

    goal = 10

    def reduce_protalTime():
        while testSnake.is_alive():
            testMap.reduce_protalTime()

    def loop():
        while testSnake.get_long() != goal:
            for _ in range(testSnake.get_step()):
                testSnake.move()
                if testSnake.is_alive():
                    if testSnake.need_genarate_point():
                        testMap.generate_point()
                else:
                    return None

            testMap.display()
            print(testSnake.get_step())
            time.sleep(0.4)
            os.system("cls")

    def game():
        loop()
        if testSnake.get_long() == goal:
            print("Goal!!")
        else:
            print("Death")
        return None


    def change_direction_by_keyboard(pressKey):
        global step
        if pressKey.event_type == "down" and pressKey.name == "shift":
            testSnake.speed_up()
            print(testSnake.get_step())

        elif pressKey.event_type == "down" and pressKey.name == "right shift":
            testSnake.speed_down()
            print(testSnake.get_step())

        elif (
            pressKey.event_type == "down"
            and pressKey.name == "right"
            and testSnake.get_direction != 2
        ):
            testSnake.change_direction(0)

        elif (
            pressKey.event_type == "down"
            and pressKey.name == "down"
            and testSnake.get_direction != 3
        ):
            testSnake.change_direction(1)

        elif (
            pressKey.event_type == "down"
            and pressKey.name == "left"
            and testSnake.get_direction != 0
        ):
            testSnake.change_direction(2)

        elif (
            pressKey.event_type == "down"
            and pressKey.name == "up"
            and testSnake.get_direction != 1
        ):
            testSnake.change_direction(3)

    keyboard.hook(change_direction_by_keyboard)

    thread_reduce = threading.Thread(target=reduce_protalTime)  # 例項化一個執行緒物件，使執行緒執行這個函式
    thread_loop = threading.Thread(target=game)  # 例項化一個執行緒物件，使執行緒執行這個函式

    thread_reduce.start()
    thread_loop.start()

    thread_reduce.join()
    thread_loop.join()


if __name__ == "__main__":

    main()
