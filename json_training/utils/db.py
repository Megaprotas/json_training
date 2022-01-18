import json

games_json_file = 'games.json'


def crate_games_db():
    with open(games_json_file, 'w') as json_file:
        json.dump([], json_file) # json file can't be empty so square brackets are required in json file


def add_game_db(name, studio):
    games = games_list()
    games.append({'name': name, 'studio': studio, 'played': False})
    _save_all_games(games)


def games_list():
    with open(games_json_file, 'r') as json_file:
        return json.load(json_file)


def mark_as_played_in_db(name):
    games = games_list()
    for game in games:
        if game['name'] == name:
            game['played'] = True
    _save_all_games(games)


def _save_all_games(games):
    with open(games_json_file, 'w') as json_file:
        json.dump(games, json_file) # add games into file


def delete_game_from_db(name):
    games = games_list()
    games = [game for game in games if game['name'] != name]
    _save_all_games(games)



