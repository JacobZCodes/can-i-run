<!DOCTYPE html>
<html>
% try:
    % user_clock_speed = processor_specs_result_dict[1]['User']['Clock Speed']
    % game_clock_speed = processor_specs_result_dict[1]['Game']['Clock Speed']
% except:
    % user_clock_speed = processor_specs_result_dict[0]['User']['Clock Speed']
    % game_clock_speed = processor_specs_result_dict[0]['Game']['Clock Speed']
% end
    <head>
        <meta charset="utf-8">
        <title>CanIRun!</title>
        <link href="/static/C:/Users/Jacob/Desktop/CanIRun_FrontEnd/clock_speed_success_style.css" type="text/css" rel="stylesheet">
        <style>
            @font-face {
            font-family: rapidfinger101;
            src: url("./static/RapidFinger101-W9RV.ttf")
            }
        </style>   
    </head>
    <body>
        <h1>CLOCK SPEED - SUCCESS!</h1>
        <h2>
            Your clock speed is a metric that helps to determine how fast your processing chip is.
            Clock speed lets you know the number of cycles your processor is executing in a single second.
            If your processor has a clock speed of 2.8 GHz, that means your processor is executing
            2800000000 cycles per second.

            You can run this game because your chip has a <span>clock speed of {{user_clock_speed}}</span>,
            while <span class="game">{{game}}</span> calls for a clock speed of <span>{{game_clock_speed}}</span>.
        </h2>
    </body>
</html>

