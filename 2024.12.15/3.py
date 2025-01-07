class ChessKing:
  
#Класс, представляющий шахматную фигуру короля.
    
    files = dict(zip('abcdefgh', range(1, 9)))  
    ranks = dict(zip(map(str, range(1, 9)), range(1, 9))) 

    def __init__(self, color: str = 'white', square: str = None):
       
        self.color = color
        if color == 'white':
            self.square = 'e1'
        else:
            self.square = 'e8'

    def __repr__(self) -> str:
     
    # Машиночитаемое строковое представление объекта.
        if self.color == 'white':
            color_prefix = 'W'
        else:
            color_prefix = 'B'
        return f"{color_prefix}K: {self.square}"

    def __str__(self) -> str:
        
    # Человекочитаемое строковое представление объекта.

        return self.__repr__()

    def is_turn_valid(self, new_square: str) -> bool:
        
    # Проверяет, возможен ли ход с текущего поля на новое.

        current_file = self.square[0]
        current_rank = int(self.square[1])
        new_file = new_square[0]
        new_rank = int(new_square[1])
        
    # Вычисляет разницу между текущими и новыми координатами

        file_diff = abs(self.files[new_file] - self.files[current_file])
        rank_diff = abs(new_rank - current_rank)
    # Проверяет, что ход возможен
        is_valid_move = (file_diff <= 1 and rank_diff <= 1) and (file_diff + rank_diff > 0)
        return is_valid_move

    def turn(self, new_square: str) -> None:
       
    # Выполняет ход на новое поле
        if not self.is_turn_valid(new_square):
           raise ValueError 
        self.square = new_square

#wk = ChessKing()
#wk.color
#'white'
#wk.square
#'e1'
#>>>
#wk.turn('e2')
#wk
#'WK: e2'
#>>>
#wk.turn('d4')  
#
#ValueError
#>>> 
#bk = ChessKing('black')
#print(bk)
#BK: e8
