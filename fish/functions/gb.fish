# Defined in - @ line 1
function gb --wraps='git branch -a' --description 'alias gb git branch -a'
  git branch -a $argv;
end
