import copy

"""
Snake 主要功能
    move    前進
    is_alive    判斷是否死亡
    __eat_point  吃點數，增加長度
    component 相關 method, attribute
        Map:
            set_boundary    設定邊界
        Protal:
            next_body_in_protal 回傳下一個在傳送門的身體，讓 Map 判斷會不會死掉( protalTime )

"""


class Snake:
    __directionMap = [[1, 0], [0, -1], [-1, 0], [0, 1]]  # 方向對照表[右下左上]

    def __init__(
        self, long: int = 1, direction: int = 0, headCoordinate: list = [0, 0]
    ) -> None:
        self.__long = long  # 設定長度
        self.__direction = self.__directionMap[direction]  # 設定方向
        self.__head = headCoordinate
        self.__bodyCoordinate = [self.__head]

        # 地圖邊界預設 10
        self.__mapWidth = 10  # 地圖寬邊界
        self.__mapHigh = 10  # 地圖高邊界

        self.generate_body(headCoordinate)  # 生成全身體
        self.__next_body_in_protal = -1  # 預設 -1 此為身體座標之 index
        self.__pointPlace = None  # point 座標
        self.__step = 1  # snake 步數

    def generate_body(self) -> None:  # 生成身體全部座標
        body = copy.deepcopy(self.__head)
        for i in range(1, self.__long):
            # 往頭的反方向長
            body[0] -= self.__direction[0]
            body[1] -= self.__direction[1]
            self.__bodyCoordinate.append(copy.deepcopy(body))

    # Map 相關

    def set_boundary(self, width: int, high: int) -> None:  # 設定邊界
        self.__width = width
        self.__high = high

    # 執行相關

    def __eat_point(self) -> bool:  # 看有沒有吃到 point ，有就刪掉 point ，並回傳 True (有吃到)
        if self.__head == self.__pointPlace:
            self.__pointPlace = None  # 刪掉 point
            return True  # 吃到
        return False  # 沒吃到

    def __hitting_wall(self, head: list) -> bool:  # 撞牆壁
        return not (0 <= head[0] < self.__width) or not (  # X軸
            0 <= head[1] < self.__high
        )  # Y軸

    def __hitting_body(self, head: list) -> bool:  # 撞身體
        return head in self.__bodyCoordinate[1 : self.__long : 1]

    def move(
        self,
    ) -> None:  # 移動，內有判斷是否進傳送門、撞牆、撞身體、吃 point ，實際執行時後面需接 need_generate_point 來判定是否需要生成 point
        nextHead = copy.deepcopy(self.__head)
        nextHead[0] += self.__direction[0]
        nextHead[1] += self.__direction[1]

        if nextHead == self.__enterProtalPlace:  # 如果下一步在傳送門入口的話
            self.__via_protal()  # 通過 protal
        elif self.__hitting_body or self.__hitting_wall:  # 撞牆或身體
            self.set_alive(False)  # 死亡
            return None  # 強行中斷
        else:
            self.__head = nextHead  # 頭變為下一步

        if self.__eat_point():
            self.__bodyCoordinate = [self.__head] + self.__bodyCoordinate[
                0 : self.__long : 1
            ]
            self.__head = self.__bodyCoordinate[0]
            self.__long += 1  # 加長身體
        else:
            self.__bodyCoordinate = [self.__head] + self.__bodyCoordinate[
                0 : self.__long - 1 : 1
            ]
            self.__head = self.__bodyCoordinate[0]

        self.__check_body_in_protal()

    def need_genarate_point(self) -> bool:  # 是否需要生成 point
        if self.__pointPlace == None:
            return True  # 要新的 point
        return False  # 不用

    def set_alive(self, state: bool) -> None:  # 調整狀態
        self.__alive = state

    def is_alive(self) -> bool:  # 看死了沒
        return self.__alive

    # protal 相關

    def __convert_protal_to_coordinate(
        self, protal: list = None, is_enter: bool = True
    ) -> list:  # 將傳送門轉換為座標系
        if is_enter:
            if protal[0] == 0:  # sideline為 0 時，protal[1]是y軸
                tmp = [-1, protal[1]]

            elif protal[0] == 1:  # sideline為 1 時，protal[1]是x軸
                tmp = [protal[1], self.__high]

            elif protal[0] == 2:  # sideline為 2 時，protal[1]是y軸
                tmp = [self.__width, protal[1]]

            elif protal[0] == 3:  # sideline為 3 時，protal[1]是x軸
                tmp = [protal[1], -1]
        else:
            if protal[0] == 0:  # sideline為 0 時，protal[1]是y軸
                tmp = [0, protal[1]]

            elif protal[0] == 1:  # sideline為 1 時，protal[1]是x軸
                tmp = [protal[1], self.__high - 1]

            elif protal[0] == 2:  # sideline為 2 時，protal[1]是y軸
                tmp = [self.__width - 1, protal[1]]

            elif protal[0] == 3:  # sideline為 3 時，protal[1]是x軸
                tmp = [protal[1], 0]

        return tmp

    def set_protal(
        self, enterProtal: list = None, exitProtal: list = None
    ) -> None:  # 設定傳送門，參數為非座標
        self.__enterProtalPlace = self.__convert_protal_to_coordinate(
            enterProtal, is_enter=True
        )
        self.__exitProtalPlace = self.__convert_protal_to_coordinate(
            exitProtal, is_enter=False
        )
        self.__exitDirection = self.__directionMap[exitProtal[0]]

    def __via_protal(self) -> None:  # 傳送
        self.__head = copy.deepcopy(self.__exitProtalPlace)  # 頭在出口
        self.__next_body_in_protal = 1  # 下一個在傳送門的 body index
        self.__direction = self.__exitDirection  # 改變方向

    def __check_body_in_protal(self) -> None:  # 改變下一個在傳送門的 body index
        if self.__next_body_in_protal != -1:  # -1 為預設值，如果不等於 -1 代表已經進 protal 了
            self.__next_body_in_protal += 1  # body index += 1
            if (
                self.__next_body_in_protal == self.__long
            ):  # 如果下一個 body index 等於 long 代表傳完了
                self.__next_body_in_protal = -1  # 改回預設值

    def body_in_protal(self) -> bool:  # 給 Map 使用
        return self.__next_body_in_protal != -1  # False 代表不在 protal 內
