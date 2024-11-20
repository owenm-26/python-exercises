# need random 6 letter word

# need a hashmap of letters in word

# need 6x6 grid of letter tries

# cant guess anything less than 6 letters or same word twice or a non-word

class WordleGame:
    def __init__(self):
        self.board = [["_"] * 5 for _ in range(6)]
        self.attempt = 1
        self.word = "stark"
        self.map = {}
        for i in range(len(self.word)):
            if self.word[i] in self.map:
                self.map[self.word[i]] += i
            else:
                self.map[self.word[i]] = i
    
    def __repr__(self):
        return f"Attempt #{self.attempt}/6!"
    
    def display_board(self):
        for r in range(len(self.board)):
            for c in range(len(self.board[0])):
                print(self.board[r][c], end=" ")
            print()

if __name__ == "__main__":
    game = WordleGame()
    print(game)
    game.display_board()
    