
# ==========================================
#           TIC-TAC-TOE GAME
# ==========================================

def display_board(board):
    print("\n")
    print("     |     |     ")
    print(f"  {board[0]}  |  {board[1]}  |  {board[2]}  ")
    print("_____|_____|_____")
    print("     |     |     ")
    print(f"  {board[3]}  |  {board[4]}  |  {board[5]}  ")
    print("_____|_____|_____")
    print("     |     |     ")
    print(f"  {board[6]}  |  {board[7]}  |  {board[8]}  ")
    print("     |     |     ")
    print()


def check_winner(board, player):
    winning_positions = [
        (0, 1, 2),  # Top row
        (3, 4, 5),  # Middle row
        (6, 7, 8),  # Bottom row
        (0, 3, 6),  # Left column
        (1, 4, 7),  # Middle column
        (2, 5, 8),  # Right column
        (0, 4, 8),  # Diagonal
        (2, 4, 6)   # Diagonal
    ]

    for a, b, c in winning_positions:
        if board[a] == player and board[b] == player and board[c] == player:
            return True

    return False


def check_draw(board):
    return all(position in ["X", "O"] for position in board)


def get_move(board, player):
    while True:
        try:
            move = int(input(f"Player {player}, enter position (1-9): "))

            if move < 1 or move > 9:
                print("❌ Please enter a number from 1 to 9.")
                continue

            index = move - 1

            if board[index] in ["X", "O"]:
                print("❌ That position is already taken. Choose another.")
                continue

            return index

        except ValueError:
            print("❌ Invalid input. Please enter a number from 1 to 9.")


def play_game():
    board = ["1", "2", "3",
             "4", "5", "6",
             "7", "8", "9"]

    current_player = "X"

    print("\n================================")
    print("       TIC-TAC-TOE GAME")
    print("================================")

    print("\nBoard positions:")
    display_board(board)

    # Change numbers into empty spaces after displaying
    board = [" ", " ", " ",
             " ", " ", " ",
             " ", " ", " "]

    while True:
        display_board(board)

        move = get_move(board, current_player)
        board[move] = current_player

        # Check if current player won
        if check_winner(board, current_player):
            display_board(board)
            print(f"🎉 Player {current_player} WINS!")
            break

        # Check for draw
        if check_draw(board):
            display_board(board)
            print("🤝 The game is a DRAW!")
            break

        # Switch player
        if current_player == "X":
            current_player = "O"
        else:
            current_player = "X"


def main():
    while True:
        play_game()

        print("\nWould you like to play again?")
        choice = input("Enter Y for Yes or N for No: ").strip().lower()

        if choice != "y":
            print("\nThanks for playing Tic-Tac-Toe! 👋")
            break


# Start the game
if __name__ == "__main__":
    main()
