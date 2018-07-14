
# Report functions
def load_file(file_name='game_stat.txt'):
    with open(file_name,'r') as file:
        games_list = []
        for line in file.readlines():
            line=line.strip().split('\t')
            games_list.append (line)
    return games_list


def count_games(file_name='game_stat.txt'):
    games_list = load_file()
    games_amount = len(games_list)
    return games_amount

# count_games()

def decide(file_name='game_stat.txt', year='2000'):
    games_list = load_file()
    year_list = []
    i=0
    year = input ('Enter game release year:')
    while i < len(games_list):
        year_list.append(games_list[i][2])
        i += 1
    if year in year_list:
        boolean = 1
        pass
    else: 
        boolean = 2
    return boolean

    
# decide()

def get_latest(file_name='game_stat.txt'):
    games_list = load_file()
    year_list = []
    i=0
    while i < len(games_list):
        year_list.append(games_list[i][2])
        i += 1
        latest_game = (max(year_list))
    for i in range (len(games_list)-1):
        if latest_game in year_list[i]:
            latest_title = games_list[i][0]
    return latest_title

# get_latest()

def count_by_genre(file_name='game_stat.txt',genre='Survival game'):
    games_list = load_file()
    genre = input ('Enter genre you want to know about: ')
    genre_list = []
    i = 0
    while i <len(games_list):
        genre_list.append(games_list[i][3])
        i +=1
    amount = genre_list.count(genre)
    return amount

# count_by_genre()


def get_line_number_by_title(file_name='game_stat.txt',title='Minecraft'):
    games_list = load_file()
    title = input ('Enter title of the game: ')
    title_list = []
    i = 0
    while i<len(games_list):
        title_list.append(games_list[i][0])
        i += 1
    for i in range (len(games_list)-1):
        if games_list[i][0] == title:
            line_number = i+1
        else: 
            pass
    return line_number
# get_line_number_by_title()