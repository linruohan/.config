# Defined in - @ line 1
function vi --wraps='sudo vi' --wraps='sudo vim' --description 'alias vi sudo vim'
  sudo vim $argv;
end
