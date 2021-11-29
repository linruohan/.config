# Defined in - @ line 1
function wifi --wraps='sudo iw dev wlp3s0 scan | grep SSID' --description 'alias wifi sudo iw dev wlp3s0 scan | grep SSID'
  sudo iw dev wlp3s0 scan | grep SSID $argv;
end
