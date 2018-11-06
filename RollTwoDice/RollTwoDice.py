import random
ROLLNUM = 2

def main():
    setOfDice = [0] * 6
    setOfDice = defineDice()

    printDiceSideBySide(setOfDice)

    play = 'y'
    game = 0

    while play == 'y':
        for i in range(0,22):
            print('_', end = '')

        print()
        game += 1
        print('game - ' + str(game))

        play = input('play again - y or n - ')

    print('you played ' + str(game) + ' times')


def defineDice():
    dice = [0] * 6
    topBot = ' ------- '
    blank =  '|       |'
    oneDotL= '| *     |'
    oneDotM= '|   *   |'
    oneDotR= '|     * |'
    twoDot = '|  * *  |'

    for num in range(0, 6):
        if num == 0:
            dice[num] = [topBot,blank,oneDotM,blank,topBot]
        elif num == 1:
            dice[num] = [topBot,blank,twoDot,blank,topBot]
        elif num == 2:
            dice[num] = [topBot,oneDotL,oneDotM,oneDotR,topBot]
        elif num == 3:
            dice[num] = [topBot,twoDot,blank,twoDot,topBot]
        elif num == 4:
            dice[num] = [topBot,twoDot,oneDotM,twoDot,topBot]
        else:
            dice[num] = [topBot,twoDot,twoDot,twoDot,topBot]

    return dice

def rollDice():
    print('roll dice')
    diceNum = random.randint(0,5)
    return diceNum

def printDiceSideBySide(diceSet):
    print(diceSet)
    for row in range(0,0):
        for col in range(0,0):
            print(diceSet[col][row], end = '\t')
        print()

main()
