# Defined in - @ line 1
function gll --wraps='git pull --rebase' --description 'alias gll git pull --rebase'
  git pull --rebase $argv;
end
