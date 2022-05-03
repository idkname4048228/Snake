import random

"""
protal 功能
    generate    生成 protal
    close   關閉 protal
"""


class Protal:
    def __init__(self) -> None:
        self.__sideline, self.__placeIndex = -1, -1
        """
            1
        0   +   2
            3
        """
        self.__width, self.__high = 10, 10

        self.__place = [self.__sideline, self.__placeIndex]

    def set_boundary(self, width: int = 10, high: int = 10) -> None:  # 設定界線
        self.__width = width
        self.__high = high

    def generate(self) -> None:  # 生成 protal
        self.__sideline = random.randint(0, 3)  # 隨機取 sideline

        if self.__sideline % 2:  # 如果是奇數，生成X軸的座標
            self.__placeIndex = random.randint(0, self.__width - 1)
        else:  # 如果是偶數，生成Y軸的座標
            self.__placeIndex = random.randint(0, self.__high - 1)

        self.__place = [self.__sideline, self.__placeIndex]

    def get_coordinate(self) -> list:  # 回傳座標
        return self.__place
