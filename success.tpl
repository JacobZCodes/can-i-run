<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>CanIRun!</title>
        <link href="./static/fail_style.css" type="text/css" rel="stylesheet"> 
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
            <h2>    Go have some fun! All checks passed. Click any of the buttons below if you want
                    to learn a little bit about why each of your specs passed its check and why that matters.
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
                <form action="/brandmodifier" method="post">
                    <input type="submit" value="Brand Modifier">
                </form>
            </div>
            <div class="btn">
                <form action="/generation" method="post">
                    <input type="submit" value="Generation">
                </form>
            </div>
            <div class="btn">
                <form action="/sku" method="post">
                    <input type="submit" value="SKU">
                </form>
            </div>
        </div>
    </body>
</html>
        