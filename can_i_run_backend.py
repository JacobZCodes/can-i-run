import cpuinfo
import csv
import requests
import sys
import json
from bs4 import BeautifulSoup
import psutil
import platform
from dxdiag import my_specs
fail_counter = 0
my_directx = my_specs['DirectX']
my_graphics = my_specs['Graphics']

app_ids = 'https://api.steampowered.com/ISteamApps/GetAppList/v2/'

bit_architecture, linkage_format = platform.architecture()
my_os = my_specs['OS']

# look into dxdiag
# look into bit archiectecutre + linkage_format 
# print(platform.processor())
my_processor = cpuinfo.get_cpu_info()['brand_raw']


r = requests.get(app_ids).text
data = json.loads(r)
dic_list = data['applist']['apps']
counter = 0
# This block of code creates a dictionary containing the entire Steam library game collection
# Keys are app id and values are the name of the game

all_games_dic = {}
for dic in dic_list:
    ap_id = dic.pop('appid')
    name = dic.pop('name')
    if name == '':
        continue
    dic[ap_id] = name
    all_games_dic.update(dic)
# END CODE BLOCK 

# Check if user input matches name key within Steam's GetAppList
game_name = input('Enter the name of the game you are trying to find the specs for: ')
for item in all_games_dic.items():
    try:
        if game_name == item[1]:
            app_id = item[0]
            break
    except KeyError:
            continue

ai = app_id

lnk = f'https://store.steampowered.com/api/appdetails/?appids={ai}'

#"pc_requirements" is the key we want
rr = requests.get(lnk).text
data = json.loads(rr)

# 
# Missing OS!!
min_specs = data[str(ai)]['data']['pc_requirements']['minimum']
min_soup = BeautifulSoup(str(min_specs),'lxml')
min_soup_tags = min_soup.find_all('li')
try:
    rec_specs = data[str(ai)]['data']['pc_requirements']['recommended']
    rec_soup = BeautifulSoup(str(rec_specs),'lxml')
    rec_soup_tags = rec_soup.find_all('li')
except:
    pass

# min_soup_tags[0].contents = min_soup_tags[0].contents.insert(0,"<strong>Minimum:<\/strong>")
print('Minimum Requiremnets')
min_reqs = {}
for tag in min_soup_tags[1:]:
    spec = tag.contents[0].text + tag.contents[1].text
    split_spec = spec.split(':')
    min_reqs[split_spec[0].strip()] = split_spec[1].strip()
for spec in min_reqs:
    print(spec)
    pass

rec_specs = []
try: 
    for tag in rec_soup_tags[1:]:
        spec = tag.contents[0].text + tag.contents[1].text
        rec_specs.append(spec)
        
except:
    #print('Could not find recommended requirements for this game')
    pass


for spec in rec_specs:
    print(spec)
    pass

print()
# Memory 
def bytes_to_gigabytes(num):
    return round(num / 1000000000,2)
my_memory = bytes_to_gigabytes(psutil.virtual_memory()[0])

# Memory


def mhz_to_ghz(num):
    return str(round(num/1000,2)) + "GHz"


my_free_storage = bytes_to_gigabytes(psutil.disk_usage('/')[2]) 


# print(f"MY SHIT CUH\n{my_os}\n{my_processor}\n{my_memory}\n{my_graphics}\n{my_directx}\n{my_free_storage}")
personal_specs = {'OS':my_os,'Processor':my_processor,'Memory':my_memory,'Graphics':my_graphics,'DirectX':my_directx,'Storage':my_free_storage}


"""COMPARE OS """
# split_os = personal_specs['OS'].split('Windows')
# other_split_os = min_reqs['OS'].split('Windows')
# split_os[1] = split_os[1].strip()
# other_split_os[1] = other_split_os[1].strip()
# version_windows = int(split_os[1].split(" ")[0])
# other_version_windows = int(other_split_os[1].split(" ")[0])
# if version_windows >= other_version_windows:
#     print('OS passed check...')
# else:
#     print('OS failed check...')

