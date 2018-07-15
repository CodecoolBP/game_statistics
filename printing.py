import reports
# Printing functions
def print_how_many_games():
    reports.load_file(file_name='game_stat.txt')
    games_amount = reports.count_games(file_name='game_stat.txt')
    print('There are %g games in the file\n' %games_amount)
    


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
    print('\nThe latest game is: %s\n' %latest_title)



def print_games_genre():
    amount = reports.count_by_genre(file_name='game_stat.txt',genre='Survival game')
    print(amount)


def print_get_line_number_by_title():
    line_number = reports.get_line_number_by_title(file_name='game_stat.txt',title='Minecraft')
    print('The line number of the game is: %g' %line_number)


def print_get_most_played():
    most_played_title = reports.get_most_played(file_name='game_stat.txt')
    print('\nThe most played game is %s' %most_played_title)

def print_sum_sold():
    summary_sold = reports.sum_sold(file_name='game_stat.txt')
    print('\n%g millions of copies of our games have been sold' %summary_sold)

def print_average():
    average = reports.get_selling_avg(file_name='game_stat.txt')
    print ('\n%g million per game is the average selling' %average)

def print_characters():
    characters = reports.count_longest_title(file_name='game_stat.txt')
    print('\n%g - characters builds the longest title of our game'%characters)

def print_get_date_avg():
    average = reports.get_date_avg(file_name='game_stat.txt')
    print ('\nThe average release date is %g' %average)

def print_get_game():
    game = reports.get_game(file_name='game_stat.txt', title='Minecraft')
    print('\nGame properties:\n%s' %game)

def print_all():
    print_how_many_games()
    print_game_given_year()
    print_latest_game()
    print_games_genre()
    print_get_line_number_by_title()
    print_get_most_played()
    print_sum_sold()
    print_average()
    print_characters()
    print_get_date_avg()
    print_get_game()
print_all()