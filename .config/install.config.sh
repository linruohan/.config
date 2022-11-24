# 1. install .config
codehub_dir=~/working/codehub
echo "config installing ......."
if [ -d ~/.config ] ;then
git clone git@github.com:theniceboy/.config.git ${codehub_dir}/theniceboy.config
cp -arv ${codehub_dir}/theniceboy.config/* ~/.config
else
git clone git@github.com:theniceboy/.config.git ~/.config
fi
cd ~/.config && patch < ${codehub_dir}/my.config/theniceboy.config.patch
echo "config installing .....done.."

# 2. rime 输入法 配置文件
echo "rime installing ......."
git clone git@gitee.com:linruohan/win10.git ${codehub_dir}
if [ ! -d ~/.config/fcitx5/rime  ];then
	git clone git@github.com:iDvel/rime-ice.git ~/.config/fcitx5/rime
else
	git clone git@github.com:iDvel/rime-ice.git ${codehub_dir}
	cp -arv ${codehub_dir}/rime-ice/* ~/.config/fcitx5/rime
fi
cp -arvf ${codehub_dir}/win10/soft_config/rime-ice_setting_cover/* ~/.config/fcitx5/rime
echo "rime installing .....done.."

# 3. install nvim config

flag="theniceboy"
case "$flag" in
    "theniceboy")
        #  2.1 theniceboy: https://github.com/theniceboy/nvim
        git clone git@github.com:theniceboy/nvim.git ~/.config
        # 打入自定义补丁
        cd ~/.config/nvim && patch < ${codehub_dir}/my.config/theniceboy_nvim.init.vim.patch
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
