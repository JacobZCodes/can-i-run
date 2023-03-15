<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>CanIRun!</title>
        <link href="/static/C:/Users/Jacob/Desktop/CanIRun_FrontEnd/storage_fail_style.css" type="text/css" rel="stylesheet">
    </head>
    <body>
        <h1>STORAGE - FAIL!</h1>
        <h2>
            It might not come as a huge surprise to find out that your computer does not have infinite storage space. But what exactly does storage space look like in 
            a digital context?

            Everytime you download a program or file onto your computer (i.e., anything that you will need in the future), that data is then physically written to your 
            hard drive via a magnetic read-write arm. Your average hard drive today spins at over 7000RPM (!), and the read-write arm "smacks" down at certain locations and writes to the metal disk via magnetism.
            This is why hard drives are considered to be non-volatile; they don't require electricity to store the data written onto them. This is why when your
            computer is powered off, you don't magically lose your precious applications and files; the magnetic markings on your hard drive do not require
            a constant flow of electricity in order to survive.

            The smallest unit of data a computer understands is called a bit; eight of these bits make up a byte, and one million of these bytes make up a Megabyte (MB).
            However, most games and applications are much larger than a single MB, and are thus measured in an even greater unit of digital storage called a GB, which
            is equivalent to 1000 MB.

            Unfortunately, you only have <span>{{specs_result_dict['Fail']["Storage"]["User"]}} GB of space available</span>, whereas <span class="game">{{game}}</span> calls for <span>{{specs_result_dict['Fail']["Storage"]["Game"]}} GB of space.</span>
        </h2>
    </body>
</html>