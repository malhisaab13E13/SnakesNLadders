# Import randint module from random library to generate random numbers.
from random import randint


def get_players_list():
    """Asks for Player names and Returns a Players list"""
    player_list = [input('Please enter name of player number 1: '),
                   input('Please enter name of player number 2: ')]

    print('\nList of Players: ', player_list)

    return player_list


def generate_ladders_position():
    """Generates and returns a unique Ladders list"""
    ladders_list = []
    i = 0

    while i < 15:
        random_num = randint(5, 85)
        if random_num not in ladders_list:
            ladders_list.append(random_num)
            i += 1
        else:
            continue

    ladders_list.sort()
    print('Ladders cells: ', ladders_list)

    return ladders_list


def generate_snakes_position(ladders_list):
    """Generates and returns a unique Snakes list"""
    snakes_list = []
    i = 0

    while i < 10:
        random_num = randint(20, 95)
        if random_num not in snakes_list and random_num not in ladders_list:
            snakes_list.append(random_num)
            i += 1
        else:
            continue

    snakes_list.sort()
    print('Snakes cells: ', snakes_list)

    return snakes_list


def roll_dice(current_position, player_name):
    """Generates random number from 1 to 6 and returns new player position"""
    roll = randint(1, 6)
    current_position += roll

    print('%s dice is: %d , New position is: %d' % (player_name, roll, current_position))

    return current_position


def check_for_ladder(current_position, ladder_list, player_name):
    """Checks if position in ladders list and returns the new player position"""
    if current_position in ladder_list:
        current_position += 15
        print("Great %s ! It's a ladder, Climb up by 15 cells. Your new position is: %d"
              % (player_name, current_position))

    return current_position


def check_for_snake(current_position, snake_list, player_name):
    """Checks if position in snakes list and returns the new player position"""
    if current_position in snake_list:
        current_position -= 10
        print("Oops %s ! You've been bitten, Go down 10 cells. Your new position is: %d"
              % (player_name, current_position))

    return current_position


def main():
    """Main function"""
    player_names = get_players_list()

    players_positions = [0, 0]

    ladders_list = generate_ladders_position()

    snakes_list = generate_snakes_position(ladders_list=ladders_list)

    # While loop to roll the dice until one player scores ABOVE 99.
    while max(players_positions) <= 99:

        for x in range(0, 2):

            players_positions[x] = roll_dice(current_position=players_positions[x], player_name=player_names[x])

            # An if statement to check if
            if players_positions[x] > 99:
                print("Hurray ! Winner is %s" % (player_names[x]))
                break

            players_positions[x] = check_for_ladder(current_position=players_positions[x], ladder_list=ladders_list,
                                                    player_name=player_names[x])
            players_positions[x] = check_for_snake(current_position=players_positions[x], snake_list=snakes_list,
                                                   player_name=player_names[x])


if __name__ == main():
    main()
