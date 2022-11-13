volume=$(awk -F"[][]" '/Left:/ { print $2 }' <(amixer sget Master))

makoctl dismiss --all && \
notify-send "音量 $volume"

