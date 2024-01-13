#!/bin/bash
cur=$(dirname "$(realpath "$0")")
# shellcheck disable=SC1091
source "${cur}/common.sh"

npm_install() {
    type node && type npm && {
        rt_log "node and npm already installed !"
        return 0
    }
    # 1 nodejs install
    # nodejs 21版本nvim lsp有问题，所以安装20版本的nodejs
    # sudo pacman -Sy nodejs npm || {
    sudo pacman -Sy nodejs-lts-iron npm || {
        rt_err "nodejs install failed"
        return 1
    }
    # npm 淘宝代理设置
    echo "strict-ssl=false
registry=https://registry.npmmirror.com/
electron_mirror=https://npmmirror.com/mirrors/electron/
electron_builder_binaries_mirror=http://npmmirror.com/mirrors/electron-builder-binaries/" > ~/.npmrc
    npm config set prefix "$HOME/.node_global"
    npm config set cache "$HOME/.node_cache"
    grep -wn NODE_PATH ~/.zshrc || echo "export NODE_PATH=~/.node_global" >> ~/.zshrc
    rt_log "node and ~/.npmrc setting success!"
    return 0
}

npm_install "$@"
