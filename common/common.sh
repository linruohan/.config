#!/usr/bin/env bash

cur=$(dirname $(realpath $0))
BIN=$(dirname $cur)
source ./common/zsh_install.sh

color_blue="\033[1;34m"
color_green="\033[0;32m"
color_red="\033[1;31m"
color_yellow="\033[1;33m"
color_clean="\033[0m"
rt_debug() {
    echo -e "${color_blue}$(date '+[%Y-%m-%d %H:%M:%S]')[INFO] $* ${color_clean}"
}
rt_warn() {
    echo -e "${color_yellow}$(date '+[%Y-%m-%d %H:%M:%S]')[INFO] $* ${color_clean}"
}
rt_log() {
    echo -e "${color_green}$(date '+[%Y-%m-%d %H:%M:%S]')[INFO] $* ${color_clean}"
}
rt_err() {
    echo -e "${color_red}$(date '+[%Y-%m-%d %H:%M:%S]')[ERROR] $* ${color_clean}"
}

neovim_install() {
    # neovim install
    type neovim && return 0
    sudo pacman -Sy neovim python-pip
    # python dep
    pip3 install pynvim
    # node dep
    npm install -g neovim
    # config files install
    flag="${1:-LunarVim}"
    [ -d ~/.config/nivm ] && mv ~/.config/nvim ~/.config/nvim.old
    case "$flag" in
        "theniceboy")
            #  2.1 theniceboy: https://github.com/theniceboy/nvim
            git clone git@github.com:theniceboy/nvim.git ~/.config/nvim
            cd ~/.config/nvim && patch < "${BIN}/patch.files/theniceboy_nvim.init.vim.patch" || rt_err "patch to theniceboy_nvim failed"
            ;;
        "scratch")
            #  2.2 git@github.com:LunarVim/Neovim-from-scratch.git
            git clone git@github.com:LunarVim/Neovim-from-scratch.git ~/.config/nvim
            ;;
        "LunarVim")
            git clone https://github.com/LunarVim/LunarVim.git ~/.config/nvim
            rt_log "stating install lunarvim ..."
            nvim +PackerSync
            ;;
        "askfiy")
            #  2.3 git@github.com:askfiy/nvim.git
            git clone git@github.com:askfiy/nvim.git ~/.config
            cd ~/.config/nvim/ && patch < ${BIN}/patch.files/askfiy.nvim.patch
            ;;
        *)
            echo default
            ;;
    esac

}

python_install() {
    #type python3 && return 0
    [ -d ~/.pip ] && {
        rt_log "python proxy is setting already !"
        return 0
    }
    # python3 代理
    mkdir -p ~/.pip
    echo "[global]
index-url = https://pypi.tuna.tsinghua.edu.cn/simple
[install]
trusted-host = https://pypi.tuna.tsinghua.edu.cn" > ~/.pip/pip.conf
    # python 安装依赖库
    pip3 install pylint pynvim jedi
    rt_log "python proxy setting success!"
}

node_install() {
    type node && return 0
    # 1 nodejs install
    sudo pacman -Sy nodejs || {
        rt_err "nodejs install failed"
        return 1
    }
    # npm 代理设置
    echo "strict-ssl=false
registry=https://registry.npmmirror.com/
electron_mirror=https://npmmirror.com/mirrors/electron/
electron_builder_binaries_mirror=http://npmmirror.com/mirrors/electron-builder-binaries/" > ~/.npmrc
    rt_log "node and ~/.npmrc setting success!"
    return 0
}

go_install() {
    type go && return 0
    # 访问https://studygolang.com/dl 获取最新版本
    sudo pacman -Sy go || {
        rt_err "golang install failed"
        return 1
    }
    # GOBIN表示我们开发程序编译后二进制命令的安装目录
    # GOPATH用于指定我们的开发工作区(workspace),是存放源代码、测试文件、库静态文件、可执行文件的工作。
    # GOROOT表示Go语言的安装目录
    echo "export GOROOT=/usr/local/go
export GOPATH=$HOME/gowork
export GOBIN=$GOPATH/bin
export PATH=$GOPATH:$GOBIN:$GOROOT/bin:$PATH" >> ~/.zshrc
    rt_log "go path setting success !"
}

git_install() {
    # lazygit auto install
    sudo pacman -Sy lazygit || {
        rt_log "statring run manual install with go"
        git clone https://github.com/jesseduffield/lazygit.git
        cd lazygit && go install || {
            rt_err "manual lazygit install failed !"
            return 1
        }
    }
    # git config
    echo "
[user]
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
[core]
	quotepath = false
[gui]
	encoding = utf-8
[i18n "commit"]
	encoding = utf-8
[i18n]
	logoutputencoding = utf-8
[pull]
	rebase = false
[delta]
    navigate = true    # use n and N to move between diff sections
    light = false
	side-by-side = true
	line-numbers = false
[merge]
    conflictstyle = diff3

[diff]
    colorMoved = default
	" > ~/.gitconfig
    rt_log "git and lazygit setting success"
}

config_main() {
    # 1. install .config from theniceboy .config
    rt_log "theniceboy config downloading ..."
    git clone git@github.com:theniceboy/.config.git theniceboy.config
    cp -arv ./theniceboy.config/* ~/.config
    cd ~/.config && patch < ${BIN}/patch.files/theniceboy.config.patch
    rt_log "theniceboy config cp done !"
}

rime_config() {
    # 2. rime 输入法 配置文件
    rt_log "rime installing ......."
    if uname | grep Linux; then
        rt_log "linux rime install !"
        install_dir="~/.local/share/fcitx5/themes"
        [ ! -d ${install_dir} ] && mkdir -p ${install_dir}
        cp -arv ../config.files/fcitx5/themes/xiaohan-rime ${install_dir}
    else
        # windows install
        git clone git@github.com:iDvel/rime-ice.git
        cp -arv ./rime-ice/* ~/.local/fcitx5/rime
        cp -arvf win10/soft_config/rime-ice_setting_cover/* ~/.local/fcitx5/rime
    fi
    rt_log "rime cfg installed success !"
}
