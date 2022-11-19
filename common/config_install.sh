#!/bin/bash

cur=$(dirname "$(realpath "$0")")
# shellcheck disable=SC1091
source "${cur}/common.sh"

config_install() {
    local isInstall
    # 1. install .config from theniceboy .config
    rt_log "theniceboy config installing ..."
    echo "install config files from theniceboy/.config: yes or no："
    isInstall=$(rt_select "yes no")
    if [ "${isInstall}" != "yes" ]; then
        rt_warn "config install skipped ..."
        return 1
    fi
    git clone git@github.com:theniceboy/.config.git "${HOME}/theniceboy.config" && {
        [ ! -d "$HOME/.config" ] && mkdir -p ~/.config
        cp -arv "${HOME}/theniceboy.config/"* "${HOME}/.config"
        cd ~/.config && patch < "${BIN:-}"/patch.files/theniceboy.config.patch
        rm -rf ~/theniceboy.config
    }
    rt_log "theniceboy config cp done !"
    return 0
}

config_install "$@"
