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

def display_stats(team, team_name):
    roster = []
    seasoned = []
    not_seasoned = []
    keepers = []

    for player in team:
        # append the players name to the roster. We want them on the roster regardless of exp
        roster.append(player["name"])
        # if the player has experienced put them in the seasoned list
        if player["experience"] == True:
            seasoned.append(player["name"])
        # if the player has no experience put them in the not_seasoned list
        if player["experience"] == False:
            not_seasoned.append(player["name"])
        # extend the keepers list with the guardians of the player
        keepers.extend(player["guardians"])

        # Get the total height of all players together
        sum_ht = sum(player["height"] for player in team)
        # Find the average of all the players
        avg_ht = int(sum_ht / len(roster))

    stats_template = dedent("""\
                     Team: {} Stats
                     {}
                     Total Players: {}
                     Players on Team: {}
                       Total Experienced Players: {}
                       Total Inexperienced Players: {}
                         The average height for the team is: {}
                         The Guardians: {} """)
    print(stats_template.format(
                team_name,  # use the team name we sent in
                "-" * (len("Team:   Stats") + len(team_name)),  # add the length of the team name plus the banner text to make the dashes
                len(team),
                ", ".join(roster),  # make the players on the team into a comma separated string
                len(seasoned),
                len(not_seasoned),
                avg_ht,
                ", ".join(keepers)))  # make the guardians into a comma separated string

def stats_menu(preferred):
    choice = main_selection()
    print(choice)
    Panthers, Bandits, Warriors = distribute_players(players_list)

    if choice == 1:
        # display the stats for the Panthers team and send in the name of the team
        display_stats(Panthers,"Panthers")
    if choice == 2:
        # display the stats for the Bandits team and send in the name of the team
        display_stats(Bandits, "Bandits")
    if choice == 3:
        # display the stats for the Warriors team and send in the name of the team
        display_stats(Warriors, "Warriors")
    return choice

if __name__ == "__main__":
    #clean_data, divide_experience, main_menu, stats_menu, distribute_players, print_stats
    clean_data()
    try:
        while True:
            stats_menu(1)
            input("\nPress ENTER to continue...")
    except SystemExit:
        print("Program Terminated, Bye!")
