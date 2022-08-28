# If you come from bash you might have to change your $PATH.
# export PATH=$HOME/bin:/usr/local/bin:$PATH

# Path to your oh-my-zsh installation.
export ZSH="$HOME/.oh-my-zsh"

# Set name of the theme to load --- if set to "random", it will
# load a random theme each time oh-my-zsh is loaded, in which case,
# to know which specific one was loaded, run: echo $RANDOM_THEME
# See https://github.com/ohmyzsh/ohmyzsh/wiki/Themes
ZSH_THEME="agnoster"

# Set list of themes to pick from when loading at random
# Setting this variable when ZSH_THEME=random will cause zsh to load
# a theme from this variable instead of looking in $ZSH/themes/
# If set to an empty array, this variable will have no effect.
# ZSH_THEME_RANDOM_CANDIDATES=( "robbyrussell" "agnoster" )

# Uncomment the following line to use case-sensitive completion.
# CASE_SENSITIVE="true"

# Uncomment the following line to use hyphen-insensitive completion.
# Case-sensitive completion must be off. _ and - will be interchangeable.
# HYPHEN_INSENSITIVE="true"

# Uncomment one of the following lines to change the auto-update behavior
# zstyle ':omz:update' mode disabled  # disable automatic updates
# zstyle ':omz:update' mode auto      # update automatically without asking
# zstyle ':omz:update' mode reminder  # just remind me to update when it's time

# Uncomment the following line to change how often to auto-update (in days).
# zstyle ':omz:update' frequency 13

# Uncomment the following line if pasting URLs and other text is messed up.
# DISABLE_MAGIC_FUNCTIONS="true"

# Uncomment the following line to disable colors in ls.
# DISABLE_LS_COLORS="true"

# Uncomment the following line to disable auto-setting terminal title.
# DISABLE_AUTO_TITLE="true"

# Uncomment the following line to enable command auto-correction.
# ENABLE_CORRECTION="true"

# Uncomment the following line to display red dots whilst waiting for completion.
# You can also set it to another string to have that shown instead of the default red dots.
# e.g. COMPLETION_WAITING_DOTS="%F{yellow}waiting...%f"
# Caution: this setting can cause issues with multiline prompts in zsh < 5.7.1 (see #5765)
# COMPLETION_WAITING_DOTS="true"

# Uncomment the following line if you want to disable marking untracked files
# under VCS as dirty. This makes repository status check for large repositories
# much, much faster.
# DISABLE_UNTRACKED_FILES_DIRTY="true"

# Uncomment the following line if you want to change the command execution time
# stamp shown in the history command output.
# You can set one of the optional three formats:
# "mm/dd/yyyy"|"dd.mm.yyyy"|"yyyy-mm-dd"
# or set a custom format using the strftime function format specifications,
# see 'man strftime' for details.
# HIST_STAMPS="mm/dd/yyyy"

# Would you like to use another custom folder than $ZSH/custom?
# ZSH_CUSTOM=/path/to/new-custom-folder

# Which plugins would you like to load?
# Standard plugins can be found in $ZSH/plugins/
# Custom plugins may be added to $ZSH_CUSTOM/plugins/
# Example format: plugins=(rails git textmate ruby lighthouse)
# Add wisely, as too many plugins slow down shell startup.
plugins=(git sudo zsh-syntax-highlighting zsh-autosuggestions)

source $ZSH/oh-my-zsh.sh

# User configuration

# export MANPATH="/usr/local/man:$MANPATH"
export PATH=$PATH:$HOME/.local/bin
# You may need to manually set your language environment
# export LANG=en_US.UTF-8
export LANG=zh_CN.UTF-8

# Preferred editor for local and remote sessions
if [[ -n $SSH_CONNECTION ]]; then
  export EDITOR='vim'
else
  export EDITOR='nvim'
fi

# Compilation flags
# export ARCHFLAGS="-arch x86_64"

