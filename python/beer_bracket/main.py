#!/usr/bin/env python3

import random

beers = {
    0: "Labatt Blue Light",
    1: "Miller Lite",
    2: "Coors Light",
    3: "Keystone Light",
    4: "Bud Light Platinum",
    5: "Bud Light",
    6: "Michelob Ultra",
    7: "Saint Archer Gold",
    8: "Busch Light",
    9: "Heineken Light",
    10: "Miller High Life Light",
    11: "Amstel Light"
}

pairs = []
seen = []


def rand_int():
    return random.randint(0, 11)


def print_beers():
    counter = 1
    for pair in pairs:
        print("Matchup {0} is {1} and {2}".format(
            counter, beers[pair[0]], beers[pair[1]]))
        counter = counter + 1
    return


def main():
    while len(pairs) < 6:
        int1 = rand_int()
        while int1 in seen:
            int1 = rand_int()
        int2 = rand_int()
        while int2 in seen or int2 == int1:
            int2 = rand_int()
        seen.append(int1)
        seen.append(int2)
        pair = (int1, int2)
        pairs.append(pair)
    print_beers()
    return


if __name__ == '__main__':
    main()
