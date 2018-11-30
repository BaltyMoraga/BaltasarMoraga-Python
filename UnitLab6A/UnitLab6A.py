def main () :
    dict = {'lol':'laughing out loud','omw':'on my way','omg':'oh my god'}
    d = 'y'
    while d=='y' :
        f = input("use dict, modify dict, view dict, or clear console? (u/m/v/c) - ")
        if f=='u' :
            dict = normal(dict)
        elif f=='m' :
            dict = mod(dict)
        elif f=='c' :
            print('\n'*50)
        else :
            dict = view(dict)

def normal (dict) :
    x='y'
    while x=='y' :
        d = input('Put in abreviattion - ')
        if d in dict :
            print(dict[d])
        else :
            print("This isnt in the dict currently")
            n = input("Would you like to add it to the dict? (y/n) - ")
            if n=='y' :
                c = input("What does that stand for - ")
                dict[d] = c

        x = input('Would you like to read another abreviattion (y/n) - ')
        print()
    return(dict)

def mod (dict) :
    x = 'y'
    while x=='y' :
        f = input("Would you like to remove or edit an entrey (r/e) - ")
        if f=='r' :
            l = input("What abreviation would you like to remove? - ")
            del dict[l]
        elif f=='e' :
            g = input("What abreviation would you like to edit? - ")
            q = input("What does that abreviation actually stand for? - ")
            del dict[g]
            dict[g] = q
        else :
            print("This isn't valid, please input an r or e for remove and edit!")
        x = input("Would you like to remove another item(y/n) - ")
        print()
    return(dict)

def view(dict) :
    for x in dict :
        print(x + ' : ' + dict[x] + '      ', end='')
    print()
    print()
    return (dict)

main()
