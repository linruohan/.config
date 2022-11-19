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
    sudo pacman -Sy nodejs npm || {
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

npm_install "$@"
