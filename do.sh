#!/usr/bin/env bash

cd $(readlink -f $(dirname "$0"))

VENV_NAME="sgw"
VENV_PATH=${WORKON_HOME:-$HOME/.local/share/virtualenvs}
source $VENV_PATH/$VENV_NAME/bin/activate

# Get token and droplet from config file
if [[ -r sgw.conf ]]
then
    source sgw.conf
else
    echo "Config file does not exist or is not readable" >&2
    exit 3
fi

python do.py -t "$TOKEN" "$@" "$DROPLET"
