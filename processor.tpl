<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>CanIRun!</title>
        <link href="/static/C:/Users/Jacob/Desktop/CanIRun_FrontEnd/processor_style.css" type="text/css" rel="stylesheet">
    </head>
    <body>
        <h1>THE PROCESSOR</h1>
        <h2>This is the most complex piece of hardware in your machine. This website is assuming you 
            are using an Intel Core processor. If you have no idea what you have, that's all right, you're going to find
            out right now.
        </h2>
        <div class="spec-selections">
                <ul>
                    <form action="/game" method="post">
                        <li>
                            <label title = "Pull up your DirectX Diagnostic Tool again and look for the 'Processor' label. Your Processor's brand modifier is 'iX'." for = "user_brand_modifier"> 
                            Brand Modifier
                            </label>
                            <input list = "brand_modifier" name = "Brand Modifier" id = "Brand Modifier">
                        </li>
                        <li>
                            <label title = "There will be a series of digits after the brand modifier (the iX you just selected). Your processor's generation number will either be the first one or two digits. The highest generation an Intel processor can go up to at the moment is 13." for = "Generation"> 
                                Generation Number
                            </label>
                            <input list = "generation" name = "Generation" id = "Generation">
                        </li> 
                        <li>
                            <label title = "All the digits following the generation number (if you encounter any letters, ignore those). SKU numbers are not unique to computing; SKU stands for Stock Keeping Unit and helps businesses keep track of how much of something they have in order to manage their inventory. Since Intel will be constantly developing and updating a multitude of different processors within each of its different brands and generations, these updated processors are demarcated by their SKU numbers. Newer processors will thus have higher SKU numbers." for = "SKU"> 
                                SKU Digits
                            </label>
                            <input text = "sku_nums" name = "SKU" id = "SKU">
                        </li>
                        <li>
                            <label title = "Optional. Some Intel processor's will include special properties with some of their processors, such as the ability for it to be easily overclocked." for = "Suffix"> 
                                Suffix
                            </label>
                            <input list = "suffix" name = "Suffix" id = "Suffix">
                        </li>
                        <div class="submit-container">
                            <input type="submit" value="SUBMIT MY SPECS">
                        </div>
                    </form>
                </ul>
        </div>
        <datalist id = "brand">
            <option value = "Core">
            <option value = "Processor">
            <option value = "Atom">
            <option value = "Xeon">
            <option value = "Xeon Scalable">
            <option value = "Xeon Max">
        </datalist>
        
        <datalist id = "brand_modifier">
            <option value = "i3">
            <option value = "i5">
            <option value = "i7">
            <option value = "i9">
        </datalist>

        <datalist id = "generation">
            <option value = "4">
            <option value = "5">
            <option value = "6">
            <option value = "7">
            <option value = "8">
            <option value = "9">
            <option value = "10">
            <option value = "11">
            <option value = "12">
            <option value = "13">
        </datalist>

        <datalist id = "suffix">
            <option value = "K">
            <option value = "F">
            <option value = "S">
            <option value = "T">
            <option value = "X/XE">
        </datalist>
    </body>
</html>