import reports
# Printing functions
def print_how_many_games():
    reports.load_file(file_name='game_stat.txt')
    games_amount = reports.count_games(file_name='game_stat.txt')
    print(games_amount)
    


def print_game_given_year():
    boolean = reports.decide(file_name='game_stat.txt', year='2000')
    if boolean == 1:
        print('True')
    elif boolean == 2:
        print('False')
    else:
        pass


def print_latest_game():
    latest_title = reports.get_latest(file_name='game_stat.txt')
    print('The latest game is: %s' %latest_title)



def print_games_genre():
    amount = reports.count_by_genre(file_name='game_stat.txt',genre='Survival game')
    print(amount)


def print_get_line_number_by_title():
    line_number = reports.get_line_number_by_title(file_name='game_stat.txt',title='Minecraft')
    print('The line number of the game is: %g' %line_number)



def print_all():
    print_how_many_games()
    print_game_given_year()
    print_latest_game()
    print_games_genre()
    print_get_line_number_by_title()
print_all()