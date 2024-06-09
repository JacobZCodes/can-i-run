from bottle import route, run, template, get, post, request, static_file, error, response, redirect, error, abort, Bottle
import requests
import re 
import json
import bs4
def find_suffix(gensku):
    """Finds if our gensku has a suffix at the end. Returns a tuple containing the gensku and the suffix
    if it has one. If there is no suffix, its value will be None.
    Params: Str -> Gensku"""
    if re.search("\D",gensku):
        p = re.compile("\D(.*)")
        m = p.search(gensku)
        suffix = m.group()
        op = re.compile(".*?(?=\D)")
        om = op.search(gensku)
        gensku = om.group()
        spec_tuple = (gensku,suffix)
        return spec_tuple
    else:
        suffix = None
        spec_tuple = (gensku,suffix)
        return spec_tuple

def find_both_processors(processor_string):
    """Splits our processor string into an Intel and AMD processor, then returns
    a tuple with two variables containing each respective processor.
    Params: Str -> Processor String
    """
    processors_pattern = re.compile("(Intel.*)(AMD.*)")
    processors_tuple = processors_pattern.search(processor_string).groups()
    return processors_tuple
    # if iX not in intel_processor, do something else - that means we're not dealing with an Intel Core processor which
    # is weird
    

def find_intel_core_chip_specs(intel_string):
    """Returns a dictionary containing the specs of any Intel Core chip.
    Params: Str -> Intel Processor String
"""
    brand_modifier_match_object = re.search("i\d",intel_string)
    gensku = re.search(".*?(?=\s|\D)",intel_string[(brand_modifier_match_object.span()[1]+1):]).group()
    brand_modifier = brand_modifier_match_object.group()
    suffix_tuple = find_suffix(gensku)
    gensku,suffix = suffix_tuple
    if int(gensku[:2])>13:
        generation = int(gensku[0])
        sku_nums = int(gensku[1:])
    else:
        generation = int(gensku[:2])
        sku_nums = int(gensku[3:])
    return {'Company': 'Intel', 'Brand Modifier': brand_modifier, 'Generation': generation, 'SKU': sku_nums, 'Suffix': suffix }


def find_older_specs(processor_string):
    """"Returns a dictionary containing the processor's clock speed and core count.
    Params Str -> Processor String
    """
    # These processors normally only specify clock speed and core count, so that's what we'll check for below.
    clock_speed_pattern = re.compile("(\d.\d)")
    clock_speed = float(clock_speed_pattern.search(processor_string).group())

    core_count_pattern = re.compile("\w+(?=((\s[cC]ore)|((\W[cC]ore))))")
    core_count = core_count_pattern.search(processor_string).group().lower()
    core_dictionary = {'dual':2,'single':1,'quad':4}
    core_count = core_dictionary[core_count]

    return{'Clock Speed':clock_speed,'Core Count':core_count}

def find_clock_speed_plus_core_count(processor_specs_dictionary):
    """Takes a user's processor specs dictionary and sends their specs via
    a GET request to techpower.com where we parse through the response
    and pull the user's processor's clock speed and core count.
    Params: Processor_Specs_Dictionary -> Dictionary"""

    print("User's processor specs:")
    for value in processor_specs_dictionary.values():
        print(value)

    link = f"https://www.techpowerup.com/cpu-specs/?ajaxsrch=Core%20{processor_specs_dictionary['Brand Modifier']}-{processor_specs_dictionary['Generation']}{processor_specs_dictionary['SKU']}{processor_specs_dictionary['Suffix']}"

    r = requests.get(link)
    soup = bs4.BeautifulSoup(r.text,'lxml')
    print(soup.find_all('td'))
    for tag in soup.find_all('td'):
        """This for-loop parses through techpowerup.com's HTML and utilizes BeautifulSoup
        to yank the clock speed and core count of the user's processor."""
        new_tag = str(tag.contents).split()
        for index,element in enumerate(new_tag):
            new_tag[index] = element.strip("'[]")
            if new_tag[index] == '/':
                core_count = int(new_tag[index-1])
            elif new_tag[index] == 'to':
                clock_speed = float(new_tag[index-1])

    return {'Clock Speed':clock_speed,'Core Count':core_count}

