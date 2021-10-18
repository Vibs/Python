
## Ex 1: Alphabet List Comprehensions
#& Create a list of capital letters in the english alphabet
# chr() == used to get a string representing of a character which points to a Unicode code integer.
# range(65-91) fordi det engelske alfabet i capital letters ligger i den range 
englishCapLetters = [chr(i) for i in range(65, 91)]
print('englishCapLetters: ', englishCapLetters)

#& Create a list of capital letter from the english aplhabet, but exclude 4 with the Unicode code point of either 70, 75, 80, 85.
lettersWithout70 = [chr(i) for i in range(65, 91) if i not in [70, 75, 80, 85]]
print('lettersWithout70: ', lettersWithout70)

#& Create a list of capital letters from from the english aplhabet, but exclude every second between F & O
# range(70, 80, 2) == mellem 70-80 skip every 2
lettersEverySecond = [chr(i) for i in range(65,91) if i not in range(70, 80, 2)]
print('lettersEverySecond: ', lettersEverySecond)

## Ex 2: Clothes List Comprehension

#& From 2 lists, using a list comprehension, create a list containing:
#[(‘Black’, ‘s’), (‘Black’, ‘m’), (‘Black’, ‘l’), (‘Black’, ‘xl’), (‘White’, ‘s’), (‘White’, ‘m’), (‘White’, ‘l’), (‘White’, ‘xl’)]
colors = ['Black', 'White']
sizes = ['s', 'm', 'l', 'xl']

# laver et nyt tuple (a, b) af de to lister
clothes = [(a, b) for a in colors for b in sizes]
print('clothes', clothes)

#If the tuple pair is in the following list, it should not be added to the comprehension generated list. == only xxl should be added
sold_out = [('Black', 'm'), ('White', 's'), ('White', 'xxl')]

[clothes.append(t) for t in sold_out if t not in clothes]
print('clothes', clothes)

