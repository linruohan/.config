# 1. install .config
git clone git@github.com:theniceboy/.config.git ~/
cd ~/.config patch < ./theniceboy.config.patch

# 2. rime 输入法 配置文件
git clone git@github.com:iDvel/rime-ice.git ~/.config/fcitx5/rime
git clone git@gitee.com:linruohan/win10.git
cp -arvf win10/soft_config/rime-ice_setting_cover/* ~/.config/fcitx5/rime

# 3. install nvim config
flag="theniceboy"
case "$flag" in
    "theniceboy")
        #  2.1 theniceboy: https://github.com/theniceboy/nvim
        git clone git@github.com:theniceboy/nvim.git ~/.config
        # 打入自定义补丁
        cd ~/.config/nvim && patch < ../theniceboy_nvim.init.vim.patch
        ;;
    "LunarVim")
        #  2.2 git@github.com:LunarVim/Neovim-from-scratch.git
        git clone git@github.com:LunarVim/Neovim-from-scratch.git ~/.config

        ;;
    "askfiy")
        #  2.3 git@github.com:askfiy/nvim.git
        git clone git@github.com:askfiy/nvim.git ~/.config
        cd ~/.config/nvim/ && patch < ../askfiy.nvim.patch
        ;;
    *)
        echo default
        ;;
esac
