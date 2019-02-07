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
        print("Guess which artist sings the following song:")
        print(str(song) + "\n")
        ans = input("Type your answer here: ")
        if (ans.lower() in artist.lower()) and len(ans) > 2:
            print("Congrats! You guessed the correct artist :)\n")
        else:
            print("Incorrect! The correct answer was " + artist + "\n")
        again = input("Would you like to play again? (y/n)? ")
        if again == "y":
            play = True
        elif again == "n":
            play = False
        else:
            print("Not a valid input. Game over.")
            play = False

main()