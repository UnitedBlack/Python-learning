# class Point:
#     color = "red"
#     circle = 2


# setattr(Point, "prop", 32)
# print(Point.__dict__)
# print(
#     getattr(
#         Point,
#         "a",
#     )
# )

# 2
# class Point:
#     color = "red"
#     circle = 2
    
#     def printing(self):
#         print(self)
        
# pt = Point()
# pt.printing()
class Point():
    def __new__(cls, *args, **kwargs):
        print("Вызов __new__ для " + str(cls))
        return super().__new__(cls)
        
    def __init__(self, x=0, y=0) -> None:
        self.x = x
        self.y = y
        
pt = Point(1, 2)