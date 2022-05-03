import random

"""
protal 功能
    generate    生成 protal
    close   關閉 protal
"""


class Protal:
    def __init__(self) -> None:
        self.__interSideline, self.__interPlaceIndex = -1, -1
        self.__exitSideline, self.__exitPlaceIndex = -1, -1
        """
            1
        0   +   2
            3
        """
        self.__width, self.__high = 10, 10

        self.__interProtal = [self.__interSideline, self.__interPlaceIndex]
        self.__exitProtal = [self.__exitSideline, self.__exitPlaceIndex]

    def set_boundary(self, width: int = 10, high: int = 10) -> None:  # 設定界線
        self.__width = width
        self.__high = high

    def generate(self) -> None:  # 生成 protal
        # 入口
        self.__interSideline = random.randint(0, 3)  # 隨機取 sideline

        if self.__interSideline % 2:  # 如果是奇數，生成X軸的座標
            self.__interPlaceIndex = random.randint(0, self.__width - 1)
        else:  # 如果是偶數，生成Y軸的座標
            self.__interPlaceIndex = random.randint(0, self.__high - 1)

        self.__interProtal = [self.__interSideline, self.__interPlaceIndex]

        self.__exitProtal = self.__interProtal
        while self.__exitProtal == self.__interProtal:
            # 出口
            self.__exitSideline = random.randint(0, 3)  # 隨機取 sideline

            if self.__exitSideline % 2:  # 如果是奇數，生成X軸的座標
                self.__exitPlaceIndex = random.randint(0, self.__width - 1)
            else:  # 如果是偶數，生成Y軸的座標
                self.__exitPlaceIndex = random.randint(0, self.__high - 1)

            self.__exitProtal = [self.__exitSideline, self.__exitPlaceIndex]

    def get_inter_coordinate(self) -> list:  # 回傳入口座標
        return self.__interProtal

    def get_exit_coordinate(self) -> list:  # 回傳出口座標
        return self.__exitProtal

    def close(self) -> None:  # 傳送門關閉
        self.__interSideline, self.__interPlaceIndex = -1, -1
        self.__exitSideline, self.__exitPlaceIndex = -1, -1
        self.__interProtal = [self.__interSideline, self.__interPlaceIndex]
        self.__exitProtal = [self.__exitProtal, self.__exitPlaceIndex]
