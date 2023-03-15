<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>CanIRun!</title>
        <link href="/static/C:/Users/Jacob/Desktop/CanIRun_FrontEnd/sku_success_style.css" type="text/css" rel="stylesheet">
    </head>
    <body>
        <h1>SKU - SUCCESS!</h1>
        <h2>
            SKU numbers are not unique to computing; SKU stands for Stock Keeping Unit and helps businesses keep track of how much of something 
            they have in order to manage their invetory. Since Intel will be constantly developping and updating a multitude of different processors within each of 
            its different brands and generations, these updated processors are demarcated by their SKU numbers. Newer processors will thus have higher SKU numbers.
            <span class="game">{{game}}</span> calls for a chip containing SKU numbers with <span>a value of {{processor_specs_result_dict['Success']['SKU']['Game']}},</span> and your processor meets or exceeds
            that with SKU numbers with <span>a value of {{processor_specs_result_dict['Success']['SKU']['User']}}.</span>
        </h2>
    </body>
</html>

