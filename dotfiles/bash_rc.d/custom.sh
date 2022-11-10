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

export KOPS_STATE_STORE="s3://clusters.k8s.glassfrog.com"

if which rbenv > /dev/null; then eval "$(rbenv init -)"; fi

ssh-pod() {
  local podname=$1
  local container="${2:-rails}"
  kubectl exec -it $podname -c $container -- /bin/bash -l
}

. $HOME/.asdf/asdf.sh
. $HOME/.asdf/completions/asdf.bash

