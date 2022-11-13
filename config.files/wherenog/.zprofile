#!/usr/bin/zsh

# profile file. Runs on login. Environmental variables are set here.

# Default programs:
export EDITOR="nvim"
export TERMINAL="foot"
export TERM="xterm-256color"
export BROWSER="firefox"

# ~/ Clean-up:
export XDG_CONFIG_HOME="$HOME/.config"
export XDG_DATA_HOME="$HOME/.local/share"
export XDG_CACHE_HOME="$HOME/.cache"
export LESSHISTFILE="-"
export CARGO_HOME="${XDG_DATA_HOME:-$HOME/.local/share}/cargo"
export GOPATH="${XDG_DATA_HOME:-$HOME/.local/share}/go"

# Other program settings:
export LESS=-R
export LESS_TERMCAP_mb="$(printf '%b' '[1;31m')"
export LESS_TERMCAP_md="$(printf '%b' '[1;36m')"
export LESS_TERMCAP_me="$(printf '%b' '[0m')"
export LESS_TERMCAP_so="$(printf '%b' '[01;44;33m')"
export LESS_TERMCAP_se="$(printf '%b' '[0m')"
export LESS_TERMCAP_us="$(printf '%b' '[1;32m')"
export LESS_TERMCAP_ue="$(printf '%b' '[0m')"
export LESSOPEN="| /usr/bin/highlight -O ansi %s 2>/dev/null"

# This is the list for lf icons:
export LF_ICONS="di=📁:\
fi=📜:\
tw=🤝:\
ow=📂:\
ln=⛓️ :\
or=❌:\
ex=🎯:\
*.txt=📜:\
*.mom=📜:\
*.me=📜:\
*.ms=📜:\
*.png=🖼️ :\
*.webp=🖼️ :\
*.ico=🖼️ :\
*.jpg=📸:\
*.jpe=📸:\
*.jpeg=📸:\
*.gif=🖼️ :\
*.svg=🖼️ :\
*.tif=🖼️ :\
*.tiff=🖼️ :\
*.xcf=🖼️ :\
*.html=🌎:\
*.xml=📰:\
*.gpg=🔒:\
*.css=🎨:\
*.pdf=📚:\
*.djvu=📚:\
*.epub=📚:\
*.csv=📓:\
*.xlsx=📓:\
*.tex=📜:\
*.md=📘:\
*.r=📊:\
*.R=📊:\
*.rmd=📊:\
*.Rmd=📊:\
*.m=📊:\
*.mp3=🎵:\
*.opus=🎵:\
*.ogg=🎵:\
*.m4a=🎵:\
*.flac=🎼:\
*.wav=🎼:\
*.mkv=🎦:\
*.mp4=🎦:\
*.webm=🎦:\
*.mpeg=🎦:\
*.avi=🎦:\
*.mov=🎦:\
*.mpg=🎦:\
*.wmv=🎦:\
*.m4b=🎦:\
*.flv=🎦:\
*.zip=📦:\
*.rar=📦:\
*.7z=📦:\
*.tar.gz=📦:\
*.z64=🎮:\
*.v64=🎮:\
*.n64=🎮:\
*.gba=🎮:\
*.nes=🎮:\
*.gdi=🎮:\
*.1=📙:\
*.nfo=📙:\
*.info=📙:\
*.log=📙:\
*.iso=📀:\
*.img=📀:\
*.bib=🎓:\
*.ged=👪:\
*.part=💔:\
*.torrent=📥:\
*.ini=⚙️ :\
*.exe=🪟:\
*.java=☕:\
*.jar=☕:\
*.c=🇨 :\
*.cpp=🇨 :\
*.go=🇬 :\
*.py=🐍:\
*.diff=📌:\
*.patch=📌:\
"
