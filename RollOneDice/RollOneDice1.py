import random
def main():
    gamesPlayed = 0
    while(input('do you want to play again? y or n - ') == 'y'):
        dice()
        gamesPlayed += 1
        print('you have played' + str(gamesPlayed) + ' times,\n__________')
    else:
        print('thanks for playing')


def dice():
    dice1 = (' ------- \n|       |\n|   *   |\n|       |\n -------')
    dice2 = (' ------- \n| *     |\n|       |\n|     * |\n -------')
    dice3 = (' ------- \n| *     |\n|   *   |\n|     * |\n -------')
    dice4 = (' ------- \n| *   * |\n|       |\n| *   * |\n -------')
    dice5 = (' ------- \n| *   * |\n|   *   |\n| *   * |\n -------')
    dice6 = (' ------- \n| *   * |\n| *   * |\n| *   * |\n -------')
    randInt = randomNumber()
    if randInt == 1:
        print(dice1)
    elif randInt == 2:
        print(dice2)
    elif randInt == 3:
        print(dice3)
    elif randInt == 4:
        print(dice4)
    elif randInt == 5:
        print(dice5)
    elif randInt == 6:
        print(dice6)
    else:
        print('why tho')

def randomNumber():
    return random.randint(1,6)

main()
