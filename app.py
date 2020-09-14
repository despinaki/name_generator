from helpers import to_dragon, to_penguin, user_exit, peng_or_drag, month_valid

def user_interaction():

    user_name = input("Enter your name or type 'exit' to exit.\n")
    user_exit(user_name)
    user_month = month_valid()
    
    my_num = peng_or_drag()
 

    if my_num == 1:
        print(f'Your dragon name is {to_dragon(user_name[0], user_month)}!')
        user_exit(input('press enter to play again or type \'exit\' to quit \n'))
        user_interaction()
    elif my_num == 2:
        print(f'Your penguin name is {to_penguin(user_name[0], user_month)}!')
        user_exit(input('press enter to play again or type \'exit\' to quit \n'))
        user_interaction()

user_interaction()