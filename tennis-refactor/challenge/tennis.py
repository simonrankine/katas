def display(player_one_points, player_two_points, player_one_advantage, player_two_advantage, player_one_sets, player_two_sets):
    print("---------------------------")
    if player_one_advantage:
        player_one_advantage_char = "A"
    else:
        player_one_advantage_char = ""
    if player_two_advantage:
        player_two_advantage_char = "A"
    else:
        player_two_advantage_char = ""
    print(f"Points: {player_one_points}{player_one_advantage_char} | {player_two_points}{player_two_advantage_char}")
    print("---------------------------")
    print(f"Sets: {player_one_sets} | {player_two_sets}")
    print("---------------------------")
def update_scores():
    player_one_points = 0
    player_two_points = 0
    player_one_advantage = False
    player_two_advantage = False
    player_one_sets = 0
    player_two_sets = 0
    while True:
        user_input = input("Enter the number of the player that scored: ")
        if user_input == "1":
            if player_one_points == 0 or player_one_points == 15:
                player_one_points += 15
            elif player_one_points == 30:
                player_one_points += 10
            else:
                # Score must be 40
                if player_one_advantage or player_two_points < 40:
                    # Player 1 wins set
                    player_one_sets += 1
                    player_one_points = 0
                    player_two_points = 0
                    player_one_advantage = False
                else:
                    if player_two_advantage:
                        player_two_advantage = False
                    else:
                        player_one_advantage = True
        elif user_input == "2":
            if player_two_points == 0 or player_two_points == 15:
                player_two_points += 15
            elif player_two_points == 30:
                player_two_points += 10
            else:
                # Score must be 40
                if player_two_advantage or player_one_points < 40:
                    # Player 1 wins set
                    player_two_sets += 1
                    player_one_points = 0
                    player_two_points = 0
                    player_two_advantage = False
                else:
                    if player_one_advantage:
                        player_one_advantage = False
                    else:
                        player_two_advantage = True
        else:
            print("Bad input :(")
        display(player_one_points, player_two_points, player_one_advantage, player_two_advantage, player_one_sets, player_two_sets)

update_scores()