"""COMPARE PROCESSOR"""
# '11th Gen Intel(R) Core(TM) i5-1135G7 @ 2.40GHz'
# 'Intel Core i5-6600K / AMD Ryzen 5 1600'

# For older games, the minimum requirement's processor name will not have the normal
# Intel namign schematic of "i5-1135G7"; it will instead have something loke
# "3.0 GHz dual core or better". You need to update the below split code
# so that it catches these cases.
my_shit = personal_specs['Processor'].split('i')[1].split(" ")[0].split('-')
brand_modifier = int(my_shit[0])
other_shit = min_reqs['Processor'].split('i')[1].split(" ")[0].split('-')
other_brand_modifier = int(other_shit[0])
# Now we need the generation number
counter = False
for char in my_shit[1]:
    if counter == True:
        break
    for num in range(10):
        try:
            if int(char) == num:
                pass
        except ValueError:
                gen_and_sku = my_shit[1].split(char)
                print(gen_and_sku)
                counter = True
                break

# print('There')
other_counter = False
for char in other_shit[1]:
    if other_counter == True:
        break
    for num in range(10):
        try:
            if int(char) == num:
                pass
        except ValueError:
                other_gen_and_sku = other_shit[1].split(char)
                other_counter = True
                break
        if char == other_shit[1][-1] and num == 9:
            other_gen_and_sku = []
            other_gen_and_sku.append(other_shit[1])

if int(gen_and_sku[0][:2]) <= 13:
    gen_num = int(gen_and_sku[0][:2])
elif int(gen_and_sku[0][:2]) > 13:
    gen_num = int(gen_and_sku[0][0])



if int(other_gen_and_sku[0][:2]) <= 13:
    print('Executing...')
    other_gen_num = int(other_gen_and_sku[0][:2])
elif int(other_gen_and_sku[0][:2]) > 13:
    print('Also executing...')
    other_gen_num = int(other_gen_and_sku[0][0])

if brand_modifier >= other_brand_modifier and gen_num >= other_gen_num:
    print('Processor passed check...')
else:
    print('Processor failed check...')

# print(brand_modifier, gen_num)
# print(other_brand_modifier,other_gen_num)



"""COMPARE RAM"""
other_ram= int(min_reqs['Memory'].split(" ")[0])
if personal_specs['Memory'] >= other_ram:
    print('RAM passed check...')
else:
    print('RAM failed check...')

"""COMPARE GRAPHICS"""
# We need to catch for if minimum requirements throws us one or two processors. We'll start 
# just catching for one processor

# Compare rank
other_num_after_gtx = min_reqs['Graphics'].split('GTX')[1].strip().split()[0]
other_look_me_up = 'GTX' + " " + other_num_after_gtx
print(other_look_me_up)
my_brand = personal_specs['Graphics'].split()
for position, element in enumerate(my_brand):
    my_brand[position] = element.strip('(R)')
my_brand = my_brand[1] + ' ' + my_brand[2]


with open('GPU_UserBenchmarks.csv') as my_csv:
    my_csv_object = csv.DictReader(my_csv)
    for dictionary in my_csv_object:
        if other_look_me_up in dictionary['Model']:
            other_rank = dictionary['Rank']
            other_benchmark = dictionary['Benchmark']
            print(other_rank,other_benchmark)
            break
    for dictionary in my_csv_object:
        if my_brand in dictionary['Model']:
            my_rank = dictionary['Rank']
            my_benchmark = dictionary['Benchmark']
            print(my_rank,my_benchmark)
            break

if my_rank <= other_rank and my_benchmark >= other_benchmark:
    print('Graphics passed check...')
else:
    print('Graphics failed check...')



print(personal_specs['Graphics'])

"""COMPARE DIRECTX"""
min_reqs['DirectX'] = int(min_reqs['DirectX'].split(" ")[1])
if personal_specs['DirectX'] >= min_reqs['DirectX']:
    print('DirectX passed check...')
else:
    print('DirectX failed check...')
# Compare Storage
min_reqs['Storage'] = int(min_reqs['Storage'].split()[0])
if personal_specs['Storage'] >= min_reqs['Storage']:
    print('Storage passed check...')
else:
    print('Storage failed check...')

