from enum import Enum

class PieceType(Enum):
    X = 'X'
    O = 'O'


class PlayingPiece:

    def __init__(self, type: PieceType):
        self.type = type
    
    def __str__(self):
        if self.type == PieceType.X:
            return "X"
        return "O"
    

class PieceX(PlayingPiece):
    def __init__(self):
        super().__init__(PieceType.X)
    
    def __str__(self):
        return "X"

class PieceO(PlayingPiece):
    def __init__(self):
        super().__init__(PieceType.O)
    
    def __str__(self):
        return "O"

#############################
class Player():
    def __init__(self, name: str, piece: PlayingPiece):
        self.name = name
        self.piece = piece
        self.rowCounts = defaultdict(int)
        self.colCounts = defaultdict(int)
        self.forwardDiagonalCounts = 0
        self.backwardDiagonalCounts = 0

#############################
from collections import defaultdict
class Board:

    def __init__(self, size):
        self.size = size
        self.board = [[' ' for _ in range(size)] for _ in range(size)]
        self.empty_positions = size**2


    def place_move(self, player: Player, row, column):
        if self.board[row][column] != " ":
            print("Invalid move, please try again!")
            return False
        self.empty_positions-=1
        self.board[row][column] = player.piece
        return True

    def display_board(self): 
        for i in range(self.size):
            print(" | ".join([str(val) for val in self.board[i]]))
        
    
    def check_win(self, player, row, column):
        player.rowCounts[row]+=1
        player.colCounts[column]+=1

        if row == column:
            player.backwardDiagonalCounts+=1
        if row + column == self.size - 1:
            player.forwardDiagonalCounts+=1
        
        if player.rowCounts[row] == self.size or player.colCounts[column] == self.size or player.backwardDiagonalCounts == self.size or player.forwardDiagonalCounts == self.size:
            return True
        return False


#############################

from abc import ABC, abstractmethod
from collections import deque
class Game:
    def __init__(self, board: Board, players: list[Player]):
        if len(players) < 2:
            raise ValueError("There should be at least two players to play the game.")
        self.board = board
        self.players = players
        self.turn = deque(players)
        self.result = None
        print("Game has been initialized")

    @abstractmethod
    def start(self):
        pass

class TicTacToeGame(Game):
    def __init__(self, board: Board, players: list[Player]):
        super().__init__(board, players)

    def start(self):
        while not self.result:
            next_player = self.turn.popleft()
            try:
                row, column = map(int, input(f"{next_player.name}, enter move (row,col): ").split(","))
                if not (0 <= row < self.board.size and 0 <= column < self.board.size):
                    raise ValueError()
            except ValueError:
                print("Invalid input. Please enter a valid row and column within board bounds.")
                self.turn.appendleft(next_player)
                continue
            placedSuccessfully = self.board.place_move(next_player, int(row), int(column))
            if placedSuccessfully:
                self.board.display_board()
                isWin = self.board.check_win(next_player, row, column)
                if isWin:
                    self.result = f"{next_player.name} won!"
                else:
                    if self.board.empty_positions == 0:
                        self.result = f"Game is a tie!"
                    self.turn.append(next_player)
            else:
                self.turn.appendleft(next_player)
        
        print(f"Result: {self.result}")


playerX = Player("Akshay", PieceX())
playerO = Player("Random", PieceO())
board = Board(3)
tictactoe_game = TicTacToeGame(board, [playerX, playerO])
tictactoe_game.start()  