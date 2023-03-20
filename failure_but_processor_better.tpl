OLD GAME - PROCESSOR SUCCEEDED, GENERAL SPECS FAILED
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
        <!--<img src="/static/C:/Users/Jacob/Desktop/CanIRun_FrontEnd/{{game}}.jpg">-->
        <div class="content">
            <h1>THE RESULT</h1>
            <h2>    Unfortunately, it doesn't like like your computer can run this game. Here's why.
            </h2>
        </div>
    </body>
    <div class="OS_Explain">
        <form action="/os" method="post">
            <input type="submit" value="OS">
        </form>
    </div>
    <div class="Memory_Explain">
        <form action="/memory" method="post">
            <input type="submit" value="Memory">
        </form>
    </div>
    <div class="DirectX_Explain">
        <form action="/directx" method="post">
            <input type="submit" value="DirectX">
        </form>
    </div>
    <div class="Storage_Explain">
        <form action="/storage" method="post">
            <input type="submit" value="Storage">
        </form>
    </div>
    <div class="Clock_Speed_Explain">
        <form action="/clockspeedsuccess" method="post">
            <input type="submit" value="Clock Speed">
        </form>
    </div>
    <div class="Core_Count_Explain">
        <form action="/corecountsuccess" method="post">
            <input type="submit" value="Core Count">
        </form>
    </div>
    
</html>
        