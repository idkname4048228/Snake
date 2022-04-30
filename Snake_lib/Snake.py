import copy


class Snake:
    def __init__(self, long: int, moveDirecrtion: list, headCoordinate: list):
        self.long = long  # 長度
        self.moveDirection = moveDirecrtion  # 面向方位
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

    def unit_move(self) -> bool:  # 單位移動
        tmp = copy.deepcopy(self.coordinate[0])
        tmp[0] += self.moveDirection[0]
        tmp[1] += self .moveDirection[1]
        self.coordinate = [tmp] + self.coordinate[0:self.long - 1:1]
        if self.alive:  # 活著嗎
            return True  # 還活著
        print("death")
        return False  # 死了，停止前進

    def multi_unit_move(self, distance) -> None:  # 蛇移動
        for i in range(distance):
            if self.unit_move():
                break

    def eat_point(self) -> None:  # 吃point，加長身體
        tmp = self.coordinate[0]
        tmp[0] += self.moveDirection[0]
        tmp[1] += self.moveDirection[1]
        self.coordinate = tmp + self.coordinate[0:self.long:1]

    def set_alive(self, isDeath: bool) -> None:  # 死了嗎
        self.alive = isDeath

