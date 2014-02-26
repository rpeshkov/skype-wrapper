#!/bin/bash

cd src_icons

for file in "away-message" "dnd-message" "invisible-message" "online-message" "offline-message"
do
    for i in {0..9}
    do
        w=$(($i*5))
        c=$(($i+1))
        convert $file.png \( digits.png -crop 5x6+$w+0 +repage \) -gravity northeast -geometry +4+3 -composite $file-$c.png
    done
done

montage -tile x1 -geometry +2+2 away-message-* -background black am.png
montage -tile x1 -geometry +2+2 dnd-message-* -background black dndm.png
montage -tile x1 -geometry +2+2 online-message-* -background black onm.png
montage -tile x1 -geometry +2+2 invisible-message-* -background black invm.png
montage -tile x1 -geometry +2+2 offline-message-* -background black offm.png
montage -tile x1 -geometry +2+2 -background black online.png away.png dnd-gray.png invisible.png offline.png st.png
montage -tile x1 -geometry +2+2 -background black loading-1.png loading-2.png loading-3.png loading-4.png loading.png
montage -tile 1x -geometry +2+2 -background black st.png loading.png onm.png am.png dndm.png invm.png offm.png ../iconset.png

rm am.png
rm dndm.png
rm onm.png
rm invm.png
rm offm.png
rm st.png
rm loading.png

