
# 

## i 写入模式
    i插入之前、a插入之后、A行尾插入、I行首插入、o下行插入、O上行插入

## x 删除光标后一个字符
    d + ←→删除光标←→字符（d +3←）、dd删除一行（其实是剪切，p粘贴）

## y+ ←→复制光标←→字符 （y+3←）

## c 删除并进入写入模式、
    w 光标向下移动一个词、cw删除一个词并进入写入模式、
    b光标到上一个词 、ciw词中删除一个词并进入写入模式，yi

## f 找词

## / 搜索、n下 N上
    【y i c d f 】
    esc 回到正常模式

## 文件操作
：w保存
：q退出vim
：source $MYVIMRC 刷新vim

## 光标移动
jkhl上下左右
## 分屏
    ：split 上下分屏 、
    ：vsplit 左右分屏 
    Q退出

## 键位映射(~/.vim/vimrc)

let mapleader=" "


syntax on 打开高亮
set number 显示行号
set norelativenumber  不显示相对行数,当前为0行,上下多少行
set wildmenu   ：命令补全
set wrap
set hlsearch  /搜索高亮
exec "nohlsearch" [没有高亮]
set cursorline 显示|竖线

set showcmd 显示输入的命令
set incsearch  一面输入一面高亮
set ignorecase 忽略大小写()
set smartcase 智能大小写(完全匹配大小写)


noremap a b [a键改b键]
noremap = nzz [=下一个关键字并作为中心点]
noremap - Nzz [-上一个关键字并作为中心点]
noremap <LEADER><CR> :nohlsearch<CR> [空格 + 回车 取消高亮]

map a b a键改b键

## 美化vim