def find_older_specs_for_lightweight_game(processor_string):
    """"Returns a dictionary containing the processor's clock speed and core count.Functions
    very similar to find_older_specs() except that we first need to split up the 
    Processor String"""
    processor_string = find_both_processors(processor_string)[0]
    clock_speed_pattern = re.compile("(\d.\d)")
    clock_speed = float(clock_speed_pattern.search(processor_string).group())

    core_count_pattern = re.compile("\w+(?=((\s[cC]ore)|((\W[cC]ore))))")
    core_count = core_count_pattern.search(processor_string).group().lower()
    core_dictionary = {'dual':2,'single':1,'quad':4}
    core_count = core_dictionary[core_count]

    return{'Clock Speed':clock_speed,'Core Count':core_count}

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

def return_game_specs(library, game):
    print(f"Parameter game is {game}")
    """Returns the System Requirements - Minimum: data in the form of a user-friendly dictionary whose
    k-v pairs mimic exactly what is seen on Steam.
    Params: Dict -> All-games dictionary
            Str -> Game name"""
    for item in library.items():
        """"Loops through our giant dictionary containing {appid:gamename} searching for a string game name
        that matches the parameter game that went into the function."""
        try:
            if game == item[1]:
                print("Game found: {game}")
                app_id = item[0]
                break
        except KeyError:
                continue
    # Game not found
    if game != item[1]:
        return -1
    """Below we make another call to the Steam API at a different endpoint. We need
    to put our newfound appid as a parameter to this URL's query so the Steam API
    knows for which game to fetch us JSON data."""
    lnk = f'https://store.steampowered.com/api/appdetails/?appids={app_id}'
    rr = requests.get(lnk).text
    print("Request sucess")
    data = json.loads(rr)
    print("JSON deserialized...")
    #"pc_requirements" is the key we want
    """We are using BeautifulSoup below to parse through the HTML and get at the 
    System Requirements - Minimum: data that's displayed for every Steam game on their storepage."""
    min_specs = data[str(app_id)]['data']['pc_requirements']['minimum']
    print("1")
    min_soup = bs4.BeautifulSoup(str(min_specs),'lxml')
    print("2")
    min_soup_tags = min_soup.find_all('li')
    print(min_soup_tags)
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
    if 'Storage' not in min_reqs.keys():
        # Some older games have 'Storage' data under 'Hard Disk Space' instead. 
        min_reqs['Storage'] = min_reqs['Hard Disk Space']
    print(f"Min reqs: f{min_reqs}")
    for key in min_reqs.keys():
        print(key)
    return min_reqs

def return_older_game_processor_specs(processor_string):
    """SCENARIO 1: *OLDER GAME* If any of our core_dictionary keys are found within the processor string and Intel is not found
    within, we can assume that we're dealing with an older, single processor. Sometimes a newish, lightweight game
    will follow normal Processor String naming schematic but will use older processors that
    still might have a core_dictionary key in the title. We will trigger a different scenario for that.
    Returns a dictionary of the processor's specifications.
    Params Str -> Processor String"""
    processor_specs_dictionary = find_older_specs(processor_string)
    return processor_specs_dictionary


def return_lightweight_game_processor_specs(processor_string):
    """SCENARIO 2: *LIGHTWEIGHT GAME* If any of our core_dictionary keys are found in a Processor String but that Processor
    String also includes Intel. This means that we are dealing with a lightweight game that is following
    normal Processor String schematic but only requires the use of older CPUs. We will also check if Intel is alone or not.
    Returns a dictionary of the processor's specifications.
    Params Str -> Processor String"""
    processor_specs_dictionary = find_older_specs_for_lightweight_game(processor_string)
    return processor_specs_dictionary

def return_standard_game_processor_specs(processor_string):
    """SCENARIO 3: *STANDARD GAME* If 'Intel' is the first string in our Processor String, then we can operate under the assumption
    that the game's publishers have followed the normal listing of "Intel Processor...[separator character]...AMD Processor"
    (e.g., NieR Automata - Intel Core i3 2100 or AMD A8-6500). We will also check to make sure that none
    of our core keys are in this Processor String so that we know that we're not dealing 
    with SCENARIO 2 (a lightweight game).
    Returns a dictionary of the processor's specifications.
    Params Str -> Processor String"""
    intel_processor = find_both_processors(processor_string)[0]
    processor_specs_dictionary = find_intel_core_chip_specs(intel_processor)
    return processor_specs_dictionary

