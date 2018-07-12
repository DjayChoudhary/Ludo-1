class Color:

    GREEN = '#0CED2C'
    RED = '#F71313'
    YELLOW = '#FFFF00'
    BLUE = '#3575EC'
    DEFAULT = '#E9E9E9'
    CYAN = '#4EB1BA'
    GRAY = '#A9A9A9'


class Board:

    SQUARE_SIZE = 40
    PANEL_WIDTH = 1.5 * Board.SQUARE_SIZE0
    PANEL_HEIGHT = 640
    BOARD_WIDTH = 640
    BOARD_HEIGHT = 640
    POINTS = [(0, 0), (0, 1), (1, 0), (1, 1)]
    POSITIVE_V = [(6, 2), (8, 1), (6, 13), (8, 12)]
    POSITIVE_H = [(1, 6), (2, 8), (13, 8), (12, 6)]


class Text:

    MADE_BY = 'Made By: Mansi Agrawal & Shivam Gupta'
    HEADER =  'LUDO - THE GAME'


class Path:

    def __init__(self):

        self.green_path = []
        self.red_path = []
        self.blue_path = []
        self.yellow_path = []
        self.gx = None
        self.gy = None 
        self.ry = None
        self.by = None
        self.count = None


    def update_coordinates(self, gx, gy, ry, by, count):

        self.gx = gx
        self.gy = gy
        self.ry = ry
        self.by = by
        self.count = count

    def start_populating(self):

        #1
        self.update_coordinates(60, 20, 540, 340, 5)
        self.direct(pow_index=0, direction='right')
        #2
        self.update_coordinates(260, 220, 340, 380, 5)
        self.direct(pow_index=3, direction='up')
        #3
        self.update_coordinates(260, 20, 340, 580, 3)
        self.direct(direction='right') 
        #4
        self.update_coordinates(340, 60, 260, 540, 5)
        self.direct(pow_index=0, direction='down')
        #5
        self.update_coordinates(380, 260, 220, 340, 5)
        self.direct(pow_index=3, direction='right')
        #6
        self.update_coordinates(580, 260, 20, 340, 3)
        self.direct(direction='down')
        #7
        self.update_coordinates(540, 340, 60, 260, 5)
        self.direct(pow_index=0, direction='left')
        #8
        self.update_coordinates(360, 380, 260, 220, 5)
        self.direct(pow_index=3, direction='down')
        #9
        self.update_coordinates(340, 580, 260, 20, 3)
        self.direct(direction='left')
        #10
        self.update_coordinates(260, 540, 340, 60, 5)
        self.direct(pow_index=0, direction='up')
        #11
        self.update_coordinates(220, 340, 380, 260, 6)
        self.direct(pow_index=3, direction='left')
        #12
        self.update_coordinates(20, 300, 580, 300, 6)
        self.direct(direction='right')

    def direct_horizontal(self, pow_index = -1, k):

        for i in range(self.count):
            if i == pow_index:
                p = 1
            else:
                p = 0
            self.green_path.append((gx  +  k*i*Board.SQUARE_SIZE, gy, p))
            self.red_path.append((gy, ry  -  k*i*Board.SQUARE_SIZE, p))
            self.blue_path.append((ry - k*i*Board.SQUARE_SIZE, by, p))
            self.yellow_path.append((by, gx + k*i*Board.SQUARE_SIZE, p))

     def direct_vertical(self, pow_index = -1, k):

        for i in range(self.count):
            if i == pow_index:
                p = 1
            else:
                p = 0
            self.green_path.append((gx, gy - k*i*Board.SQUARE_SIZE, p))
            self.red_path.append((gy - k*i*Board.SQUARE_SIZE,ry, p))
            self.blue_path.append((ry, by + k*i*Board.SQUARE_SIZE, p))
            self.yellow_path.append((by + k*i*Board.SQUARE_SIZE, gx, p))
 

    def direct(self, direction, pow_index = -1):
        if direction=='right':
            self.direct_horizontal(pow_index, 1)
        elif direction=='left':
            self.direct_horizontal(pow_index, -1)
        elif direction=='down':
            self.direct_vertical(pow_index, -1)
        else:
            self.direct_vertical(pow_index, 1)

path = Path()
path.start_populating()
