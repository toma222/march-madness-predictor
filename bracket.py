
class Bracket:
    def __init__(self, Games):
        self.Games = Games
    # def


class Games:
    def __init__(self, teams):
        self.teams = teams


class Team:
    def __init__(self, name, data, score):
        self.name = name
        self.data = data
        self.score = score

    def GetData(self, i):
        return self.data[i]

    def GetName(self):
        return self.name


class Roster:
    def __init__(self, Games):
        self.Games = Games

    def FromRoster(self, name):
        for t in self.teams:
            if t.GetName() == name:
                return t

    def GetGame(self, Index):
        return self.Games[Index]
