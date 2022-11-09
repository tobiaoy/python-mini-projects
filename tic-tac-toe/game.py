from player import HumanPlayer, RandomComputerPlayer, GeniusComputerPlayer
import time

class TicTacToe:
    def __init__(self):
        self.board = [' ' for  _ in range(9)] #use a single list to rep a 3x3 board
        self.current_winner = None
        
    def print_board(self):
        # this is just getting the rows
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')
            
    def empty_squares(self):
        return ' ' in self.board # returns boolean
    
    def num_empty_squares(self):
        return len(self.available_moves()) # or return self.board.count because it's a list
            
    @staticmethod
    def print_board_nums():
        # 0 | 1 | 2 etc (tells us what number corresponds to what box)
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | ' + ' |')
        
    def available_moves(self):
        # return []
        moves = []
        for (i,x) in enumerate(self.board): # enumerate is essentially going to create a list and assign tuples that have the 'index, the value' at that index
            # ['x', 'x' , 'o'] --> [(0, 'x'), (1, 'x'), (2, 'o')]
            if x == ' ':
                moves.append(i)
        return moves
        # alternatively -> return [i for i,x in enumerate(self.board) if spot == ' ']  
        
    def winner(self, square, letter):
        # winner if 3 in a row anywhere.. we have to check all of these!
        # first let's check the row
        row_ind = square // 3
        row = self.board[row_ind*3 : (row_ind + 1) * 3]
        if all([spot == letter for spot in row]): # look into list comprehension
            return True
        
        #check column
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([spot == letter for spot in column]): # look into list comprehension
            return True
        
        # check diagonals
        # but only if the square is an even number (0, 2, 4, 6, 8)
        # these are the only moves possible to win diagonal
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]] # left to right
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]] # right to left
            if all([spot == letter for spot in diagonal2]):
                return True
            
        # if all these checks fail, we don't have a winner
        
    def make_move(self, square, letter):
        # if valid move, then make the move (assign square to letter)
        # then return true. if invalid, return false
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False
    

        
def play(game, x_player, o_player, print_game=True):
    # returns the winner of the game(the letter)! or None for a tie
    if print_game:
        game.print_board_nums()
        
                
    letter = 'X' # starting letter
    # iterate while the game still has empty squares
    # (we don't have to worry about the winner because we'll just return that
    # which breaks the loop)
    
    while game.empty_squares():
        # get the move from the appropriate player
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)
            
        #define a function to make a move
        if game.make_move(square, letter):
            if print_game:
                print(letter + f' makes a move to square {square}')
                game.print_board()
                print('') #just empty line
                
            if game.current_winner:
                if print_game:
                    print(letter + ' wins!')
                return letter
                
            # after we made our move, we need to alternate letters
            letter = 'O' if letter == 'X' else 'X'
            
            #delay after a move
            #time.sleep(0.9)
              
    if print_game:
        print("It's a tie...")
            
if __name__ == '__main__':
    x_wins = 0
    o_wins = 0
    ties = 0
    
    for _ in range(1000):
        x_player = RandomComputerPlayer('X')
        o_player = GeniusComputerPlayer('O')
        t = TicTacToe()
        result = play(t, x_player, o_player, print_game=False)
        
        if result == 'X':
            x_wins += 1
        elif result == 'O':
            o_wins += 1
        else:
            ties += 1
        print(f'After 1000 iterations, we see {x_wins} X wins, {o_wins} O wins, and {ties} ties')
    
        
    