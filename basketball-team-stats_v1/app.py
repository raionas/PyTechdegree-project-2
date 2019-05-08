import constants
import sys
from copy import deepcopy

players = constants.PLAYERS
teams_list = constants.TEAMS
players_list = deepcopy(players)
skilled = []
not_skilled = []

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
print("\nTotal Players: ", len(players_list))

def divide_experienced(all_players):
# Accept all_players as an argument which should be ALL 18 players.

# ... now run your logic here...
    for skill in players_list:
        if skill['experience'] == True:
            skilled.append(skill)
        elif skill['experience'] == False:
            not_skilled.append(skill)
    print("Skilled: ", len(skilled))
    print("Not Skilled: ", len(not_skilled))
# Then you could return a 2-item Tuple each containing a List.
    return skilled, not_skilled

def team_stats():
    while True:
        # Main Menu
        print("\n\nBASKETBALL TEAM STATS TOOL\n")
        print("----MENU---\nHere are your choices:\n1) Display Team Stats\n2) Quit\n")
        main_menu = input("Enter an option: ")
        try:
            menu_opt = int(main_menu)
            if menu_opt == 1:
                count = 0
                for team in teams_list:
                    count += 1
                    print(count,")" ,team)
            elif menu_opt == 2:
                sys.exit()
            else:
                if menu_opt == 0 or menu_opt > 2:
                    print("{}, is not available from the MENU.\nPlease ENTER only the available options (1-2).".format(main_menu))

        except ValueError:
            print("{}, That's an invalid input.\nPlease Enter a NUMBER only from the MENU.".format(main_menu))

        # Sub-menu
        sub_menu = input("Enter an option: ")
        try:
            team_opt = int(sub_menu)
            # Now to use it... (somewhere else in Dunder Main)
            # Team balancing
            skilled, not_skilled = divide_experienced(players_list)
            if len(skilled) % len(not_skilled) == 0:
                Panthers = skilled[0:3] + not_skilled[0:3]
                Bandits = skilled[3:6] + not_skilled[3:6]
                Warriors = skilled[6:9] + not_skilled[6:9]

            # Displaying Stats
            if team_opt == 1:
                roster1 = []
                print("Team: {} Stats\n{}\nTotal Players: {}".format("Panthers", "-" * len("Team: Panthers Stats"),len(Warriors)))
                for items in Panthers:
                    roster1.append(items["name"])
                print("Players on Team:\n  {}".format(", ".join(roster1)))

            elif team_opt == 2:
                roster2 = []
                print("Team: {} Stats\n{}\nTotal Players: {}".format("Bandits", "-" * len("Team: Bandits Stats"),len(Bandits)))
                for items in Bandits:
                    roster2.append(items["name"])
                print("Players on Team:\n   {}".format(", ".join(roster2)))

            elif team_opt == 3:
                roster3 = []
                seasoned_warriors = []
                not_seasoned_wars = []
                print("Team: {} Stats\n{}\nTotal Players: {}".format("Bandits", "-" * len("Team: Bandits Stats"),len(Bandits)))
                for items in Warriors:
                    roster3.append(items["name"])
                print("Players on Team:\n   {}".format(", ".join(roster3)))
                 # counting experienced palyers
                for items in Warriors:
                    if items["experience"] == True:
                        seasoned_warriors.append(items["name"])
                    if items["experience"] == False:
                        not_seasoned_wars.append(items["name"])
                print("    Total Experienced Players: {}".format(len(seasoned_warriors)))
                print("    Total Inexperienced Players: {}".format(len(not_seasoned_wars)))

                warriors_avg_ht = sum(items["height"] for items in Warriors)
                print("      The average height for the Warriors Team is: {} inches".format(warriors_avg_ht))

            else:
                if team_opt == 0 or team_opt > 3:
                    print("{}, is not available from the MENU.\nPlease ENTER only the available options (1-3).".format(sub_menu))

        except ValueError:
            print("{}, That's an invalid input.\nPlease Enter a NUMBER only from the MENU.".format(sub_menu))

        input("\nPress ENTER to continue...")
    #return



if __name__ == "__main__":
    try:
        team_stats()
        #seasoned_players()
    except SystemExit:
        print("Program Terminated.")
