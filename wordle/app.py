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
                self.map[self.word[i]] += 1
            else:
                self.map[self.word[i]] = 1
    
    def __repr__(self):
        return f"Attempt #{self.attempt}/6!"
    
    def display_board(self):
        for r in range(len(self.board)):
            for c in range(len(self.board[0])):
                print(self.board[r][c], end=" ")
            print()
    def play(self):
        success = False
        while self.attempt < 7 and not success:
            success = self.make_guess()

    def make_guess(self):
        while(True):
            guess = input("Enter your 5 letter guess: ")

            if len(guess) != 5:
                print("Guesses must be 5 letters long. Please try again")
                continue

            elif not guess.isalpha():
                print("Only letters allowed. Please try again")
                continue


            guess = guess.lower()
            

            for i in range(self.attempt):
                if "".join(self.board[i]) == guess:
                    print("You've already guessed that word! Please try again")
                    break
            else:
                print(f'Your guess: {guess}')

                for j in range(5):
                    if guess[j] == self.word[j]:
                        self.board[self.attempt-1][j] = guess[j].upper()
                    elif guess[j] in self.word:
                         self.board[self.attempt-1][j] = guess[j]+ str(1)
                    else:
                        self.board[self.attempt-1][j] = guess[j]
                
                self.attempt +=1
                self.display_board()
                if guess == self.word:
                    print("Congratulations, you've guessed the word!")
                    return True
                else:
                    return False
        

if __name__ == "__main__":
    game = WordleGame()
    print(game)
    game.display_board()

    game.play()
    