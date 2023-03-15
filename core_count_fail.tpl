<!DOCTYPE html>
<html>
% try:
    % user_core_count= processor_specs_result_dict[1]['User']['Core Count']
    % game_core_count = processor_specs_result_dict[1]['Game']['Core Count']
% except:
    % user_core_count = processor_specs_result_dict[0]['User']['Core Count']
    % game_core_count = processor_specs_result_dict[0]['Game']['Core Count']
% end
    <head>
        <meta charset="utf-8">
        <title>CanIRun!</title>
        <link href="/static/C:/Users/Jacob/Desktop/CanIRun_FrontEnd/core_count_fail_style.css" type="text/css" rel="stylesheet">
    </head>
    <body>
        <h1>CORE COUNT - FAIL!</h1>
        <h2>
            Your CPU also contains something called cores. These cores are constituent parts of the CPU that
            function as sort of mini-CPUs within the overarching main CPU. Within similar CPUs, more cores
            usually equates to more processing power.

            You cannot run this game since your CPU only has <span>{{user_core_count}}
            cores</span>, while <span class="game">{{game}}</span> calls for <span>{{game_core_count}} cores.</span>
        </h2>
    </body>
</html>



