import copy


class Snake():
    def __init__(self, long: int, moveDirecrtion: list, headCoordinate: list):
        self.long = long  # 長度
        self.moveDirection = moveDirecrtion  # 面向方位
        self.coordinate = []  # 蛇整體座標

        for i in range(long):
            self.coordinate.append([])
        self.coordinate[0] = headCoordinate  # 蛇頭座標

        tmp = copy.deepcopy(headCoordinate)
        for i in range(long - 1):  # 將全蛇的座標生出來
            tmp[0] -= self.moveDirection[0]
            tmp[1] -= self.moveDirection[1]
            self.coordinate[i + 1] = copy.deepcopy(tmp)

    def unit_move(self) -> None:
        tmp = copy.deepcopy(self.coordinate[0])
        tmp[0] += self.moveDirection[0]
        tmp[1] += self.moveDirection[1]
        self.coordinate = [tmp] + self.coordinate[0:self.long - 1:1]

    def multi_unit_move(self, distance):  # 蛇移動
        for i in range(distance):
            self.unit_move()

    def eat_move(self) -> None:
        tmp = self.coordinate[0]
        tmp[0] += self.moveDirection[0]
        tmp[1] += self.moveDirection[1]
        self.coordinate = tmp + self.coordinate[0:self.long:1]

def main():
    direction = [0, 1]
    coordinate = [0, 0]
    testSnake = Snake(3, direction, coordinate)
    print(testSnake.coordinate)
    testSnake.multi_unit_move(2)
    print(testSnake.coordinate)

if __name__ == "__main__":
    main()