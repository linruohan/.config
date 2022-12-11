#!/bin/bash
cur=$(dirname "$(realpath "$0")")
# shellcheck disable=SC1091
source "${cur}/common.sh"

zsh_install() {
    local zsh_path
    type zsh || sudo pacman -Sy zsh
    zsh_path=$(which zsh)
    [ "${zsh_path}" = "${SHELL}" ] && {
        rt_log "zsh is already in use !"
        return 0
    }
    grep "${zsh_path}" /etc/shells || echo "${zsh_path}" >> /etc/shells
    usermod -s "${zsh_path}"
    return 0
}

ohmyzsh_install() {
    # wget install ohmyzsh
    [ -d ~/.oh-my-zsh ] || {
        type wget || sudo pacman -Sy wget
        sh ${BIN}/common/ohmyzsh-install.sh
        cd ~/.oh-my-zsh && patch < "${BIN}/patch.files/ohmyzsh.patch"
    }
    # install plugins
    grep -rw "zsh-syntax-highlighting" ~/.zshrc || {
        # zsh-syntax-highlighting
        git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting
        #  zsh-autosuggestions
        git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions
        # 替换主题和插件
        sed -i 's|^ZSH_THEME=.*|ZSH_THEME="agnoster"|' ~/.zshrc
        sed -i 's|^plugins=.*|plugins=(git zsh-syntax-highlighting zsh-autosuggestions sudo)|' ~/.zshrc
    }
}

shell_tool_install() {
    (type shellcheck && type shfmt) || sudo pacman -Ss shellcheck shfmt
}

zsh_install "$@"
shell_tool_install "$@"
ohmyzsh_install "$@"
