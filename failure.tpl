<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>CanIRun!</title> 
        <link href="/static/C:/Users/Jacob/Desktop/CanIRun_FrontEnd/fail_style.css" type="text/css" rel="stylesheet"> 
        <style>
            @font-face {
            font-family: rapidfinger101;
            src: url("./static/RapidFinger101-W9RV.ttf")
            }
        </style>       
    </head>
    <body>
        <div class="content">
            <h1>THE RESULT</h1>
            <h2>    Unfortunately, it doesn't like like your computer can run this game. Click any of the buttons below
                    to get an in depth explanation of the functionality behind that specific piece of hardware. Note
                    that although some parts of your hardware may have individually passed or failed their own check,
                    this does not dictate the overall ability of your machine to run your game.
            </h2>
        </div>
    
        <div class="container">
            <div class="btn">
                <form action="/os" method="post">
                    <input type="submit" value="OS">
                </form>
            </div>
            <div class="btn">
                <form action="/memory" method="post">
                    <input type="submit" value="Memory">
                </form>
            </div>
            <div class="btn">
                <form action="/directx" method="post">
                    <input type="submit" value="DirectX">
                </form>
            </div>
            <div class="btn">
                <form action="/storage" method="post">
                    <input type="submit" value="Storage">
                </form>
            </div>
            <div class="btn">
                <form action="/clockspeed" method="post">
                    <input type="submit" value="Clock Speed">
                </form>
            </div>
            <div class="btn">
                <form action="/corecount" method="post">
                    <input type="submit" value="Core Count">
                </form>
            </div>
        </div>
    </body>
</html>
        