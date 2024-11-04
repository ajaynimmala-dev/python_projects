# from random import randint
# class Point:
#     def __init__(self,low_left,up_right):
#         self.low_left=low_left
#         self.up_right=up_right
#         print("low_left :",low_left)
#         print("up_right:",up_right)
#     def is_point_inside(self):
#         print("enter the point")
#         enter_x_point=int(input("x point"))
#         enter_y_point=int(input("y point"))
#         self.enter_x_point=enter_x_point
#         self.enter_y_point=enter_y_point
#         if self.low_left[0]<enter_x_point<self.up_right[0] and self.low_left[1]<enter_y_point<self.up_right[1]:
#             return(True)
#         else:
#             return(False)
#     def distance(self):
#         return[(self.enter_x_point-self.low_left[0])**2+(self.enter_y_point-self.low_left[1])**2]
#
# while True:
#     point1=Point((randint(0,5),randint(0,5)),(randint(5,9),randint(5,9)))
#     result=point1.is_point_inside()
#     print(result)
#     distance=point1.distance()
#     print(distance)

from random import randint
from math import *

class Point:

    def __init__(self,x,y):
        self.x=x
        self.y=y

    def is_point(self,rect_points):
        # print("lower point:",rect_points.low_left,"\n","upper point:","\n",rect_points.up_right)
        if rect_points.low_left[0]<self.x <rect_points.up_right[0] and rect_points.low_left[1]<self.y<rect_points.up_right[1]:
            return True
        else:
            return False

class Rectangle:

    def __init__(self,low_left,up_right):

        self.low_left=low_left

        self.up_right=up_right

    def Area(self):
        self.lenght=(self.up_right[0]-self.low_left[0])

        self.breadth=(self.up_right[1]-self.low_left[1])

        self.area=self.lenght*self.breadth


        return(self.area)


rect_points = Rectangle((randint(0, 5), randint(0, 5)), (randint(5, 10), randint(5, 10)))

print("the rectangle points are:".title(), rect_points.low_left, rect_points.up_right)

point1 = Point((int(input("Guess X Point"))), int(input("Guess Y Point")))

Result = point1.is_point(rect_points)

print("your point was in side the rectangle".title(),Result)

Area_Rectangle=Rectangle.Area(rect_points)

print("the area of rectangle is:".title(),Area_Rectangle)


