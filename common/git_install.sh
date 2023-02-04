#!/bin/bash

cur=$(dirname "$(realpath "$0")")
# shellcheck disable=SC1091
source "${cur}/common.sh"

git_install() {
    type git || sudo pacman -Sy git
    # lazygit auto install
    type lazygit || sudo pacman -Sy lazygit || {
        rt_log "lazygit manual install with go"
        git clone https://github.com/jesseduffield/lazygit.git
        (cd lazygit && go install) || {
            rt_err "manual lazygit install failed !"
        }
    }
	git config --system http.sslverify false
    git config --global https.proxy http://127.0.0.1:15732
    git config --global http.proxy http://127.0.0.1:15732
    # git config
    rt_log "gitconfig setting ...."
    grep "linruohan" ~/.gitconfig && (
        rt_log "gitconfig setting already"
        return 1
    )
    echo '''[user]
	name = linruohan
	email = mjt1220@126.com
[filter "lfs"]
	required = true
	clean = git-lfs clean -- %f
	smudge = git-lfs smudge -- %f
	process = git-lfs filter-process
[oh-my-zsh]
	hide-dirty = 0
	hide-status = 0
[credential "https://gitee.com"]
	provider = generic
[core]
	pager = delta
[delta]
	navigate = true 
	light = false   
	side-by-side = false
	line-numbers = true
[interactive]
	diffFilter = delta --color-only --features=interactive
[merge]
	conflictstyle = diff3
[diff]
	colorMoved = default''' > ~/.gitconfig
    rt_log "git and lazygit setting success"
}

git_install "$@"
