#!/usr/bin/env bash
source ./common/common.sh

install_cmd() {
    # shell 相关
    {
        rt_log "[oh-my-zsh] & [shfmt shellcheck] install stating ..."
        zsh_install && ohmyzsh_install && shell_tool_install
        # add alias
        cat "./home.files/.zshrc" >> ~/.zshrc
    }
    # 编辑器安装
    {
        python_install
        node_install
        go_install
        git_install
        neovim_install
    }

}

main() {
    install_cmd
}

main
