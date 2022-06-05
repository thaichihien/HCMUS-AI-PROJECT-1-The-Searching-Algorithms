from math import ceil
import turtle
import numpy as np
from environment import BLOCKED


screen = turtle.Screen()
screen.setup(width= 1.0,height= 1.0)
try:
    screen.addshape('AI/Lab01-Search/robot.gif')
except:
    pass
class Matrix:
    def __init__(self,origin =(0,0)) -> None:
        self.pen = turtle.Turtle()
        self.pen.speed(0)
        self.size = 40
        self.leftmost_pos = origin
        self.pen.hideturtle()

    
    def draw(self,matrix):
        screen.tracer(0)
        pos = list(self.leftmost_pos)    #origin

        if matrix.shape[1] > 22:
            self.size = 40 - (matrix.shape[1] - 22)*2
        else:self.size = 40 - (matrix.shape[0] - 16)*1.5
        
        self.size = ceil(self.size)
        #draw a row
        for y in range(matrix.shape[0]):
            for x in range(matrix.shape[1]):
                self.draw_square_matrix(pos,matrix[y][x])
                pos[0] += self.size
            pos[0] = self.leftmost_pos[0]
            pos[1] += self.size


        for x in range(matrix.shape[1]):
            pos = (self.leftmost_pos[0] + self.size*x + self.size/2 - 2,self.leftmost_pos[1] - 30)
            self.pen.up()
            self.pen.setpos(pos)
            self.pen.down()
            self.pen.write(x,font=('Arial', 11, 'normal'))

        for y in range(matrix.shape[0]):
            pos = (self.leftmost_pos[0] -20 ,self.leftmost_pos[1] + self.size*y + self.size/2 - 2)
            self.pen.up()
            self.pen.setpos(pos)
            self.pen.down()
            self.pen.write(y,align= 'right',font=('Arial', 11, 'normal'))

        self.pen.hideturtle()
        screen.update()
        screen.tracer(1)

    def draw_square_matrix(self,pos,IsBlock):
        self.pen.up()
        self.pen.setpos(pos)
        self.pen.down()

        if IsBlock == BLOCKED:
            self.pen.fillcolor("#9772FB")
            self.pen.begin_fill()

            for i in range(4):
                self.pen.forward(self.size)           
                self.pen.left(90)
            self.pen.end_fill()
            self.pen.fillcolor('Black')
        else:
            for i in range(4):
                self.pen.forward(self.size)           
                self.pen.left(90)

    def draw_start_goal(self,start,goal,start_color="#00FFAB",goal_color="#FF0054"):
        screen.tracer(0)
        self.draw_square(start,start_color)
        self.draw_square(goal,goal_color)
        screen.update()
        screen.tracer(1)


    def draw_square(self,pos,pen_color):
        screen.tracer(0)
        start_pos = (self.leftmost_pos[0] + self.size*pos[0],self.leftmost_pos[1] + self.size*pos[1])
        self.pen.speed(0)
        self.pen.pencolor('Black')
        self.pen.width(1)
        self.pen.up()
        self.pen.setpos(start_pos)
        self.pen.down()

        self.pen.fillcolor(pen_color)
        self.pen.begin_fill()

        for i in range(4):
            self.pen.forward(self.size)           
            self.pen.left(90)
        self.pen.end_fill()
        self.pen.fillcolor('Black')
        #screen.update()
        screen.tracer(1)

    


class Robot:
    def __init__(self,pos_matrix,size_block) -> None:
        self.pen = turtle.Turtle()
        self.pen.hideturtle()
        self.pen.speed(3)
        self.pen.pencolor('Green')
        self.pen.width(5)
        self.size = size_block
        self.leftmost_pos = pos_matrix

    
    def play(self,path):
        try:
            self.pen.shape('AI/Lab01-Search/robot.gif')
        except:
            pass
        self.pen.showturtle()
        self.pen.forward(0)
        temp = path.pop()

        self.pen.up()
        cur_pos = (self.leftmost_pos[0] + self.size*temp[1] + self.size/2,
                    self.leftmost_pos[1] + self.size*temp[0] + self.size/2)
        self.pen.setpos(cur_pos)
        self.pen.down()
        while path:
            temp = path.pop()
            
            next_pos = (self.leftmost_pos[0] + self.size*temp[1] + self.size/2,
                    self.leftmost_pos[1] + self.size*temp[0] + self.size/2)
            
            self.pen.setheading(self.pen.towards(next_pos))
            self.pen.forward(self.size)


        return True


    def reset(self):
        self.pen.clear()
        self.pen.hideturtle()
        self.pen.shape('classic')



