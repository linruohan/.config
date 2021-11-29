#!/bin/bash
xrandr --output LVDS1 --off --output DP1 --off --output HDMI1 --primary --mode 1920x1080 --pos 0x0 --rotate normal --output VGA1 --off --output VIRTUAL1 --off --output VGA-1-2 --off
/bin/bash ~/scripts/dwm-status.sh &
/bin/bash ~/scripts/wp-autochange.sh &
picom -b
/bin/bash ~/scripts/tap-to-click.sh &
/bin/bash ~/scripts/inverse-scroll.sh &
#/bin/bash ~/scripts/setxmodmap-colemak.sh &
nm-applet &
fcitx &
xfce4-power-manager &
xfce4-volumed-pulse &
/bin/bash ~/scripts/run-mailsync.sh &
~/scripts/autostart_wait.sh &
