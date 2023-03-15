<!--User data will be POSTed, game data will be imported via a POSTed game name variable-->
% import utils
% library = utils.create_dictionary_library()
% game_specs = utils.return_game_specs(library, user_game) # MAKE SURE game IS POSTed
% processor_string = game_specs['Processor']
% game_processor_specs = utils.return_processor_specs(processor_string)
% print(game_processor_specs)
<!--Retrieve the specs for the game processor within the HTML by accessing keys of our Python variable
game_processor_specs-->
<ul>
        <li><b>Brand - </b>User:{{user_brand}} Game: Core</li>
        <li><b>Brand Modifier - </b>User:{{user_brand_modifier}} Game: {{game_processor_specs['Brand Modifier']}}</li>
        <li><b>Generation - </b>User:{{user_generation}} Game: {{game_processor_specs['Generation']}}</li>
        <li><b>SKU - </b>User:{{user_sku_nums}} Game:{{game_processor_specs['SKU']}}</li>
        <li><b>Suffix - </b>User:{{user_suffix}} Game: {{game_processor_specs['Suffix']}}</li>
</ul>
<br>
<br>


