# objects for Project 4



class Player:
    def __init__(self, playerID=0, batOrder=0, firstName="", lastName="", position="", atBats=0, hits=0):
        self.playerID = playerID
        self.batOrder = batOrder
        self.firstName = firstName
        self.lastName = lastName
        self.position = position
        self.atBats = atBats
        self.hits = hits

    def getPlayerID(self):
        return self.playerID

    def getBatOrder(self):
        return self.batOrder

    def getFirstName(self):
        return self.firstName

    def getLastName(self):
        return self.lastName

    def getFullName(self):
        return f"{self.firstName} {self.lastName}"
    
    def getPosition(self):
        return self.position

    def getAtBats(self):
        return self.atBats

    def getHits(self):
        return self.hits

    def getAverage(self):
        try:
            average = round(self.hits / self.atBats, 3)
        except ZeroDivisionError:
            average = 0
        return f"{average:.3f}"

class Lineup:
    def __init__(self, results):
        self.__lineup = []
        for row in results:
            self.__lineup.append(make_list_object(row))

    def addPlayer(self, new_player):
        self.__lineup.append(new_player)

    def remove(self, index=0):
        return self.__lineup.pop(index)

    def getLineupCount(self):
        return len(self.__lineup)

    def get(self, index=0):
        return self.__lineup[index]

    def move(self, player_index, player):
        self.__lineup.insert(player_index, player)

    def __iter__(self):
        self.__index = -1
        return self

    def __next__(self):
        if self.__index == len(self.__lineup) - 1:
            raise StopIteration
        self.__index += 1
        item = self.__lineup[self.__index]
        return item

def make_list_object(row):
    return Player(row["playerID"], row["batOrder"], row["firstName"], row["lastName"], row["position"], row["atBats"], row["hits"])

