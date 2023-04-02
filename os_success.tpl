<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>CanIRun!</title>
        <link href="./static/os_success_style.css" type="text/css" rel="stylesheet">
        <link href="./static/favicon-16x16.png" rel="icon">
        <style>
            @font-face {
            font-family: rapidfinger101;
            src: url("./static/RapidFinger101-W9RV.ttf")
            }
        </style>   

    </head>
    <body>
        <h1>OS - SUCCESS!</h1>
        <h2>Your OS can run <span class="game">{{game}}</span>! You are running <span>{{specs_result_dict['Success']['OS']['User']}}</span> and <span class="game">{{game}}</span>
            requires <span>{{specs_result_dict['Success']['OS']['Game']}}</span>. The OS (Operating System) is the fundamental, overarching software
            that structures your computer at its most primitive, or lowest, level. Since your 
            OS has a higher version number than <span class="game">{{game}}'s</span> OS, your computer can run <span class="game">{{game}}</span>.
        </h2>
    </body>
</html>