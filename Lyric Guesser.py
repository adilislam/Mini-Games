import random
from openpyxl import load_workbook


def main():
    wb = load_workbook('./songs.xlsx')
    sheet = wb['Sheet1']
    play = True
    while play == True:
        num = random.randint(500,710)
        song = sheet['A' + str(num)].value
        artist = sheet['B' + str(num)].value
        lyric = sheet['C' + str(num)].value
        lyric = lyric[0:150]
        print("Guess which song the following song lyric comes from:")
        print(str(lyric) + "\n")
        ans = input("Type your answer here: ")
        if song.lower() == ans.lower():
            print("Congrats! You guessed the correct song :)\n")
        else:
            print("Incorrect! The correct answer was " + song + " by " + artist + "\n")
        again = input("Would you like to play again? (y/n)? ")
        if again == "y":
            play = True
        elif again == "n":
            play = False
        else:
            print("Not a valid input. Game over.")
            play = False

main()