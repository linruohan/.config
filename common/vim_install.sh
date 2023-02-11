#!/bin/bash

cur=$(dirname "$(realpath "$0")")
# shellcheck disable=SC1091
source "${cur}/common.sh"

neovim_install() {
    # neovim install
    type nvim || sudo pacman -Sy neovim python-pip
    # config files install
    echo "install neovim config: y or n"
    isInstall=$(rt_select "yes no")
    [ "${isInstall}" = "no" ] && {
        rt_warn "neovim config install skipped !"
        return 1
    }
    flag=$(rt_select "LunarVim theniceboy scratch askfiy")
    flag="${flag:-LunarVim}"
    [ -d ~/.config/nivm ] && mv ~/.config/nvim ~/.config/nvim.old
    rt_log "[${flag}] nvim installing ..."
    case "$flag" in
        "theniceboy")
            #  2.1 theniceboy: https://github.com/theniceboy/nvim
            git clone git@github.com:theniceboy/nvim.git ~/.config/nvim
            (cd ~/.config/nvim && patch < "${BIN}/patch.files/theniceboy_nvim.init.vim.patch") || {
                rt_err "patch to theniceboy_nvim failed"
            }
            rt_log "start nvim with [nvim +PlugInstall]"
            ;;
        "scratch")
            #  2.2 git@github.com:LunarVim/Neovim-from-scratch.git
            git clone git@github.com:LunarVim/Neovim-from-scratch.git ~/.config/nvim
            rt_log "start nvim with [nvim +PackerSync]"
            ;;
        "LunarVim")
            git clone https://github.com/LunarVim/LunarVim.git /tmp
            sh /tmp/LunarVim/utils/installer/install.sh
            rt_log "start nvim with [nvim +PackerSync]"
            rm -rf /tmp/LunarVim
            ;;
        "askfiy")
            #  2.3 git@github.com:askfiy/nvim.git
            git clone git@github.com:askfiy/nvim.git ~/.config
            cd ~/.config/nvim/ && patch < "${BIN}/patch.files/askfiy.nvim.patch"
            ;;
        *)
            rt_log "install skipped"
            ;;
    esac
}

neovim_install
