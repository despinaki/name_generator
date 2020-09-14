drag_dict = {
    'a': 'ara',
    'b': 'bor',
    'c': 'cli',
    'd': 'dor',
    'e': 'elv',
    'f': 'for',
    'g': 'gra',
    'h': 'hor',
    'i': 'ika',
    'j': 'jet',
    'k': 'kla',
    'l': 'luu',
    'm': 'mog',
    'n': 'neu',
    'o': 'oxl',
    'p': 'pyr',
    'q': 'quo',
    'r': 'rex',
    's': 'sym',
    't': 'tro',
    'u': 'uwe',
    'v': 'vor',
    'w': 'wel',
    'x': 'xyl',
    'y': 'yer',
    'z': 'zul'
}
peng_dict = {
    'a': 'arp',
    'b': 'boog',
    'c': 'cle',
    'd': 'dil',
    'e': 'eep',
    'f': 'fly',
    'g': 'geb',
    'h': 'hoo',
    'i': 'iki',
    'j': 'jee',
    'k': 'klee',
    'l': 'loof',
    'm': 'mango',
    'n': 'neep',
    'o': 'ordy',
    'p': 'phil',
    'q': 'queen',
    'r': 'rest',
    's': 'sloop',
    't': 'tree',
    'u': 'uvan',
    'v': 'ver',
    'w': 'woop',
    'x': 'xeus',
    'y': 'yeeb',
    'z': 'zogo'
}
month_dict = {
    1: 'on',
    2: 'uin',
    3: 'exus',
    4: 'fly',
    5: 'mon',
    6: 'rah',
    7: 'flex',
    8: 'trim',
    9: 'pi',
    10: 'yelp',
    11: 'fin',
    12: 'leet'
}
def to_dragon(letter, month):
    return drag_dict[letter] + month_dict[int(month)]


def to_penguin(letter, month):

    return peng_dict[letter] + month_dict[int(month)]
    
def user_exit(userinput):
    if userinput=='exit':
        exit()
    
def month_valid():
    my_bool = True
    while my_bool:
        try:

            month = input("Enter your birth month (1-12) or type 'exit' to exit.\n")
                
            if int(month) <= 12 and int(month) >= 1:
                my_bool= False
                return int(month)  
        except:
            user_exit(month)
            my_bool = True
            
      
        
def peng_or_drag():
    my_bool = True
    while my_bool:
        somevar = (input("Enter 1 for your dragon name or 2 for your penguin name or type 'exit' to exit.\n"))
        user_exit(somevar)
        if int(somevar) == 1 or int(somevar) == 2:
            mybool = False
            return int(somevar)