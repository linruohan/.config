#!/bin/bash
cur=$(dirname "$(realpath "$0")")
# shellcheck disable=SC1091
source "${cur}/common.sh"

python_install() {
    [ -f ~/.pip/pip.conf ] && {
        rt_log "python proxy is setting already !"
        return 0
    }
    # python3 代理
    mkdir -p ~/.pip
    echo "[global]
index-url = https://pypi.tuna.tsinghua.edu.cn/simple
[install]
trusted-host = https://pypi.tuna.tsinghua.edu.cn" > ~/.pip/pip.conf
    # python 安装依赖库
    pip3 install pylint pynvim jedi pillow requests
    rt_log "python proxy setting success!"
}

python_install "$@"
