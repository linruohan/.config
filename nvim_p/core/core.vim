"
" ██████╗ ██████╗ ██████╗ ███████╗  ██╗   ██╗██╗███╗   ███╗
"██╔════╝██╔═══██╗██╔══██╗██╔════╝  ██║   ██║██║████╗ ████║
"██║     ██║   ██║██████╔╝█████╗    ██║   ██║██║██╔████╔██║
"██║     ██║   ██║██╔══██╗██╔══╝    ╚██╗ ██╔╝██║██║╚██╔╝██║
"╚██████╗╚██████╔╝██║  ██║███████╗██╗╚████╔╝ ██║██║ ╚═╝ ██║
" ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝ ╚═══╝  ╚═╝╚═╝     ╚═╝

"============
"首次安装使用
"============
"Vim-Plug的首次下载安装
if empty(glob('/home/xiaohan/.config/nvim/autoload/plug.vim'))
	silent !curl -fLo /home/xiaohan/.config/nvim/autoload/plug.vim --create-dirs
				\ https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim
	autocmd VimEnter * PlugInstall --sync | source $MYVIMRC
endif

"let g:powerline_pycmd="py3"

"模块化配置
source /home/xiaohan/.config/nvim/core/general_config.vim
source /home/xiaohan/.config/nvim/core/key_bindings.vim
source /home/xiaohan/.config/nvim/core/special_config.vim
source /home/xiaohan/.config/nvim/core/language_config.vim
source /home/xiaohan/.config/nvim/plug/plug_list.vim
source /home/xiaohan/.config/nvim/plug/plug_settings.vim
source /home/xiaohan/.config/nvim/theme/theme.vim
