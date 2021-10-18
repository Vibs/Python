
#! list comprehension: en forkortet måde at skrive et for-each loop på
# fx: i stedet for:
l1 = []

for i in range(1, 10):
    l1.append(i)

# kan man sige:
l2 = [i for i in range(1,10)]

#& man kan inkludere if else i list comprehension
# printer: ['Not even', 2, 'Not even', 4, 'Not even', 6, 'Not even', 8, 'Not even']
evenNotEven = [i if i % 2 == 0 else 'Not even' for i in range(1,10)]

# vs uden list comprehension:
evenNotEven1 = []

for i in range(1,10):
    if i % 2 == 0:
        evenNotEven1.append(i)
    else:
        evenNotEven1.append('Not even')

#
#
#
#
#
#
#
#



