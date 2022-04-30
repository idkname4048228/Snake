class Point:
    def __init__(self):
        self.place = [0, 0]

    def set_place(self, place: list):  # 展示
        self.place = place

    def display(self):
        print(self.place)
