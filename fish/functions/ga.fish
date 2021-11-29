# Defined in - @ line 1
function ga --wraps='git branch -a' --wraps='git add' --description 'alias ga git add'
  git add $argv;
end
