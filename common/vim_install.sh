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
    flag=$(rt_select "LunarVim askfiy NvChad")
    flag="${flag:-LunarVim}"
    [ -d ~/.config/nivm ] && mv ~/.config/nvim ~/.config/nvim.old
    rt_log "[${flag}] nvim installing ..."
    case "$flag" in
        "NvChad")
            [ -d "$HOME/.config/nvim" ] && mv ~/.config/nvim ~/.config/nvim.bak
            git clone https://github.com/NvChad/NvChad.git ~/.config/nvim
            git clone https://github.com/linruohan/NvChad_custom.git ~/.config/nvim/lua/custom
            rt_log "start nvim with [nvim]"
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
