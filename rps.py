import random
import time
from playsound import playsound
from random import randint
from time import sleep

def play():
        
    user = input("\nWhat is your choice? 'r' for rock, 'p' for paper, and 's' for scissors: ").lower()
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        print("Waiting for opponent...")
        sleep(randint(1,6))
        print('\nIt\'s a tie\nYour Choice: ' + user + ". Their Choice: " + computer)
        play()

    if is_win(user, computer):
        print("Waiting for opponent...")
        sleep(randint(1,6))
        print('\nYou win!\nYour Choice: ' + user + ". Their Choice: " + computer)
        playsound(r'C:\Users\jetfl\Coding\Rock-Paper-Scissors\Sound\win.wav')
        input("\nPress enter to play again")
        play()

    if is_win(computer, user):
        print("Waiting for opponent...")
        sleep(randint(1,6))
        print('\nYou lost!!\nYour Choice: ' + user + ". Their Choice: " + computer)
        playsound(r'C:\Users\jetfl\Coding\Rock-Paper-Scissors\Sound\lose.wav')
        input("\nPress enter to play again")
        play()
    
    else:
        print("\nError!!!\nYou have to type 'r', 'p', or 's'")
        time.sleep(2)
        input("\nPress enter to continue")
        play()


def is_win(user, computer):
    if (user == 'r' and computer == 's') or (user == 's' and computer == 'p') \
    or (user == 'p' and computer == 'r'):
        return True

input("Press enter to play")
play()