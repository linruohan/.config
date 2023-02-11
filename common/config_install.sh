#!/bin/bash

cur=$(dirname "$(realpath "$0")")
# shellcheck disable=SC1091
source "${cur}/common.sh"

config_install() {
    local isInstall
    rt_log "theniceboy config installing ..."
    echo "install config files from theniceboy/.config: yes or no："
    isInstall=$(rt_select "yes no")
    [ "${isInstall}" == "no" ] && {
        rt_warn "config install skipped ..."
        return 1
    }
    git clone https://github.com/theniceboy/.config.git "${HOME}/theniceboy.config" && {
        [ ! -d "$HOME/.config" ] && mkdir -p ~/.config
        cp -arv "${HOME}/theniceboy.config/"* "${HOME}/.config"
        cd ~/.config && patch < "${BIN:-}"/patch.files/theniceboy.config.patch
        cd ~/.config && 7z x ~/codehub/*.config/.config.7z
        rm -rf ~/theniceboy.config
    }
    rt_log "theniceboy config setting done !"
    return 0
}

config_install "$@"
