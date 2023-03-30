import requests
import json
import bs4
import re 
""""This code pulls the System Requirements - Minimum: data from the Steam API. It then puts
the data into a dictionary so each individual specification can be neatly pulled."""
# JSON data housing appid-name data for every game on Steam

# This block of code transforms the above data into something we can use. This below code
# creates a dictionary containing the entire Steam library game collection whose keys are app ids and 
# values are the name of the game.
def create_dictionary_library():
    """Makes an API request to Steam's API and pulls JSON data holding app-id/game name information for
    every game on Steam. Function then creates a user-friendly dictionary whose k-v pairs are {appid:gamename}.
    Returns {appid: gamename} dictionary.
    Params: None"""
    app_ids = 'https://api.steampowered.com/ISteamApps/GetAppList/v2/'
    r = requests.get(app_ids).text
    data = json.loads(r)
    list_dictionaries = data['applist']['apps']
    all_games_dic = {}
    for dic in list_dictionaries:
        app_id = dic.pop('appid')
        name = dic.pop('name')
        if name == '':
            continue
        dic[app_id] = name
        all_games_dic.update(dic)
    return all_games_dic

def find_app_id(library, game):
    """Returns app id for any game on Steam.
    Params: Dict -> All-games dictionary
            Str -> Game name"""
    for item in library.items():
        """"Loops through our giant dictionary containing {appid:gamename} searching for a string game name
        that matches the parameter game that went into the function."""
        try:
            if game == item[1]:
                app_id = item[0]
                return app_id
        except KeyError:
                continue



def return_game_specs(library, game):
    """Returns the System Requirements - Minimum: data in the form of a user-friendly dictionary whose
    k-v pairs mimic exactly what is seen on Steam.
    Params: Dict -> All-games dictionary
            Str -> Game name"""
    for item in library.items():
        """"Loops through our giant dictionary containing {appid:gamename} searching for a string game name
        that matches the parameter game that went into the function."""
        try:
            if game == item[1]:
                app_id = item[0]
                break
        except KeyError:
                continue
    """Below we make another call to the Steam API at a different endpoint. We need
    to put our newfound appid as a parameter to this URL's query so the Steam API
    knows for which game to fetch us JSON data."""
    lnk = f'https://store.steampowered.com/api/appdetails/?appids={app_id}'
    rr = requests.get(lnk).text
    data = json.loads(rr)
    #"pc_requirements" is the key we want
    """We are using BeautifulSoup below to parse through the HTML and get at the 
    System Requirements - Minimum: data that's displayed for every Steam game on their storepage."""
    min_specs = data[str(app_id)]['data']['pc_requirements']['minimum']
    min_soup = bs4.BeautifulSoup(str(min_specs),'lxml')
    min_soup_tags = min_soup.find_all('li')
    min_reqs = {}
    for tag in min_soup_tags:
        """Right now, these tags look messy. We want to strip away the actual <li>,<b>,etc. tags and
        just get at the text within so we can formulate our minimum requirements dictionary."""
        if isinstance(tag.contents[0],bs4.element.NavigableString):
            """Checks and skips over tag <li>Requires a 64-bit processor and operating system<br/></li>. This
            tag is completely irrelevant for my program and including it would break the program since
            it wouldn't allow for an 'OS' key.
            """
            continue
        spec = tag.contents[0].text + tag.contents[1].text
        split_spec = spec.split(':')
        min_reqs[split_spec[0].strip()] = split_spec[1].strip()
    return min_reqs


