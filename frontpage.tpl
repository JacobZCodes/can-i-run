<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>CanIRun!</title>
        <link href="./static/frontpage_style.css" type="text/css" rel="stylesheet">    </head>
    </head>
    <body>
        <h1>CAN I RUN?</h1>
        <h2>Learn a little bit about your computer's hardware while also
            seeing if your Windows PC can run any game on Steam.
        </h2>
        <div class="spec-selections">
                <ul>
                    <form action="/processor" method="post">
                            <li>
                                <label title="Operating System. Open your DirectX Diagnostic Tool by pressing the Windows key and entering 'dxdiag'. There you will be able to see information about your current OS, Memory, and DirectX." for = "OS"><b>OS</b></label><input list="OS" name="OS">
                            </li>
                            <li>
                                <label title="See 'OS'. Your diagnostic tool will display your Memory in MB, but you need to convert it to GB here." for = "Memory"><b>Memory</b></label><input list="Memory" name="Memory">
                            </li> 
                            <li>
                                <label title = "See 'OS'. You just need to input the integer version number here." for = "DirectX"><b>DirectX</b></label><input list="DirectX" name="DirectX">
                            </li>
                            <li>
                                <label title="Press the Windows key and enter 'File Explorer'. Select 'This PC' on the left-hand side and look beneath the line labeled 'Devices and drives'. There you should see X GB free of Y GB; X is the amount of storage space you have available." for = "Storage"><b>Storage</b></label><input list="Storage" name="Storage">
                            </li>
                            <div class="submit-container">
                                <input type="submit" value="SUBMIT MY SPECS">
                            </div>
                    </form>
                </ul>
        </div>
        <datalist id="OS">
            <option value="Windows 11">
            <option value="Windows 10">
            <option value="Windows 7">
        </datalist>
    
        <datalist id="Memory">
            <option value="1">
            <option value="8">
            <option value="16">
        </datalist>
    
        <datalist id="DirectX">
            <option value="4">
            <option value="7">
            <option value="12">
        </datalist>
    
        <datalist id="Storage">
            <option value="100">
            <option value="20">
            <option value="300">
            <option value="400">
        </datalist>
    </body>
</html>