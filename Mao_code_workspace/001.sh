# Prompts
POWERLEVEL9K_LEFT_SEGMENT_SEPARATOR='\uE0C0'
#POWERLEVEL9K_LEFT_SUBSEGMENT_SEPARATOR='\uE0C0'
POWERLEVEL9K_RIGHT_SEGMENT_SEPARATOR='\uE0C2'
#POWERLEVEL9K_RIGHT_SUBSEGMENT_SEPARATOR='\uE0C2'
POWERLEVEL9K_LEFT_PROMPT_ELEMENTS=(dir dir_writable vcs virtualenv)
POWERLEVEL9K_RIGHT_PROMPT_ELEMENTS=(status background_jobs command_execution_time ip)
POWERLEVEL9K_SHORTEN_DIR_LENGTH=2
POWERLEVEL9K_SHORTEN_DELIMITER=..
POWERLEVEL9K_PROMPT_ON_NEWLINE=true
POWERLEVEL9K_MULTILINE_FIRST_PROMPT_PREFIX=$'\n'
POWERLEVEL9K_MULTILINE_LAST_PROMPT_PREFIX="\uF460%F{073}\uF460%F{109}\uF460%f "
export ZSH="/Users/john/.oh-my-zsh"
POWERLEVEL9K_MODE='nerdfont-complete'
ZSH_THEME="powerlevel10k/powerlevel10k"
export UPDATE_ZSH_DAYS=13
HIST_STAMPS="yyyy/mm/dd"
plugins=(
    git
    colored-man-pages
    colorize
    github
    brew
    osx
    docker
    docker-compose
    autojump
    zsh-autosuggestions
    zsh-syntax-highlighting
    autopep8
    python
)
source $ZSH/oh-my-zsh.sh
alias zshconfig="vim ~/.zshrc"
alias vimconfig="vim ~/.vimrc"
alias ansibleconfig="vim ~/.ansible/ansible.cfg"
alias grep='grep --color=auto'