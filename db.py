# db for Project 4
# Must now house all functions to work with Player Data
# Read all players, add player, delete player, update batting order,
#... update batting data


import sqlite3
from contextlib import closing


from objects import Player, Lineup


conn = None


def connect():
    global conn
    if not conn:
        DB_FILE = "player_db.sqlite"
        conn = sqlite3.connect(DB_FILE)
        conn.row_factory = sqlite3.Row


def close():
    if conn:
        conn.close()


def get_players():
    query = '''SELECT *
                FROM Player'''
    with closing(conn.cursor()) as c:
        c.execute(query)
        results = c.fetchall()
    return Lineup(results)


def get_player(playerID):
    query = '''SELECT *
                FROM Player
                WHERE playerID = ?'''
    with closing(conn.cursor()) as c:
        c.execute(query, (playerID,))
        results = c.fetchall()
    return Lineup(results)


def add_player(player):
    sql = '''INSERT INTO Player
            (batOrder, firstName, lastName, position, atBats, hits)
            VALUES (?, ?, ?, ?, ?, ?)'''
    with closing(conn.cursor()) as c:
        c.execute(sql, (player.batOrder, player.firstName, player.lastName, player.position, player.atBats, player.hits))
        conn.commit()


def delete_player(player):
    sql = '''DELETE FROM Player WHERE playerID = ?'''
    with closing(conn.cursor()) as c:
        c.execute(sql, (player,))
        conn.commit()

# >.<
def update_bat_order(lineup):
    for player in lineup:
        sql = '''UPDATE Player
                SET batOrder = ?,
                firstName = ?,
                lastName = ?,
                position = ?,
                atBats = ?,
                hits = ?
            WHERE playerID = ?'''
        with closing(conn.cursor()) as c:
        
            c.execute(sql, (player.batOrder, player.firstName, player.lastName, player.position, player.atBats, player.hits, player.playerID))
            conn.commit()

# I wasn't completely sure what exactly you wanted here to be honest.
def update_player(player):
    sql = '''UPDATE Player
            SET batOrder = ?,
                firstName = ?,
                lastName = ?,
                position = ?,
                atBats = ?,
                hits = ?
            WHERE playerID = ?'''
    with closing(conn.cursor()) as c:
        c.execute(sql, (player.batOrder, player.firstName, player.lastName, player.position, player.atBats, player.hits, player.playerID))
        conn.commit()


def main():
    # code you provided to test the get_players function
    connect()
    players = get_players()
    if players != None:
        for player in players:
            print(player.batOrder, player.firstName, player.lastName,
                player.position, player.atBats, player.hits, player.getAverage())
    else:
        print("Code is needed for the get_players function.")
    

# Some testing stuff...
    # print()
    # id = int(input("number? "))
    # ps = get_player(id)
    # for p in ps:
    #     print(p.batOrder, p.firstName, p.lastName, p.position, p.atBats, p.hits, p.getAverage())


if __name__ == "__main__":
    main()





