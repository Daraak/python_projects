import random
import time

print("""\nRules for the game:-
        In this game you gonna play with computer/system!
        You will get the options to chose your input (chose the specified number belongs to the given options).
        You will be having 5 turns for a single game and after every turn winner will be shown.
        At last (after finishing all of the 5 turns) the score of both system and player will be returned
        and according to that winner will be announced.
        """)
print('----------------------------------------------------------------------------------------------------------------')
time.sleep(3)
print(input('So let\'s begin, press "Enter" to start the game:'))
time.sleep(2)
print('Loading', end='')
time.sleep(1)
for i in range(5):
    print('.', end='')
    time.sleep(1)
print('\n--------------------------------------------------------------------------------------------------------------')
play_score = 0
comp_score = 0
k = 'y'
while k == 'y':
    for i in range(5):
        comp_opt = ['Stone', 'Paper', 'Scissor']
        comp_opt_1 = random.choice(comp_opt)
        print('\nWhat would you like to be your input, chose the number accordingly;'
              '\n1.Stone', '\n2.Paper', '\n3.Scissor')
        player = input('Tell me your choice:- ')
        if player == '1':
            player_in = 'Stone'
            if player_in == 'Stone' and comp_opt_1 == 'Stone':
                print('Match Draw!')
                play_score += 0
                comp_score += 0
            elif player_in == 'Stone' and comp_opt_1 == 'Paper':
                print('Computer Wins!')
                comp_score += 1
            elif player_in == 'Stone' and comp_opt_1 == 'Scissor':
                print('You Wins!')
                play_score += 1
        elif player == '2':
            player_in = 'Paper'
            if player_in == 'Paper' and comp_opt_1 == 'Paper':
                print('Match Draw!')
                play_score += 0
                comp_score += 0
            elif player_in == 'Paper' and comp_opt_1 == 'Stone':
                print('You Wins!')
                play_score += 1
            elif player_in == 'Paper' and comp_opt_1 == 'Scissor':
                print('Computer Wins!')
                comp_score += 1
        elif player == '3':
            player_in = 'Scissor'
            if player_in == 'Scissor' and comp_opt_1 == 'Scissor':
                print('Match Draw!')
                play_score += 0
                comp_score += 0
            if player_in == 'Scissor' and comp_opt_1 == 'Stone':
                print('Computer Wins!')
                comp_score += 1
            elif player_in == 'Scissor' and comp_opt_1 == 'Paper':
                print('You Wins')
                play_score += 1
        else:
            print('Wrong Input!, You could have chosen from the given options.')
    print('\nCalculating Score and announcing the winner', end='')
    time.sleep(1)

    for i in range(5):
        print('.', end='')
        time.sleep(1)
    print(f'\n>> Computer Score:- {comp_score}')
    print(f'>> Your Score:- {play_score}')
    if play_score > comp_score:
        print('Congrats! You are the winner of this game.')
    elif play_score < comp_score:
        print('Unfortunately! You have lost the game.')
    else:
        print('Match Tie! Both of you have equal score')
    choice = input('\nDo you want to play the game again [y / n], Default[n]:- ')
    if choice == 'n' or choice == '':
        k = 'n'
        print('Hope you will be back soon.')
    elif choice == 'y':
            k = 'y'
    else:
        print('Wrong Input! QUITTING')
        exit()