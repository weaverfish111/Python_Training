## Monopoly.py
## Richard Weaver
## 18/03/2022

import random
import matplotlib.pyplot as plt	

from turtle import position

def throw_two_dice():
    double = 0
    min_val = 1
    max_val = 6
    dice_1 = random.randint(min_val, max_val)
    dice_2 = random.randint(min_val, max_val)
    roll = dice_1 + dice_2
    # print(f"throw = {roll}")
    # print(f"The Total Value of the Dice Roll Was {roll}")
    if dice_1 == dice_2:
        # print("A Double Has Been Thrown!")
        double = 1
    return(roll)

def simulate_monopoly():
    position = 0
    throw = 0
    properties_left = 28
    board_values = [0, 60, 0, 60, 0, 200, 100, 0, 100, 120, 0, 140, 150, 140, 160, 200, 180,
                    0, 180, 200, 0, 220, 0, 220, 240, 200, 260, 260, 150, 280, 0, 300, 300,
                    0, 320, 200, 0, 350, 0, 400]
    possessions = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ]
    completed_list = list(range(40))    
    position_list = []
    position_value = 0
    # print(completed_list)
    ## While looped actioning simulation
    # while possessions != board_values:
    while properties_left != 0: ##change to properties left
        throw += 1
        position += throw_two_dice()
        # print(f"on Throw {throw} Position is {position}")
        ## If function here (if over 40 minus 40)
        if position >= 40:
            position = position - 40 

        # if position not in position_list:
            # Must sort list position.list!
            ## Will change to only add if money is allowing.
            # position_list.append(position)
            # position_list.sort()
            # print(position_list)

            # Trying to create corrolation between position and board_value
            # position_value = board_values[position]         ### Something may be wrong here... why it is not inputting correct
                                                            ### The position is changing, because the list is an empty list being added to...
                                                            ### Position list index 1 is not constant...
                                                            ### But it works the first go round, but not after...? Why?

        
        if board_values[position] > 0 and possessions[position] == 0:
            possessions[position] = board_values[position]
            # print("Property Bought!")
            properties_left -= 1
            # print(possessions)
            # print(f"Number of properties left = {properties_left}")

        if possessions == board_values:
            print("done")
        
        # print(f"On Throw {throw} the Position is {position} (Value = {position_value})")
        # print(len(position_list))
        # print(position_list)
        # print(completed_list)
    return(throw) ##Show how many throws it take to buy all properties (not inclusing spots like jail(20) and start (0)

def simulate_monopoly_games(total_games):
    number_of_throws_for_completion = []
    for game in range(0, total_games):
        number_of_throws = simulate_monopoly()
        number_of_throws_for_completion.append(number_of_throws)

    ## Histogram Graph showing Number of Turns
    plt.hist(number_of_throws_for_completion)
    plt.title(f'Histogram showing Number of Turns taken in {total_games} Games of Monopoly')
    plt.xlabel('Number Of Turns Taken')
    plt.ylabel('Number of Number of Games')
    plt.show()
    return(number_of_throws_for_completion)


print(simulate_monopoly_games(10000))
