
class Person:
    # han vil lave getter og setter udenfor init i stedet for at sige: self.name = name
    def __init__(self, name):
        self.name = name


# når jeg laver klassen flere gange, så overskriver den bare den gamle definition af klassen
#   dette ville den ikke gøre i java - der ville den lave en fejl
# pass == signalerer at denne funktion eller klasse er tom
class Person:
    def __init__(self):
        pass


# __age == __ == gør age-variablen private
class Person:
    def __init__(self, name):
        self.name = name
        self.__age = 23

p = Person('Vibe')

print(p.__age) # printer fejl


# Klasse med private variabler (proporties)
#   man vil dog aldrig i pyhton bare lave det private af ingen grund
#   man vil kun lave den private af en eller anden grund, som fx at man tjekker noget: 
#       if type(name) != str: 
#           print('puhaaa') 
#       else:
#           self.__name = name

#   Claus siger at ligeså snart man har et eller andet kriterie for hvad variablen må være, så kan man ikke klare det med en public variabel - så skal man bruge en private
#!  hele pointen med at vi laver proporties for at lave variablerne private, er FOR AT man kan bruge dot-notation - for at man kan skrive:
#   p.name = 'Vibe'
#   I STEDET FOR:
#   p.setName('Vibe')
#!      fordi det er nemmere at læse (åbenbart)
class Person:
    def __init__(self, name):
        self.name = name # her er det en public variabel -> har vi lavet til proporty
        self.__age = 23

    # denne svarer til en getter
    @property
    def name(self):
        return self.__name

    # vi vil godt blive ved med at lave dot-notation - så derfor gør vi det på denne måde i stedet for at lave en getter og setter
    # konceptet er det samme som getter og setter
    # når man så bruger dot-notation, så vil den bruge. fx:
    #       p = Person('Henning') - bruger nu setteren og ikke bare direkte
    @name.setter
    def name(self, name):
        self.__name = name

    

    def getAge(self):
        return self.__age
