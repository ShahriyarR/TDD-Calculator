#!/bin/sh -e
set -x

python3 -m autoflake --remove-all-unused-imports --recursive --remove-unused-variables --in-place src --exclude=__init__.py
python3 -m black src test
python3 -m isort src test