# Set personal aliases, overriding those provided by oh-my-zsh libs,
# plugins, and themes. Aliases can be placed here, though oh-my-zsh
# users are encouraged to define aliases within the ZSH_CUSTOM folder.
# For a full list of active aliases, run `alias`.
#
# Example aliases
# alias zshconfig="mate ~/.zshrc"
# alias ohmyzsh="mate ~/.oh-my-zsh"

export XMODIFIERS="@im=fcitx"
export XIM=fcitx
export XIM_PROGRAM=fcitx

export ZSH_AUTOSUGGEST_HIGHLIGHT_STYLE='fg=5'
# wayland input chinese alias
#alias kitty="WAYLAND_DISPLAY=kitty kitty"
# 1. arch or manjaro OS commands
alias pi='sudo pacman -Sy'
alias pu='sudo pacman -Syyu'
alias pr='sudo pacman -Rscn'
alias pq='sudo pacman -Qs'
alias yi="yay -S"
alias yu="yay -Syyu"
alias yr="yay -Rscn"
alias yq="yay -Qs"

alias wifi1='iwlist scan | grep "ESSID:"'
alias wifi='nmcli device wifi list | head -10'
alias shouji='nmcli device wifi connect "HONOR 30" password "12345678"'
alias kuandai='nmcli device wifi connect "xiaohan001" password "Mm1214875764"'
alias duankaiwifi='nmcli device disconnect wlp3s0'
# 2. custom: dir commands
alias wo='cd ~/working'
alias co='cd ~/codehub'
alias m="cd ~"
# ===========================
alias rm='rm -rf'
alias ln='ln -i'
alias cp1='cp -arv'
alias cp='rsync -avPh'
alias mv='mv -i'
alias mkdir='mkdir -pv'
alias ..='cd ../../'
alias ...='cd ../../..'
alias l.='lsd -d .* --color=auto'
alias ll='lsd -laF --color=auto'
alias ls='lsd --color=auto'

alias .2='cd ../..'
alias .3='cd ../../..'
alias .4='cd ../../../..'
alias .5='cd ../../../../..'

# 2.1 custom cat commands
alias nocomment='grep -Ev "^(#|$)"'
alias tf='tail -f '
alias grep='grep --color=auto'
alias egrep='egrep --color=auto'
alias fgrep='fgrep --color=auto'
alias diff='colordiff'

# 2.3 custom time commands
alias now='date "+%Y-%m-%d %H:%M:%S.%s"'
alias timestamp='now; echo s: $(date +"%s"); echo ms: $(echo `expr \`date +%s%N\` / 1000000`)'

# 2.4 net commands
alias curl='curl -O'

# 2.5 memory status commands
alias du='du -h'
alias du1='du -h -d 1'
alias du2='du -h -d 2'
alias du3='du -h -d 3'
alias meminfo='free -h -l -t'
alias cpuinfo='lscpu'

# 2.6 ps commands
alias ports='netstat -tulanp'
alias chown='chown --preserve-root'
alias chmod='chmod --preserve-root'
alias chgrp='chgrp --preserve-root'
alias psg='ps -ef | grep '
alias psme='ps -ef | grep $USER --color=always '
alias psmem='ps auxf | sort -nr -k 4'
alias psmem10='ps auxf | sort -nr -k 4 | head -10'
alias pscpu='ps auxf | sort -nr -k 3'
alias pscpu10='ps auxf | sort -nr -k 3 | head -10'
alias dinfo='df -h; free -h -l -t; netstat -tulanp'
alias h='history'
alias j='jobs -l'

# 3. custom tools
alias vi=nvim
alias ra='ranger'
alias lg='lazygit'

# 4. git commands
alias gr='git rm -rf'
alias gp='git push origin master'
alias ga='git add'
alias gs='git status'
alias gll='git pull'
alias gc='git commit -m'
alias gb='git branch -a'
alias gd='git diff'
