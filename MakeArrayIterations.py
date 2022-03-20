# Python 3 program to print all
# possible strings of length k

# The method that prints all
# possible strings of length k.
# It is mainly a wrapper over
# recursive function printAllKLengthRec()

import numpy


class Enum:
    def __init__(self):
        self.Combos = []
        self.num = 0

    def GetNum(self):
        return self.num

    def printAllKLength(self, set, k):

        n = len(set)
        self.printAllKLengthRec(set, "", n, k)

    def printAllKLengthRec(self, set, prefix, n, k):

        # Base case: k is 0,
        # print prefix
        if (k == 0):

            print(prefix)
            self.num += 1
            self.Combos.append(prefix)
            return

        # One by one add all characters
        # from set and recursively
        # call for k equals to k-1
        for i in range(n):

            # Next character of input added
            newPrefix = prefix + set[i]

            # k is decreased, because
            # we have added a new character
            self.printAllKLengthRec(set, newPrefix, n, k - 1)


# Driver Code
if __name__ == "__main__":

    print("First Test")
    set1 = ['.1', '-.1', '0']
    set2 = ['2', '2', '2']
    k = 11
    En = Enum()  # .printAllKLength(['0.1', '-.1', '0'], 11)
    En.printAllKLength(['1', '2', '3'], 3)

    print(numpy.add(set1, set2))
    print(En.num)
    print(En.Combos[0])
