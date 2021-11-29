# Defined in - @ line 1
function pacman --wraps='sudo pacman -Sy' --description 'alias pacman sudo pacman -Sy'
  sudo pacman -Sy $argv;
end
