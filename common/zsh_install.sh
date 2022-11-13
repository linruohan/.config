#!/usr/bin/env bash
zsh_install() {
    type zsh || sudo pacman -Sy zsh
    grep $(which zsh) /etc/shells || echo $(which zsh) >> /etc/shells
    usermod -s $(which zsh) $(whoami)
    return 0
}

ohmyzsh_install() {
    # wget install ohmyzsh
    [ -d ~/.oh-my-zsh ] && return 0
    type wget || sudo pacman -Sy wget
    sh -c "$(wget -O- https://gitee.com/pocmon/mirrors/raw/master/tools/install.sh)"
    # install plugins
    grep -rw "zsh-syntax-highlighting" ~/.zshrc && return 0
    # zsh-syntax-highlighting
    git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting
    #  zsh-autosuggestions
    git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions
    # 替换主题和插件
    sed -i 's|^ZSH_THEME=.*|ZSH_THEME="agnoster"|' ~/.zshrc
    sed -i 's|^plugins=.*|plugins=(git zsh-syntax-highlighting zsh-autosuggestions sudo)|' ~/.zshrc
}

shell_tool_install() {
    type shellcheck && type shfmt && return 0
    # shellcheck install
    type pacman && sudo pacman -Ss shellcheck shfmt
}
