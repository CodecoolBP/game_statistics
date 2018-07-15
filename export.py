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
    print(latest_title, file=f)



def export_games_genre():
    f = open("file.txt","a")
    amount = reports.count_by_genre(file_name='game_stat.txt',genre='Survival game')
    print(amount, file=f)


def export_get_line_by_title():
    f = open("file.txt","a")
    line_number = reports.get_line_number_by_title(file_name='game_stat.txt',title='Minecraft')
    print(line_number, file=f)

def export_get_most_played():
    f = open("file.txt","a")
    most_played_title = reports.get_most_played(file_name='game_stat.txt')
    print(most_played_title,file=f)

def export_sum_sold():
    f = open("file.txt","a")
    summary_sold = reports.sum_sold(file_name='game_stat.txt')
    print(summary_sold, file=f)

def export_average():
    f = open("file.txt","a")
    average = reports.get_selling_avg(file_name='game_stat.txt')
    print (average, file=f)

def export_characters():
    f = open("file.txt","a")
    characters = reports.count_longest_title(file_name='game_stat.txt')
    print(characters,file=f)

def export_get_date_avg():
    f = open("file.txt","a")
    average = reports.get_date_avg(file_name='game_stat.txt')
    print (average,file=f)

def export_get_game():
    f = open("file.txt","a")
    game = reports.get_game(file_name='game_stat.txt', title='Minecraft')
    print(game,file=f)

def export_all():
    export_how_many_games()
    export_game_given_year()
    export_latest_game()
    export_games_genre()
    export_get_line_by_title()
    export_get_most_played()
    export_sum_sold()
    export_average()
    export_characters()
    export_get_date_avg()
    export_get_game()
export_all()