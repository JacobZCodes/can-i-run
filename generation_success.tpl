<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>CanIRun!</title>
        <link href="./static/generation_success_style.css" type="text/css" rel="stylesheet">
        <link href="./static/favicon-16x16.png" rel="icon">
        <style>
            @font-face {
            font-family: rapidfinger101;
            src: url("./static/RapidFinger101-W9RV.ttf")
            }
        </style>   

    </head>
    <body>
        <h1>GENERATION - SUCCESS!</h1>
        <h2>
            Not all chips with the same brand modifier are produced equally. As Intel technology is rapidly growing and improving, they are constantly making loads
            of improvements for chips under the umbrella of a single brand modifier before going off and creating an entirely new brand modifier. These intra
            brand modifier variations can be visualized in the chip's generation number(s), which follow directly after the brand modifier. 
            
            Your chip matches the required <span>{{processor_specs_result_dict['Success']['Brand Modifier']['Game']}}</span> of <span class="game">{{game}}.</span> In addition, <span class="game">{{game}}</span> calls for a <span>generation number of {{processor_specs_result_dict['Success']['Generation']['Game']}},</span> and your chip meets or 
            exceeds this with a <span>generation number of {{processor_specs_result_dict['Success']['Generation']['User']}}.</span>
        </h2>
    </body>
</html>

