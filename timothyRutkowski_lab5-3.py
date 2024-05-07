# Timothy Rutkowski 03/25/24 timothyRutkowski_lab5-3.py

# Rock, Paper, Scissors
# This program will play rock, paper, scissors against the user,
# loop until told to stop,
# and keep track of total games played, computer wins, player wins, and ties

import random

# Main Function of program
def main():
    global ties, player_wins, com_wins
    # Initiate results to 0
    total_games = 0
    ties = 0
    player_wins = 0
    com_wins = 0
    
    while True:
        com_choice = random.randint(1, 3)
        players_choice = get_players_choice()
        player_string = get_string_choice(players_choice)
        winner = calculate_winner(players_choice, com_choice)
        display_com_choice(com_choice)
        who_won(winner, ties, player_wins, com_wins)
        total_games += 1
        print_results(total_games, ties, player_wins, com_wins)
        
        if not play_again():
            break
        
# Function to get players choice of either rock, paper, or scissors as 1, 2, or 3        
def get_players_choice():
    choice = int(input('\n1 - rock \n2 - paper \n3 - scissors \n\nEnter Choice: '))  
    while choice not in {1, 2, 3}:
        print('Invalid Input: Please enter 1, 2, or 3')
        choice = int(input('\n1 - rock \n2 - paper \n3 - scissors \n\nEnter Choice: '))
    return choice

# Function to converts players choice of 1, 2, or 3 to rock, paper, or scissors
def get_string_choice(players_choice):
    if players_choice == 1:
        return 'rock'
    elif players_choice == 2:
        return 'paper'
    else:
        return 'scissors'

# Function to determine the winner of the game
def calculate_winner(players_choice, com_choice):
    if players_choice == com_choice:
        global ties
        ties += 1
        return 0  # Tie
    elif (players_choice == 1 and com_choice == 3) or \
         (players_choice == 2 and com_choice == 1) or \
         (players_choice == 3 and com_choice == 2):
        global player_wins
        player_wins += 1
        return 1  # Player win
    else:
        global com_wins
        com_wins += 1
        return 2  # Computer win

# Function to display the computers choice    
def display_com_choice(com_choice):
    if com_choice == 1:
        print('\nThe Computer chose rock')
    elif com_choice == 2:
        print('\nThe Computer chose paper')
    else:
        print('\nThe Computer chose scissors')

# Function to display who won the game    
def who_won(winner, ties, player_wins, com_wins):
    if winner == 0:
        print('Tie game!')
    elif winner == 1:
        print('You win!')
    else:
        print('The Computer wins!')

# Function to display the total games played and their results
def print_results(total_games, ties, player_wins, com_wins):
    print(f'\nTotal games: {total_games}')
    print(f'Ties: {ties}')
    print(f'Your wins: {player_wins}')
    print(f'Computer wins: {com_wins}')

# Function to ask user if they want to play again    
def play_again():
    play_again = input('\nWould you like to play again? \n1 - yes \n2 - no\n\nEnter Choice: ')
    return play_again == '1'

# Call main function
main()