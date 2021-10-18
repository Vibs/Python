
#¤ Exercise 0.1 Slicing
#By using the slicing syntax change the following collections.
#After slicing:


#! NOTER omkring slicing:
#+ list[start:stop:step]
# fx: 
#   myList = [1, 2, 3, 4, 5, 6, 7]
#   myList[::2] # --> [1, 3, 5, 7]
#
#

myList = [1, 2, 3, 4, 5, 6, 7]
print(myList[::2]) 

#& ['Hello', 'World', 'Huston', 'we', 'are', 'here'] should become -> ['World', 'Huston', 'we', 'are']
l = ['Hello', 'World', 'Huston', 'we', 'are', 'here']
t = ['Hello', 'World', 'Huston', 'we', 'are', 'here']

#& should become -> ['World', 'Huston', 'we', 'are']

worldIndex = l.index('World')
hereIndex = l.index('here')

print(l[worldIndex:hereIndex])

#& ['Hello', 'World', 'Huston', 'we', 'are', 'here'] -> ['Hello', 'World']
print(l[0:2])

#& ['Hello', 'World', 'Huston', 'we', 'are', 'here'] -> ['are', 'here']
print(l[-2:])

#& ['Hello', 'World', 'Huston', 'we', 'are', 'here'] -> ['are']
print(l[-2:-1])

#& ['Hello', 'World', 'Huston', 'we', 'are', 'here'] -> ['Hello', 'Huston', 'are']
#l1 = []
#for i in range(0, len(l), 2):
#    l1.append(l[i])

#print(l1)

print(l[::2]) # : tag alt, 

#& ['Hello', 'World', 'Huston', 'we', 'are', 'here'] -> ['here', 'are', 'we', 'Huston', 'World', 'Hello']
print(l[::-1]) # :: tag ALT med --> -1 reverse det!!!

#& ('Hello', 'World', 'Huston', 'we', 'are', 'here') should become -> ['World', 'Huston', 'we', 'are']
print(list(t[1:5])) # + list() == en built-in function

#& 'Hello World Huston we are here' -> 'World Huston we'
s = 'Hello World Huston we are here'

print(s[s.index('World'):s.index(' are')])



# ¤ EXERCISE 2


def isVowel(c):
    return c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u' or c == ' '

def removeVowels(str):
    charList = []

    for c in str:
        if not isVowel(c): # or not c == ' ':
            charList.append(c)

    return sorted(charList)

print(removeVowels("hej med dig"))


#£ EXERCISE 3
#& Create a list of strings with names in it. (l = [‘Claus’, ‘Ib’, ‘Per’])

nameList = ["Claus", "Per", "Ib", "Lizza, Zelda"]

#& Sort this list by using the sorted() build in function.

# sorted() returnerer den sorterede liste - ændrer IKKE på originallisten
nameListSorted = sorted(nameList) 
print(nameListSorted)

#& Sort the list in reversed order.

# reverse() returner none men ændrer i originallisten!!!
nameListSorted.reverse()
print(nameListSorted)

#& Sort the list on the lenght of the name.

print(sorted(nameListSorted, key=len))

#& Sort the list based on the last letter in the name.
def lastLetter(word):
    return word[-1]

print(sorted(nameListSorted, key=lastLetter))

#& Sort the list with the names where the letter ‘a’ is in the name first.

def hasAnA(word):
    return not 'a' in word

print(sorted(nameListSorted, key=hasAnA))



#¤ Opgave 4
#& 1. Create a file and call it lyrics.txt (it does not need to have any content)

#1. Cd guide til mappe hvor ny fil skal oprettes
#docker run -it --rm -v ${PWD}:/docs python bash
#Cd ind i docs-mappen
#Åbne python-interpreter inde i mappen
#Python
#Opret ny fil:
#f = open(‘[filnavn.type]’, ‘[rettigheder]’)
#f = open(‘lyrics.txt’, ‘w’)

import os

def createFile(path, fileName, mode):
    # på denne her måde kan vi selv bestemme hvor filen skal ligge
    # man skal definere den sti, hvorfra den mappe vi står i NU
    return open(os.path.join(path, fileName), mode)





#& 2. Create a new file and call it songs.docx and in this file write 3 lines of text to it.
songsFile = createFile('Python\sessions\ses2', 'songs.docx', 'w')

songsFile.write('Hej\nmed\ndig')

#& 3. open and read the content and write it to your terminal window. 
#& * you should use both the read(), readline(), and readlines() methods for this. (so 3 times the same output).

# readline() == læser én linje og laver mellemrum efter
# read() == læser HELE filen
# readlines() == læser hver linje ind som præcist skrevet tekst i en liste
songsFile = createFile('Python\sessions\ses2', 'songs.docx', 'r')
print(songsFile.readline() + songsFile.readline() + songsFile.readline()) 

songsFile = createFile('Python\sessions\ses2', 'songs.docx', 'r')
print(songsFile.read())

songsFile = createFile('Python\sessions\ses2', 'songs.docx', 'r')
print(songsFile.readlines())



#¤ Opgave 5

#& 1. Based on this list of tuples:
listOfTuples = [(1,2),(2,2),(3,2),(2,1),(2,2),(1,5), (10,4), (10, 1), (3, 1)]
#& Sort the list so the result looks like this: [(2, 1), (3, 1), (10, 1), (1, 2), (2, 2), (2, 2), (3, 2), (10, 4), (1, 5)]

# vi skal sortere efter den sidste værdi i hvert tuple - derfor laver vi en funktion som finder den sidste værdi i et tuple

def sortTuples(tuple):
    return tuple[-1]

listOfTuplesSorted = sorted(listOfTuples, key=sortTuples)

print(listOfTuplesSorted)


