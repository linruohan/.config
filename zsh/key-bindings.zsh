zle -N zle-line-init
zle -N zle-keymap-select

KEYTIMEOUT=1

# fzf
export FZF_DEFAULT_OPTS='--bind ctrl-e:down,ctrl-u:up --preview ""[[ $(file --mime {}) =~ binary ]] && echo {} is a binary file || (ccat --color=always {} || highlight -O ansi -l {} || cat {}) 2> /dev/null | head -500'
export FZF_DEFAULT_COMMAND='ag --hidden --ignore .git -g ""'
export FZF_COMPLETION_TRIGGER='\'
export FZF_TMUX_HEIGHT='80%'
export FZF_PREVIEW_COMMAND='[[ $(file --mine {}) =~ binary ]] && echo {} is a binary file || (ccat --color=always {} || highlight -O ansi -l {} cat {}) 2> /dev/null | head -500'

source ~/.config/zsh/key-bindings.zsh
source ~/.config/zsh/completion.zsh

if [ -f ~/.sconfig/zsh/zshrc ];then
	source ~/.sconfig/zsh/zshrc
fi
