def main():
   vowel = input('whats your string')
   print(vowel)
   print(deVowel(vowel))
   input('pause')

   list = [1,2,3,4]
   m = 2
   print(mathStuff(list, m))

def deVowel(vowel):
    noVowel = ''
    for x in vowel:
        if(x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u' or x == 'y' or x == 'A' or x == 'E' or x == 'I' or x == 'O' or x == 'U' or x == 'Y'):
         y = 82000
        else:
            noVowel = noVowel + x
    return (noVowel)

def mathStuff(list, m):
    listf = []
    for x in list:
        listf.append(float(x) * float(m))
    return(listf)

main()
