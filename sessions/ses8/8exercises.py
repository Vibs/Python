
#¤ 
class Deck:
    def __init__(self):
        self.cards = ['A', 'K', '4', '7']

    def __getitem__(self, key):
        return self.cards[key]

    def __len__(self):
        return len(self.cards)

    def __add__(self, other):
        return self.cards + other.cards

    def __repr__(self):
        return f'{self.__dict__}'

    def __str__(self):
        return f'{self.cards}'

    def __setitem__(self, no, value):
        self.cards[no] = value

    def __delitem__(self, no):
        del(self.cards[no]) # her bruger vi jo faktisk top-level syntax INDE i metoden - lidt ironisk

d1 = Deck()
d2 = Deck()

# jeg vil have fat i det første kort i decket
# __getitem__
print(d1[0])

# __len__
print(len(d1))

# __add__
print(d1 + d2)

# __repr__ eller __str__
print(d1)

# __setitem__
d1[0] = 'Queen'
print(d1[0])

# __deitem__
del(d1[0])
print(d1)


#¤  linked list
#linkedList
#    - en ting på listen indeholde værdien og så en pointer hen på det næste obj
#    - det er hurtigere at slette elementer fra denne, fordi alle elemtnerene ikke skal rykke sig en plads ligesom på en arrayliste
#        - i stedet så rykker man bare pointeren på ét enkelt obj over til det næste

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None # node-obj


linkedList = LinkedList()

linkedList.head = Node('Vibe')
linkedList.head.next = Node('Rasmus')