def return_processor_specs(processor_string):
    """Assesses which specification publishing schematic we are dealing with and calls the appropriate
    function to deal with said naming schematic. Returns a dictionary of the processor's specifications.
    Returns a dictionary of the processor's specifications.
    Params Str -> Processor String"""
    if re.search('(dual)|(quad)|(single)', processor_string.lower()) and not re.search('Intel',processor_string):
        # SCENARIO 1 - OLDER GAME
        processor_specs_dictionary = return_older_game_processor_specs(processor_string)
        return processor_specs_dictionary
    if re.search('(dual)|(quad)|(single)', processor_string.lower()) and re.search('Intel',processor_string):
        # SCENARIO 2 - LIGHTWEIGHT GAME
        processor_specs_dictionary = return_lightweight_game_processor_specs(processor_string)
        return processor_specs_dictionary
    if re.match("Intel", processor_string) and not re.search("(dual)|(quad)|(single)",processor_string.lower()):
        # SCENARIO 3 - STANDARD GAME
        processor_specs_dictionary = return_standard_game_processor_specs(processor_string)
        return processor_specs_dictionary
"""
game = {'OS': 'Windows 10 (64-bit versions only)', 'Processor': 'Intel Core i3-4150 | AMD FX-4300 or equivalent', 'Memory': '4 GB RAM', 'Graphics': 'NVIDIA GeForce GTX950 / GTX1050 with 2 GB VRAM | AMD Radeon R9 270 / R9 370 / RX460 with 2 GB VRAM', 'DirectX': 'Version 9.0c', 'Network': 'Broadband Internet connection', 'Storage': '90 GB available space', 'Sound Card': 'DirectX 9.0c compatible sound card', 'Additional Notes': 'Mouse and Keyboard supported. Game contains EasyAntiCheat anti-cheat technology and Denuvo anti-tamper technology.'}
user = {'OS': "Windows 7 Premium", 'Memory': '11 GB RAM', 'Storage': '50 GB available', 'DirectX': 'Version 6 or later'}
"""
def compare_specs(user_spec_dictionary,game_spec_dictionary):
    """Takes in a dictionary of the user's specs and the requeseted game's specs. Returns a result dictionary
    whose values are a success and fail dictionary showing where the user succeeded or failed a check.
    Params Dict -> User Specs Dictionary
    Dict -> Game Specs Dictionary"""

    # If game_spec_dictionary is -1, then we couldn't find the game
    if game_spec_dictionary == -1:
        return -1
    print(f"Game spec dictionary is: {game_spec_dictionary}")
    result_dict = {}
    fail_dict = {}
    success_dict = {}

    # Each block of code within this function parses an individual spec for its integer value. Their
    # corresponding if statements make comparisions between the user's and the game's integer value; if the
    # game's value is greater than the user's, the fail_dict is updated with a key of the corresponding
    # spec and a value of a dictionary whose keys are 'User' or 'Game' and whose values
    # are the entire string of the spec in question (as opposed to just their integer value).
    os_pattern = re.compile("7|8|10|11")
    user_os = os_pattern.search(user_spec_dictionary['OS'])
    user_os = int(user_os.group())
    try:
        game_os = os_pattern.search(game_spec_dictionary['OS *'])
    except:
        game_os = os_pattern.search(game_spec_dictionary['OS'])
    game_os = int(game_os.group())
    if user_os >= game_os:
        try:
            success_dict['OS']={'User': user_spec_dictionary['OS'], 'Game': game_spec_dictionary['OS *']}
        except:
            success_dict['OS']={'User': user_spec_dictionary['OS'], 'Game': game_spec_dictionary['OS']}
    else:
        try:
            fail_dict['OS']={'User': user_spec_dictionary['OS'], 'Game': game_spec_dictionary['OS *']}
        except:
            fail_dict['OS']={'User': user_spec_dictionary['OS'], 'Game': game_spec_dictionary['OS']}


    
    user_memory = int(re.sub('\D','', user_spec_dictionary['Memory']))
    game_memory = int(re.sub('\D','', game_spec_dictionary['Memory']))
    if user_memory >= game_memory:
        success_dict['Memory']={'User': user_spec_dictionary['Memory'], 'Game': game_spec_dictionary['Memory']}
    else:
        fail_dict['Memory']={'User': user_spec_dictionary['Memory'], 'Game': game_spec_dictionary['Memory']}

    user_storage = int(re.sub('\D','', user_spec_dictionary['Storage']))
    game_storage = int(re.sub('\D','', game_spec_dictionary['Storage']))
    if user_storage >= game_storage:
        success_dict['Storage']={'User': user_spec_dictionary['Storage'], 'Game': game_spec_dictionary['Storage']}

        
    else:
        fail_dict['Storage']={'User': user_spec_dictionary['Storage'], 'Game': game_spec_dictionary['Storage']}

    user_directx = int(re.sub('\D','', user_spec_dictionary['DirectX']))
    try:
        # Some games choose not to provide a DirectX spec. If that's the case,
        # we're going to auto-pass the user here by setting game_directx = 0.
        game_directx = game_spec_dictionary['DirectX'].split('.')
        # Sometimes games give their DirectX in terms of floats, so we need to account
        # for that by attempting to split their string on the "."
        game_directx = int(re.sub('\D','', game_directx[0]))
    except KeyError:
        game_directx = 0

    if game_directx == 0:
        success_dict['DirectX']={'User': user_spec_dictionary['DirectX'], 'Game': 'not given'}

    elif user_directx >= game_directx:
        success_dict['DirectX']={'User': user_spec_dictionary['DirectX'], 'Game': game_spec_dictionary['DirectX']}

    else:
        fail_dict['DirectX']={'User': user_spec_dictionary['DirectX'], 'Game': game_spec_dictionary['DirectX']}

    result_dict = {'Fail': fail_dict, 'Success': success_dict}
    print("Executed succesfully")
    return result_dict
    # Now we want to return a result dictionary that has both a success and fail dictionary as values (changed
    # from returning just a fail dictionray)

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

