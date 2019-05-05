import constants
import sys
from copy import deepcopy

players = constants.PLAYERS
teams_list = constants.TEAMS
players_list = deepcopy(players)

if __name__ == "__main__":
# clean data: remove "and"; height to int; experience boolean
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
    print(players_list)

    print("BASKETBALL TEAM STATS TOOL\n")
    print("----MENU---\n")

    print("Here are your choices:\n1) Display Team Stats\n2) Quit\n")
    menu_opt = int(input("Enter an option: "))
# Main Menu
    if menu_opt == 1:
        count = 0
        for team in teams_list:
            count += 1
            print(count,")" ,team)
    elif menu_opt == 2:
        sys.exit()
# Sub-menu
# Team balancing
    team_opt = int(input("Enter an option: "))
    team_1 = []
    team_2 = []
    team_3 = []
    def team_stats(team):
        while True:
            for key,value in players_list:
                for name in key:
                    if key == "name":
                        team_1.append(value)
                        team_2.append(value)
                        team_3.append(value)
                        print(count)
            return(team)

# Display number of players
    if team_opt == 1:
        len(team_1)
        team_stats(team_1)
    if team_opt == 2:
        team_stats(team_2)
    if team_opt == 3:
        team_stats(team_3)
# Display players in team
