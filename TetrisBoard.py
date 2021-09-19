from PositionalVectors import Vector2
import ShapeRectBorder
import Shapes

# creating tetris board
class TetrisBoard():
    # constructor
    def __init__(self):
        # creating 2d array for board, 20, 10, 0 means nothing there, 1 means something is there, 2 means active piece
        self.board = [
            [2,1,1,1,1,1,1,1,1,1],
            [2,0,0,0,0,0,0,0,0,1],
            [2,0,0,0,0,0,0,0,0,1],
            [2,0,0,0,0,0,0,0,0,1],
            [2,0,0,0,0,0,0,0,0,1],
            [2,0,0,0,0,0,0,0,0,1],
            [2,0,0,0,0,0,0,0,0,1],
            [2,0,0,0,0,0,0,0,0,1],
            [2,0,0,0,0,0,0,0,0,1],
            [2,0,0,0,0,0,0,0,0,1],
            [2,0,0,0,0,0,0,0,0,1],
            [2,0,0,0,0,0,0,0,0,1],
            [2,0,0,0,0,0,0,0,0,1],
            [2,0,0,0,0,0,0,0,0,1],
            [2,0,0,0,0,0,0,0,0,1],
            [2,0,0,0,0,0,0,0,0,1],
            [2,0,0,0,0,0,0,0,0,1],
            [2,0,0,0,0,0,0,0,0,1],
            [2,0,0,0,0,0,0,0,0,1],
            [2,0,0,0,0,0,0,0,0,1]]


    # creating basic move functions, not permenent since it will only affect 1 square
    def moveRight(self,x,y):
        
        # using an if statement to check if x will go over the array
        if y <= 8:
            print(x)
            print(y)
            try : 
                self.board[y+1][x] = self.board[x][y]

            except IndexError:
                print(-1)

        
        # using else to check if the prevouis statement is true
        else:
            self.board[y][0] = self.board[y][x]
        
        # setting the prevouis piece to 0
        self.board[y][x] = 0
        

    # creating update function, ran every frame
    def update(self):
        # clearing all the shapes
        Shapes.tetrisBoard.clear()


        # looping through tetris board, x
        for x in range(10):
            # looping through tetris board, y
            for y in range(20):
                # creating the selected tile
                selectedtile = self.board[y][x]
                print(selectedtile, " x: ",x," y: ", y)
                # checking if the number is 1, numbers can convert into bool, in this case 1 is true and 0 is false
                if selectedtile:
                    # adding color
                    if selectedtile == 1:
                        color = (120,120,120)
                    
                    if selectedtile == 2:
                        color = (0,0,120)


                    # adding the pieces to an array
                    Shapes.tetrisBoard.append(ShapeRectBorder.RectBorder( Vector2(x*32.5+560, 650- y * 32.5), Vector2(25,25), color, 5, (0,0,0) ))


# creating the variable of the tetris board
tetrisBoard = TetrisBoard()