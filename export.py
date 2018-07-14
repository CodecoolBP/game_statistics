# Export functions
import reports
def export_how_many_games():
    f = open("file.txt","w")
    reports.load_file(file_name='game_stat.txt')
    games_amount = reports.count_games(file_name='game_stat.txt')
    print (games_amount, file=f)

    


def export_game_given_year():
    f = open("file.txt","a")
    boolean = reports.decide(file_name='game_stat.txt', year='2000')
    if boolean == 1:
        print('True', file=f)
    elif boolean == 2:
        print('False', file=f)
    else:
        pass



def export_latest_game():
    f = open("file.txt","a")
    latest_title = reports.get_latest(file_name='game_stat.txt')
    print('The latest game is: %s' %latest_title, file=f)



def export_games_genre():
    f = open("file.txt","a")
    amount = reports.count_by_genre(file_name='game_stat.txt',genre='Survival game')
    print(amount, file=f)


def export_get_line_by_title():
    f = open("file.txt","a")
    line_number = reports.get_line_number_by_title(file_name='game_stat.txt',title='Minecraft')
    print('The line number of the game is: %g' %line_number, file=f)



def export_all():
    export_how_many_games()
    export_game_given_year()
    export_latest_game()
    export_games_genre()
    export_get_line_by_title()
export_all()