class State:
    def __init__(self, rows, cols, board) -> None:
        self.rows = rows
        self.cols = cols
        self.board = board

    def __str__(self) -> str:
        result = ""
        for row in self.board:
            for cell in row:
                result += str(cell) + " "
            result += "\n"  
        return result
    def in_board(self, x, y):
        return 0 <= x < self.rows and 0 <= y < self.cols
    def getAttractCoord(self):
        for row in self.board:
            for cell in row:
                if cell.current_type == "attract":
                    return cell.x, cell.y

    def getRepelCoord(self):
        for row in self.board:
            for cell in row:
                if cell.current_type == "repel":
                    return cell.x, cell.y 