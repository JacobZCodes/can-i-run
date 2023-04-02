<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>CanIRun!</title>
        <link href="./static/directx_fail_style.css" type="text/css" rel="stylesheet">
        <link href="./static/favicon-16x16.png" rel="icon">
        <style>
            @font-face {
            font-family: rapidfinger101;
            src: url("./static/RapidFinger101-W9RV.ttf")
            }
        </style>   

    </head>
    <body>
        <h1>DIRECTX - FAIL!</h1>
        <h2>
            <p>In the old days of gaming, video game companies had to communicate directly with a system's hardware in order for that system to be able
            to run their game. This was very problematic as these game companies would have to strenuously account for the many different types
            of hardware across different systems. Microsoft then created a solution to this problem in 1995 with their release of DirectX.

            DirectX can be thought of as the middleman between the system and the game's backend design. DirectX is merely a bundle of different APIs that allow for
            a standardized communication between a game and the system it is trying to run on.</p> <p>An API, or Application Programming Interface, can simply be thought
            of as DirectX on a smaller scale; APIs allow for data-related communication between two applications.

            For example, I utilized the Steam API in the construction of this website. In order to get information about the game you entered, I used your inputted data
            (the name of your requested game) to then communicate with the Steam API. I said, "Hey Steam, I have the name of this game. Can you give information about it?" and 
            Steam responded by sending me certain information. Obviously I am simplifying the nature of this digital communication for explanatory purposes,
            but this is the essence of an API call.</p>

            <p>Coming back to DirectX, you are currently running version <span>{{specs_result_dict['Fail']['DirectX']['User']}}</span> of DirectX, while <span class="game">{{game}}</span> requires <span>{{specs_result_dict['Fail']['DirectX']['Game']}}</span>. DirectX is constantly
            being updated to account for the exponential growth in the technology surrounding game development, so it is for this reason that it is critical
            that your DirectX is up to date.</p>
        </h2>
    </body>
</html>