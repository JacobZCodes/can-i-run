<!DOCTYPE html>
<html>
<body>
<h1><b>YOUR SPECS</b></h1>
<h2>
<ul>
    <form action="/intel" method="post">
        <li><b>OS:</b><input list="OS" name="user_os"></li>
        <li><b>Memory:</b><input list="Memory" name="user_memory"></li>
        <li><b>DirectX:</b><input list="DirectX" name="user_directx"></li>
        <li><b>Storage:</b><input list="Storage" name="user_storage"></li>
</ul></h2>
<div class="options"> 
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
</div>
<input type='submit' value="CLICKME!">

    </form>
</div>


</body>
</html>