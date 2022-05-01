import os
import time
import threading

from Snake_lib.Map import Map
from Snake_lib.Snake import Snake
from Snake_lib.Point import Point


def main():
    testSnake = Snake(5, 0, [0, 9])
    testPoint = Point()

    testMap = Map(testSnake, testPoint)

    direction = 0

    testSnake.change_direction(direction)

    def loop():
        while True:
            if testSnake.unit_move():
                testMap.display()
                time.sleep(0.2)
                os.system("cls")
            else:
                return False

    def change_direction_by_keyborad():
        inputValue = int(input()) % 4
        
        while True:

            testSnake.change_direction(inputValue)
            inputValue = int(input()) % 4

    thread_1 = threading.Thread(target=loop)  # 例項化一個執行緒物件，使執行緒執行這個函式
    thread_2 = threading.Thread(target=change_direction_by_keyborad)  # 例項化一個執行緒物件，使執行緒執行這個函式


    thread_1.start()  # 啟動這個執行緒
    thread_2.start()  # 啟動這個執行緒
    thread_1.join()  # 等待thread_1結束，如果不打join程式會直接往下執行
    thread_2.join()  # 等待thread_2結束，如果不打join程式會直接往下執行


if __name__ == '__main__':
    main()
