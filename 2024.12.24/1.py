from math import sqrt

class Point:
    """Класс для представления точки на двумерной плоскости."""
    
    def __init__(self, x: float, y: float):
        self._x = x
        self._y = y

    @property
    def x(self) -> float:
        return self._x

    @x.setter
    def x(self, value):
        raise TypeError("Координата x неизменяема")

    @property
    def y(self) -> float:
        return self._y

    @y.setter
    def y(self, value):
        raise TypeError("Координата y неизменяема")

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Point):
            return False
        return self._x == other.x and self._y == other.y

    def __repr__(self) -> str:
        return f"Point({self._x}, {self._y})"

class Line:
    """Класс для представления отрезка на двумерной плоскости."""
    
    def __init__(self, start: Point, end: Point):
        self._start = start
        self._end = end
        self._length = self.length_calc(start, end)

    @property
    def start(self) -> Point:
        return self._start

    @start.setter
    def start(self, value: Point):
        if not isinstance(value, Point):
            raise TypeError("Начальная точка должна быть экземпляром Point")
        self._start = value
        self._length = self.length_calc(self._start, self._end)


    @property
    def end(self) -> Point:
        return self._end

    @end.setter
    def end(self, value: Point):
        if not isinstance(value, Point):
            raise TypeError("Конечная точка должна быть экземпляром Point")
        self._end = value
        self._length = self.length_calc(self._start, self._end)

    @property
    def length(self) -> float:
        return self._length

    @length.setter
    def length(self, value):
        raise TypeError("Объект length неизменяем")

    @staticmethod
    def length_calc(point1: Point, point2: Point) -> float:
        return ((point2.x - point1.x)  2 + (point2.y - point1.y)  2) ** 0.5

    def repr(self):
        return f"Line({self.start}, {self.end})"

    def str(self):
        return f"Line from {self.start} to {self.end}"

class Polygon:
    """Класс для представления многоугольника."""
    
     @property
    def perimeter(self) -> float:
        if not self.is_closed():
            raise ValueError("Многоугольник не замкнут")
        return sum(line.length for line in self)

    def is_closed(self) -> bool:
        if len(self) < 3:
            return False
        return self[0].start == self[-1].end and all(self[i].end == self[i + 1].start for i in range(len(self) - 1))
        
#>>> 
#>>>p1 = Point(0, 3)
#>>>p2 = Point(4, 0)
#>>>p3 = Point(8, 3)
#>>>p1
#(0,3)
#>>>
#>>>repr(p1) == str(p1)
#True
#>>>
#>>>p1 == Point(0, 3)
#True
#>>>
#>>>p1.x, p1.y
#(0, 3)
#>>>
#>>>p2.y = 5
#...
#TypeError: "Координата y неизменяема"
#>>>
#>>>
#>>>l1 = Line(p1, p2)
#>>>l2 = Line(p2, p3)
#>>>l3 = Line(p3, p1)
#>>>
#>>>l1
#(0,3)———(4,0)
#>>>
#>>>repr(l1) == str(l1)
#True
#>>>
#>>>l1.length
#5.0
#>>>
#>>>l1.length = 10
#...
#TypeError: "Объект length неизменяем"
#>>> 
#>>>l3.start = 12
#...
#TypeError: "Начальная точка должна быть экземпляром Point"
#>>> 
#>>> 
#>>>pol1 = Polygon(l1, l2, l3)
#>>>
#>>>pol1.perimeter
#18.0
#>>>pol1.perimeter = 20
#...
#TypeError: "Конечная точка должна быть экземпляром Point"
#>>>
#>>>l3.end = Point(-10, -10)
#>>>pol1.perimeter
#...
#ValueError: "Многоугольник не замкнут"