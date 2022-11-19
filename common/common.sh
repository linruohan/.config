#!/bin/bash

COMMON_DIR=$(dirname "$(realpath "$0")")
BIN=$(dirname "${COMMON_DIR}")
export BIN=$BIN
export COMMON_DIR=$COMMON_DIR

# color variables
color_blue="\033[1;34m"
color_green="\033[0;32m"
color_red="\033[1;31m"
color_yellow="\033[1;33m"
color_clean="\033[0m"

# DEBUG print
rt_debug() {
    echo -e "${color_blue}$(date '+[%Y-%m-%d %H:%M:%S]')[INFO] $* ${color_clean}"
}
# WARN print
rt_warn() {
    echo -e "${color_yellow}$(date '+[%Y-%m-%d %H:%M:%S]')[INFO] $* ${color_clean}"
}
# LOG print
rt_log() {
    echo -e "${color_green}$(date '+[%Y-%m-%d %H:%M:%S]')[INFO] $* ${color_clean}"
}

# ERROR print
rt_err() {
    echo -e "${color_red}$(date '+[%Y-%m-%d %H:%M:%S]')[ERROR] $* ${color_clean}"
}

# FUNC: select menu
# ARGS: item lists -- string splitting by space
# RETS: item values
rt_select() {
    select item in $1; do
        echo "${item}"
        return 1
    done
    return 0
}
