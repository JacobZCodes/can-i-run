import requests
from utils import find_app_id, create_dictionary_library
"""For the final route on CanIRun!, the background changes to an image of the user's inputted game.
This code serves to dynamically produce that background."""
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

# if __name__ == "__main__":
#     print(find_app_id(create_dictionary_library(),'Dishonored'))

pull_game_image(create_dictionary_library(), 236430)

