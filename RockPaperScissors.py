import random

NUM_OF_RESPONSES = 3  # default value

rock = "rock"
paper = "paper"
scissors = "scissors"
moves = [rock, paper, scissors]
winmoves = {rock:scissors, paper:rock, scissors:paper}
user_count = 0
cpu_count = 0

def findwinner(user_input, cpu_move):
    if user_input == cpu_move:
        return "computer played " + str(cpu_move) + "\ndraw!"
    elif cpu_move in winmoves[user_input]:
        global user_count
        user_count += 1
        return "computer played " + str(cpu_move) + "\nyou win, computer sad :("
    global cpu_count
    cpu_count += 1
    return "computer played " + str(cpu_move) + "\ncomputer wins, computer happy :)"

def main():
    play_times = NUM_OF_RESPONSES
    user_times = input("How many games do you wanna play ")
    if user_times.isdigit() and int(user_times) < 100:
        play_times = int(user_times)
    else:
        print("lmao ur dumb, imma make you play", NUM_OF_RESPONSES, "times")
    
    while play_times > 0:
        user_input = input("Choose a move ")
        cpu_move = random.choice(moves)
        while user_input not in moves:
            user_input = input("lmao ur dumb, enter a real move ")
        print(findwinner(user_input, cpu_move), "\n")
        play_times -= 1
    print("you won", user_count, "games")
    print("i won", cpu_count, "games\n")
    if user_count > cpu_count:
        print("you win! computer sad :(\n")
    elif cpu_count > user_count:
        print("i win! computer happy :)\n")
    else:
        print("its a draw! we both happy and sad :) :(\n")
    print("thanks for playin")

main()
        
    
    



