# Question1: Accept co-ordintes as tuple and return slope of line
class Line:
    def __init__(self,coor1,coor2):
        self.coor1 = coor1
        self.coor2 = coor2

    def distance(self):
        x1,y1 = self.coor1
        x2,y2 = self.coor2
        return ((x2-x1)**2 + (y2-y1)**2))**0.5

    def slope(self):
        x1,y1 = self.coor1
        x2,y2 = self.coor2
        return (y2-y1)/(x2-x1)


    c1 = (1,1)
    c2 = (4,5)
    sample_line1 = Line(c1,c2)
    sample_line1.distance()
    sample_line1.slope()

# Question2: Cylinder area, volume
pi = 3.1412
class Cylinder:
    def __init__(self,height=1,radius=1):
        self.radius = radius
        self.height = height

    def volume(self):
        return pi*self.radius**2*self.height

    def surface_area(self):
        return (2*pi*self.radius*self.height + 2*pi*self.radius**2)
        
