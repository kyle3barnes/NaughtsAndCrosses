import random

spaces = [i for i in range(1, 10)]


def setup_board():
    board = ""

    for space in spaces:
        counter = 1  # PROBLEM WITH COUNTER - WHEN COUNTER STARTS AT 1, SPACE ISN'T RECOGNISED AS BEING EQUAL TO 0 WHEN SPACE % 3
        #                                     WHEN COUNTER STARTS AT 0, THE FIRST SPACE IS DISPLAYED AS IT IS WHEN COUNTER % 3 = 0

        if space == 'X' or space == 'O':
            if counter == 9:
                board += space
            elif counter % 3 == 0:
                board += space + "\n- - - - - \n"
            else:
                board += space + " | "
        elif space == 9:
            board += str(space)
        elif space % 3 == 0:
            board += (str(space) + "\n- - - - - \n")
        else:
            board += (str(space) + " | ")
        counter += 1

    print(board)

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
            shapes = ['O', 'X']
            user_input = (input("Enter the shape you would like to play ['O' or 'X']: ")).upper()
            while user_input not in shapes:
                user_input = (input("Error, enter 'O' for naughts and 'X' for crosses: ")).upper()
        except ValueError:
            print("Error, enter 'O' for naughts and 'X' for crosses: ")
            continue
        else:
            comp_shape = shapes[(len(shapes) - 1) - shapes.index(user_input)]
            return user_input, comp_shape


def get_comp_choice_random():
    comp_choice = random.randint(1, 9)
    return comp_choice


def update_board(choice, shape):
    spaces[choice - 1] = shape
    setup_board()


if __name__ == '__main__':
    spaces, board = setup_board()
    print()
    print("callum gay")
    user_shape, comp_shape = get_shape()
    user_choice = get_user_choice()
    update_board(user_choice, user_shape)
    comp_choice = get_comp_choice_random()
    update_board(comp_choice, comp_shape)
