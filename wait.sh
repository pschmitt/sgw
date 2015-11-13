#!/usr/bin/env bash

usage() {
    echo "Usage: $(basename $0) online|offline HOST [WAIT_CHAR]"
}

wait_online () {
    while ! ping -c 1 -W 1 "$1" > /dev/null 2>&1
    do
        echo -n "$2"
        sleep 1
    done
    echo
}

wait_offline() {
    while ping -c 1 -W 1 "$1" > /dev/null 2>&1
    do
        echo -n "$2"
        sleep 1
    done
    echo
}

[[ "$#" -lt 2 ]] && { usage; exit 2; }

case "$1" in
    on|online)
        wait_online "$2" "$3" ;;
    off|offline)
        wait_offline "$2" "$3" ;;
    *)
        usage
        exit 2
        ;;
esac
