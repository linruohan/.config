#!/bin/bash
# shellcheck disable=SC1091
source ./common/common.sh

install_cmd() {
    # shell 相关
    {
        sh "./common/zsh_install.sh"          # ohmyzsh shfmt shellcheck
        cat "./home.files/.zshrc" >> ~/.zshrc # alias add
    }
    # env and cfg 安装
    {
        sh "./common/config_install.sh"       # ~/.config
        sh "./common/input_method_install.sh" # rime
        sh "./common/git_install.sh"          # git and lazygit
        sh "./common/python_install.sh"       # pip and pynivm
        sh "./common/npm_install.sh"          # ~/.npmrc
        sh "./common/go_install.sh"           # gopath
        sh "./common/vim_install.sh"          # nvim and ~/.config/nvim
    }
}

main() {
    install_cmd
    return 0
}

main
