#!/usr/bin/env bash

# install basics
sudo apt-get install ssh git software-center gnome-terminal software-properties-common default-jdk

sudo apt-add-repository ppa:synapse-core/testing
sudo apt-get update
sudo apt-get install synapse

# configure git
git config --global user.email "lewis.hoffman@gmail.com"
git config --global user.name "Lewis Hoffman"
git config --global alias.co checkout
git config --global alias.br branch
git config --global alias.ci commit
git config --global alias.st status
git config --global push.default simple


######## MANUAL STEPS #########

# WEB: Download chrome
sudo dpkg -i ~/Downloads/chrome-xxx.deb
sudo apt-get install -f

google-chrome-stable
# WEB: log in:to chrome

# generate new ssh key
ssh-keygen

# WEB: install new ssh key in github

# WEB: Download RubyMine.

######## END MANUAL STEPS #########


# setup checked-in configs:

git clone git@github.com:leword/boot.git

# setup dotfile symlinks
ln -sf ~/boot/dotfiles/.gconf          ~/.gconf
ln -sf ~/boot/dotfiles/.bashrc         ~/.bashrc
ls -sf ~/boot/dotfiles/.config/xfce4   ~/.config/xfce4
ln -sf ~/boot/dotfiles/.config/synapse ~/.config/synapse


## After rubymine install/first run?  or point rubymine to dotfiles

rm -rf ~/.RubyMine70/config/codestyles
rm -rf ~/.RubyMine70/config/keymaps
rm -rf ~/.RubyMine70/config/options
rm -rf ~/.RubyMine70/config/inspection
rm -rf ~/.RubyMine70/config/quicklists
rm -rf ~/.RubyMine70/config/tasks

ls -sf ~/boot/dotfiles/.config/.RubyMine70/config/codestyles ~/.RubyMine70/config/codestyles
ls -sf ~/boot/dotfiles/.config/.RubyMine70/config/keymaps ~/.RubyMine70/config/keymaps
ls -sf ~/boot/dotfiles/.config/.RubyMine70/config/options ~/.RubyMine70/config/options
ls -sf ~/boot/dotfiles/.config/.RubyMine70/config/inspection ~/.RubyMine70/config/inspection
ls -sf ~/boot/dotfiles/.config/.RubyMine70/config/quicklists ~/.RubyMine70/config/quicklists
ls -sf ~/boot/dotfiles/.config/.RubyMine70/config/tasks ~/.RubyMine70/config/tasks

#ls -sf ~/boot/dotfiles/.config/xfce4-session ~/.config/xfce4-session