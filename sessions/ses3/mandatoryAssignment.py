# Assignments:

#& 1. Model an organisation of employees, management and board of directors in 3 sets.

boardOfDirectors = {'Benny', 'Hans', 'Tine', 'Mille', 'Torben', 'Troels', 'Søren'}

management = {'Tine', 'Trunte', 'Rane'}

employees = {'Niels', 'Anna', 'Tine', 'Ole', 'Trunte', 'Bent', 'Rane', 'Allan', 'Stine', 'Claus', 'James', 'Lars'}

# who in the board of directors is not an employee?

directorAndNotEmployee = boardOfDirectors - employees
print(directorAndNotEmployee)

# ELLER
directorAndNotEmployee = boardOfDirectors.difference(employees)
print(directorAndNotEmployee)

# who in the board of directors is also an employee?

directorAndEmployee = boardOfDirectors - directorAndNotEmployee
print(directorAndEmployee)

# how many of the management is also member of the board?
managementAndBoard = management.intersection(boardOfDirectors)
print("Hej " + str(len(managementAndBoard)))

# All members of the managent also an employee?
print(management.issubset(employees))

# All members of the management also in the board?
print(management.issubset(boardOfDirectors))

# Who is an employee, member of the management, and a member of the board?
print(managementAndBoard.intersection(employees))
# ELLER
print(set(boardOfDirectors) & set(management) & set(employees))

# Who of the employee is neither a memeber or the board or management?
# Hvem er KUN employee
print(employees - boardOfDirectors - management)

#¤ 2. Using a list comprehension create a list of tuples from the folowing datastructure
dictionary = {'a' : 'Alpha', 'b' : 'Beta', 'g': 'Gamma'} # det er et dictionary

listWithTuples = [(x, dictionary[x]) for x in dictionary]

print(listWithTuples)

# 3. From these 2 sets:
set1 = {'a', 'e', 'i', 'o', 'u', 'y'}
set2 = {'a', 'e', 'i', 'o', 'u', 'y', 'æ' ,'ø', 'å'}

# Of the 2 sets create a:
# Union == at alle værdier lægges sammen BORTSET fra gentagne værdier
setUnion = set1.union(set2)
print(setUnion)

# Symmetric Difference
print(set1.symmetric_difference(set2))

# Difference
print(set1.difference(set2))
print(set2.difference(set1))

# Disjoint
print(set1.isdisjoint(set2))

#4. Date Decoder.
#A date of the form 8-MAR-85 includes the name of the month, which must be translated to a number.
date = '8-MAR-85'

#Create a dict suitable for decoding month names to numbers.
months = {'JAN': '01', 'FEB': '02', 'MAR': '03', 'APR': '04', 'MAY': '05', 'JUN': '06', 
'JUL': '07', 'AUG': '08', 'SEP': '09', 'OCT': '10', 'NOV': '11', 'DEC': '12'}

#Create a function which uses string operations to split the date into 3 items using the "-" character.
def splitDate(date):
    return date.split('-')

newDate = splitDate(date)
    
#Translate the month, correct the year to include all of the digits.
def writeFullYear(year):
    return '19' + year if int(year) > 21 else '20' + year # [værdi] if [condition] else [værdi]

newDate[1] = months[newDate[1]] # converts month
newDate[2] = writeFullYear(newDate[2]) # converts year

print(newDate)

#The function will accept a date in the "dd-MMM-yy" format and respond with a tuple of ( y , m , d ).
def dateToTuple(date):
    dateList = splitDate(date)
    dateList.reverse()

    return tuple(x for x in dateList)

print(dateToTuple(date))