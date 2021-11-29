# Defined in - @ line 1
function wifi_show --wraps='nmcli dev wifi list' --wraps='nmcli dev wifi list | head -10' --description 'alias wifi_show nmcli dev wifi list | head -10'
  nmcli dev wifi list | head -10 $argv;
end
