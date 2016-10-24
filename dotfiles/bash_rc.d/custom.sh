#!/usr/bin/env bash

# Add RVM to PATH for scripting
export PATH="$PATH:$HOME/.rvm/bin"


# add sphinx path for glassfrog
export SPHINX_PATH="/usr/bin"

#source /home/lewis/.rvm/scripts/rvm
 [[ -s "$HOME/.rvm/scripts/rvm" ]] && . "$HOME/.rvm/scripts/rvm" # Load RVM function

export PATH="$PATH:$HOME/.local/bin"
