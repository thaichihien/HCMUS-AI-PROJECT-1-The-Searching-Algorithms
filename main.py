import search_algorithm as sa,visualization as vs
from environment import Maze,FileSystem



input_resource = FileSystem('input.txt')
ORIGIN_MATRIX = (-150,-300)
ORIGIN_MENU = (-700,-300)


def information():
    text_pen = vs.Text(ORIGIN_MENU)
    text_pen.print_text((100,680),'University of Science - VNUHCM',FONT_SIZE=11)
    text_pen.print_text((0,640),'PROJECT 1: The Searching Algorithm',FONT_SIZE=19,mode='bold')
    text_pen.print_text((0,610),'Subject: Fundamentals of Artificial Intelligence')
    text_pen.print_text((0,585),'Implemented by : Thai Chi Hien')
    text_pen.print_text((0,560),'Lecture: Pham Trong Nghia')
    text_pen.print_text((0,535),'TA: Nguyen Thai Vu')

    text_pen.print_text((0,500),'Please edit the matrix, starting point, ending point and',FONT_SIZE=14)
    text_pen.print_text((138,478),'input.txt',FONT_SIZE=14,mode='underline')
    text_pen.print_text((0,478),'obstacles in the               file located in the same',FONT_SIZE=14)
    text_pen.print_text((0,456),'directory as this source file',FONT_SIZE=14)

    text_pen.print_text((0,425),'Choose one of the algorithms below to find the path:',FONT_SIZE=14)

    note_block = vs.Block(ORIGIN_MENU)
    note_block.print_block((50,130),vs.COLOR_START_POINT,30,'Starting Point')
    note_block.print_block((250,130),vs.COLOR_END_POINT,30,'Goal Point')
    note_block.print_block((50,90),vs.COLOR_OBSTACLE_POINT,30,'Obstacle Point')
    note_block.print_block((250,90),vs.COLOR_VISITED_POINT,30,'Visited Point')



def disable_allbuttons(current_button,search,robot):
    cost_text.pen.clear()
    if search != None:
        search.clear()
        robot.reset()
    for butt in button:
        if butt == current_button:continue
        butt.disable()

def enable_allbuttons():
    for butt in button:
        butt.reset_button()

#set up maze
test_maze = Maze(input_resource.maze_size())
test_maze.add_obstacles(input_resource.obstacles())
#test_maze.add_obstacle([(3,6),(5,6),(5,2),(3,2)])
map_maze = vs.Matrix(ORIGIN_MATRIX)
map_maze.draw(test_maze.matrix)
map_maze.draw_start_goal(input_resource.source(),input_resource.goal())
robot = vs.Robot(ORIGIN_MATRIX,map_maze.size)
cost_text = vs.Text(ORIGIN_MENU)
search = sa.SearchAlgorithm(test_maze.matrix,map_maze)
path_to_goal = []
cost_path = 0
cost_expanded = 0


#set up buttons and corresponding functions
button = (vs.Button(ORIGIN_MENU,'Breadth-first search'),
          vs.Button(ORIGIN_MENU,'Uniform-cost search'),
          vs.Button(ORIGIN_MENU,'Iterative deepening search'),
          vs.Button(ORIGIN_MENU,'Greedy-best first search'),
          vs.Button(ORIGIN_MENU,'Graph-search A*')
          )


function_run = { 0:search.find_BFS,
                 1:search.find_UCS,
                 2:search.find_IDS,
                 3:search.find_GBFS,
                 4:search.find_ASS,
                }


#set up buttons UI
first_pos_button = (50,380)
for i,butt in enumerate(button):
    butt.create((first_pos_button[0],first_pos_button[1] - 50*i))


#main
information()
active = 0
while True:
    try:
        for i,butt in enumerate(button):
            butt.update()
          

            if butt.result():
                disable_allbuttons(butt,search,robot)
                path_to_goal,cost_path,cost_expanded = function_run[i](input_resource.source(),input_resource.goal())
                robot.play(path_to_goal)
                cost_text.print_text((0,40),'Cost of the path : {0}'.format(cost_path),FONT_SIZE=15,mode = 'bold')
                cost_text.print_text((0,10),'Cost of the expanded node : {0}'.format(cost_expanded),FONT_SIZE=15,mode = 'bold')
                enable_allbuttons()

    except:
        break