import copy


class Snake:
    def __init__(self, long: int, moveDirecrtion: int, headCoordinate: list):
        self.long = long  # 長度
        self.direction = [[1, 0], [0, -1], [-1, 0], [0, 1]]
        self.directionCode = moveDirecrtion
        self.moveDirection = self.direction[self.directionCode]  # 面向方位
        self.coordinate = []  # 蛇整體座標
        self.alive = True

        for i in range(long):
            self.coordinate.append([])
        self.coordinate[0] = headCoordinate  # 蛇頭座標

        tmp = copy.deepcopy(headCoordinate)
        for i in range(long - 1):  # 將全蛇的座標生出來
            tmp[0] -= self.moveDirection[0]
            tmp[1] -= self.moveDirection[1]
            self.coordinate[i + 1] = copy.deepcopy(tmp)
        
        self.lastSpace = self.coordinate[-1]

    def change_direction(self, direction: int):
        self.directionCode = direction
        self.moveDirection = self.direction[self.directionCode]  # 面向方位

    def unit_move(self) -> None:  # 單位移動
        self.lastSpace = self.coordinate[-1]
        tmp = copy.deepcopy(self.coordinate[0])
        tmp[0] += self.moveDirection[0]
        tmp[1] += self .moveDirection[1]
        self.coordinate = [tmp] + self.coordinate[0:self.long - 1:1]

    def multi_unit_move(self, distance: int) -> None:  # 蛇移動
        for i in range(distance):
            self.unit_move()

    def eat_point(self) -> None:  # 吃point，加長身體
        self.long += 1
        self.coordinate = self.coordinate + [self.lastSpace]

    def set_alive(self, isAliveInMap: bool) -> None:  # 頭撞地圖
        isAlive = True
        for i in range(1, len(self.coordinate)):  # 頭撞身體
            if self.coordinate[0] == self.coordinate[i]:
                isAlive = False
                break
        self.alive = isAliveInMap and isAlive
