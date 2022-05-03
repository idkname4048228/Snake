import time
import random
from Snake_lib.Snake import Snake
from Snake_lib.Protal import Protal
from Snake_lib.Point import Point
"""
Map 主要功能:
    display 展示全地圖
    
    component 有 Snake, Protal, Point
    附加功能
        set_boundary_to_snake   讓 snake 知道界線
        set_point_to_snake  讓 snake 知道 point 座標

        is_snake_in_protal  判斷 snake 是否在 protal 裡面
        reduce_protalTime   減少 protalTime
    
    
"""
class Map:
    def __init__(
        self, width: int = 10, high: int = 10
    ) -> None:
        # 邊界預設皆為 10
        self.__width = width
        self.__high = high

    def set_snake(self, snake: Snake = None) -> None:   # 設定 Snake
        snake.set_boundary(self.__width, self.__high)
        self.__snake = snake
    
    def set_protal(self, protal: Protal = None) -> None:    # 設定 Protal
        protal.set_boundary(self.__width, self.__high)
        self.__protal = protal
    
    def set_point(self, point: Point = None) -> None:   #設定 Point
        point.set_boundary(self.__width, self.__high)
        self.__point = point

    def generate_point(self) -> None:   # 叫 Point 產生
        bodyCoordinate = self.__snake.get_body()
        self.__point.generate(bodyCoordinate = bodyCoordinate)
        tmpPlace = self.__point.get_place
        self.__snake.set_point(tmpPlace)    #設定 Snake 的 Point 座標
    
    def generate_protal(self) -> None:  #叫 Protal 產生
        self.__protal.generate()    # 產生
        long = self.__snake.get_long
        self.__protalTime = random.randint(long, long + 10) # 設定 protalTime

        self.__snake.set_protal(self.__protal.get_inter_coordinate(), self.__protal.get_exit_coordinate())  # 讓 Snake 知道 Protal 的座標

        # 將 Protal 座標化
        protal = self.__protal.get_inter_coordinate()
        self.__interProtal = self.__convert_protal_to_coordinate(protal)
        protal = self.__protal.get_exit_coordinate()
        self.__exitProtal = self.__protal.get_exit_coordinate(protal)
        
    def __convert_protal_to_coordinate(
        self, protal: list = None
    ) -> list:  # 將傳送門轉換為座標系
        if protal[0] == 0:  # sideline為 0 時，protal[1]是y軸
            tmp = [-1, protal[1]]

        elif protal[0] == 1:  # sideline為 1 時，protal[1]是x軸
            tmp = [protal[1], self.__high]

        elif protal[0] == 2:  # sideline為 2 時，protal[1]是y軸
            tmp = [self.__width, protal[1]]

        elif protal[0] == 3:  # sideline為 3 時，protal[1]是x軸
            tmp = [protal[1], -1]
        return tmp
    
    def reduce_protalTime(self) -> None:    # protalTime 倒計時，檢查 Snake 是否會死
        time.delay(1)
        self.__protalTime -= 1
        if self.__protalTime == 0:
            if self.__snake.body_in_protal():
                self.__snake.set_alive(False)   #死了
            self.__protal.close()
            self.__interProtal = None
            self.__exitProtal = None

            delayTime= random.randint(0, 5)
            time.sleep(delayTime)
            self.generate_protal

    def display(self) -> None:
        map = []
        for xAxis in range(self.__width):
            map.append([])
            for yAxis in range(self.__high):
                map[xAxis].append(0)

        bodyCoordinate = self.__snake.get_body()
        pointPlace = self.__point.get_place()

        for coordinate in bodyCoordinate:
            map[coordinate[0]][coordinate[1]] = 1
        
        map[pointPlace[0]][pointPlace[1]] = 'O'

        print(" __", end = '')  # 最上右
        for top in range(self.__width):
            if self.__interProtal == [self.__high, top]:    # 入口protal
                print("(i)", end = '')
            elif self.__exitProtal == [self.__high, top]:   # 出口protal
                print("(o)", end = '')
            else:
                print("___", end = '')                # 牆壁
        print("__ ")    #最上左


        for yAxis in range(self.__high, -1, -1):
            # 左界線
            if self.__interProtal == [-1, yAxis]:
                print("(i)", end = '')
            elif self.__exitProtal == [-1, yAxis]:
                print("(o)", end = '')
            print(" | ", end ='')

            # 主體
            for xAxis in range(self.__width):
                if xAxis != 0:
                    print(" ", xAxis, sep = '', end = ' ')
                else:
                    print("   ", end = '')
            
            # 右界線
            if self.__interProtal == [self.__width, yAxis]:
                print("(i)")
            elif self.__exitProtal == [self.__width, yAxis]:
                print("(o)")
            print(" | ")

        print(" ¯¯", end = '')  # 最下右
        for top in range(self.__width):
            if self.__interProtal == [self.__high, top]:    # 入口protal
                print("(i)", end = '')
            elif self.__exitProtal == [self.__high, top]:   # 出口protal
                print("(o)", end = '')
            else:
                print("¯¯¯", end = '')                # 牆壁
        print("¯¯ ")    #最下左
