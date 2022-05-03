import random
"""
protal 功能
    生成 protal

"""

class Protal():
    def __init__(
        self
    ) -> None:
        self.__sideline, self.__placeIndex = -1, -1
        """
            1
        0   +   2
            3
        """
        self.__width, self.__high = 10, 10
    
    def set_boundary(self, width: int = 10, high: int = 10) -> None:
        self.__width = width
        self.__high = high

    def generate(self) -> None:
        line = random.randint(0, 3)
        if line % 2:
            placeIndex = random.randint(0, self.__width - 1)
        else:
            placeIndex = random.randint(0, self.__high - 1)

        