class Button:
    FONT_SIZE = 12
    FONT = ('Arial', FONT_SIZE, 'bold')
    CURRENT_COLOR = "White"

    def __init__(self,origin,message,shape = 'circle',onetime = True) -> None:
        self.pen = turtle.Turtle()
        self.pen.speed(0)
        self.pen.fillcolor('White')
        self.leftmost_pos = origin
        self.IsClick = False
        self.text = message
        self.pen.shape(shape)
        self.onetime = onetime

    def create(self,pos):
        screen.tracer(0)
        self.pen.hideturtle()
        self.pos = pos
        self.text_on_button()

        self.pen.showturtle()
        screen.tracer(1)

    def text_on_button(self):
        self.pen.up()
        self.pen.setpos(self.leftmost_pos[0] + self.pos[0] + 25,self.leftmost_pos[1] + self.pos[1] - 20)
        self.pen.down()

        self.pen.write(self.text,font=self.FONT)
        self.pen.up()
        self.pen.setpos(self.leftmost_pos[0] + self.pos[0],self.leftmost_pos[1] + self.pos[1] - 10)
        self.pen.down()

    def update(self):
        if self.onetime:
            self.pen.onclick(self.event_click_onetime)
        else:self.pen.onclick(self.event_click)

    def result(self):
        return self.IsClick

    def event_click_onetime(self,x,y):
        if not self.IsClick:
            self.event_click_animation()
            self.IsClick = True
            
    def event_click(self,x,y):
        self.event_click_animation()
        self.IsClick = not self.IsClick

    def event_click_animation(self):
        if self.onetime:
            self.pen.fillcolor('Green')
        else:
            if self.CURRENT_COLOR != "Green":
                self.CURRENT_COLOR = "Green"
            else: 
                self.CURRENT_COLOR = "White"

            self.pen.fillcolor(self.CURRENT_COLOR)

    def reset_button(self):
        self.IsClick = False
        self.pen.fillcolor('White')
        self.CURRENT_COLOR = 'White'
        self.text_on_button()
        self.pen.showturtle()
        

    def disable(self):
        self.pen.hideturtle()
        self.pen.clear()


class Text:
    def __init__(self,origin) -> None:
        self.pen = turtle.Turtle()
        self.pen.speed(0)
        self.leftmost_pos = origin
        self.pen.hideturtle()

    def print_text(self,pos,message : str,FONT_SIZE = 12,mode = 'normal'):
        screen.tracer(0)
        self.pen.up()
        self.pen.setpos(self.leftmost_pos[0] + pos[0] + 25,self.leftmost_pos[1] + pos[1] - 20)
        self.pen.down()

        
        self.pen.write(message,font= ('Arial', FONT_SIZE, mode))
        screen.tracer(1)

class Block(Text):
    def __init__(self, origin,shape='square') -> None:
        super().__init__(origin)
        self.pen.shape(shape)
    

    def print_block(self,pos,color_block : str,size :int,message : str,FONT_SIZE = 12,mode = 'normal'):
        self.pen.hideturtle()
        self.print_text(pos,message,FONT_SIZE,mode)

        screen.tracer(0)
        self.pen.width(1)
        self.pen.up()
        self.pen.setpos(self.leftmost_pos[0] + pos[0] - size + 15,self.leftmost_pos[1] + pos[1] -25)
        self.pen.down()

        self.pen.fillcolor(color_block)
        self.pen.begin_fill()

        for i in range(4):
            self.pen.forward(size)           
            self.pen.left(90)
        self.pen.end_fill()
        self.pen.fillcolor('Black')
        screen.tracer(1)