import constants
import sys
from copy import deepcopy
from textwrap import dedent

players = constants.PLAYERS
teams_list = constants.TEAMS
players_list = deepcopy(players)
skilled = []
not_skilled = []

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

def divide_experienced(all_players):
    for skill in players_list:
        if skill['experience'] == True:
            skilled.append(skill)
        elif skill['experience'] == False:
            not_skilled.append(skill)
    return skilled, not_skilled

def team_stats():
    while True:
        print("\n\nBASKETBALL TEAM STATS TOOL\n")
        print("----MENU---\nHere are your choices:\n1) Display Team Stats\n2) Quit\n")
        main_menu = input("Enter an option: ")
        try:
            menu_opt = int(main_menu)
            if menu_opt == 1:
                count = 0
                for team in teams_list:
                    count += 1
                    print(count,")",team)
            elif menu_opt == 2:
                sys.exit()
            else:
                if menu_opt == 0 or menu_opt > 2:
                    print("{}, is not available from the MENU.\nPlease ENTER only the available options (1-2).".format(main_menu))

        except ValueError:
            print("{}, That's an invalid input.\nPlease Enter a NUMBER only from the MENU.".format(main_menu))

        sub_menu = input("Select a team (1-3): ")
        try:
            team_opt = int(sub_menu)

            skilled, not_skilled = divide_experienced(players_list)
            if len(skilled) % len(not_skilled) == 0:
                Panthers = skilled[0:3] + not_skilled[0:3]
                Bandits = skilled[3:6] + not_skilled[3:6]
                Warriors = skilled[6:9] + not_skilled[6:9]

            if team_opt == 1:
                roster1 = []
                seasoned_panthers = []
                not_seasoned_panthers = []
                panthers_keepers = []

                print("Team: {} Stats\n{}\nTotal Players: {}".format("Panthers", "-" * len("Team: Panthers Stats"),len(Warriors)))
                for items in Panthers:
                    roster1.append(items["name"])
                    if items["experience"] == True:
                        seasoned_panthers.append(items["name"])
                    if items["experience"] == False:
                        not_seasoned_panthers.append(items["name"])
                    panthers_keepers.extend(items["guardians"])

                panthers_sum_ht = sum(items["height"] for items in Panthers)
                panthers_avg_ht = int(panthers_sum_ht / len(roster1))

                stats_template = dedent("""
                                 Players on Team: {}
                                   Total Experienced Players: {}
                                   Total Inexperienced Players: {}
                                     The average height for the Bandits Team is: {}
                                     The Panthers Guardians: {} """)

                print(stats_template.format(
                            ", ".join(roster1),
                           len(seasoned_panthers),
                           len(not_seasoned_panthers),
                           panthers_avg_ht,
                           panthers_keepers))

                # print("Players on Team:\n  {}".format(", ".join(roster1)))
                # print("    Total Experienced Players: {}".format(len(seasoned_panthers)))
                # print("    Total Inexperienced Players: {}".format(len(not_seasoned_panthers)))
                # print("      The average height for the Bandits Team is: {} inches".format(panthers_avg_ht))
                # print("      The Panthers Guardians: {}".format(", ".join(panthers_keepers)))

            elif team_opt == 2:
                roster2 = []
                seasoned_bandits = []
                not_seasoned_bandits = []
                bandits_keepers = []

                print("Team: {} Stats\n{}\nTotal Players: {}".format("Bandits", "-" * len("Team: Bandits Stats"),len(Bandits)))
                for items in Bandits:
                    roster2.append(items["name"])
                    if items["experience"] == True:
                        seasoned_bandits.append(items["name"])
                    if items["experience"] == False:
                        not_seasoned_bandits.append(items["name"])
                    bandits_keepers.extend(items["guardians"])

                bandits_sum_ht = sum(items["height"] for items in Bandits)
                bandits_avg_ht = int(bandits_sum_ht / len(roster2))

                print("Players on Team:\n   {}".format(", ".join(roster2)))
                print("    Total Experienced Players: {}".format(len(seasoned_bandits)))
                print("    Total Inexperienced Players: {}".format(len(not_seasoned_bandits)))
                print("      The average height for the Bandits Team is: {} inches".format(bandits_avg_ht))
                print("      The Bandits Guardians: {}".format(", ".join(bandits_keepers)))

            elif team_opt == 3:
                roster3 = []
                seasoned_warriors = []
                not_seasoned_wars = []
                warriors_keepers = []

                print("Team: {} Stats\n{}\nTotal Players: {}".format("Warriors", "-" * len("Team: Warriors Stats"),len(Bandits)))
                for items in Warriors:
                    roster3.append(items["name"])
                    if items["experience"] == True:
                        seasoned_warriors.append(items["name"])
                    if items["experience"] == False:
                        not_seasoned_wars.append(items["name"])
                    warriors_keepers.extend(items["guardians"])

                warriors_sum_ht = sum(items["height"] for items in Warriors)
                warriors_avg_ht = int(warriors_sum_ht / len(roster3))
                print("Players on Team:\n   {}".format(", ".join(roster3)))
                print("    Total Experienced Players: {}".format(len(seasoned_warriors)))
                print("    Total Inexperienced Players: {}".format(len(not_seasoned_wars)))
                print("      The average height for the Warriors Team is: {} inches".format(warriors_avg_ht))
                print("      The Warriors Guardians: {}".format(", ".join(warriors_keepers)))

            else:
                if team_opt == 0 or team_opt > 3:
                    print("{}, is not available from the MENU.\nPlease ENTER only the available options (1-3).".format(sub_menu))

        except ValueError:
            print("{}, That's an invalid input.\nPlease Enter a NUMBER only from the MENU.".format(sub_menu))

        input("\nPress ENTER to continue...")

if __name__ == "__main__":
    try:
        team_stats()
    except SystemExit:
        print("Program Terminated. Bye!")
