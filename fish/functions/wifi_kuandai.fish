# Defined in - @ line 1
function wifi_kuandai --wraps='nmcli device wifi connect "xiaohan001" password "Mm1214875764"' --wraps='nmcli device wifi connect "xiaohan001" password "Mm1214875764" && nmcli dev wifi list | head -5' --description 'alias wifi_kuandai nmcli device wifi connect "xiaohan001" password "Mm1214875764" && nmcli dev wifi list | head -5'
  nmcli device wifi connect "xiaohan001" password "Mm1214875764" && nmcli dev wifi list | head -5 $argv;
end
