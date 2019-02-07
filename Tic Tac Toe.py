board = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def make_board():
    print('|' + str(board[0]) + '|' + str(board[1]) + '|' + str(board[2]) + '|')
    print(' -----')
    print('|' + str(board[3]) + '|' + str(board[4]) + '|' + str(board[5]) + '|')
    print(' -----')
    print('|' + str(board[6]) + '|' + str(board[7]) + '|' + str(board[8]) + '|')


def play(team):
    spot = input("Player " + team + ": Where would you like to place your piece (enter a value 1-9)? ")
    if board[int(spot) - 1] != 'x' and board[int(spot) - 1] != 'o':
        board[int(spot) - 1] = team
    else:
        while board[int(spot) - 1] == 'x' or board[int(spot) - 1] == 'o':
            spot = input("Spot has already been taken, try again ")
    board[int(spot) - 1] = team
    make_board()


def find_winner(team):
    return ((board[6] == team and board[7] == team and board[8] == team) or  # across the top
            (board[3] == team and board[4] == team and board[5] == team) or
            (board[0] == team and board[1] == team and board[2] == team) or  # across the bottom
            (board[6] == team and board[3] == team and board[0] == team) or  # down the middle
            (board[7] == team and board[4] == team and board[1] == team) or  # down the middle
            (board[8] == team and board[5] == team and board[2] == team) or  # down the right side
            (board[6] == team and board[4] == team and board[2] == team) or  # diagonal
            (board[8] == team and board[4] == team and board[0] == team))  # diagonal


def main():
    again = True
    while again:
        for x in range(10):
            board[x - 1] = x
        make_board()
        count = 0
        while count < 9:
            if count % 2 == 0:
                play('x')
                count += 1
            else:
                play('o')
                count += 1
            if find_winner('x'):
                count = 10
                print("Congrats, Player x wins!")
            elif find_winner('o'):
                count = 10
                print("Congrats, Player o wins!")
        if count == 9:
            print("It's a draw!")
        ans = input("Would you like to play again? (y/n)? ")
        if ans.lower() == 'y':
            again = True
        else:
            again = False


main()
