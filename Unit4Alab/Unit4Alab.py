def main():
   vowel = input('whats your string')
   print(vowel)
   print(deVowel(vowel))

def deVowel(vowel):
    noVowel = ''
    for x in vowel:
        if(x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u' or x == 'y'):
         y = 82
        else:
            noVowel = noVowel + x
    return (noVowel)
main()