def pull_game_image(library, app_id):
    game_name = library[app_id]
    """Edits URI housing Steam static files by inputting our game's app id after the /apps route
    within the Steam cloudflare URI. This function then utilizes the requests module
    to pull a bytes response from the server. This bytes response is then written to a .jpg file
    whose naming schematic will always follow GameName.jpg.
    Returns a .jpg image.
    Params: Dict -> All-games dictionary
            Int -> App ID
    """
    with open(game_name + '.jpg', 'wb') as my_file:
        r = requests.get(f'https://cdn.cloudflare.steamstatic.com/steam/apps/{app_id}/header.jpg?t=1669076148')
        my_file.write(r.content)

    return None

def compare_processor_specs(find_clock_speed_plus_core_count,user_processor_spec_dictionary,game_processor_spec_dictionary):
    """Takes in a dictionary of the user's processor's specs and the requeseted game's processor's specs. Returns a result dictionary
    whose values are a success and fail dictionary showing where the user succeeded or failed a check.
    Params Dict -> User Processor Specs Dictionary
    Dict -> Game Processor Specs Dictionary
    Func -> Find_Clock_Speed_Plus_Core_Count"""
    fail_dict = {}
    info_dict = {}
    # The specs in the CPU are hierarchial, meaning that a child spec of a user's processor can be greater
    # than a child spec of a game's required processor, but if the parent spec of the game's processor trumps
    # the parent spec of the user's processor, then the user's superior child spec will be ignored. This
    # is a complex scenario because although said child spec may be relationally superior to another child
    # spec, its ultimate success or failure will always be primarily determined by that of its parent spec.
    # For this reason, I am deeming these child successes/failures "conditional" successes/failures, which will
    # be stored in the info_dict dictionary.
    success_dict = {}
    result_dict = {}
    if len(game_processor_spec_dictionary.keys()) < 3:
        # Check here if we are dealing with an older or lightweight game
        # For now, just assume that user passes here, but in future we need to find clock speed and core count
        # for the user's processor
        new_user_processor_spec_dictionary = find_clock_speed_plus_core_count(user_processor_spec_dictionary)
        # New because we no longer care about their processor's hardcore specs per se,
        # we want to dig deeper and look at its core count + clock speed
        if new_user_processor_spec_dictionary['Clock Speed'] >= game_processor_spec_dictionary['Clock Speed'] and new_user_processor_spec_dictionary['Core Count'] >= game_processor_spec_dictionary['Core Count']:
            result_dict[1] = {'User': {'Clock Speed': new_user_processor_spec_dictionary['Clock Speed'], 'Core Count': new_user_processor_spec_dictionary['Core Count']}, 'Game': {'Clock Speed': game_processor_spec_dictionary['Clock Speed'],'Core Count': game_processor_spec_dictionary['Core Count']}}
            return result_dict
        else:
            # Not neccesarily a complete failure...
            result_dict[0] = {'User': {'Clock Speed': new_user_processor_spec_dictionary['Clock Speed'], 'Core Count': new_user_processor_spec_dictionary['Core Count']}, 'Game': {'Clock Speed': game_processor_spec_dictionary['Clock Speed'], 'Core Count': game_processor_spec_dictionary['Core Count']}}
            return result_dict

    # Right now my program only knows how to work with Intel Core processors. We're just going to compare Brand
    # Modifier, Generation, and SKU. One and done.
    if int(re.search("\d", user_processor_spec_dictionary['Brand Modifier']).group()) > int(re.search("\d", game_processor_spec_dictionary['Brand Modifier']).group()):
        success_dict['Brand Modifier']={'User': user_processor_spec_dictionary['Brand Modifier'], 'Game': game_processor_spec_dictionary['Brand Modifier']}
        info_dict['Generation']={'User': user_processor_spec_dictionary['Generation'], 'Game': game_processor_spec_dictionary['Generation']}
        info_dict['SKU']={'User': user_processor_spec_dictionary['SKU'], 'Game': game_processor_spec_dictionary['SKU']}
        result_dict = {'Fail': fail_dict, 'Success': success_dict, 'Info': info_dict}
        return result_dict

    elif int(re.search("\d", user_processor_spec_dictionary['Brand Modifier']).group()) == int(re.search("\d", game_processor_spec_dictionary['Brand Modifier']).group()):
        success_dict['Brand Modifier']={'User': user_processor_spec_dictionary['Brand Modifier'], 'Game': game_processor_spec_dictionary['Brand Modifier']}
        #
    else:
        fail_dict['Brand Modifier']={'User': user_processor_spec_dictionary['Brand Modifier'], 'Game': game_processor_spec_dictionary['Brand Modifier']}
        info_dict['Generation']={'User': user_processor_spec_dictionary['Generation'], 'Game': game_processor_spec_dictionary['Generation']}
        info_dict['SKU']={'User': user_processor_spec_dictionary['SKU'], 'Game': game_processor_spec_dictionary['SKU']}
        result_dict = {'Fail': fail_dict, 'Success': success_dict, 'Info': info_dict}
        return result_dict


    if int(user_processor_spec_dictionary['Generation']) > game_processor_spec_dictionary['Generation']:
        success_dict['Generation']={'User': user_processor_spec_dictionary['Generation'], 'Game': game_processor_spec_dictionary['Generation']}
        info_dict['SKU']={'User': user_processor_spec_dictionary['SKU'], 'Game': game_processor_spec_dictionary['SKU']}
        result_dict = {'Fail': fail_dict, 'Success': success_dict, 'Info': info_dict}
        return result_dict

    elif int(user_processor_spec_dictionary['Generation']) == game_processor_spec_dictionary['Generation']:
        success_dict['Generation']={'User': user_processor_spec_dictionary['Generation'], 'Game': game_processor_spec_dictionary['Generation']}

    else:
        fail_dict['Generation']={'User': user_processor_spec_dictionary['Generation'], 'Game': game_processor_spec_dictionary['Generation']}
        info_dict['SKU']={'User': user_processor_spec_dictionary['SKU'], 'Game': game_processor_spec_dictionary['SKU']}
        result_dict = {'Fail': fail_dict, 'Success': success_dict, 'Info': info_dict}
        return result_dict


    if int(user_processor_spec_dictionary['SKU']) >= game_processor_spec_dictionary['SKU']:
        success_dict['SKU']={'User': user_processor_spec_dictionary['SKU'], 'Game': game_processor_spec_dictionary['SKU']}
        result_dict = {'Fail': fail_dict, 'Success': success_dict, 'Info': info_dict}
        return result_dict

    else:
        fail_dict['SKU']={'User': user_processor_spec_dictionary['SKU'], 'Game': game_processor_spec_dictionary['SKU']}
        result_dict = {'Fail': fail_dict, 'Success': success_dict, 'Info': info_dict}
        return result_dict


