#!/usr/bin/env bash

set -e
set -x

python3 -m flake8 src
python3 -m black src test --check --diff
python3 -m isort src test --check --diff
