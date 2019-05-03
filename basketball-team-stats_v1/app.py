import constants
import sys

players_list = constants.PLAYERS
teams_list = constants.TEAMS
player_info = {}

# clean data: remove 'and'; height to int; experience boolean
for items in players_list:
    if items['experience'] == 'YES':
        items['experience'] = 'TRUE'
    elif items['experience'] == 'NO':
        items['experience'] = 'FALSE'
    feet = items['height']
    feet_str = feet.split()
    items['height'] = feet_str[0]
    keeper = items['guardians']
    keeper_str = keeper.replace('and','')
    items['guardians'] = keeper_str.replace('and','')
    player_info.update(items)
    print(player_info)

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
        team_opt = int(input("Enter an option: "))

# Display number of players: team balancing
        #if team_opt == 1:
# Display players in team
