import random
from Snake_lib.Snake import Snake
from Snake_lib.Point import Point


class Map:
    def __init__(self, snake: Snake = None, point: Point = None, width: int = 10, hight: int = 10):
        self.widthLimit = width
        self.hightLimit = hight
        self.middleOfWidth = self.widthLimit // 2  # 為了亂數
        self.middleOfHight = self.hightLimit // 2

        self.snake = snake
        self.point = point

        self.x_axis = 0
        self.y_axis = 0
        self.pointPlace = [self.x_axis, self.y_axis]

        self.block_init()
        self.generate_point()

    # 傳送門(預想)

    def set_snake(self, snake: Snake):
        self.snake = snake

    def is_die(self) -> None:
        if (self.snake.coordinate[0][0] > self.snake.location.width or
            self.snake.coordinate[0][1] > self.snake.location.hight or
            self.snake.coordinate[0][0] < 0 or
                self.snake.coordinate[0][1] < 0):
            self.snake.set_alive(False)  # 死了
        else:
            self.snake.set_alive(True)  # 活著

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
            self.block[selectBlock][0], self.block[selectBlock][1])
        self.y_axis = random.randint(
            self.block[selectBlock][2], self.block[selectBlock][3])

        self.pointPlace = [self.x_axis, self.y_axis]
        print(self.pointPlace, tmp, selectBlock)

        while (self.pointPlace in self.snake.coordinate):
            self.x_axis = random.randint(
                self.block[selectBlock][0], self.block[selectBlock][1])
            self.y_axis = random.randint(
                self.block[selectBlock][2], self.block[selectBlock][3])

            self.pointPlace = [self.x_axis, self.y_axis]
            print(self.pointPlace)

        self.point.set_place(self.pointPlace)

    def block_init(self):
        self.block = [(0, self.middleOfWidth, 0, self.middleOfHight),  # 左下
                      (self.middleOfWidth, self.widthLimit - 1,
                       0, self.middleOfHight),  # 右下
                      (0, self.middleOfWidth, self.middleOfHight,
                       self.hightLimit - 1),  # 左上
                      (self.middleOfWidth, self.widthLimit - 1, self.middleOfHight, self.hightLimit - 1)]  # 右上

    def display(self):
        tmp = []
        for i in range(self.widthLimit):
            tmp.append([])
            for j in range(self.hightLimit):
                tmp[i].append(0)

        for i in self.snake.coordinate:
            tmp[i[0]][i[1]] = 1

        tmp[self.pointPlace[0]][self.pointPlace[1]] = 3

        for i in range(self.hightLimit - 1, -1, -1):
            for j in range(self.widthLimit):
                if tmp[j][i]:
                    print(tmp[j][i], end=' ')
                else:
                    print(' ', end = ' ')
            print()
