
class GameProfile:
    def __init__(self, teams, weights, AddWeights):

        # First layer weights 1st team offense

        addArray = []

        for i in range(len(weights)):
            addArray.append(round(weights[i] + float(AddWeights[i])))

        self.w = addArray

        self.slr = 0.  # FINAL RESULT YEEEAAAA

        self.teams = teams

    def SolveFirstLayer(self):

        # TODO take score of both teams and subtract them

        Score = 0.

        T1 = 0.
        T2 = 0.

        for i in range(len(self.w)):
            T1 += (self.teams[0].GetData(i) * self.w[i])
            T2 += (self.teams[1].GetData(i) * self.w[i])

        Score = (T2 - T1)

        if Score > 0:
            # print(self.teams[0].GetName())
            return 1
        elif Score < 0:
            # print(self.teams[1].GetName())
            return 0
        elif Score == 0:
            # print('Tie')
            return 2

    def GetCurWeights(self):
        return self.w
