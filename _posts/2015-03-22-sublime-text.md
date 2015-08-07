---
layout:     post
title:      Sublime Text - The text editor you'll fall in love with
date:       2015-03-22 06:42
summary:    How to get the Sublime Text license with only Notepad plus plus and its plugin.
permalink:	hack-sublime-text
---

In previous article, I had introduced about some advantages of Sublime Text. In this blog, I happily bring you Sublime 3. In addition, I will show you how to get the correct license with only Notepad++ and its plugin.

__Step 1:__ Download the Sublime Text Installation file and install it's program. (Supposedly, the installation path is C:\Program Files (x86)\Sublime Text 3\)

__Step 2:__ Download the Notepad++ Setup file and Hex Editor Plugin.

__Step 3:__ Open Sublime_text3.exe by Notepad++, ofcourse, you will get some unreadable characters, but don't be panic, Click Plugins/HEX-Editor/View in Hex or the hot-key Ctrl+Alt+Shift+H 

__Step 4:__ Press Ctrl+H to replace:

Find : 74 03 33 FF 47 85 FF 0F 85 9A 06 00 00 BE 1C BE

Replace : 75 03 33 FF 90 85 FF 0F 85 9A 06 00 00 BE 1C BE

Or:

Find: 75 03 33 FF 90 85 FF 0F 85 9A 06 20 20 BE 1C BE

Replace: 75 03 33 FF 90 85 FF 0F 85 9A 06 00 00 BE 1C BE  

 Press Replace All,

__Step 5:__ Run sublime_text3.exe, Help/Enter License and input this key:

{% highlight python lineanchors %}
—--BEGIN LICENSE—--
doa#doanguyen.com
Unlimited User License
EA7E-18848
...00000000..........00000000...
......00................00......
......00................00......
......00....0000000.....00......
......00................00......
......00................00......
......00................00......
......00................00..... 
—--END LICENSE—--
{% endhighlight %}
You've got this. Now you can enjoy your new editor.