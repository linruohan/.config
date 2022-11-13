#!/bin/bash

config_main() {
    # 1. install .config from theniceboy .config
    rt_log "theniceboy config downloading ..."
    git clone git@github.com:theniceboy/.config.git theniceboy.config
    cp -arv ./theniceboy.config/* ~/.config
    cd ~/.config && patch < ${BIN}/patch.files/theniceboy.config.patch
    rt_log "theniceboy config cp done !"
}

rime_config() {
    # 2. rime 输入法 配置文件
    rt_log "rime installing ......."
    git clone git@github.com:iDvel/rime-ice.git
    cp -arv ./rime-ice/* ~/.local/fcitx5/rime
    cp -arvf win10/soft_config/rime-ice_setting_cover/* ~/.local/fcitx5/rime
    rt_log "rime cfg installed success !"
}
