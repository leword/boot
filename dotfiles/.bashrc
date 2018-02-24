# ~/.bashrc: executed by bash(1) for non-login shells.
# see /usr/share/doc/bash/examples/startup-files (in the package bash-doc)
# for examples

for FILE in ~/boot/dotfiles/bash_rc.d/*
do
  source $FILE
done


alias db='psql r3_holacracy_tool_dev'
