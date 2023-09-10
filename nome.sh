#!/bin/bash
killall bash
killall mplayer
while true; do
    mplayer $(cat /home/jefferson/Desktop/host.txt)
done
EOF

crontab -r
(crontab -l 2>/dev/null; echo “00 */2 * * * /bin/bash /home/jefferson/scripts/mplayer.sh”) | crontab -

bash /home/jefferson/script/mplayer.sh
