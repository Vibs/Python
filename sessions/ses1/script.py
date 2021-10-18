
# + def = keyword man bruger til at definere en funktion
# + indenting == {}
# def msg(){
#   print("Hello World")
# }


def msg(name):
    print('Hello World')
    if name == 'Vibe': # ikke parentes og kolon og ikke 
        print(f'Hello {name}') # + PRINT!!!!!
    else:
        print('You\'re not Vibe')

msg('Vibe')
