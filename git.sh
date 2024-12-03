#!/usr/bin/env sh

while :
do
    echo "saving project"
    cd "$(dirname "$0")"

    git add -u
    echo "all files uppdated"

    timestamp() {
            date +"at %H:%M:%S on %d/%m/%Y"
    }

    git commit -am "Regular auto-commit $(timestamp)"
    echo "commit complete"
    
    git push
    echo "pushed to github"
    echo "sleeping for 300 seconds and repeates"
    sleep 300
done