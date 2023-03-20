<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>CanIRun!</title>
        <link href="./static/os_fail_style.css" type="text/css" rel="stylesheet">
        <style>
            @font-face {
            font-family: rapidfinger101;
            src: url("./static/RapidFinger101-W9RV.ttf")
            }
        </style>   

    </head>
    <body>
        <h1>OS - FAIL!</h1>
        <h2>Your OS is too weak to run <span class="game">{{game}}</span>. You are running <span>{{specs_result_dict['Fail']['OS']['User']}}</span> while <span class="game">{{game}}</span>
            requires <span>{{specs_result_dict['Fail']['OS']['Game']}}</span>. The OS (Operating System) is the fundamental, overarching software
            that structures your computer at its most primitive, or lowest, level. Since your 
            OS has a lower version number than <span class="game">{{game}}'s</span> OS, your computer cannot run <span class="game">{{game}}</span>.
        </h2>
    </body>
</html>