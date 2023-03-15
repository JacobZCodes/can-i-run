import csv
import requests
import bs4
from utils import compare_processor_specs, return_processor_specs





def find_clock_speed_plus_core_count(processor_specs_dictionary):
    """Takes a user's processor specs dictionary and sends their specs via
    a GET request to techpower.com where we parse through the response
    and pull the user's processor's clock speed and core count.
    Params: Processor_Specs_Dictionary -> Dictionary"""

    link = f"https://www.techpowerup.com/cpu-specs/?ajaxsrch=Core%20{processor_specs_dictionary['Brand Modifier']}-{processor_specs_dictionary['Generation']}{processor_specs_dictionary['SKU']}{processor_specs_dictionary['Suffix']}"

    r = requests.get(link)
    soup = bs4.BeautifulSoup(r.text,'lxml')
    for tag in soup.find_all('td'):
        """This for-loop parses through techpowerup.com's HTML and utilizes BeautifulSoup
        to yank the clock speed and core count of the user's processor."""
        new_tag = str(tag.contents).split()
        for index,element in enumerate(new_tag):
            new_tag[index] = element.strip("'[]")
            if new_tag[index] == '/':
                core_count = new_tag[index-1]
            elif new_tag[index] == 'to':
                clock_speed = new_tag[index-1]

    return {'Clock Speed':clock_speed,'Core Count':core_count}
    


        