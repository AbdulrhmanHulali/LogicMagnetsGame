import copy

class Game:
    def __init__(self, init_state) -> None:
        self.state = init_state
        self.history = [init_state]  

    def canMove(self, state, x, y):
        if x < 0 or x >= state.rows or y < 0 or y >= state.cols:
            return False
        cell_type = state.board[x][y].current_type
        return cell_type == 'road' or cell_type == 'solve'

    def move(self, state, x, y, old_x, old_y, magnet_type):
        new_state = copy.deepcopy(state)
        new_state.board[old_x][old_y].current_type = 'road'
    
        if magnet_type == "repel":
            new_state.board[x][y].current_type = 'repel'
        else:
            new_state.board[x][y].current_type = magnet_type

        if new_state.board[x][y].initial_type == 'solve':
            new_state.board[x][y].current_type = 'repel'

        self.history.append(new_state)
        return new_state



    def attract(self, state, x, y):
        new_state = copy.deepcopy(state)

    
        for i in range(x - 1, -1, -1):
            if new_state.board[i][y].current_type == "iron":
                new_state.board[i][y].current_type = 'road'
                new_state.board[i + 1][y].current_type = 'iron'
            elif new_state.board[i][y].current_type == "repel":
                new_state.board[i][y].current_type = 'road'
                new_state.board[i + 1][y].current_type = 'repel'
                break
            elif new_state.board[i][y].current_type != "road":
                break

        for i in range(x + 1, new_state.rows):
            if new_state.board[i][y].current_type == "iron":
                new_state.board[i][y].current_type = 'road'
                new_state.board[i - 1][y].current_type = 'iron'
            elif new_state.board[i][y].current_type == "repel":
                new_state.board[i][y].current_type = 'road'
                new_state.board[i - 1][y].current_type = 'repel'
                break
            elif new_state.board[i][y].current_type != "road":
                break

        for j in range(y - 1, -1, -1):
            if new_state.board[x][j].current_type == "iron":
                new_state.board[x][j].current_type = 'road'
                new_state.board[x][j + 1].current_type = 'iron'
            elif new_state.board[x][j].current_type == "repel":
                new_state.board[x][j].current_type = 'road'
                new_state.board[x][j + 1].current_type = 'repel'
                break
            elif new_state.board[x][j].current_type != "road":
                break

        for j in range(y + 1, new_state.cols):
            if new_state.board[x][j].current_type == "iron":
                new_state.board[x][j].current_type = 'road'
                new_state.board[x][j - 1].current_type = 'iron'
            elif new_state.board[x][j].current_type == "repel":
                new_state.board[x][j].current_type = 'road'
                new_state.board[x][j - 1].current_type = 'repel'
                break
            elif new_state.board[x][j].current_type != "road":
                break

        self.history.append(new_state)
        return new_state  

    def repel(self, state, x, y, description):
        new_state = copy.deepcopy(state)

        for j in range(y - 1, -1, -1):
            if new_state.board[x][j].current_type == "iron":
                if j > 0 and new_state.board[x][j - 1].current_type == "iron":
                    if new_state.in_board(x, j - 2) and new_state.board[x][j - 2].current_type in ["road", "solve"]:
                        new_state.board[x][j - 2].current_type = "iron"
                        new_state.board[x][j - 1].current_type = "iron"
                        new_state.board[x][j].current_type = "road"
                    break
                elif new_state.in_board(x, j - 1) and new_state.board[x][j - 1].current_type in ["road", "solve"]:
                    new_state.board[x][j - 1].current_type = "iron"
                    new_state.board[x][j].current_type = "road"
                break
            elif new_state.board[x][j].current_type == "attract":
                if new_state.in_board(x, j - 1) and new_state.board[x][j - 1].current_type in ["road", "solve"]:
                    new_state.board[x][j - 1].current_type = "attract"
                    new_state.board[x][j].current_type = "road"
                break

        for j in range(y + 1, new_state.cols):
            if new_state.board[x][j].current_type == "iron":
                if j < new_state.cols - 1 and new_state.board[x][j + 1].current_type == "iron":
                    if new_state.in_board(x, j + 2) and new_state.board[x][j + 2].current_type in ["road", "solve"]:
                        new_state.board[x][j + 2].current_type = "iron"
                        new_state.board[x][j + 1].current_type = "iron"
                        new_state.board[x][j].current_type = "road"
                    break
                elif new_state.in_board(x, j + 1) and new_state.board[x][j + 1].current_type in ["road", "solve"]:
                    new_state.board[x][j + 1].current_type = "iron"
                    new_state.board[x][j].current_type = "road"
                break
            elif new_state.board[x][j].current_type == "attract":
                if new_state.in_board(x, j + 1) and new_state.board[x][j + 1].current_type in ["road", "solve"]:
                    new_state.board[x][j + 1].current_type = "attract"
                    new_state.board[x][j].current_type = "road"
                break

        for i in range(x - 1, -1, -1):
            if new_state.board[i][y].current_type == "iron":
                if i > 0 and new_state.board[i - 1][y].current_type == "iron":
                    if new_state.in_board(i - 2, y) and new_state.board[i - 2][y].current_type in ["road", "solve"]:
                        new_state.board[i - 2][y].current_type = "iron"
                        new_state.board[i - 1][y].current_type = "iron"
                        new_state.board[i][y].current_type = "road"
                    break
                elif new_state.in_board(i - 1, y) and new_state.board[i - 1][y].current_type in ["road", "solve"]:
                    new_state.board[i - 1][y].current_type = "iron"
                    new_state.board[i][y].current_type = "road"
                break
            elif new_state.board[i][y].current_type == "attract":
                if new_state.in_board(i - 1, y) and new_state.board[i - 1][y].current_type in ["road", "solve"]:
                    new_state.board[i - 1][y].current_type = "attract"
                    new_state.board[i][y].current_type = "road"
                break

        for i in range(x + 1, new_state.rows):
            if new_state.board[i][y].current_type == "iron":
                if i < new_state.rows - 1 and new_state.board[i + 1][y].current_type == "iron":
                    if new_state.in_board(i + 2, y) and new_state.board[i + 2][y].current_type in ["road", "solve"]:
                        new_state.board[i + 2][y].current_type = "iron"
                        new_state.board[i + 1][y].current_type = "iron"
                        new_state.board[i][y].current_type = "road"
                    break
                elif new_state.in_board(i + 1, y) and new_state.board[i + 1][y].current_type in ["road", "solve"]:
                    new_state.board[i + 1][y].current_type = "iron"
                    new_state.board[i][y].current_type = "road"
                break
            elif new_state.board[i][y].current_type == "attract":
                if new_state.in_board(i + 1, y) and new_state.board[i + 1][y].current_type in ["road", "solve"]:
                    new_state.board[i + 1][y].current_type = "attract"
                    new_state.board[i][y].current_type = "road"
                break

        self.history.append((new_state, description))
        return new_state

    def moveAttract(self, x, y):
        attract_x, attract_y = self.state.getAttractCoord()
        if attract_x is not None and attract_y is not None and self.canMove(self.state, x, y):
            self.state = self.move(self.state, x, y, attract_x, attract_y, "attract")
            self.state = self.attract(self.state, x, y)  
        else:
            print('Invalid move for attract magnet!')

    def moveRepel(self, x, y):
        repel_x, repel_y = self.state.getRepelCoord()
        if repel_x is not None and repel_y is not None and self.canMove(self.state, x, y):
            self.state = self.move(self.state, x, y, repel_x, repel_y, "repel")
            self.state = self.repel(self.state, x, y, "Repel move") 
        else:
            print('Invalid move for repel magnet!')

    def printHistory(self):
        print("\nHistory of moves:")
        for index, item in enumerate(self.history):
            print(f"\nMove {index + 1}:")
            if isinstance(item, tuple):
                state, description = item
                print(description)
                print(state)  
            else:
                print(item)

    def checkWin(self):
        for row in self.state.board:
            for cell in row:
                if cell.current_type == "road" and cell.is_Solve:
                    return False  
        return True  

    def play(self):
        while True:
            print(str(self.state))
            if self.checkWin():
                print("Congratulations! You've won the game!")
                self.printHistory()
                break

            move_type = input("Enter 'attract' to move the red magnet or 'repel' to move the purple magnet: ")
            new_x = int(input("Enter the new x-coordinate for the magnet: "))
            new_y = int(input("Enter the new y-coordinate for the magnet: "))

            if move_type == 'attract':
                self.moveAttract(new_x, new_y)
            elif move_type == 'repel':
                self.moveRepel(new_x, new_y)
            else:
                print("Invalid input. Please enter 'attract' or 'repel'.")

