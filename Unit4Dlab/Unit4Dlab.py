def main():
    shoppingCart = [['tooth paste','q-tips','milk'],['milk','candy','apples'],['paper','pencils','q-tips']]
    print(allInOne(shoppingCart))
    print('you have ' + str(countQTips(shoppingCart)) + 'q-tips')

def allInOne(largeList):
    bigList = []
    for lists in largeList:
        for items in lists:
            if items not in bigList:
                bigList.append(items)
    return bigList

def countQTips(largeList):
    qTipCount = 0
    for lists in largeList:
        for items in lists:
            if items == 'q-tips':
                qTipCount += 1
    return qTipCount

main()
