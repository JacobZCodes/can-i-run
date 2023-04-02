<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>CanIRun!</title>
        <link href="./static/memory_success_style.css" type="text/css" rel="stylesheet">
        <link href="./static/favicon-16x16.png" rel="icon">
        <style>
            @font-face {
            font-family: rapidfinger101;
            src: url("./static/RapidFinger101-W9RV.ttf")
            }
        </style>   

    </head>
    <body>
        <h1>MEMORY - SUCCESS!</h1>
        <h2><p>Your computer has something called RAM, or Random Access Memory. Every time you touch a key, move your mouse, or open a 
            computer program, electrical impulses are firing off and being read by your computer in the form of 1's and 0's, otherwise known as binary. 

            This binary data then commands a piece of hardware within your computer called your hard disk drive, commonly referred to as just a hard drive. Your
            hard drive is where all your games, applications, and software within your computer physically live.</p> <p>Everytime you download a program or file onto your
            computer (i.e., anything that you will need in the future), that data is then physically written to your hard drive via a magnetic read-write arm. Your
            average hard drive today spins at over 7000RPM (!), and the read-write arm "smacks" down at certain locations and writes to the metal disk via magnetism.
            This is why hard drives are considered to be non-volatile; they don't require electricity to store the data written onto them. This is why when your
            computer is powered off, you don't magically lose your precious applications and files; the magnetic markings on your hard drive do not require
            a constant flow of electricity in order to survive.</p>

            On the other hand, your computer also has volatile memory; this means that it does require electricity in order to exist. When your computer is powered off,
            this data is completely wiped away and lost, as opposed to your hard drive. This disappearing data is known as RAM, or Random Access Memory. This nomenclature
            is a little misleading as all the "random access" part means is that your RAM has direct access to any memory address on your computer.

            In terms of gaming, your RAM is critical because within your game, there is tons of game-specific data that your computer needs to work with. Although
            your game application is stored in the hard disk drive, the actions you take within the game - shooting an enemy, running down a corridor, crafting a pick-axe -
            these are all related to your RAM.

            <p>Since your RAM is directly related to how quickly your game reacts to your system's input, it is obviously one of the most important factors. You have
            <span>{{specs_result_dict['Success']['Memory']['User']}} GB RAM </span>and <span class="game">{{game}}</span> requires <span>{{specs_result_dict['Success']['Memory']['Game']}}</span>.</p>
        </h2>
    </body>
</html>