#!/usr/bin/env bash

cd $(readlink -f $(dirname "$0"))

VENV_NAME="sgw"
VENV_PATH=${WORKON_HOME:-$HOME/.local/share/virtualenvs}
source $VENV_PATH/$VENV_NAME/bin/activate

# Get token and droplet from config file
source sgw.conf

python do.py -t "$TOKEN" "$@" "$DROPLET"
