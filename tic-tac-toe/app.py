import numpy as np

def new_game():
    
    print("---------Welcome to Tic-Tac-Toe---------")
    player_1_name: str = input("Enter Player 1's name: ")
    player_2_name: str = input("Enter Player 2's name: ")
    sides = {'X':player_1_name, 'O': player_2_name}
    opposite_side = {'X': 'O', 'O': 'X'}

    board = ChessBoard(sides=sides )
    print(board)

    board.display_board()
    while (not board.board_is_full() and not board.is_win(opposite_side[board.turn])):
        board.take_turn()
    print(f"{board.sides[opposite_side[board.turn]]} wins!!!")

class ChessBoard:
    def __init__(self, sides ):
        self.sides = sides
        self.board = [["_"] * 3 for _ in range(3)]
        self.turn = 'X'

    def __repr__(self):
        resp = ""
        player_num = 1
        for side in self.sides:
            resp +=(f"P{player_num} ({self.sides[side]}) is using {side}\n")
            player_num+=1
        return resp
    
    def display_board(self):
        for r in range(len(self.board)):
            
            for c in range(len(self.board[0])):
                print('  ',self.board[r][c], end="")
            print()
        print()
    
    def board_is_full(self):
        for r in range(len(self.board)):
            for c in range(len(self.board[0])):
                if self.board[r][c] == '_':
                    return False
        return True
    
    def is_win(self, player):

            # check if horizontal win
            for r in range(len(self.board)):
                if self.board[r] == [player, player, player]:
                    return True

            # check if diagonal win
            if player == self.board[0][0] == self.board[1][1] == self.board[2][2] or player == self.board[0][2] == self.board[1][1] == self.board[2][0]:
                return True
            
            # check vertical 
            for c in range(len(self.board)):
                if player == self.board[0][c] == self.board[1][c] == self.board[2][c]:
                    return True
            
            return False
            
    def take_turn(self):
        while True:
            user_input: str = input(f"{self.sides[self.turn].upper()} Enter a tuple of your coordinates for your turn [i.e. 1,2]: ")
            if user_input: 
                coordinates = user_input.split(',')
                if coordinates.__len__() != 2:
                    print("Incorrect number of arguments. Please give 2.")
                    continue
                elif not coordinates[0].isnumeric() or not coordinates[1].isnumeric():
                    print("Please enter numbers.")
                    continue
                coordinates = [int(coordinates[0].strip()), int(coordinates[1].strip())]

                if coordinates[0] not in range(3) or coordinates[1] not in range(3):
                    print("Indexes provided are out of range. Please consider numbers from 0 to 2 only")
                    continue

                elif self.board[coordinates[0]][coordinates[1]] == '_':
                    self.board[coordinates[0]][coordinates[1]] = self.turn
                    break
                else:
                    print('That spot is already taken. Please try again')
                    continue
            else:
                print('Please enter a valid coordinates in format: #,#')
                continue

        # change turn
        if self.turn == 'X':
            self.turn = 'O'
        else:
            self.turn = 'X'
        self.display_board()
        

        


if __name__ == "__main__":
    new_game()