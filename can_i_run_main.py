from bottle import route, run, template, get, post, request, static_file, error, response, redirect, error, abort, Bottle
import os
import requests
import utils
# t
# https://damp-retreat-58247.herokuapp.com/
# ONLY WORKS WITH INTEL CORE - INTEL CORE CHIPS + DOES NOT SUPPORT GRAPHICS COMPARISON YET
# testing git diff
app = Bottle()
@app.route('/', method=['GET'])
def frontpage():
    return template('frontpage.tpl')    

@app.route('/processor', method=['POST'])
def processor():
    global specs_form_data
    specs_form_data = {}
    print("before for loop")
    for data in request.forms.items():
        print(f"Of type {type(request.forms.items())}")
        print("inside for loop")
        # This for loop allows us to take our POSTed data and put it into a global dictionary that we
        # can access anywhere in this program.
        specs_form_data[data[0]] = data[1]  
    return template('processor.tpl')

@app.route('/game', method=['POST'])
def game():
    global specs_form_data
    global processor_form_data
    processor_form_data = {}
    for data in request.forms.items():
        # This for loop allows us to take our POSTed data and put it into a global dictionary that we
        # can access anywhere in this program.
        processor_form_data[data[0]] = data[1]
    return template('game.tpl')

@app.route('/result', method=['POST'])
def result(utils_find_clock_speed_plus_core_count=utils.find_clock_speed_plus_core_count,utils_find_app_id=utils.find_app_id,utils_compare_processor_specs=utils.compare_processor_specs,utils_return_processor_specs=utils.return_processor_specs,utils_compare_specs=utils.compare_specs,utils_return_game_specs=utils.return_game_specs,utils_create_dictionary_library=utils.create_dictionary_library):
    # Two different possible routes here, depends on whether 
    # user can run game or not
    # debug this shit
    global specs_form_data
    global specs_result_dict
    global processor_specs_result_dict
    # game_id = utils_find_app_id(utils_create_dictionary_library(),request.forms.get('game'))
    # try:
    specs_result_dict = utils_compare_specs(specs_form_data,utils_return_game_specs(utils_create_dictionary_library(),request.forms.get('game')))
    # except:
    #     print("aborting!")
    #     abort(400)
    game_spec_dictionary = utils_return_game_specs(utils_create_dictionary_library(),request.forms.get('game'))
    processor_specs_result_dict = utils_compare_processor_specs(utils_find_clock_speed_plus_core_count,processor_form_data,utils_return_processor_specs(game_spec_dictionary['Processor']))
    global game
    if 0 in processor_specs_result_dict.keys() or 1 in processor_specs_result_dict.keys():
        # Checking if we're dealing with a prcessor from an older or lightweight game. If so,
        # we have to deal with it a bit differently.
        if 0 in processor_specs_result_dict.keys():
            # User cannot run game
            game = request.forms.get('game')
            return template("failure.tpl",game=game,specs_result_dict=specs_result_dict,processor_specs_result_dict=processor_specs_result_dict)

        elif 1 in processor_specs_result_dict.keys() and len(specs_result_dict['Fail']) == 0:
            # User can run game since both processor and general specs check out
            game = request.forms.get('game')
            return template("successful.tpl",game=game,specs_result_dict=specs_result_dict,processor_specs_result_dict=processor_specs_result_dict)

        elif 1 in processor_specs_result_dict.keys() and len(specs_result_dict['Fail']) != 0:
            # User cannot run game due to a general spec failing, but the user's processor
            # is superior
            game = request.forms.get('game')
            return template("failure.tpl",game=game,specs_result_dict=specs_result_dict,processor_specs_result_dict=processor_specs_result_dict)

    elif 0 not in processor_specs_result_dict.keys() and 1 not in processor_specs_result_dict.keys() and (len(specs_result_dict['Fail']) or len(processor_specs_result_dict['Fail'])):
        game = request.forms.get('game')
        return template("fail.tpl",game=game,specs_result_dict=specs_result_dict,processor_specs_result_dict=processor_specs_result_dict)
    
    else:
        game = request.forms.get('game')
        return template("success.tpl",game=game,specs_result_dict=specs_result_dict,processor_specs_result_dict=processor_specs_result_dict)


