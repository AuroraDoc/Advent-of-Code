# trying to split by ; and , to get the game data
# format: {1: {
#               red: []
#               blue: []
#               green: []
#               }}

impossible_total = 0
with open('day2.txt', 'r') as data:
    games = {}
    game_num = 1
    for line in data:
        games.update({game_num: {"red": [],
                                 "blue": [],
                                 "green": []}})  # sets up the format I want
        game_round = line.split(":")  # takes off the game and game number
        rounds = game_round[1].split(";")  # each round in the game. Returns a list of each round seperated in a list
        for subgame in rounds:
            if "red" in subgame:
                red_idx = subgame.find("red")
                if subgame[red_idx - 3].isnumeric():
                    red_num = subgame[red_idx - 3] + subgame[red_idx - 2]
                else:
                    red_num = subgame[red_idx - 2]
                if int(red_num) > 12:
                    games[game_num]["red"].append(red_num)
                    impossible_total += game_num
                    break
                else:
                    games[game_num]["red"].append(red_num)

            if "green" in subgame:
                green_idx = subgame.find("green")
                if subgame[green_idx - 3].isnumeric():
                    green_num = subgame[green_idx - 3] + subgame[green_idx - 2]
                else:
                    green_num = subgame[green_idx - 2]
                if int(green_num) > 13:
                    games[game_num]["green"].append(green_num)
                    impossible_total += game_num
                    break
                else:
                    games[game_num]["green"].append(green_num)

            if "blue" in subgame:
                blue_idx = subgame.find("blue")
                if subgame[blue_idx - 3].isnumeric():
                    blue_num = subgame[blue_idx - 3] + subgame[blue_idx - 2]
                else:
                    blue_num = subgame[blue_idx - 2]
                if int(blue_num) > 14:
                    games[game_num]["blue"].append(blue_num)
                    impossible_total += game_num
                    break
                else:
                    games[game_num]["blue"].append(blue_num)

        game_num += 1

    print(5050 - impossible_total)  # 5050 is all the sets of games added up
