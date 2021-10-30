

class A:
    def __init__(self): # self == det objekt som bliver oprettet
        self.name = 'Claus'
    def ___len__(self):
        return len(self.name)

    def __add__(self, other):
        return self.name + other.name

    # hvis vi prøver på at skrive et obj ud, skrive den der der noget ud
    # i python kan man også lave en toString - der findes to toString i py:
    #   __repr__ == en formel måde at repræsentere obj på - beskrivelse til programmør
    #   __str__ == en uformel - beskrivelse til min mormor
    def __repr__(self):

        # self.__dict__ == vil ikke returnere string - derfor omformaterer vi den via f'{}'
        return f'{self.__dict__}'

    def __str__(self):
        return self.name


a = A()
b = A()

# print(len(a))
print("Hej")

print(a + b)

print(repr(a)) # her bruger den enten __repr__ eller __str__-metoden
print(a)


#
#
#

