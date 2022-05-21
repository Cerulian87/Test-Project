#Johnathon Martin
#Project 4
#08MAY22
#This is the Team Management Python program, project 4, refactored to use SQL!

# UI

from objects import Player, Lineup
import db
from datetime import datetime, date, timedelta



def main_menu(): 
    print()
    print("MENU OPTIONS")
    print("1 - Display lineup")
    print("2 - Add player")
    print("3 - Remove player")
    print("4 - Move Player")
    print("5 - Edit player position")
    print("6 - Edit player stats")
    print("7 - Exit program")
    print()
    print("POSITIONS")
    print("C, 1B, 2B, 3B, SS, LF, CF, RF, P")
    print("=" * 60)

def get_int(prompt):  # I absolutely loved this idea, stealing it forever
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid whole number. Please try again.\n")


def display_lineup(): 
    print(f"{'': <3}{'Player': <31}{'POS': >6}{'AB': >6}{'H': >6}{'AVG': >8}")
    print("-" * 60)
    lineup = db.get_players()

    for player in lineup:
        print(f"{player.getPlayerID():<3}{player.getFullName():<31}{player.getPosition():>6}"
                f"{player.getAtBats():>6}{player.getHits():>6}{player.getAverage():>8}")

    print()
   

def add_player(): 
    v_position = ("C","1B","2B","3B","SS","LF","CF","RF","P")
    first_name = input("Enter Player's First Name: ")
    last_name = input("Enter Player's Last Name: ")
    while True:
        try:
            position = input("Enter Position: ")
            if position in v_position:
                break
            else:
                print("Invalid position. Try again.")
                
        except:
            continue


        
    while True:
        try:
            bat_order = get_int("Enter Batting Order: ")
            at_bats = get_int("Enter At bats: ")
            
            hits = get_int("Enter Hits: ")
            while True:
                if hits >= 0 and hits <= at_bats:
                    break
                elif hits < 0 or hits > at_bats:
                    print("Hits cannot exceed at bats or be a negative number.")
                    print()
                    hits = get_int("Enter Hits: ")
        except:
            continue
        break
        
    new_player = Player(batOrder=bat_order, firstName=first_name, lastName=last_name, position=position, atBats=at_bats, hits=hits)
    db.add_player(new_player)
    print(first_name, "was added.\n")
    print()


def remove_player(): 
    lineup = db.get_players()
    number = get_int("Enter a linup number to remove: ")
    if number < 1 or number > lineup.getLineupCount():
        print("Invalid lineup number.\n")
    else:
        
        player = lineup.remove(number - 1)
        print(f'{player.getFullName()} was deleted.')
        player = db.delete_player(number)
    print()


def move_player():
    lineup = db.get_players()
    number = get_int("Enter a current lineup number to move: ")
    if number < 1 or number > lineup.getLineupCount():
        print("Invalid lineup number.\n")
    else:
        player = lineup.get(number - 1)
        print(f"{player.getFullName()} was selected")
        new_number = get_int("Enter a new lineup number: ")
        if new_number < 1 or new_number > lineup.getLineupCount():
            print("Invalid lineup number.\n")
        else:
            player.batOrder = new_number
            print(f"{player.getFullName()} was moved.")
            db.update_bat_order(lineup)
    print()


def edit_position(): 
    lineup = db.get_players()
    v_position = ("C","1B","2B","3B","SS","LF","CF","RF","P")

    number = get_int("Enter a lineup number to edit: ")
    if number < 1 or number > lineup.getLineupCount():
        print("Invalid entry. Please try again.")
    else:
        player = lineup.get(number - 1)
        print(f"You selected {player.getFullName()} POS = {player.getPosition()}")
        while True:
            try:

                new_position = input("Enter a new Position: ")
                if new_position in v_position:
                    player.position = new_position
                    print(f"{player.getFullName()} was updated.")
                    db.update_player(player)
                    break

                else:
                    print("Invalid entry, please try again.")
            except:
                continue


    print()

def edit_stats(): 
    lineup = db.get_players()

    number = get_int("Enter a lineup number to edit: ")
    if number < 1 or number > lineup.getLineupCount():
        print("Invalid entry. Please try again.")
    else:
        player = lineup.get(number - 1)
        print(f"You selected {player.getFullName()}")
        while True:
            try:

                new_at_bats = get_int("Enter new At Bats: ")
                if new_at_bats < 0:
                    print("Invalid number. Please use 0 or a positive integer.")
                else:
                    new_hits = get_int("Enter new Hits: ")
                    if new_hits < 0 or new_hits > new_at_bats:
                        print("Invalid number. Please use 0 or a positive integer.")
                    else:

                        player.atBats = new_at_bats
                        player.hits = new_hits
                        print(f"{player.getFullName()} was updated.")
                        db.update_player(player)
                        break

            except ValueError:
                print("Invalid entry. Please try again.")
                continue


    print()

def main():


    print("=" * 60)
    print("\t\t Baseball Team Management Program")
    print()
    current_date = datetime.today()
    date_format = "%Y-%m-%d"
    print(f"CURRENT DATE: {current_date:{date_format}}")
    game_date_str = input("GAME DATE: ")
    if game_date_str == "":
        pass
    else:
        game_date = datetime.strptime(game_date_str, date_format)

        days_till_game = (game_date - current_date).days + 1
        print(f"DAYS UNTIL GAME: {days_till_game}")



    main_menu()

    db.connect()

    while True:
        command = input("Menu Option: ")
        if command == "1":
            display_lineup()
        elif command == "2":
            add_player()
        elif command == "3":
            remove_player()
        elif command == "4":
            move_player()
        elif command == "5":
            edit_position()
        elif command == "6":
            edit_stats()
        elif command == "7":
            break
        else:
            print("Invalid menu option. Please try again.")
            print()
            main_menu()
    db.close()
    print("Bye!")

if __name__ == "__main__":
    main()
          


