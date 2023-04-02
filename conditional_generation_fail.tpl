<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>CanIRun!</title>
        <link href="./static/conditional_generation_fail_style.css" type="text/css" rel="stylesheet">
        <link href="./static/favicon-16x16.png" rel="icon">
        <style>
            @font-face {
            font-family: rapidfinger101;
            src: url("./static/RapidFinger101-W9RV.ttf")
            }
        </style>   
    </head>
    <body>
        <h1>GENERATION - FAIL!</h1>
        <h2>
            Not all chips with the same brand modifier are produced equally. As Intel technology is rapidly growing and improving, they are constantly making loads
            of improvements for chips under the umbrella of a single brand modifier before going off and creating an entirely new brand modifier. These intra
            brand modifier variations can be visualized in the chip's generation number(s), which follow directly after the brand modifier. 
            
            Your chip's <span>generation number is {{processor_specs_result_dict['Info']['Generation']['User']}}</span> and <span class="game">{{game}}</span> calls for a
            generation number of <span>at least {{processor_specs_result_dict['Info']['Generation']['Game']}}.</span> However,
            in this situation the generation number can be ignored since your <span class="game">{{game}}'s</span> brand modifier trumps that of yours.
        </h2>
    </body>
</html>