"""             SPECS EXPLANATION ROUTES             """
@app.route('/os', method=['POST'])
def os_explain():
    global specs_result_dict
    if 'OS' in specs_result_dict['Fail'].keys():
        return template("os_fail.tpl", specs_result_dict=specs_result_dict, game=game)
    else:
        return template("os_success.tpl", specs_result_dict=specs_result_dict, game=game)
@app.route('/memory', method=['POST'])
def memory_explain():
    global specs_result_dict
    if 'Memory' in specs_result_dict['Fail'].keys():
        return template("memory_fail.tpl", specs_result_dict=specs_result_dict, game=game)
    else:
        return template("memory_success.tpl", specs_result_dict=specs_result_dict, game=game)
@app.route('/directx', method=['POST'])
def directx_explain():
    global specs_result_dict
    if 'DirectX' in specs_result_dict['Fail'].keys():
        return template("directx_fail.tpl", specs_result_dict=specs_result_dict, game=game)
    else:
        return template("directx_success.tpl", specs_result_dict=specs_result_dict, game=game)
@app.route('/storage', method=['POST'])
def storage_explain():
    global specs_result_dict
    if 'Storage' in specs_result_dict['Fail'].keys():
        return template("storage_fail.tpl", specs_result_dict=specs_result_dict, game=game)
    else:
        return template("storage_success.tpl", specs_result_dict=specs_result_dict, game=game)

"""             PROCESSOR EXPLANATION ROUTES             """

@app.route('/brandmodifier', method=['POST'])
def brandmodifier_explain():
    global processor_specs_result_dict
    if 'Brand Modifier' in processor_specs_result_dict['Success'].keys():
        return template("brandmodifier_success.tpl", processor_specs_result_dict=processor_specs_result_dict, game=game)
    else:
        return template("brandmodifier_fail.tpl", processor_specs_result_dict=processor_specs_result_dict, game=game)

@app.route('/generation', method=['POST'])
def generation_explain():
    global processor_specs_result_dict
    if 'Brand Modifier' in processor_specs_result_dict['Success'].keys() and 'Generation' in processor_specs_result_dict['Fail'].keys():
        return template("generation_fail.tpl", processor_specs_result_dict=processor_specs_result_dict, game=game)
    if 'Brand Modifier' in processor_specs_result_dict['Success'].keys() and len(processor_specs_result_dict['Success'].keys()) == 1:
        return template("conditional_generation_success.tpl", processor_specs_result_dict=processor_specs_result_dict, game=game)
    elif 'Brand Modifier' not in processor_specs_result_dict['Success'].keys():
        return template("conditional_generation_fail.tpl", processor_specs_result_dict=processor_specs_result_dict, game=game)
    elif 'Generation' not in processor_specs_result_dict['Success'].keys():
        return template("generation_fail.tpl", processor_specs_result_dict=processor_specs_result_dict, game=game)
    elif 'Brand Modifier' in processor_specs_result_dict['Success'].keys() and 'Generation' in processor_specs_result_dict['Success'].keys():
        return template("generation_success.tpl", processor_specs_result_dict=processor_specs_result_dict, game=game)

@app.route('/sku', method=['POST'])
def sku_explain():
    global processor_specs_result_dict
    if 'Brand Modifier' in processor_specs_result_dict['Success'].keys() and 'Generation' in processor_specs_result_dict['Success'].keys() and 'SKU' in processor_specs_result_dict['Success'].keys():
        return template("sku_success.tpl", processor_specs_result_dict=processor_specs_result_dict, game=game)

    elif 'Brand Modifier' in processor_specs_result_dict['Success'].keys() and 'Generation' in processor_specs_result_dict['Info'].keys() and int(processor_specs_result_dict['Info']['Generation']['User']) >= processor_specs_result_dict['Info']['Generation']['Game']:
        return template("conditional_sku_success.tpl", processor_specs_result_dict=processor_specs_result_dict, game=game)

    elif 'Brand Modifier' in processor_specs_result_dict['Success'].keys() and 'Generation' in processor_specs_result_dict['Info'].keys() and int(processor_specs_result_dict['Info']['Generation']['User']) < processor_specs_result_dict['Info']['Generation']['Game']:
        return template("conditional_sku_fail.tpl", processor_specs_result_dict=processor_specs_result_dict, game=game)

    elif 'Brand Modifier' in processor_specs_result_dict['Success'].keys() and 'Generation' not in processor_specs_result_dict['Success'].keys():
        return template("conditional_sku_fail.tpl", processor_specs_result_dict=processor_specs_result_dict, game=game)
    
    elif 'Brand Modifier' in processor_specs_result_dict['Success'].keys() and len(processor_specs_result_dict['Success'].keys()) == 1:
        return template("conditional_sku_success.tpl", processor_specs_result_dict=processor_specs_result_dict, game=game)
    
    elif 'Brand Modifier' not in processor_specs_result_dict['Success'].keys():
        return template("conditional_sku_fail.tpl", processor_specs_result_dict=processor_specs_result_dict, game=game)
    
    elif 'Brand Modifier' in processor_specs_result_dict['Success'].keys() and 'Generation' in processor_specs_result_dict['Success'].keys() and len(processor_specs_result_dict['Success'].keys()) == 2:
        return template("conditional_sku_success.tpl", processor_specs_result_dict=processor_specs_result_dict, game=game)

