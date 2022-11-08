# 1. install .config
git clone git@github.com:theniceboy/.config.git ~/
cd ~/.config patch < ./theniceboy.config.patch

# 2. install nvim config
#  2.1 theniceboy: https://github.com/theniceboy/nvim
git clone git@github.com:theniceboy/nvim.git ~/.config
# 打入自定义补丁
cd ~/.config/nvim && patch < ../theniceboy_nvim.init.vim.patch
#  2.2 git@github.com:LunarVim/Neovim-from-scratch.git
git clone git@github.com:LunarVim/Neovim-from-scratch.git ~/.config

#  2.3 git@github.com:askfiy/nvim.git
git clone git@github.com:askfiy/nvim.git ~/.config
cd ~/.config/nvim/ && patch < ../askfiy.nvim.patch
