#!/bin/bash

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
export PYTHONPATH="${PYTHONPATH}:$SCRIPT_DIR/src"
python "$SCRIPT_DIR/src/shell.py" "$@"
