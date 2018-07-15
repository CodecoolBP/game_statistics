
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
    print('Is there a game from %s?' %year)
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
    print('How many %s games do we have?' %genre)
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
    title = input ('\nEnter title of the game that you are looking for: ')
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

def get_most_played(file_name='game_stat.txt'):
    games_list = load_file()
    sold_list = []
    i=0
    while i < len(games_list):
        sold_list.append(games_list[i][1])
        i += 1
    j=0
    for i in range(len(sold_list)):
        while float(sold_list[i]) > float(sold_list[j]):
            how_much_sold = sold_list[i]
            j+=1
        if float(sold_list[i]) < float(sold_list[j]):
            how_much_sold = sold_list[j]
    for i in range (len(games_list)-1):
        if how_much_sold in sold_list[i]:
            most_played_title = games_list[i][0]
    return most_played_title

# get_most_played()

def sum_sold(file_name='game_stat.txt'):
    games_list = load_file()
    copies_list = []
    i=0
    while i < len(games_list):
        copies_list.append(games_list[i][1])
        i += 1
    i = 0
    summary_sold = 0
    while i <len(copies_list):
        summary_sold += float(copies_list[i])
        i+=1
    return summary_sold
# sum_sold()

def get_selling_avg(file_name='game_stat.txt'):
    summary_sold = sum_sold(file_name='game_stat.txt')
    games_amount =count_games(file_name='game_stat.txt')
    average = summary_sold/games_amount
    return average
# get_selling_avg()

def count_longest_title(file_name='game_stat.txt'):
    games_list = load_file()
    title_list = []
    i = 0
    while i<len(games_list):
        title_list.append(games_list[i][0])
        i += 1
    longest_title=max(title_list,key=len)
    characters=len(longest_title)
    return characters
# count_longest_title()

def get_date_avg(file_name='game_stat.txt'):
    games_list = load_file()
    year_list = []
    i=0
    while i < len(games_list):
        year_list.append(games_list[i][2])
        i += 1
    realise_dates = 0
    i=0
    while i <len(year_list):
        realise_dates += int(year_list[i])
        i+=1
    games_amount =count_games(file_name='game_stat.txt')
    average_not_round = realise_dates/games_amount
    average = int(round(average_not_round,0))
    return average
# get_date_avg()

def get_game(file_name='game_stat.txt', title='Minecraft'):
    games_list = load_file()
    title = input ('What properties has: ')
    i=0
    while i < len(games_list):
        if title == games_list[i][0]:
            game = games_list[i]
            i+=1
        else:
            break
    return game
# get_game()