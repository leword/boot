alias kak='killall -w autokey-gtk; autokey-gtk & >/dev/null 2>&1'
alias nocaps='/usr/bin/setxkbmap -option "ctrl:nocaps"'
alias togglecaps='xdotool key Caps_Lock'
alias gl="git for-each-ref --count=10 --sort=-committerdate refs/heads/ --format='%(refname:short)'"
alias s="./bin/spring"
alias ks="ps auxw | grep spring | grep -v grep | awk '{print \$2}' | xargs kill -9"
alias kc="kubectl"
alias kz="killall -9 zoom"
alias bpod="kc get pods | grep backend | awk '{print \$1}' | head -1"
alias prails="kc config use-context eu-production && kubectl exec -it `bpod` -c rails -- bundle exec rails c"
alias sshb="ssh -i ~/.ssh/k8s-admin-keypair admin@bastion.eu.k8s.glassfrog.com -p 9642"
alias gmr="k8s/update-releases rails && git add . && git rebase --continue"

