import random

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value,max_value)
    return roll

while True:
    players = input("Enter the number of player(2-4) : ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <=4:
            break 
        else:
            print("Must be 2-4 player")
    else:
        print("Invalid, Try again")

max_score = 30
player_scores = [0 for _ in range(players)]

while max(player_scores) < max_score:
    for player_idx in range(players):
        print("\nplayer", player_idx+1, "turn just started")
        print('Your total score is ', player_scores[player_idx],"\n")
        cur_score = 0

        while True:
            should_roll = input("Would you like to roll(y) ? : ")
            if should_roll.lower() != 'y':
                break 
            value = roll()

            if value == 1:
                cur_score = 0
                print("You rolled a 1!Turn done!")
            else:
                cur_score += value
                print("you rolled a",value)
            
            print('your score is ', cur_score)

        player_scores[player_idx] += cur_score
        print('Your total score is ', player_scores[player_idx])

max_score = max(player_scores)
winning_idx = player_scores.index(max_score)
print("Player number", winning_idx+1, "is the winner with the score of", max_score)
