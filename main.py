
from random import random
from time import sleep

from MakeArrayIterations import Enum
from ai import GameProfile
from bracket import Bracket, Games, Roster, Team


if __name__ == '__main__':

    WINNING_SCORE = 1

    Game1 = Games(teams=[Team('UAB Blazers', [80.7, 38.4, 13.0, 9.6, 4.3, 11.5, 46.8, 73.8, 37.9, 34
                                              ], 0),
                         Team('Houston Cougars', [75.8, 39.2, 16.7, 8.2, 5.2, 11.3, 46.9, 66.9, 34.1, 34
                                                  ], 0)])

    Game2 = Games(teams=[Team('Baylor Bears', [76.5, 37.1, 15.8, 8.8, 3.4, 12.5, 46.4, 69.8, 34.6, 32
                                               ], 0),
                         Team('North Carolina', [77.5, 39.8, 14.8, 5.4, 3.8, 11.7, 45.3, 77.2, 36.2, 33
                                                 ], 0)])

    Game3 = Games(teams=[Team('Delleware', [73.8, 32.8, 12.7, 6.6, 3.7, 12.6, 46.9, 74.3, 35.2, 34
                                            ], 0),
                         Team('Villinova', [72.6, 34.9, 12.1, 6.2, 2.3, 10.0, 43.7, 82.3, 35.9, 33
                                            ], 0)])

    Game4 = Games(teams=[Team('Wright State', [75.5, 34.9, 13.9, 5.8, 2.9, 12.3, 46.5, 76.8, 32.9, 34
                                               ], 0),
                         Team('Arizona', [65.4, 35.5, 13.4, 6.7, 4.2, 11.9, 41.4, 66.1, 30.7, 31
                                          ], 0)])

    Game5 = Games(teams=[Team('LSU', [73.1, 36.9, 12.7, 11.1, 4.4, 14.5, 44.0, 73.2, 31.9, 33, 32
                                      ], 0),
                         Team('Iowa state', [66.5, 32.0, 14.7, 8.4, 3.1, 13.8, 43.9, 68.4, 32.1, 32
                                             ], 0)])

    Rost = Roster(Games=[Game1, Game2, Game3, Game4, Game5])

    # -------------- Calcs everything ---------------

    En = Enum()  # .printAllKLength(['0.1', '-.1', '0'], 11)
    En.printAllKLength(['0.1#', '-0.1#', '0#'], 10)

    Fitness = 0
    Gen = 0
    WinningWeights = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    while Fitness < .98:

        Keep = 0
        Test = 0

        AiKeepers = []

        for i in En.Combos:
            # parse the string to an array of numbers and send it into a half baked AI
            w = i.split('#')

            GamesEvaled = 0
            Correct = 0

            Test += 1

            for Game in Rost.Games:
                AI = GameProfile(teams=Game.teams, weights=WinningWeights,
                                 AddWeights=w)

                outcome = AI.SolveFirstLayer()

                if outcome == WINNING_SCORE:
                    Correct += 1

            if Correct == 5:
                Keep += 1
                AiKeepers.append(AI)

        Fitness = Keep / Test
        Gen += 1
        WinningWeights.clear()

        # prefer models that are close to zero

        keep = AiKeepers[0]

        WinningWeights = keep.w

        print('-' * 50)
        print(f'Generation {Gen} Finished with {Fitness} Accuracy')
        print(f'Generation finished with {WinningWeights} As Weights')
        print('-' * 50)
        sleep(5)
    # UAB blazers lost
