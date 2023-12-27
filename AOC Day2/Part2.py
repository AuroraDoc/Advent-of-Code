# Plan: Have a variable of each color and if new_col > max_col max_col = new_col

total = 0
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
                games[game_num]["red"].append(int(red_num))

            if "green" in subgame:
                green_idx = subgame.find("green")
                if subgame[green_idx - 3].isnumeric():
                    green_num = subgame[green_idx - 3] + subgame[green_idx - 2]
                else:
                    green_num = subgame[green_idx - 2]
                games[game_num]["green"].append(int(green_num))

            if "blue" in subgame:
                blue_idx = subgame.find("blue")
                if subgame[blue_idx - 3].isnumeric():
                    blue_num = subgame[blue_idx - 3] + subgame[blue_idx - 2]
                else:
                    blue_num = subgame[blue_idx - 2]
                games[game_num]["blue"].append(int(blue_num))

        red_max = max(games[game_num]["red"])
        green_max = max(games[game_num]["green"])
        blue_max = max(games[game_num]["blue"])
        line_total = int(red_max) * int(blue_max) * int(green_max)
        total += line_total
        game_num += 1
        print(total)
