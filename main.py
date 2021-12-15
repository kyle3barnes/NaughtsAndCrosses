import random

spaces = [i for i in range(1, 10)]


def setup_board():
    board = ""

    for space in spaces:
        if space == 9:
            board += str(space)
        elif space % 3 == 0:
            board += (str(space) + "\n- - - - - \n")
        else:
            board += (str(space) + " | ")
    return spaces, board


def get_user_choice():
    while True:
        try:
            user_input = int(input("Enter the number of space on the board you would like to play: "))
            while user_input not in spaces:
                user_input = int(input("Error, enter a valid number [1-9]: "))
        except ValueError:
            print("Error, enter a valid number [1-9]: ")
            continue
        else:
            return user_input


def get_shape():
    while True:
        try:
            user_input = input("Enter the shape you would like to play ['O' or 'X']: ")
            while user_input not in ['O', 'X']:
                user_input = input("Error, enter 'O' for naughts and 'X' for crosses: ")
        except ValueError:
            print("Error, enter 'O' for naughts and 'X' for crosses: ")
            continue
        else:
            return user_input


def get_comp_choice_random():
    comp_choice = random.randint(1, 10)
    return comp_choice


def update_board(user_choice, shape):
    spaces[user_choice] = shape
    setup_board()


if __name__ == '__main__':
    spaces, board = setup_board()
    print(board)
    print()
    print("callum gay")
    user_choice = get_user_choice()
    shape = get_shape()
    update_board(user_choice, shape)
    comp_choice = get_comp_choice_random()
