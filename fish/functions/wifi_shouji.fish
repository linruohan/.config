# Defined in - @ line 1
function wifi_shouji --wraps='nmcli device wifi connect "HONOR 30" password "12345678"' --wraps='nmcli device wifi connect "HONOR 30" password "12345678";wifishow | head -5' --wraps='nmcli device wifi connect "HONOR 30" password "12345678" && wifishow | head -5' --wraps='nmcli device wifi connect "HONOR 30" password "12345678" && nmcli dev wifi list | head -5' --description 'alias wifi_shouji nmcli device wifi connect "HONOR 30" password "12345678" && nmcli dev wifi list | head -5'
  nmcli device wifi connect "HONOR 30" password "12345678" && nmcli dev wifi list | head -5 $argv;
end
