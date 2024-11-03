class Cells:
    def __init__(self, x, y, type,is_Solve)->None:
        self.x = x
        self.y = y
        self.is_Solve = is_Solve
        self.initial_type = type 
        self.current_type = type  
    def __str__(self) -> str:
        if self.current_type == "iron":
            return ' ⚫ ' if not self.is_Solve else ' 🟤 '
        elif self.current_type == "attract":
            return ' 🔴 ' if not self.is_Solve else ' 🟢 '
        elif self.current_type == "repel":
            return ' 🟣 ' if not self.is_Solve else ' 🔵 '
        elif self.current_type == "solve":
            return ' ⚪ ' 
        elif self.current_type == "road":
            return ' 🟡 ' if not self.is_Solve else ' ⚪ '
        else:
            return ' ❌ '