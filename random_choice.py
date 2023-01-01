from random import choice

animes = [['naruto', 'pepehype', 'forever', 'series'],
['haikyuu', 'sports', 'short', 'series'],
['mushishi', 'chill', 'short', 'series'],
['march comes in like a lion', 'slice of life', 'short', 'series']]

# input mood
print('What mood are you in?')
mood = input()

# loop through and find a matching mood
for item in animes:
    if item[1] == mood:
        print(mood + ' anime: ' + item[0])