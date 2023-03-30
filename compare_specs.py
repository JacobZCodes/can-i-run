fail_count = 0
"""COMPARE OS """
split_os = {{os}}.split('Windows')
other_split_os = min_reqs['OS'].split('Windows')
split_os[1] = split_os[1].strip()
other_split_os[1] = other_split_os[1].strip()
version_windows = int(split_os[1].split(" ")[0])
other_version_windows = int(other_split_os[1].split(" ")[0])
if version_windows >= other_version_windows:
    pass
else:
    fail_count += 1

"""COMPARE PROCESSOR"""
# '11th Gen Intel(R) Core(TM) i5-1135G7 @ 2.40GHz'
# 'Intel Core i5-6600K / AMD Ryzen 5 1600'

# For older games, the minimum requirement's processor name will not have the normal
# Intel namign schematic of "i5-1135G7"; it will instead have something loke
# "3.0 GHz dual core or better". You need to update the below split code
# so that it catches these cases.
my_shit = {{processor}}.split('i')[1].split(" ")[0].split('-')
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
                counter = True
                break

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
    other_gen_num = int(other_gen_and_sku[0][:2])
elif int(other_gen_and_sku[0][:2]) > 13:
    other_gen_num = int(other_gen_and_sku[0][0])

if brand_modifier >= other_brand_modifier and gen_num >= other_gen_num:
    pass
else:
    fail_count += 1




"""COMPARE RAM"""
other_ram= int(min_reqs['Memory'].split(" ")[0])
if {{memory}} >= other_ram:
    pass
else:
    fail_count += 1

"""COMPARE GRAPHICS"""
# We need to catch for if minimum requirements throws us one or two processors. We'll start 
# just catching for one processor

# Compare rank
other_num_after_gtx = min_reqs['Graphics'].split('GTX')[1].strip().split()[0]
other_look_me_up = 'GTX' + " " + other_num_after_gtx
my_brand = {{graphics}}.split()
for position, element in enumerate(my_brand):
    my_brand[position] = element.strip('(R)')
my_brand = my_brand[1] + ' ' + my_brand[2]


with open('GPU_UserBenchmarks.csv') as my_csv:
    my_csv_object = csv.DictReader(my_csv)
    for dictionary in my_csv_object:
        if other_look_me_up in dictionary['Model']:
            other_rank = dictionary['Rank']
            other_benchmark = dictionary['Benchmark']
            break
    for dictionary in my_csv_object:
        if my_brand in dictionary['Model']:
            my_rank = dictionary['Rank']
            my_benchmark = dictionary['Benchmark']
            break

if my_rank <= other_rank and my_benchmark >= other_benchmark:
    pass
else:
    fail_count += 1




"""COMPARE DIRECTX"""
min_reqs['DirectX'] = int(min_reqs['DirectX'].split(" ")[1])
if {{directx}} >= min_reqs['DirectX']:
    pass
else:
    fail_count += 1

# Compare Storage
min_reqs['Storage'] = int(min_reqs['Storage'].split()[0])
if {{storage}} >= min_reqs['Storage']:
    pass
else:
    fail_count += 1

