import time
import random
from Snake_lib.Snake import Snake
from Snake_lib.Protal import Protal
from Snake_lib.Point import Point
"""
Map 主要功能:
    display 展示全地圖
    generate_point  生成點數
    
    component 有 Snake, Protal
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

        # point 相關設定
        self.__xAxisOfPoint = 0
        self.__yAxisOfPoint = 0
        self.__placeOfPoint = [self.__xAxisOfPoint, self.__yAxisOfPoint]

    def set_snake(self, snake: Snake = None) -> None:
        snake.set_boundary(self.__width, self.__high)
        self.__snake = snake
    
    def set_protal(self, protal: Protal = None) -> None:
        protal.set_boundary(self.__width, self.__high)
        self.__protal = protal

    def generate_point(self):
        head = self.__snake.__head
        

""
class Map:
    def __init__(
        self, width: int = 10, hight: int = 10
    ):
        self.widthLimit = width
        self.hightLimit = hight
        self.middleOfWidth = self.widthLimit // 2  # 為了亂數
        self.middleOfHight = self.hightLimit // 2

        self.x_axis = 0
        self.y_axis = 0
        self.pointPlace = [self.x_axis, self.y_axis]

        self.block_init()
        self.generate_point()

        self.inProtal = [-1, -1]
        self.outProtal = [-1, -1]
        self.protalTime = 0

    # 傳送門(預想)
    def set_protal(self):
        block = random.randint(0, 3)
        """
            1
        0   +   2
            3
        """
        if block % 2:
            place = random.randint(0, self.middleOfWidth - 1)
        else:
            place = random.randint(0, self.middleOfHight - 1)
        self.inProtal = [block, place]

        block = random.randint(0, 3)  # 設定出口座標，不跟入口重複
        while place == self.inProtal[1]:
            if block % 2:
                place = random.randint(0, self.middleOfWidth - 1)
            else:
                place = random.randint(0, self.middleOfHight - 1)
        self.outProtal = [block, place]

        self.protalTime = random.randint(self.snake.long, self.snake.long + 10)

    def reduce_protalTime(self):
        self.protalTime -= 1
        if self.protalTime == 0:

            self.inProtal, self.outProtal = [-1, -1], [-1, -1]
            delay_time = random.randint(0, 5)
            time.sleep(delay_time)
            self.set_protal()

    def set_snake(self, snake: Snake):
        self.snake = snake

    def is_snake_die(self) -> None:
        headCoordinate = self.snake.coordinate[0]
        if (
            headCoordinate[0] >= self.widthLimit
            or headCoordinate[1] >= self.hightLimit
            or headCoordinate[0] < 0
            or headCoordinate[1] < 0
        ):
            self.snake.set_alive(False)  # 死了
            print("Wall")
        elif self.snake.inProtal and self.protalTime == 0:
            self.snake.set_alive(False)
            print("Protal")
        else:
            self.snake.set_alive(True)  # 活著

        if self.snake.nextInProtal != -1:
            self.snake.nextInProtal += 1
            if self.snake.nextInProtal == self.snake.long - 1:

                self.snake.inProtal = False
                self.snake.nextInProtal = -1

        if self.is_head_in_protal():
            self.snake.inProtal = True
            self.snake.nextInProtal = 1
            self.set_head_to_outprotal()

    def is_head_in_protal(self):
        headCoordinate = self.snake.coordinate[0]
        if headCoordinate[0] == -1:
            block = 0
        elif headCoordinate[1] == self.hightLimit:
            block = 1
        elif headCoordinate[0] == self.widthLimit:
            block = 2
        elif headCoordinate[1] == -1:
            block = 3
        else:
            return False

        if block % 2:
            if [block, headCoordinate[0]] == self.inProtal:
                self.snake.set_alive(True)

        else:
            if [block, headCoordinate[1]] == self.inProtal:
                self.snake.set_alive(True)
        return True

    def set_head_to_outprotal(self):
        self.snake.change_direction(self.outProtal[0])
        if self.outProtal[0] == 0:
            self.snake.coordinate[0] = [0, self.outProtal[1]]

        elif self.outProtal[0] == 1:
            self.snake.coordinate[0] = [self.outProtal[1], self.hightLimit - 1]

        elif self.outProtal[0] == 2:
            self.snake.coordinate[0] = [self.widthLimit - 1, self.outProtal[1]]

        elif self.outProtal[0] == 3:
            self.snake.coordinate[0] = [self.outProtal[1], 0]

    def set_point(self, point: Point):
        self.point = point

    def generate_point(self) -> None:  # 產生point
        tmp = 0
        if self.snake.coordinate[0][0] <= self.middleOfWidth:
            tmp += 0  # 左為0
        else:
            tmp += 1  # 右為1
        if self.snake.coordinate[0][1] <= self.middleOfHight:
            tmp += 0  # 下為0
        else:
            tmp += 2  # 上為2
        """    
          2  |  3
        -----+-----
          0  |  1
        """

        selectBlock = (tmp + random.randint(1, 3)) % 4  # 選擇區塊， tmp 是蛇的頭所在區塊
        """
        亂數最大為 3 ，所以 tmp 最後不會是蛇頭在的區塊
        tmp = 2, randint = 3 -> tmp = (2 + 3) % 4 = 1
        """

        self.x_axis = random.randint(
            self.block[selectBlock][0], self.block[selectBlock][1]
        )
        self.y_axis = random.randint(
            self.block[selectBlock][2], self.block[selectBlock][3]
        )

        self.pointPlace = [self.x_axis, self.y_axis]

        while self.pointPlace in self.snake.coordinate:
            self.x_axis = random.randint(
                self.block[selectBlock][0], self.block[selectBlock][1]
            )
            self.y_axis = random.randint(
                self.block[selectBlock][2], self.block[selectBlock][3]
            )

            self.pointPlace = [self.x_axis, self.y_axis]

        self.point.set_place(self.pointPlace)

    def block_init(self):
        self.block = [
            (0, self.middleOfWidth, 0, self.middleOfHight),  # 左下
            (self.middleOfWidth, self.widthLimit - 1, 0, self.middleOfHight),  # 右下
            (0, self.middleOfWidth, self.middleOfHight, self.hightLimit - 1),  # 左上
            (
                self.middleOfWidth,
                self.widthLimit - 1,
                self.middleOfHight,
                self.hightLimit - 1,
            ),
        ]  # 右上

    def display(self):
        tmp = []
        for i in range(self.widthLimit):
            tmp.append([])
            for j in range(self.hightLimit):
                tmp[i].append(0)

        if self.snake.coordinate[0] == self.pointPlace:
            self.snake.eat_point()
            self.generate_point()

        tmp[self.pointPlace[0]][self.pointPlace[1]] = 3

        for i in self.snake.coordinate:
            tmp[i[0]][i[1]] = 1

        print(" __", end="")  # 上界線
        for i in range(10):
            if self.inProtal == [1, i]:  # protal
                print("(i)", end="")
            elif self.outProtal == [1, i]:
                print("(o)", end="")
            else:
                print("___", end="")
        print("__ ")

        for i in range(self.hightLimit - 1, -1, -1):

            if self.inProtal == [0, i]:  # 左界線
                print("(i)", end="")  # protal
            elif self.outProtal == [0, i]:
                print("(o)", end="")
            else:
                print(" | ", end="")

            for j in range(self.widthLimit):
                if tmp[j][i]:
                    print(" ", tmp[j][i], sep="", end=" ")
                else:
                    print("  ", end=" ")

            if self.inProtal == [2, i]:
                print("(i)")  # 右界線
            elif self.outProtal == [2, i]:
                print("(o)")
            else:
                print(" | ")  # protal

        print(" ¯¯", end="")  # 下界線
        for i in range(10):
            if self.inProtal == [3, i]:
                print("(i)", end="")  # protal
            elif self.outProtal == [3, i]:
                print("(o)", end="")
            else:
                print("¯¯¯", end="")
        print("¯¯ ", end="")

        print(
            "protal time =",
            self.protalTime,
            "\n",
            self.snake.nextInProtal,
            self.snake.long - 1,
            self.snake.inProtal,
        )
""