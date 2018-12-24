#Problem: A robot makes 3 random straight line cuts on a pizza.
#The end points of each cut are chosen independently at random.
#What is the expected number of pieces of pizza you will get?


import random
import math

#Generates a random point on the circumfrence of a circle
#centered at (0,0) with a radius of 1.  This is our pizza.
#With a domain of [-10000,10000] we reduce the probability
#of problematic cuts (identical, paralell) to essentailly 0
def point_on_circ():
    x=random.randint(-100000,100000)/100000.0
    y=random.choice([-1,1])*math.sqrt(1-x**2)
    return (x,y)

#Computes the slope between two points.
def slope((x1,y1),(x2,y2)):
    m = (y2-y1)/(x2-x1)
    return m

#Finds the intersection of the lines determined by the first two
#and last two points (respectively).
def solution((x1,y1),(x2,y2),(x3,y3),(x4,y4)):
    m1 = slope((x1,y1),(x2,y2))
    m2 = slope ((x3,y3),(x4,y4))
    x = (y1-m1*x1-y3+m2*x3)/(m2-m1)
    y = y1-m1*x1+m1*x
    return (x,y)

#Checks to see if a point is inside of the circle.
def point_in_circ((x,y)):
    if x**2+y**2<=1:
        return 1
    else:
        return 0

#Generates 6 random points and finds the intersections
#of the three "cuts".
def pizza_cuts():
    points = []
    for i in range(0,6):
        points.append(point_on_circ())
    s1=solution(points[0],points[1],points[2],points[3])
    s2=solution(points[2],points[3],points[4],points[5])
    s3=solution(points[0],points[1],points[4],points[5])
    return [s1,s2,s3]

#Takes three intersections and checks to see if they are
#inside of the circle.  The total number of pieces in the circle
#is equal to the number of intersections in the circle plus 4.
def num_of_pieces():
    solutions = pizza_cuts()
    intersections = 0
    for i in solutions:
        intersections += point_in_circ(i)
    pieces = intersections + 4
    return pieces


#Computes the average number of pieces in n trials.  The average
#tends to 5 as n tends to infinity which is the correct solution!
def main():
    total = 0
    for i in range(0,1000):
        total += num_of_pieces()
    print total/1000.0



if __name__== '__main__':
    main()