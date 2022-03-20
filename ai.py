
class GameProfile:
    def __init__(self, teams, weights, AddWeights):

        # First layer weights 1st team offense

        addArray = []

        for i in range(len(weights)):
            addArray.append(weights[i] + float(AddWeights[i]))

        self.w = addArray

        self.slr = 0.  # FINAL RESULT YEEEAAAA
        self.Score = 0.

        self.teams = teams

    def SolveFirstLayer(self):

        # new Ai model
        # go over every value in the teams and have the ai decide a negitive or a positive value to find the winning team

        Score = 0.
        for t in self.teams:
            for i in range(len(self.w)):
                Score += (t.GetData(i) * self.w[i])

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
