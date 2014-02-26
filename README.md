#Description

Skype wrapper script for injecting custom status icons.

In desktop environments that doesn't provide classic tray (i.e. Unity), sni-qt package comes into play for displaying Skype status icons. It converts tray icons into indicators suitable for Unity. Since most indicators use monochrome icons, colored Skype status icon looks foreign among the others.

However, a little hack can be done against sni-qt. Every icon that sni-qt converts to indicator, first stored in temporary folder and only after that icon will be displayed. So, what this hack does, is that it copies predefined icons into temporary folder, where sni-qt will store tray icons of application. That icons have exactly same name that sni-qt will use for them and rights are restricted to read-only to forbid them to be overwritten. So, when sni-qt see that the icon is already present in temporary folder, it just takes this icon and use it.

Well, that's exactly what this script does! :) It launches Skype, detects where sni-qt will place icons cache and injects own icons there.

Here's screenshot with (cute) and without (ugly) wrapper in Elementary OS:

![Ugly & Cute](http://eos-tips.com/wp-content/uploads/2014/02/ugly-and-cute.png)

#Usage

    git clone git://github.com/rpeshkov/skype-wrapper.git ~/bin/skype-wrapper
    cd ~/bin/skype-wrapper
    killall skype
    ./skype-wrapper.py

#Iconset
![Elementary Skype iconset](http://eos-tips.com/wp-content/uploads/2014/02/iconset.png)