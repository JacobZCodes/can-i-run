<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>CanIRun!</title>
        <link href="/static/C:/Users/Jacob/Desktop/CanIRun_FrontEnd/conditional_sku_fail_style.css" type="text/css" rel="stylesheet">
        <style>
            @font-face {
            font-family: rapidfinger101;
            src: url("./static/RapidFinger101-W9RV.ttf")
            }
        </style>   

    </head>
    <body>
        <h1>SKU - FAIL!</h1>
        <h2>
            SKU numbers are not unique to computing; SKU stands for Stock Keeping Unit and helps businesses keep track of how much of something 
            they have in order to manage their invetory. Since Intel will be constantly developping and updating a multitude of different processors within each of 
            its different brands and generations, these updated processors are demarcated by their SKU numbers. Newer processors will thus have higher SKU numbers.
            <span class="game">{{game}}</span> calls for a chip containing SKU numbers with a <span>value of {{processor_specs_result_dict['Info']['SKU']['Game']}}</span>, and your processor <span>falls short</span>
            of that with SKU numbers with a <span>value of {{processor_specs_result_dict['Info']['SKU']['User']}}.</span> However,
            the SKU numbers can be ignored here as a check earlier in the processor string failed,
            meaning that even if your SKU numbers are higher than those of <span class="game">{{game}},</span> this doesn't matter
            in this scenario.
        </h2>
    </body>
</html>