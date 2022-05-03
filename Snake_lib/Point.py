import random

"""
Point 主要功能
    generate    生成，並不跟 snake 重複
"""


class Point:
    def __init__(self) -> None:
        self.__width, self.__high = 10, 10
        self.__xAxis, self.__yAxis = -1, -1
        self.__place = [self.__xAxis, self.__yAxis]

    def set_boundary(self, width: int = 10, high: int = 10) -> None:  # 設定界線
        self.__width = width
        self.__high = high

    def generate(self, bodyCoordinate: list[list]) -> None:  # 生成 point
        head = bodyCoordinate[0]  # 蛇頭
        block = 0  # 區塊
        if head <= self.__width // 2:
            block += 0
        else:
            block += 1
        if head <= self.__high // 2:
            block += 0
        else:
            block += 2
        """    
          2  |  3
        -----+-----
          0  |  1
        """

        selectBlock = (block + random.randint(1, 3)) % 4  # 選擇區塊， block 是蛇的頭所在區塊
        """
        亂數最大為 3 ，所以 tmp 最後不會是蛇頭在的區塊
        tmp = 2, randint = 3 -> tmp = (2 + 3) % 4 = 1
        """

        def random_select():
            """
            將地圖分為 4 塊，取亂數時只用 1/4 的地圖下去計算，再配對回去
            """
            xAxis = random.randint(0, self.__width // 2 - 1)
            yAxis = random.randint(0, self.__high // 2 - 1)

            if selectBlock == 0:  # 左下
                self.__xAxis, self.__yAxis = xAxis, yAxis
            elif selectBlock == 1:  # 右下
                self.__xAxis, self.__yAxis = xAxis + self.__width // 2, yAxis
            elif selectBlock == 2:  # 左上
                self.__xAxis, self.__yAxis = xAxis, yAxis + self.__high // 2
            elif selectBlock == 3:  # 右上
                self.__xAxis, self.__yAxis = (
                    xAxis + self.__width // 2,
                    yAxis + self.__high // 2,
                )

            self.__place = [self.__xAxis, self.__yAxis]

        while self.__place in bodyCoordinate:
            random_select()

    def get_place(self) -> list:  # 回傳位置
        return self.__place
