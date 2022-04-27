import copy
import random


class map():
    def __init__(self, width=0, hight=0):
        self.widthLimit = width
        self.hightLimit = hight
    #傳送門(預想)
    

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

    def is_death(self) -> bool:
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
    def __init__(self, width: int, hight: int):
        self.location = map()
        self.width_limit = width
        self.hight_limit = hight

        self.x_axis = random.randint(0, self.width_limit)
        self.y_axis = random.randint(0, self.hight_limit)

        self.place = [self.x_axis, self.y_axis]

    def be_eaten(self) -> None:     #被吃掉時新增另一個
        self.x_axis = random.randint(0, self.hight_limit)
        self.y_axis = random.randint(0, self.width_limit)

        self.place = [self.x_axis, self.y_axis]

    def set_map(self, map: map) -> None:  # 設定地圖
        self.location = map
        self.width_limit = map.width
        self.hight_limit = map.hight

    def display(self):  #展示
        print(self.place)



def main():
    direction = [0, 1]
    coordinate = [0, 0]
    testSnake = Snake(3, direction, coordinate)
    print(testSnake.coordinate)
    testSnake.multi_unit_move(2)
    print(testSnake.coordinate)


if __name__ == "__main__":
    main()