@app.route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='./static')

@app.route('/corecount', method=['POST'])
def core_count():
    global processor_specs_result_dict
    # Since a key of 0 doesn't mean an all out failure, we need to check whether 
    # this specific spec succeeded or failed
    try:
        if int(processor_specs_result_dict[0]['User']['Core Count']) >= int(processor_specs_result_dict[0]['Game']['Core Count']):
            return template("core_count_success.tpl", game=game,specs_result_dict=specs_result_dict,processor_specs_result_dict=processor_specs_result_dict)
        elif processor_specs_result_dict[0]['User']['Core Count'] < processor_specs_result_dict[0]['Game']['Core Count']:
            return template("core_count_fail.tpl", game=game,specs_result_dict=specs_result_dict,processor_specs_result_dict=processor_specs_result_dict)
    except:
        if int(processor_specs_result_dict[1]['User']['Core Count']) >= int(processor_specs_result_dict[1]['Game']['Core Count']):
            return template("core_count_success.tpl", game=game,specs_result_dict=specs_result_dict,processor_specs_result_dict=processor_specs_result_dict)
        elif processor_specs_result_dict[1]['User']['Core Count'] < processor_specs_result_dict[1]['Game']['Core Count']:
            return template("core_count_fail.tpl", game=game,specs_result_dict=specs_result_dict,processor_specs_result_dict=processor_specs_result_dict)

@app.route('/clockspeed', method=['POST'])
def clock_speed():
    global processor_specs_result_dict
    # Since a key of 0 doesn't mean an all out failure, we need to check whether 
    # this specific spec succeeded or failed
    try:
        if float(processor_specs_result_dict[0]['User']['Clock Speed']) >= float(processor_specs_result_dict[0]['Game']['Clock Speed']):
            return template("clock_speed_success.tpl", game=game,specs_result_dict=specs_result_dict,processor_specs_result_dict=processor_specs_result_dict)
        elif float(processor_specs_result_dict[0]['User']['Clock Speed']) < float(processor_specs_result_dict[0]['Game']['Clock Speed']):
            return template("clock_speed_fail.tpl", game=game,specs_result_dict=specs_result_dict,processor_specs_result_dict=processor_specs_result_dict)
    except:
        if float(processor_specs_result_dict[1]['User']['Clock Speed']) >= float(processor_specs_result_dict[1]['Game']['Clock Speed']):
            return template("clock_speed_success.tpl", game=game,specs_result_dict=specs_result_dict,processor_specs_result_dict=processor_specs_result_dict)
        elif float(processor_specs_result_dict[1]['User']['Clock Speed']) < float(processor_specs_result_dict[1]['Game']['Clock Speed']):
            return template("clock_speed_fail.tpl", game=game,specs_result_dict=specs_result_dict,processor_specs_result_dict=processor_specs_result_dict)

"""             ERROR HANDLING             """
@app.error(500)
def error_500(error):
    return template("error500.tpl")

@app.error(400)
def error_400(error):
    return template("errorgamenotfound.tpl")
if os.environ.get('APP_LOCATION') == 'heroku':
    run(app,host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
if __name__ == "__main__":
    run(app,host='localhost', port=8080, debug=True)
