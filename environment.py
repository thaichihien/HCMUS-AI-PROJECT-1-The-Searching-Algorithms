import numpy as np

BLOCKED = 2
VISITED = 1

class Maze:
    def __init__(self,size) -> None:    
        self.matrix = np.zeros(size,dtype=int)


    def add_obstacles(self,obstacle_list):
        while obstacle_list:
            obstacle = obstacle_list.pop(0)
            self.add_obstacle(obstacle)

    def add_obstacle(self,points):
        for i in range(len(points)):
            if(i == len(points) - 1):
                self.draw_line(points[i],points[0])
            else: self.draw_line(points[i],points[i+1])


    def draw_line(self,A,B):  #A(x0,y0) ,B(x1,y1)
        xA = A[1]
        yA = A[0]
        xB = B[1]
        yB = B[0]
        result = []

        if not ( 0 <= xA < self.matrix.shape[0] and 0 <= yA < self.matrix.shape[1]      #out of matrix
                and 0 <= xB < self.matrix.shape[0] and 0 <= yB < self.matrix.shape[1]):
                raise Exception("point is out of matrix")
    
        if A == B:      #the same point
            self.matrix[xA,yA] = BLOCKED
            return
            
        self.matrix[xA,yA] = BLOCKED
        self.matrix[xB,yB] = BLOCKED
        draw_vertitial = abs(xB - xA) < abs(yB-yA) 
        if draw_vertitial:
            xA,yA,xB,yB = yA,xA,yB,xB

        if xA > xB :     #draw from left to right
            xA,yA,xB,yB = xB,yB,xA,yA

        
        x = np.arange(xA + 1,xB)
        y = np.round(((yB - yA) / (xB - xA)) * (x - xA) + yA).astype(int)

        #x = x.tolist()
        #y = y.tolist()
        if draw_vertitial: x,y =y,x

        #for x0,y0 in zip(x,y):
            #result.append((x0,y0))
        self.matrix[x,y] = BLOCKED



class FileSystem:
    def __init__(self,filename) -> None:
        file  = open(filename)
        self.resource = file.readlines()
        file.close()

        #First line
        temp = list(map(int,self.resource[0].split(' ')))
        M,N = temp[0],temp[1]
        self.size = (N,M)

        #Second line
        temp = list(map(int,self.resource[1].split(' '))) 
        self.S = (temp[0],temp[1])
        self.G = (temp[2],temp[3])

        #Third line
        n = int(self.resource[2])
        self.obstacle_list = []
        for i in range(n):
            temp = list(map(int,self.resource[3 + i].split(' '))) 
            obstacle = []
            while temp:
                x = temp.pop(0)
                y = temp.pop(0)
                point = (x,y)
                obstacle.append(point)
            self.obstacle_list.append(obstacle)
    
    
    def maze_size(self):
        return self.size

    def source(self):
        return self.S

    def goal(self):
        return self.G

    def obstacles(self):
        return self.obstacle_list