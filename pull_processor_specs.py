import re
import utils
"""The code in the file is used to pull the specs for the minimum required processor(s) for any game
on Steam. Processor String refers to "System Requirements - Minimum - Processor: " on the store
page for every Steam game. This data is pulled with a call to the Steam API."""


def return_older_game_processor_specs(processor_string):
    """SCENARIO 1: *OLDER GAME* If any of our core_dictionary keys are found within the processor string and Intel is not found
    within, we can assume that we're dealing with an older, single processor. Sometimes a newish, lightweight game
    will follow normal Processor String naming schematic but will use older processors that
    still might have a core_dictionary key in the title. We will trigger a different scenario for that.
    Returns a dictionary of the processor's specifications.
    Params Str -> Processor String"""
    processor_specs_dictionary = utils.find_older_specs(processor_string)
    return processor_specs_dictionary


def return_lightweight_game_processor_specs(processor_string):
    """SCENARIO 2: *LIGHTWEIGHT GAME* If any of our core_dictionary keys are found in a Processor String but that Processor
    String also includes Intel. This means that we are dealing with a lightweight game that is following
    normal Processor String schematic but only requires the use of older CPUs. We will also check if Intel is alone or not.
    Returns a dictionary of the processor's specifications.
    Params Str -> Processor String"""
    processor_specs_dictionary = utils.find_older_specs_for_lightweight_game(processor_string)
    return processor_specs_dictionary

def return_standard_game_processor_specs(processor_string):
    """SCENARIO 3: *STANDARD GAME* If 'Intel' is the first string in our Processor String, then we can operate under the assumption
    that the game's publishers have followed the normal listing of "Intel Processor...[separator character]...AMD Processor"
    (e.g., NieR Automata - Intel Core i3 2100 or AMD A8-6500). We will also check to make sure that none
    of our core keys are in this Processor String so that we know that we're not dealing 
    with SCENARIO 2 (a lightweight game).
    Returns a dictionary of the processor's specifications.
    Params Str -> Processor String"""
    intel_processor = utils.find_both_processors(processor_string)[0]
    processor_specs_dictionary = utils.find_intel_core_chip_specs(intel_processor)
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


