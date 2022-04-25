import random
import requests
response = requests.get('http://www.mieliestronk.com/corncob_lowercase.txt')
data = (response.text).split('\r')
rword =data[random.randint(1,len(data))].strip()
gcount = 6
rlist = list(rword)
wordlen = len(rword)
guesslist = []
dumlist = list('_'*wordlen)
print(dumlist)
while(gcount > 0):
    print("No. of tried remaining are",gcount)
    g = input('Guess an alphabet in the word: ')
    if len(g) > 1:
        print('Please enter a single alphabet')
    elif g in guesslist:
        print('You already guessed the letter',g)
    elif g in rlist:
        guesslist.append(g)
        n = [j for j, letter in enumerate(rword) if letter == g]
        for i in n:
            dumlist[i] = rlist[i]
        print(dumlist)
        if(dumlist == rlist):
            print('You guessed it correctly!, The word is',rword)
            gcount = 0
        gcount = gcount - 1
    else:
        print('Provided alphabet not found, Try again!')
        guesslist.append(g)
        gcount = gcount-1
    if(gcount == 0):
        print('Your 6 tries are over!, The word is',rword)


