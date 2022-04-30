from Snake_lib.Map import Map
from Snake_lib.Snake import Snake
from Snake_lib.Point import Point

def main():
    testSnake = Snake(9, [0, 1], [0, 9])
    testPoint = Point()
    
    testMap = Map(testSnake, testPoint)

    testMap.display()

if __name__ == '__main__':
    main()

