#!/bin/bash
cur=$(dirname "$(realpath "$0")")
# shellcheck disable=SC1091
source "${cur}/common.sh"

go_install() {
    type go || sudo pacman -Sy go || {
        rt_err "golang install failed!\n please 访问https://studygolang.com/dl 获取最新版本, install manual"
        return 1
    }
		export GO111MODULE=on
		export GOPROXY=https://goproxy.cn
		export GOPATH="~/gowork"
		go env -w GO111MODULE=on
		go env -w GOPROXY=https://goproxy.cn,direct
		go env -w GOPATH=$GOROOT/bin
    # GOBIN表示我们开发程序编译后二进制命令的安装目录
    # GOPATH用于指定我们的开发工作区(workspace),是存放源代码、测试文件、库静态文件、可执行文件的工作。
    # GOROOT表示Go语言的安装目录
    grep "GOPATH" ~/.zshrc || echo "export GOPATH=$HOME/gowork
export GOBIN=\$GOPATH/bin
export PATH=\$GOPATH:\$GOBIN:\$GOROOT/bin:\$PATH" >> ~/.zshrc
    rt_log "go path setting success !"
}

go_install "$@"
