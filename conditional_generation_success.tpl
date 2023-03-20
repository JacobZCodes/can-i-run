<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>CanIRun!</title>
        <link href="/static/C:/Users/Jacob/Desktop/CanIRun_FrontEnd/conditional_generation_success_style.css" type="text/css" rel="stylesheet">
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
            
            Your chip's <span>generation number is {{processor_specs_result_dict['Info']['Generation']['User']}}</span> and <span class="game">{{game}}</span> calls for a
            generation number of <span>at least {{processor_specs_result_dict['Info']['Generation']['Game']}}.</span> However,
            in this situation the generation number can be ignored since your brand modifier trumps that of <span class="game">{{game}}.</span>
        </h2>
    </body>
</html>

