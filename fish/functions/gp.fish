# Defined in - @ line 1
function gp --wraps='git push -u linruohan master' --wraps='git push linruohan' --description 'alias gp git push linruohan'
  git push linruohan $argv;
end
