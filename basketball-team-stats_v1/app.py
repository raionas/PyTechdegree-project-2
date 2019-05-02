import constants
import sys

players_list = constants.PLAYERS
teams_list = constants.TEAMS

if __name__ == "__main__":
    print("BASKETBALL TEAM STATS TOOL\n")
    print("----MENU---\n")

    print("Here are your choices:\n1) Display Team Stats\n2) Quit\n")
    menu_opt = int(input("Enter an option: "))
# Main Menu
    if menu_opt == 1:
        count = 0
        for team in teams_list:
            count += 1
            print(count,')' ,team)
    elif menu_opt == 2:
        sys.exit()
# Sub-menu
        player_info = {}
        line = str()

        team_opt = int(input("Enter an option: "))
# clean data: remove 'and'; height to int; experience boolean
        for items in players_list:
            for word in items['guardians']:
                word = word.find('and')
                del items[word]
                player_info.update(items)


# Display number of players: team balancing
        #if team_opt == 1:
# Display players in team
