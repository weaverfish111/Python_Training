## Monopoly.py
## Richard Weaver
## 18/03/2022

import random
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
        print("A Double Has Been Thrown!")
        double = 1
    return(roll)

def simulate_monopoly():
    position = 0
    throw = 0
    completed_list = list(range(41))
    # throw = throw_two_dice()
    position_list = []
    while position <= 40:
        throw += 1
        position += throw_two_dice()
        print(f"On Throw {throw} the Position is {position}")
        if position not in position_list:
            position_list.append(position)
            print(position_list)
        elif position > 40:
            position = position % 40
        if position_list == completed_list:
            print("done")
    return(position_list)

    #     elif position + position >= 40:
    #         position = position - 40
    #     elif position_list == completed_list:
    #         print("done")
            
    #     # print(position)
    # # print(position_list)
    # return(position_list)

print(simulate_monopoly())
# print(throw_two_dice())










# def practice_with_dice():
#     double_count = 0
#     for throws in range(0, 1000, 1):
#         throws = throw_two_dice()
#         # print(throws)
#         double_count += throw_two_dice()
#     print(double_count)
#     return(double_count)
















# # Need to work out how to call variable from 'throw_two_dice' function into this function!
#         if double_count >= 0:
#             print(f"Number of doubles is {double_count}")
    


# print(practice_with_dice())


# def simulate_monopoly_games(total_games):
#     # total_games = #number of games being simulated
#     return(#number of throws required before all streets were held by the player.)
