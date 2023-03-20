<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>CanIRun!</title>
        <link href="./static/brandmodifier_fail_style.css" type="text/css" rel="stylesheet">
        <style>
            @font-face {
            font-family: rapidfinger101;
            src: url("./static/RapidFinger101-W9RV.ttf")
            }
        </style>   
    </head>
    <body>
        <h1>BRAND MODIFIER - FAIL!</h1>
        <h2>
            Each Intel Core processor chip has something called a brand modifier. These don't really provide any specific information other than give a rough estimate
            of when that chip was produced. For example, you wouldn't need to know too much about cars to figure that a 2019 Subaru Outback will run better than the a
            car of the same make and model manufactured in 2000. Since your chip has an <span>{{processor_specs_result_dict['Fail']['Brand Modifier']['User']}} brand modifier</span> and <span class="game">{{game}}</span> calls for an <span>{{processor_specs_result_dict['Fail']['Brand Modifier']['Game']}} brand modifier</span>,
            you cannot run <span class="game">{{game}}.</span>
        </h2>
    </body>
</html>

