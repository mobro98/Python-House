import turtle 

class polygon:
    def __init__(self, num_of_sides, the_location, the_color):
        self.sides = num_of_sides
        self.location = the_location
        self.the_color = color
    def num_sides(self):
        return self.sides
    def draw(self, pen):
        pen.goto(self.location[0], self.location[1])
        pen.the_color(self.the_color)
        pen.down()
        pen.begin_fill()

class triangle(polygon):
    def __init__(self, vx1, vx2, vx3 , the_color):
        polygon.__init__(self,3, vx1, the_color)
        self.vertex_1 = vx1
        self.vertex_2 = vx2
        self.vertex_3 = vx3
    def draw(self,pen):
        polygon.draw(self,pen)
        pen.goto(self.vertex_2[0],self.vertex_2[1])
        pen.goto(self.vertex_3[0],self.vertex_3[1])
        pen.goto(self.location[0],self.location[1])
        pen.up()
        pen.end_fill()
        def __str__(self):
            return "triangle( " + str(self.location) + ", " + str(self.vertex_2) + ", " + str(self.vertex_3) + " )"


class rectangle(polygon):
    def __init__(self,vx1,vx2,the_color):
        polygon.__init__(self,4,vx1,the_color)
        self.vertex_2=(vx2[0],vx1[1])
        self.vertex_3=vx2
        self.vertex_4=(vx1[0],vx2[1])
        
    def draw(self, pen):
        polygon.draw(self,pen)
        pen.goto(self.vertex_2[0],self.vertex_2[1])
        pen.goto(self.vertex_3[0],self.vertex_3[1])
        pen.goto(self.vertex_4[0],self.vertex_4[1])
        pen.goto(self.location[0],self.location[1])
        pen.up()
        pen.end_fill()
        def __str__(self):
            return "rectagle( "+str(self.location) + " , " + str(self.vertex_3) + " )"

class circle:
    def __init__(self, the_center, the_radius, color_the):
        self.center = the_center
        self.radius = the_radius
        self.color = color_the
    def draw(self, pen):
        pen.goto(self.center[0],self.center[1])
        pen.fillcolor(self.color)
        pen.begin_fill()
        pen.down()
        pen.circle(self.radius)
        pen.up()
        pen.end_fill()
        
    def __str__(self):
        return "circle (" + str(self.center) + ", " + str(self.radius) + " )"
    


def main():
    walls = rectangle((0,0) , (100,100),"blue")
    window_1 = rectangle( (15,70), (30,85),"gray")
    window_2 = rectangle( (70,70), (85,85), "gray")
    door = rectangle( (40,0) , (55,30),"green")
    roof = triangle( (0,100), (100,100), (50,150), "red")
    knob = circle( (44,12),2,"black")
    print(walls)
    print(window_1)
    print(window_2)
    print(door)
    print(roof)
    print(knob)
    ts=turtle.Screen() 
    pen=turtle.Turtle()
    walls.draw(pen)
    window_1.draw(pen)
    window_2.draw(pen)
    door.draw(pen)
    roof.draw(pen)
    knob.draw(pen)
    rectagle( (0, 0) , (100, 100) )
    rectagle( (15, 70) , (30, 85) )
    rectagle( (70, 70) , (85, 85) )
    rectagle( (40, 0) , (55, 30) )
    triangle( (0, 100), (100, 100), (50, 150) )
    circle ((44, 12), 2 )
    main()
