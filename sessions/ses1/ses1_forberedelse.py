
## python vs java
# None --> null
# and, or, not --> &&, ||, !
# True, False - med stort
# is --> peger det på samme obj?
# == --< har det samme værdier
#String literal:
n = 20
print(f'Jeg har {n} papegøjer')


## Interpreted or compiled?
# https://nedbatchelder.com/blog/201803/is_python_interpreted_or_compiled_yes.html
# compiled == programmet bliver compilet til (typisk) machine code og så kørt
# interpreted == man kører programmet og det bliver fortolket én linje ad gangen
# 
# python er både compiled og interpreted
# det bliver kørt interpreted style 
# men bliver fortolket af en indbygget ting som compiler til bytecode

#£ Datatyper
# https://realpython.com/python-data-types/#floating-point-numbers
#& intergers
# kan være ligeså store som man vil

#& floating point
# kan man skrive: 
f = .4e7 # == 4000000.0
f1 = 4e7 # == 40000000.0
print(f)
print(f1)

#& complex numbers

#& strings
# hedder str
# kan være både med " og '
# hvis man vil skrive " eller ' kan man lave stringen med den anden:

s = "Her er der en string med ' i"
print(s)

s1 = 'Her er der en string med " i'
print(s1)

# eller man kan bruge \ for escape sequence

#& bool
# False og True - skrives med stort
x = True
y = False
# man kan konvertere andre datatyper til bools
# empty string, og 0 == false
print('boll(0): ' + str(bool(0))) # == false
print("bool(''): " + str(bool(''))) # == false

# strings og ikke-0 == true
print(bool(1)) # == True
print(bool('Hej')) # == True
print(bool(' ')) # == True


#& built-in functions 
#/ math
print(max(4, 7, 1, 100)) # = 100
print(min(900, 345, 100)) # = 100

print(pow(2, 3)) # == 2^3 == 

print(round(3.4)) # == 3
print(round(2.6)) # == 2

print(sum([1, 2, 3])) # == 6

## operators
# https://realpython.com/python-operators-expressions/

# at sammenligne floats
f = 1.1 + 2.2

#! dette er dårlig praksis
print(f == 3.3) # == False
#+ i stedet skal man: 
print(abs(f - 3.3) < 0.00000000001) # == True


# is --> peger det på samme obj?
# == --> har det samme værdier

#! ikke heeelt sikker på jeg er færdiiiig/det virkeeer
x = 367
y = 365 + 2
b = y
z = y + 1 - 1

print(x == y) # True
print(x is y) # False
print(x is z) # True
print(x == z) # True
print(x is 367)





## default value
# man kan bruge or til at sige: 
#   hvis den første værdi er empty så sat variablen til defaultvalue
#   syntax:     s = string or '<default_value>'

s = '' or 'defaultString'
print(s) # == defaultString


noget = ['lol', 2, 'hej', (1, 4, 5)]

print(str(noget))

print(s[-2:0]) 


n = '12345' * 5 # == '1234512345123451234512345'
print(n[::5]) # == '11111' den tager hver femde char
print(n[4::5]) # == '55555' den tager hver femde char og starter på index 4

print(s[8:0:-2]) # == ttuf - den stepper gennem stringen bagfra pga. -2
print(s[::-1]) # printer stringen bagfra



