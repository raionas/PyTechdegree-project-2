import constants
import sys
from copy import deepcopy
from textwrap import dedent

players = constants.PLAYERS
teams_list = constants.TEAMS
players_list = deepcopy(players)
skilled = []
not_skilled = []

def clean_data():
    for items in players_list:
        if items["experience"] == "YES":
            items["experience"] = True
        elif items["experience"] == "NO":
            items["experience"] = False
        feet = items["height"]
        feet_str = feet.split()
        items["height"] = int(feet_str[0])
        keeper = items["guardians"]
        keeper_str = keeper.split(" and ")
        items["guardians"] = keeper_str
    return players_list

def divide_experienced(all_players):
    for skill in players_list:
        if skill['experience'] == True:
            skilled.append(skill)
        elif skill['experience'] == False:
            not_skilled.append(skill)
    return skilled, not_skilled

def main_selection():
    while True:
        print("\nBASKETBALL TEAM STATS TOOL\n")
        print("----MENU---\nHere are your choices:\n1) Display Team Stats\n2) Quit")
        try:
            main_menu = input("Enter an option (1-2): ")
            menu_opt = int(main_menu)
            if menu_opt == 1:
                count = 0
                for team in teams_list:
                    count += 1
                    print(count,")",team)
            elif menu_opt == 2:
                sys.exit()

            elif menu_opt == 0 or menu_opt > 2:
                    print("{}, is not available from the MENU.\nPlease ENTER only the available options (1-2).".format(main_menu))
                    continue

        except ValueError:
            print("{}, That's an invalid input.\nPlease Enter a NUMBER only from the MENU.".format(main_menu))
            continue

        try:
            sub_menu = input("Select a team (1-3): ")
            team_opt = int(sub_menu)

            if team_opt == 0 or team_opt > 3:
                print("{}, is not available from the MENU.\nPlease ENTER only the available options (1-3).".format(sub_menu))
                continue

        except ValueError:
            print("{}, That's an invalid input.\nPlease Enter a NUMBER only from the MENU.".format(sub_menu))
            continue

        return team_opt

def distribute_players(headcount):
    skilled, not_skilled = divide_experienced(players_list)
    if len(skilled) % len(not_skilled) == 0:
        Panthers = skilled[0:3] + not_skilled[0:3]
        Bandits = skilled[3:6] + not_skilled[3:6]
        Warriors = skilled[6:9] + not_skilled[6:9]
    return Panthers, Bandits, Warriors

def stats_menu(preferred):
    choice = main_selection()
    stats_template = dedent("""\
                     Team: {} Stats
                     {}
                     Total Players: {}
                     Players on Team: {}
                       Total Experienced Players: {}
                       Total Inexperienced Players: {}
                         The average height for the Bandits Team is: {}
                         The Panthers Guardians: {} """)

    # skilled, not_skilled = divide_experienced(players_list)
    # if len(skilled) % len(not_skilled) == 0:
    #     Panthers = skilled[0:3] + not_skilled[0:3]
    #     Bandits = skilled[3:6] + not_skilled[3:6]
    #     Warriors = skilled[6:9] + not_skilled[6:9]
    Panthers, Bandits, Warriors = distribute_players(players_list)

    if choice == 1:
        roster1 = []
        seasoned_panthers = []
        not_seasoned_panthers = []
        panthers_keepers = []

        for items in Panthers:
            roster1.append(items["name"])
            if items["experience"] == True:
                seasoned_panthers.append(items["name"])
            if items["experience"] == False:
                not_seasoned_panthers.append(items["name"])
            panthers_keepers.extend(items["guardians"])

        panthers_sum_ht = sum(items["height"] for items in Panthers)
        panthers_avg_ht = int(panthers_sum_ht / len(roster1))

        print(stats_template.format(
                    "Panthers",
                    "-" * len("Team: Panthers Stats"),
                    len(Warriors),
                    ", ".join(roster1),
                    len(seasoned_panthers),
                    len(not_seasoned_panthers),
                    panthers_avg_ht,
                    ", ".join(panthers_keepers)))

    elif choice == 2:
        roster2 = []
        seasoned_bandits = []
        not_seasoned_bandits = []
        bandits_keepers = []

        for items in Bandits:
            roster2.append(items["name"])
            if items["experience"] == True:
                seasoned_bandits.append(items["name"])
            if items["experience"] == False:
                not_seasoned_bandits.append(items["name"])
            bandits_keepers.extend(items["guardians"])

        bandits_sum_ht = sum(items["height"] for items in Bandits)
        bandits_avg_ht = int(bandits_sum_ht / len(roster2))

        print(stats_template.format(
                    "Bandits",
                    "-" * len("Team: Bandits Stats"),
                    len(Bandits),
                    ", ".join(roster2),
                    len(seasoned_bandits),
                    len(not_seasoned_bandits),
                    bandits_avg_ht,
                    ", ".join(bandits_keepers)))

    elif choice == 3:
        roster3 = []
        seasoned_warriors = []
        not_seasoned_warriors = []
        warriors_keepers = []

        for items in Warriors:
            roster3.append(items["name"])
            if items["experience"] == True:
                seasoned_warriors.append(items["name"])
            if items["experience"] == False:
                not_seasoned_warriors.append(items["name"])
            warriors_keepers.extend(items["guardians"])

        warriors_sum_ht = sum(items["height"] for items in Warriors)
        warriors_avg_ht = int(warriors_sum_ht / len(roster3))

        print(stats_template.format(
                    "Warriors",
                    "-" * len("Team: Warriors Stats"),
                    len(Warriors),
                    ", ".join(roster3),
                    len(seasoned_warriors),
                    len(not_seasoned_warriors),
                    warriors_avg_ht,
                    ", ".join(warriors_keepers)))

    return choice

if __name__ == "__main__":
    #clean_data, divide_experience, main_menu, stats_menu, distribute_players, print_stats
    clean_data()
    try:
        while True:
            #main_selection() # nothing catches the value
            stats_menu(1)
            input("\nPress ENTER to continue...")
    except SystemExit:
        print("Program Terminated. Bye!")
