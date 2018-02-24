#!/usr/bin/env bash


# add sphinx path for glassfrog
export SPHINX_PATH="/usr/bin"


export PATH="$PATH:$HOME/.local/bin"

export PAPERTRAIL_API_TOKEN=W1p3Xwe4N9uffOaqO7J
export PARALLEL_TEST_FIRST_IS_1=true
export GOPATH=${HOME}/workspace/go
export PATH="$GOPATH/bin:$PATH"
export PATH="/usr/local/opt/gettext/bin:$PATH"
export PATH="$HOME/.rbenv/bin:$PATH"
if which rbenv > /dev/null; then eval "$(rbenv init -)"; fi
