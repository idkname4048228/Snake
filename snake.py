import copy
import random


class map():
    def __init__(self, width=10, hight=10):
        self.width = width
        self.hight = hight
    # 傳送門(預想)


class Snake():
    def __init__(self, long: int, moveDirecrtion: list, headCoordinate: list):
        self.long = long  # 長度
        self.moveDirection = moveDirecrtion  # 面向方位
        self.coordinate = []  # 蛇整體座標
        self.location = map()

        for i in range(long):
            self.coordinate.append([])
        self.coordinate[0] = headCoordinate  # 蛇頭座標

        tmp = copy.deepcopy(headCoordinate)
        for i in range(long - 1):  # 將全蛇的座標生出來
            tmp[0] -= self.moveDirection[0]
            tmp[1] -= self.moveDirection[1]
            self.coordinate[i + 1] = copy.deepcopy(tmp)

    def unit_move(self) -> None:  # 單位移動
        tmp = copy.deepcopy(self.coordinate[0])
        tmp[0] += self.moveDirection[0]
        tmp[1] += self.moveDirection[1]
        self.coordinate = [tmp] + self.coordinate[0:self.long - 1:1]
        if self.is_death():  # 界線
            print("death")
            return False  # 死了，停止前進
        return True  # 還活著

    def multi_unit_move(self, distance) -> None:  # 蛇移動
        for i in range(distance):
            if not(self.unit_move()):
                break

    def eat_move(self) -> None:  # 吃point，加長身體
        tmp = self.coordinate[0]
        tmp[0] += self.moveDirection[0]
        tmp[1] += self.moveDirection[1]
        self.coordinate = tmp + self.coordinate[0:self.long:1]

    def is_death(self) -> bool:  # 死了嗎
        if (self.coordinate[0][0] > self.location.width or
            self.coordinate[0][1] > self.location.hight or
            self.coordinate[0][0] < 0 or
                self.coordinate[0][1] < 0):
            return True  # 死了
        else:
            return False  # 活著

    def set_map(self, map: map) -> None:  # 設定地圖
        self.location = map


class Point():
    def __init__(self):
        self.location = map()
        self.widthLimit = self.location.width
        self.hightLimit = self.location.hight
        self.middleOfWidth = self.widthLimit // 2  # 為了亂數
        self.middleOfHight = self.hightLimit // 2

        self.block_init()
        self.generate_point()
        

        self.x_axis = random.randint(0, self.widthLimit)
        self.y_axis = random.randint(0, self.hightLimit)

        self.place = [self.x_axis, self.y_axis]

    def generate_point(self, snake: Snake) -> None:  #在被吃掉時會執行，初始化也會
        tmp = 0
        if snake.coordinate[0][0] <= self.middleOfWidth:
            tmp += 0  # 左為0
        else:
            tmp += 1  # 右為0
        if snake.coordinate[0][1] <= self.middleOfHight:
            tmp += 0  # 下為0
        else:
            tmp += 2  # 上為0
        """    
          2  |  3
        -----+-----
          0  |  1
        """

        selectBlock = (tmp + random.randint(4)) % 4  # 選擇區塊， tmp 是蛇的頭所在區塊
        """
        亂數最大為 3 ，所以 tmp 最後不會是蛇頭在的區塊
        tmp = 2, randint = 3 -> tmp = (2 + 3) % 4 = 1
        """

        self.x_axis = random.randint(self.block[selectBlock][0], self.block[selectBlock][1])
        self.y_axis = random.randint(self.block[selectBlock][2], self.block[selectBlock][3])

        self.place = [self.x_axis, self.y_axis]

    def block_init(self):
        self.block = [(0, self.middleOfWidth, 0, self.middleOfHight),  # 左下
                      (self.middleOfWidth, self.widthLimit, 0, self.middleOfHight),  # 右下
                      (0, self.middleOfWidth, self.middleOfHight, self.hightLimit),  # 左上
                      (self.middleOfWidth, self.widthLimit, self.middleOfHight, self.hightLimit)]  # 右上


    def set_map(self, map: map) -> None:  # 設定地圖
        self.location = map
        self.widthLimit = map.width
        self.hightLimit = map.hight
        self.middleOfWidth = self.widthLimit // 2  # 為了亂數
        self.middleOfHight = self.hightLimit // 2
        

    def display(self):  # 展示
        print(self.place)


def main():
    direction = [0, 1]
    coordinate = [0, 0]
    testSnake = Snake(3, direction, coordinate)
    print(testSnake.coordinate)
    
    testpoint = Point(testsnake)
    testpoint.display()


if __name__ == "__main__":
    main()
